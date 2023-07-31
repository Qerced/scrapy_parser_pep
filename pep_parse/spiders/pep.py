import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org/']

    def parse(self, response):
        for pep in ...:
            yield response.follow(
                pep,
                callback=self.parse_pep,
                cb_kwargs=dict(number=..., name=...)
            )

    def parse_pep(self, response, number, name):
        data = {
            'number': number,
            'name': name,
            'status': ...
        }
        yield PepParseItem(data)
