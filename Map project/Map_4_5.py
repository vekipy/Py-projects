import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from mpl_toolkits.basemap import Basemap
from geopy.geocoders import Nominatim
import pandas as pd

plt.ion()
fig=plt.figure(figsize=(70,70), edgecolor='w')
m = Basemap(projection='cyl', llcrnrlat=-90, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180, resolution='c')
m.etopo(scale=0.5, alpha=0.5)
m.drawparallels(np.arange(-90.,91.,15.))
m.drawmeridians(np.arange(-180.,181.,30.))

spomenici=pd.read_excel("C:/Users/User/Desktop/Python mapa/sites-2017.xls");
geolocator=Nominatim()


 
def velicina (e):
    vel=0;
    if (0<=e<=137224.8356):
        vel=3;
    elif (137224.8356<=e<=274449.6713):
        vel=5;
    elif (274449.6713<=e<=20275275.16):
        vel=10;
    elif e>20275275.16:
        vel=15;
    return (vel)



def stamp ():
  global spomenici
  for i in range(len(spomenici)):
    b=spomenici.loc[i,'name_en']
    c=spomenici.loc[i,'area_hectares']
    d=m(spomenici.loc[i,'longitude'], spomenici.loc[i,'latitude'])
    f=velicina(c);
    if f==3:
     mali=plt.plot(d[0],d[1],'ok',color='b',markersize=f)
     plt.text(d[0]+0.5,d[1]+0.5,b,fontsize=5,ha='center',) 
    elif f==5:
     s_m=plt.plot(d[0],d[1],'ok',color='b',markersize=f)
     plt.text(d[0]+0.5,d[1]+0.5,b,fontsize=5,ha='left') 
    elif f==10:
     s_v=plt.plot(d[0],d[1],'ok',color='b',markersize=f)
     plt.text(d[0]+0.5,d[1]+0.5,b,fontsize=5,ha='right')
    elif f==15:
     v=plt.plot(d[0],d[1],'ok',color='b',markersize=f)
     plt.text(d[0]+0.5,d[1]+0.5,b,fontsize=5,ha='center') 
    if i>249:
        if f==3:
         nmali,=plt.plot(d[0],d[1],'ok',color='r',markersize=f)
         plt.text(d[0]+0.5,d[1]+0.5,b,fontsize=7,color='r',ha='right') 
        elif f==5:
         ns_m,=plt.plot(d[0],d[1],'ok',color='r',markersize=f)
         plt.text(d[0]+0.5,d[1]+0.5,b,fontsize=7,color='r',ha='right') 
        elif f==10:
         ns_v,=plt.plot(d[0],d[1],'ok',color='r',markersize=f)
         plt.text(d[0]+0.5,d[1]+0.5,b,fontsize=7,color='r',ha='right')
        elif f==15:
         nv,=plt.plot(d[0],d[1],'ok',color='r',markersize=f)
         plt.text(d[0]+0.5,d[1]+0.5,b,fontsize=7,color='r',ha='right') 
      
  plt.legend((mali[0],s_m[0], s_v[0],v[0]),('Mali/Small','Srednje mali/Middle small',\
             'Srednje veliki/Middle big','Veliki/Big'),loc='upper right')
  plt.title('Svetski spomenici od kulturnog znacaja',fontsize=16,style=('italic')) 
  plt.show()
  plt.pause(12)
  

stamp()

while True:
     ime=raw_input('Unesite naziv novog kulturnog spomenika \n \
                   Input monument name: ')
     mesto=raw_input('Unesite naziv mesta spomenika \n\
                     Input name of the place: ')
     try: 
         vel2=int(input('Unesite povrsinu spomenika u ha \n \
                        Input size of area in hectares: '))
     except ( NameError,TypeError): 
        vel2=input('Pogresan unos. Unesite povrsinu spomenika u ha \n \
                   Wrong input. Input the size again: ')
     location=geolocator.geocode(mesto);
     if location==None:
         mesto=raw_input('Pogresan naziv mesta. Unesite naziv mesta ponovo \n \
                         Wrong name of place. Input it again: ')
         location=geolocator.geocode(mesto);
     else: pass
     lo=location.longitude
     la=location.latitude
     dodatak={"name_en":ime,"longitude":lo,"latitude":la,"area_hectares":vel2}
     spomenici=spomenici.append(dodatak,ignore_index=True)
     unos=raw_input('Da li ste zavrsili sa unosom? d/n \n\
                    Are you finish with inputs?  d(yes)/n(no): ')
     if unos=='d':break
     elif unos=='n':
      continue


#
ani=anim.FuncAnimation(fig, stamp(), interval=1000)

#    


   