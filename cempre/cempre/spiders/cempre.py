from scrapy.http.request.form import FormRequest
from scrapy.http import Request
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.shell import inspect_response

from ..items import CempreItem
from ..loaders import CoopLoader


class CempreSpider(BaseSpider):
    name = "cempre"
    allowed_domains = ["cempre.org.br"]
    start_urls = ['http://www.cempre.org.br/servicos_resultado.php']
    DOMAIN = 'http://www.cempre.org.br/'

    def make_requests_from_url(self, url):
        return FormRequest(url, dont_filter=True, formdata={
            'cidade': 'XX',
            'codeps': 'fHx8fHx8fHwz',
            'enviado': '1',
            'estado': 'XX',
            'material': 'XX',
            'x': '79',
            'y': '7',
        })

    def parse(self, response):
        items = self.parse_coops(response)
        items += self.parse_pages(response)

        return items

    def parse_coops(self, response):
        coops = []
        hxs = HtmlXPathSelector(response)
        groups = hxs.select('//span[@class="tit_empresa_pesquisa"]/..')

        for group in groups:
            loader = CoopLoader(item=CempreItem(), response=response, selector=group)

            loader.add_xpath('name', './span/text()[1]')
            loader.add_xpath('address', './text()[1]')
            loader.add_xpath('district', './text()[2]')
            loader.add_xpath('city', './text()[3]')
            loader.add_xpath('postal_code', './text()[4]')
            loader.add_xpath('material', './text()[5]')

            coops.append(loader.load_item())

        return coops

    def parse_pages(self, response):
        requests = []
        hxs = HtmlXPathSelector(response)
        pages = hxs.select('//p[@class="font_text"]/a/@href').extract()

        for page in pages:
            page_absurl = self.DOMAIN + page

            requests.append(Request(page_absurl, callback=self.parse_coops))

        return requests
