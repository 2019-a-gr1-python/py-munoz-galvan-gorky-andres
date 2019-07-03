contenedor = response.css('div.product-tile-inner')
titulo = contenedor.css('a.name::text')
contenedor.xpath('//div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src')
url = contenedor.xpath('//div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src')
def transformar_url_imagen(texto):
    
    url = 'https://www.fybeca.com'
    cadena_a_reemplazar = '../..'
    return texto.replace(cadena_a_reemplazar,url)
from scrapy.loader.processors import MapCompose
class ProductoFybecaDos(scrapy.Item):
    titulo = scrapy.Field()
    imagen = scrapy.Field(
        input_processor = MapCompose(transformar_url_imagen) 
    )
it = ItemLoader(item=ProductoFybecaDos())
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader
it = ItemLoader(item=ProductoFybecaDos())
id.add_value('imagen',url.extract_first())
il.add_value('imagen',url.extract_first())
il = ItemLoader(item=ProductoFybecaDos())
il.add_value('imagen',url.extract_first())
il.add_value('titulo', titulo.extract_first())
il.load_item()
%history -f itemLoader.py
