import requests


def calculate_distance(coord1, coord2):  # координаты на вход, а на выходе расстояние в метрах
    x2, y2 = list(map(float, coord2.split(',')))
    x1, y1 = list(map(float, coord1.split(',')))

    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    return int(dist * 111000)


def coord_to_address(coordinates):
    # coordinates = 'longitude,lattitude'
    # координаты на вход, самый подходящий адрес
    # по мнению geocode-maps.yandex на выход
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": coordinates,
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

        # возврат адреса
        return toponym['metaDataProperty']['GeocoderMetaData']['text']


def get_closest_organisation(coordinates):
    # coordinates = 'longitude,lattitude'
    # на вход координаты, на выходе название организации,
    # если она лежит в пределах 50 метров от этх координат
    search_api_server = "https://search-maps.yandex.ru/v1/"

    search_params = {
        "apikey": "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3",
        "lang": "ru_RU",
        'type': 'biz',
        'text': coord_to_address(coordinates)
    }

    response = requests.get(search_api_server, params=search_params)
    if response:
        json_response = response.json()
        print(json_response)
        # Получаем первую найденную организацию.
        organization = json_response["features"][0]
        # Название организации.
        org_name = organization["properties"]["CompanyMetaData"]["name"]
        # Адрес организации и координата.
        org_address = organization["properties"]["CompanyMetaData"]["address"]
        point = ','.join(list(map(str, organization["geometry"]["coordinates"])))

        # расстояние между координатой запроса и организацией
        distance = calculate_distance(coordinates, point)

        print(org_name, org_address, distance)

        search_radius = 50
        if distance < search_radius:
            return f'{org_name}({org_address})'
        return f'В пределах {search_radius} м ничего не нашлось'
