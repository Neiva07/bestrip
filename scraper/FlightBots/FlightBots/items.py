from scrapy.item import Item, Field


class FlightbotsItem(Item):
    price = Field()
    bag = Field()
    date = Field()
    flight = Field()
    company = Field()
    link_URL = Field()
    provider = Field()
