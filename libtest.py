import math
# import matplotlib.pyplot as plt
from operator import itemgetter

# print(math.sqrt(10))

# x=[]
# y=[]

# print(plt.get_backend())


# for i in range(0, 360,1):
#     angulo= math.radians(i)
#     x.append(angulo)
#     y.append(math.sin(angulo))

# plt.plot(x, y)
# plt.ylabel("Funcion seno")
# plt.show(block=True)

# print("Usted ha elegido la opción 3")
                        # break
                        # RF01: El programa dispone de manera predefinida la ubicación de
                        # cuatro zonas wifi con su respectivo promedio de usuarios.

# zona_1=[10.127, -74.950, 0]
# zona_2= [10.196, -74.935, 0]
# zona_3= [10.305, -75.040, 2490]
# zona_4=[10.196, -74.935, 101]

# zonas_wifi=[zona_1, zona_2, zona_3, zona_4]
# trabajo=[10.103, -74.902]

# def distancia(valor1, valor2):
#     global zona_1
#     global zona_2
#     global zona_3
#     global zona_4
#     global trabajo
#     global casa
#     global parque

#     # Radio de la tierra -- r=d/2
#     r = 6372.795477598
#     lat1 = math.radians(trabajo[0])
#     lon1 = math.radians(trabajo[1])

#     lat2 = math.radians(zona_1[0])
#     lon2 = math.radians(zona_1[1])

#     print (lat1, lon1, lat2, lon2 )
#     lat_delta = lat2-lat1
#     lon_delta = lon2-lon1

#     seno_lat=(math.sin(lat_delta/2)**2)
#     seno_lon=(math.sin(lon_delta/2)**2)
    
#     cos_lat2 = math.cos(lat2)*seno_lon
#     cos_lat1 = math.cos(lat1)*cos_lat2
 
#     asin_raiz = math.asin(math.sqrt(seno_lat+cos_lat1))


#     distancia_wifi=((2*r)*asin_raiz)*1000
   
#     return distancia_wifi


# print(distancia())

def x():

    zona_1=[10.127, -74.950, 0, 10]
    zona_2= [10.196, -74.935, 0, 100]
    zona_3= [10.305, -75.040, 2490, 985]
    zona_4=[10.196, -74.935, 101, 1500]


    zonas=[zona_1, zona_2, zona_3, zona_4]

    zonas_ordenadas_cercanos=sorted(zonas ,key=itemgetter(2))
    zonas_ordenadas=sorted(zonas_ordenadas_cercanos, key=itemgetter(3))

    print(zonas_ordenadas)

    print(zonas_ordenadas[0][3], zonas_ordenadas[0][2])
    print(zonas_ordenadas[1][3], zonas_ordenadas[1][2])
    print(zonas_ordenadas[2][3], zonas_ordenadas[2][2])
    print(zonas_ordenadas[3][3], zonas_ordenadas[3][2])

print(x())