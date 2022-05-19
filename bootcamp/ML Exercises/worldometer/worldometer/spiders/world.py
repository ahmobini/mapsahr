'''import scrapy


class WorldSpider(scrapy.Spider):
    name = 'world' 
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country']

    def parse(self, response):
        countries = response.xpath('//*[@id="example2"]/tbody/tr') 
       # print(countries) # ye list bar migardoone ke bayad roosh halghe bezanim
        for country in countries:
            country_name = country.xpath(".//td[2]/a/text()").get() #text() mohtaviat ro bar migardoone, get() nazanim data ro bar migardoone
            # population = country.xpath('.//td[3]/text()').get()
            # Yearly_change = country.xpath('td[4]/text()').get() 
            # print(country_name)
            # print(population)
            # # print(Yearly_change)

            # yield {
            #     'country': country_name,
            #     'population': population
            # }

            link = country.xpath(".//td[2]/a/@href").get()
            yield response.follow(url = link, callback = self.parse_country, meta = {'name': country_name}) # url ro bedim engar roosh click mikone mire dakhelesh
        

        def parse_country():
            country = response.meta.get('name')
            # rows = response.xpath('//*[@id="example2"]/tbody/tr') 
       # print(countries) # ye list bar migardoone ke bayad roosh halghe bezanim
            rows = response.xpath('.//div[5]/table/tbody/tr')
            for row in rows:
                year = row.xpath('.//td/text()').get()
                population = row.xpath('.//td/')

                yield {
                    'country_name' : country,
                    'year' : year,
                    'population' : population

                }
            # country_name = country.xpath(".//td[2]/a/text()").get() #text() mohtaviat ro bar migardoone, get() nazanim data ro bar migardoone
            # population = country.xpath('.//td[3]/text()').get()
            # Yearly_change = country.xpath('td[4]/text()').get() 
            # print(country_name)
            # print(population)
'''
import scrapy

class DivarCrawlerSpider(scrapy.Spider):
    