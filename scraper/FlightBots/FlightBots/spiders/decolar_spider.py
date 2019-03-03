from scrapy import Spider
from scrapy.selector import Selector

from  FlightBots.items import FlightbotsItem

class DecolarSpider(Spider):
    name="Decolar"
    allowed_domains = ["Decolar.com"]
    start_urls = ["https://www.decolar.com/shop/flights/search/roundtrip/BEL/SFO/2019-08-02/2019-08-15/2/0/0/"]

    def parse(self, response):
        flights = Selector(response).xpath('//*[@id="clusters"]/span[1]/span[1]/cluster/div/div/div/span')
        
        for flight in flights:
            item = FlightbotsItem()
            item['flight'] = {
                depart_airport : flight.xpath('//*route-info-item[1]/span/airport-item/span'),
                depart_city: flight.xpath('//*route-info-item[2]/span/span/span')
            }
            yield item
