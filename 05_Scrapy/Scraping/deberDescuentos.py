import numpy as np
product_names = response.css('.product-tile-inner > .name::text').extract()
product_names
product_names = np.array(product_names)
product_names
precio_normal = list(map(lambda x: x.split(')')[0][12:] , response.css('div.side > div.price::attr(data-bind)').extract()))
precio_normal
precio_normal
precio_normal = np.array(precio_normal)
precio_normal
precio_normal = np.array(precio_normal,dtype='float32')
precio_normal
precio_con_descuento = list( map(lambda x: x.split(')')[0][12:],response.css('div.price-member > div::attr(data-bind)').extract()))
precio_con_descuento = np.array(precio_con_descuento,dtype='float32')
precio_con_descuento
precio_final = precio_normal - precio_con_descuento
precio_final
producto_mayor_precio_final = product_names[precio_final == precio_final.max()]
producto_mayor_precio_final
precio_normal[product_names == producto_mayor_precio_final[0]]
precio_con_descuento[product_names == producto_mayor_precio_final[0]]
%history -f deberDescuentos.py
