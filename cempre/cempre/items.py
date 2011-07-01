# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class CempreItem(Item):

    name = Field()
    address = Field()
    district = Field()
    city = Field()
    postal_code = Field()
    material = Field()
