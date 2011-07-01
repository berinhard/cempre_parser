from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import MapCompose


def value_from_keyvalue_text(u):
    value = u.split(':')[1]
    return value.strip()

def city_name(u):
    value = value_from_keyvalue_text(u)
    value = value.split('/')[0]
    return value.strip().encode('utf-8')

class CoopLoader(XPathItemLoader):

    name_out = MapCompose(unicode.strip)
    address_out = MapCompose(value_from_keyvalue_text)
    district_out = MapCompose(value_from_keyvalue_text)
    city_out = MapCompose(city_name)
    postal_code_out = MapCompose(value_from_keyvalue_text)
    material_out = MapCompose(value_from_keyvalue_text)
