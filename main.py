import requests
import sys
from os import mkdir
from PyQt5 import QtCore, QtWidgets, QtGui
from UI import Ui_Form


class MapVision(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.f = 0
        self.setupUi(self)
        self.setWindowTitle("MapVision v0.3")
        self.search.clicked.connect(self.showing)
        self.map_showing.toggled.connect(self.onClicked)
        self.sattelite_showing.toggled.connect(self.onClicked)
        self.gibrid_showing.toggled.connect(self.onClicked)

    def showing(self):
        dic = {0: "map", 1: "sat", 2: "sat,skl"}
        self.data = [self.map_showing.isChecked(), self.sattelite_showing.isChecked(), self.gibrid_showing.isChecked()]
        how_showed = dic[self.data.index(1)]

        if bool(str(self.requested.toPlainText())):  # если поле с адресом не пусто
            geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

            geocoder_params = {
                "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                "geocode": self.requested.toPlainText(),
                "format": "json"
            }

            response = requests.get(geocoder_api_server, params=geocoder_params)
            # запрос у геокодера по введённому адресу

            if response:
                # Преобразуем ответ в json-объект
                json_response = response.json()
                # Получаем первый топоним из ответа геокодера.
                toponym = json_response["response"]["GeoObjectCollection"][
                    "featureMember"][0]["GeoObject"]
                # Координаты центра топонима:
                toponym_coodrinates = toponym["Point"]["pos"]
                # Долгота и широта:
                toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

                self.lat.setText(str(toponym_longitude))
                self.lon.setText(str(toponym_lattitude))
                # подстановка координат найденного адреса и перемещение на него

                pt = f'{toponym_longitude},{toponym_lattitude},round'
                # данные точки

                request = f"https://static-maps.yandex.ru/1.x/?ll={self.lat.text()},{self.lon.text()}&z={self.scale.text()}&l={how_showed}&pt={pt}"
        else:
            request = f"https://static-maps.yandex.ru/1.x/?ll={self.lat.text()},{self.lon.text()}&z={self.scale.text()}&l={how_showed}"

        result = requests.get(request)
        if result:
            try:
                mkdir("data/")
            except Exception as e:
                pass
            with open("data/map.png", "wb") as file:
                file.write(result.content)
            self.map.setPixmap(QtGui.QPixmap("data/map.png"))
            self.f = 1
            for childWidget in self.findChildren(QtWidgets.QWidget):
                childWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
                childWidget.clearFocus()


    def onClicked(self):
        if self.f:
            self.showing()


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_PageUp:
            scaling = int(self.scale.text())
            if scaling < 17:
                self.scale.setText(str(scaling + 1))
            self.showing()
        elif event.key() == QtCore.Qt.Key_PageDown:
            scaling = int(self.scale.text())
            if scaling > 0:
                self.scale.setText(str(scaling - 1))
            self.showing()

        elif event.key() == QtCore.Qt.Key_Up:  # нажатие на стрелку вверх
            lon = float(self.lon.text())  # текущая широта
            scaling = int(self.scale.text())  # масштаб карты
            if lon + ((18 - scaling) / scaling ** 2.5) < 80:
                self.lon.setText(str(lon + ((18 - scaling) / scaling ** 2.5)))
                # изменение по формуле: предидущее значение + ((18 - масштаб) / масштаб ** 2.5)
                self.showing()  # отрисовка карты
            self.requested.setPlainText('')  # очистка поля поиска адреса
        elif event.key() == QtCore.Qt.Key_Down:
            lon = float(self.lon.text())  # текущая широта
            scaling = int(self.scale.text())  # масштаб карты
            if lon - ((18 - scaling) / scaling ** 2.5) > -80:
                self.lon.setText(str(lon - ((18 - scaling) / scaling ** 2.5)))
                # изменение по формуле: предидущее значение - ((18 - масштаб) / масштаб ** 2.5)
                self.showing()  # отрисовка карты
            self.requested.setPlainText('')  # очистка поля поиска адреса
        elif event.key() == QtCore.Qt.Key_Left:
            lat = float(self.lat.text())  # текущая долгота
            scaling = int(self.scale.text())  # масштаб карты
            if lat - ((18 - scaling) / scaling ** 2.5) > -180:
                self.lat.setText(str(lat - ((18 - scaling) / scaling ** 2.5)))
                # изменение по формуле: предыдущее значение + ((18 - масштаб) / масштаб ** 2.5)
                self.showing()  # отрисовка карты
            self.requested.setPlainText('')  # очистка поля поиска адреса
        elif event.key() == QtCore.Qt.Key_Right:
            lat = float(self.lat.text())  # текущая долгота
            scaling = int(self.scale.text())  # масштаб карты
            if lat + ((18 - scaling) / scaling ** 2.5) < 180:
                self.lat.setText(str(lat + ((18 - scaling) / scaling ** 2.5)))
                # изменение по формуле: предидущее значение - ((18 - масштаб) / масштаб ** 2.5)
                self.showing()  # отрисовка карты
            self.requested.setPlainText('')  # очистка поля поиска адреса


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = MapVision()
    ex.show()
    sys.exit(app.exec_())
