import requests
import sys
from os import mkdir
from PyQt5 import QtCore, QtWidgets, QtGui
from UI import Ui_Form


class MapVision(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("MapVision v0.2")
        self.search.clicked.connect(self.showing)

    def showing(self):
        request = f"https://static-maps.yandex.ru/1.x/?ll={self.lat.text()},{self.lon.text()}&z={self.scale.text()}&l=map"
        print(request)
        result = requests.get(request)
        if result:
            try:
                mkdir("data/")
            except Exception as e:
                pass
            with open("data/map.png", "wb") as file:
                file.write(result.content)
            self.map.setPixmap(QtGui.QPixmap("data/map.png"))
            for childWidget in self.findChildren(QtWidgets.QWidget):
                childWidget.setFocusPolicy(QtCore.Qt.ClickFocus)

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
            self.lon.setText(str(lon + ((18 - scaling) / scaling ** 2.5)))
            # изменение по формуле: предидущее значение + ((18 - масштаб) / масштаб ** 2.5)
            self.showing()  # отрисовка карты
        elif event.key() == QtCore.Qt.Key_Down:
            lon = float(self.lon.text())  # текущая широта
            scaling = int(self.scale.text())  # масштаб карты
            self.lon.setText(str(lon - ((18 - scaling) / scaling ** 2.5)))
            # изменение по формуле: предидущее значение - ((18 - масштаб) / масштаб ** 2.5)
            self.showing()  # отрисовка карты
        elif event.key() == QtCore.Qt.Key_Left:
            lat = float(self.lat.text())  # текущая долгота
            scaling = int(self.scale.text())  # масштаб карты
            self.lat.setText(str(lat - ((18 - scaling) / scaling ** 2.5)))
            # изменение по формуле: предыдущее значение + ((18 - масштаб) / масштаб ** 2.5)
            self.showing()  # отрисовка карты
        elif event.key() == QtCore.Qt.Key_Right:
            lat = float(self.lat.text())  # текущая долгота
            scaling = int(self.scale.text())  # масштаб карты
            self.lat.setText(str(lat + ((18 - scaling) / scaling ** 2.5)))
            # изменение по формуле: предидущее значение - ((18 - масштаб) / масштаб ** 2.5)
            self.showing()  # отрисовка карты


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = MapVision()
    ex.show()
    sys.exit(app.exec_())
