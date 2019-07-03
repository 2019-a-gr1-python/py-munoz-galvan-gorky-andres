import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlOnu(CrawlSpider):
    name = 'crawl_books' #Heredado (conservar el nombre)
    allowed_domains = [ #Heredado (conservar el nombre)
        'books.toscrape.com'
    ]
    start_urls = [ #Heredado (conservar el nombre)
        'http://books.toscrape.com'
    ]
    
    regla_uno = ( #Heredado (conservar el nombre)
        Rule(LinkExtractor(), callback='parse_page')
        ,
    )

    url_segmento_permitido = ('mystery_3','fantasy_19')

    regla_dos = ( #Heredado (conservar el nombre)
        Rule(LinkExtractor(
            allow_domains = allowed_domains,
            allow=url_segmento_permitido
        ), callback='parse_page')
        ,
    )

    

    url_segmento_restringido = (
        'ar/sections',
        'zh/sections',
        'ru/sections'
    )

    regla_tres = ( #Heredado (conservar el nombre)
        Rule(LinkExtractor(
            allow_domains = allowed_domains,
            allow=url_segmento_permitido,
            deny = url_segmento_restringido
        ), callback='parse_page')
        ,
    )

    rules = regla_dos

    def parse_page(self,response):
        lista_libros = response.css('li > article.product_pod > h3 > a::attr(title)').extract()

        for libro in lista_libros:
            with open('libros.txt','a+') as archivo:
                archivo.write(libro+'\n')


