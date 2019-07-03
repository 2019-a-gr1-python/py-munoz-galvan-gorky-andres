clear
contenedor = response.css('div.product-tile-inner')
titulo = contenedor.css('a.name::text')
contenedor.xpath('//div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src')
contenedor.xpath('//div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src').extract()
url = contenedor.xpath('//div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src').extract()
url = contenedor.xpath('//div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src')
class ProductoFybeca(scrapy.Item):
    titulo = scrapy.Field()
    imagen = scrapy.Field()
primer_producto = ProductoFybeca()
primer_producto['titulo'] = titulo.extract_first()
primer_producto['imagen'] = url.extract_first()
primer_producto
def transformar_url_imagen(text):
    url = 'https://www.fybeca.com'
    cadena_a_reemplazar = '../..'
    return texto.replace(cadena_a_reemplazar,url)
class ProductoFybeca(scrapy.Item):
    titulo = scrapy.Field()
    imagen = scrapy.Field()
from scrapy.loader.processors import MapCompose

class ProductoFybeca(scrapy.Item):
    titulo = scrapy.Field()
    imagen = scrapy.Field(
        //div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src
        
        
        a
    )
class ProductoFybeca(scrapy.Item):
    titulo = scrapy.Field()
    imagen = scrapy.Field(
        //div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src
        
       
       
     
    )
class ProductoFybeca(scrapy.Item):
    titulo = scrapy.Field()
    imagen = scrapy.Field(
        input_processor = MapCompose(transformar_url_imagen) 
    )
primer_producto['titulo'] = titulo.extract_first()
primer_producto['imagen'] = url.extract_first()
primer_producto
class ProductoFybecaDos(scrapy.Item):
    titulo = scrapy.Field()
    imagen = scrapy.Field(
        input_processor = MapCompose(transformar_url_imagen) 
    )
primer_producto_dos = ProductoFybecaDos()
%history -f items.py
