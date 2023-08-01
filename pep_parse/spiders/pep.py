import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for pep in response.css('#numerical-index tbody tr'):
            yield response.follow(
                pep.css('a::attr(href)').get(),
                callback=self.parse_pep,
                cb_kwargs=dict(
                    number=pep.css('a::text').get(),
                    name=pep.css('a::text').getall()[1]
                )
            )

    def parse_pep(self, response, number, name):
        yield PepParseItem(
            number=number,
            name=name,
            status=response.css('dl[class^="rfc2822"] abbr::text').get()
        )
