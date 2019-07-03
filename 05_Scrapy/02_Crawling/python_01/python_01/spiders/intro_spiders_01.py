import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'

    def start_requests(self):
        urls = [
            'http://books.toscrape.com/catalogue/category/books_1/index.html'
        ]

        for url in urls:
            yield scrapy.Request(url=url)


    def parse(self,response):
        etiqueta_contenedor = response.css(".product_pod")
                
        titulos = etiqueta_contenedor.css("h3 > a::attr(title)").extract()
        stocks = etiqueta_contenedor.css('div.product_price > p.instock.availability::text').extract()

        precios = etiqueta_contenedor.css('div.product_price > p.price_color::text').extract()
        print(titulos)
        print(stocks)
        print(precios)

      

        with open('prueba.txt','+a') as file:
            file.writelines(titulos)
            file.writelines(stocks)
            file.writelines(precios)