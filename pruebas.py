#!/usr/bin/env python
#-*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()


#EUROPA---------------------------------------------------------------------------

#Italia
G.add_node("Roma", pos=(100, -60))#YA
G.add_node("Milán", pos=(80, -30))#YA
G.add_node("Venecia", pos=(130,-70))#YA

Italia = ["Roma","Milán","Venecia"]


#Francia
G.add_node("París", pos=(150,60))#YA
G.add_node("Montpellier", pos=(170,60))#YA
G.add_node("Versalles", pos=(190,80))#YA

Francia = ["París","Montpellier","Versalles"]


#España
G.add_node("Madrid", pos=(80, 40))#YA
G.add_node("Barcelona", pos=(100,30))#YA
G.add_node("Valencia", pos=(110,-10))#YA

España = ["Madrid", "Barcelona", "Valencia"]


#Alemania
G.add_node("Berlín", pos=(170, 80))#YA
G.add_node("Hamburgo", pos=(165, 90))#YA
G.add_node("Fráncfort", pos=(150, 100))#YA
G.add_node("Zúrich",pos=(170,70))#YA
G.add_node("Múnich",pos=(190,80))#YA

Alemania = ["Zúrich","Berlín", "Hamburgo", "Fráncfort"]


#Polonia
G.add_node("Torun", pos=(190,130))#YA
G.add_node("Cracovia", pos=(130,150))#YA
G.add_node("Varsovia", pos=(150,140))#YA

Polonia = ["Torun", "Cracovia", "Varsovia"]


#Inglaterra
G.add_node("Londres", pos=(100,500))#YA
G.add_node("Mánchester", pos=(115,480))#YA
G.add_node("Birmingham", pos=(130,490))#YA

Inglaterra = ["Londres", "Mánchester", "Birmingham"]


#Irlanda
G.add_node("Dublín", pos=(150,300))#YA
G.add_node("Cork", pos=(120,250))#YA

Irlanda = ["Dublín", "Cork"]


#Portugal
G.add_node("Lisboa", pos=(70,130))#YA
G.add_node("Braga", pos=(90,140))#YA

Portugal = ["Lisboa", "Braga"]


#Grecia
G.add_node("Atenas", pos=(160,210))#YA

Grecia = ["Atenas"]


#Rumanía
G.add_node("Bucarest", pos=(130,50))#YA
G.add_node("Sibiu", pos=(150,70))#YA

Rumanía = ["Bucarest", "Sibiu"]


#Austria
G.add_node("Viena", pos=(150,300))#YA

Austria = ["Viena"]

#Finlandia
G.add_node("Helsinki", pos=(180,310))#YA
G.add_node("Turku", pos=(170,290))#YA

Finlandia = ["Helsinki","Turku"]

#Suecia
G.add_node("Estocolmo", pos=(100,600))#YA

Suecia = ["Estocolmo"]

#Países bajos

G.add_node("Ámsterdam",pos=(150,100))#YA
PaisesBajos = ["Ámsterdam"]

Europa = [Italia, Francia, España, Alemania, Polonia, Inglaterra, Irlanda, Portugal, Grecia, Rumanía, Austria, Finlandia,Suecia, PaisesBajos]
Europa1 = ["Italia", "Francia", "España", "Alemania", "Polonia", "Inglaterra", "Irlanda", "Portugal", "Grecia", "Rumanía", "Austria", "Finlandia", "Suecia", "Paises Bajos"]

#AFRICA---------------------------------------------------------------------------

#Marruecos
G.add_node("Rabat", pos=(130,-250))#YA
G.add_node("Tánger", pos=(140,-230))#YA

Marruecos = ["Rabat", "Tánger"]


#Argelia
G.add_node("Argel", pos=(160,-200))#YA
G.add_node("Orán", pos=(180,-215))#YA

Argelia = ["Argel", "Orán"]


#Egipto
G.add_node("El Cairo", pos=(120,-90))#YA
G.add_node("Hurgada", pos=(150,-100))#YA

Egipto = ["El Cairo", "Hurgada"]


#Sudán
G.add_node("Jartum", pos=(140,-60))#YA

Sudán = ["Jartum"]


#Nigeria
G.add_node("Abuya", pos=(170,-30))#YA

Nigeria = ["Abuya"]

#Angola
G.add_node("Luanda", pos=(210,-30))#YA

Angola = ["Luanda"]


#Botsuana
G.add_node("Gaborone", pos=(190,-200))#YA
G.add_node("Maun", pos=(170,-230))#YA

Botsuana = [ "Gaborone", "Maun"]


#Sudáfrica
G.add_node("Johannesburgo", pos=(210,-210))#YA
G.add_node("Durban", pos=(200,-200))#YA

Sudáfrica = ["Johannesburgo", "Durban"]

Africa1 = ["Marruecos", "Argelia", "Egipto", "Sudán", "Nigeria","Angola", "Botsuana", "Sudáfrica"]
Africa = [Marruecos, Argelia, Egipto, Sudán, Nigeria, Angola, Botsuana, Sudáfrica]

#ASIA---------------------------------------------------------------------------

#Rusia
G.add_node("Moscú", pos=(150, 90))#YA
G.add_node("Sochi", pos=(140, 120))#YA
G.add_node("Kazán", pos=(180,100))#YA

Rusia = ["Moscú","Kazán", "Sochi"]


#Turquía
G.add_node("Ankara", pos=(120,350))#YA
G.add_node("Estambul", pos=(100,300))#YA
G.add_node("Antalya", pos=(115,325))#YA

Turquía = ["Estambul", "Ankara", "Antalya"]


#India
G.add_node("Bombay", pos=(140,180))#YA
G.add_node("Nueva Delhi", pos=(120,160))#YA

India = ["Bombay", "Nueva Delhi"]

#China
G.add_node("Pekín", pos=(210, 60))#YA
G.add_node("Shanghái", pos=(230,40))#YA
G.add_node("Shenzhen", pos=(220,50))#YA
G.add_node("Hong Kong",pos=(240,60))#YA

China = ["Pekín", "Shanghái", "Shenzhen"]

#Kazajistán
G.add_node("Astaná", pos=(200,310))#YA
G.add_node("Shymkent", pos=(220,300))#YA

Kazajistán = ["Astaná", "Shymkent"]


#Uzbekistán
G.add_node("Samarcanda", pos=(300,400))#YA
G.add_node("Taskent", pos=(330,390))#YA

Uzbekistán = ["Samarcanda", "Taskent"]


#Arabia Saudita
G.add_node("Meca", pos=(200,40))#YA
G.add_node("Riad", pos=(220,20))#YA
G.add_node("Abha", pos=(230,0))#YA

ArabiaSaudita = ["Meca", "Riad", "Abha"]


#Emiratos Árabes Unidos
G.add_node("Dubái", pos=(210,80))#YA
G.add_node("Abu Dabi", pos=(230,100))#YA

EmiratosÁrabesUnidos = ["Dubái", "Abu Dabi"]

#Indonesia
G.add_node("Yakarta", pos=(300,470))#YA
G.add_node("Surabaya", pos=(320,450))#YA

Indonesia = ["Yakarta", "Surabaya"]

#Tailandia
G.add_node("Bangkok", pos=(300,120))#YA
G.add_node("Phuket", pos=(280,80))#YA

Tailandia = ["Bangkok", "Phuket"]


#Corea del Sur
G.add_node("Seúl", pos=(380,100))#YA
G.add_node("Busan", pos=(400,120))#YA
G.add_node("Daejeon", pos=(420,140))#YA

CoreaDelSur = ["Seúl", "Busan", "Daejeon"]


#Corea del Norte
G.add_node("Kaesong", pos=(450,130))#YA
G.add_node("Haeju", pos=(480,170))#YA

CoreaDelNorte = ["Kaesong", "Haeju"]


#Japon
G.add_node("Tokio", pos=(500, 300))#YA
G.add_node("Hiroshima", pos=(480,320))#YA
G.add_node("Kioto", pos=(490,280))#YA

Japón = ["Tokio", "Hiroshima", "Kioto"]


#Filipinas
G.add_node("Manila", pos=(380,0))#YA
G.add_node("Cebú", pos=(350,-20))#YA

Filipinas = ["Manila", "Cebú"]


Asia = [Rusia, Turquía, India, China,Kazajistán, Uzbekistán, ArabiaSaudita, EmiratosÁrabesUnidos, Indonesia,Tailandia, CoreaDelSur, CoreaDelNorte, Japón, Filipinas]
Asia1 = ["Rusia", "Turquía", "India", "China", "Kazajistán", "Uzbekistán", "Arabia Saudita", "Emiratos Árabes Unidos", "Indonesia", "Tailandia","Corea del Sur", "Corea del Norte", "Japón", "Filipinas"]

#OCEANÍA---------------------------------------------------------------------------


#Australia
G.add_node("Perth", pos=(620,40))#YA
G.add_node("Sídney", pos=(650, 50))#YA
G.add_node("Melbourne", pos=(680, 80))#YA
G.add_node("Brisbane", pos=(670,40))

Australia = ["Perth", "Sídney", "Melbourne", "Brisbane"]


#Nueva Zelanda
G.add_node("Wellington", pos=(580,100))#YA
G.add_node("Auckland", pos=(550,110))#YA

NuevaZelanda = ["Wellington", "Auckland"]


Oceanía = [Australia, NuevaZelanda]
Oceanía1 = ["Australia", "Nueva Zelanda"]

#SUR AMÉRICA---------------------------------------------------------------------------

#Colombia
G.add_node("Bogotá", pos=(-100, -100))#YA
G.add_node("Medellin", pos=(-60,-40))#YA
G.add_node("Cartagena", pos=(60, -70))#YA

Colombia = ["Bogotá","Medellin","Cartagena"]

#Ecuador
G.add_node("Quito", pos=(-200,-50))#YA
G.add_node("Guayaquil", pos=(-250,-90))#YA

Ecuador = ["Quito","Guayaquil"]

#Perú
G.add_node("Lima", pos=(-20, -100))#YA
G.add_node("Cusco", pos=(-50,-130))#YA

Perú = ["Lima","Cusco"]

#Brasil
G.add_node("Río de Janeiro", pos=(5, -100))#YA
G.add_node("Sao Pablo", pos=(50,-90))#YA


Brasil = ["Río de Janeiro","Sao Pablo"]

#Chile
G.add_node("Santiago", pos=(-140,-80))#YA
G.add_node("Concepción", pos=(-180,-100))#YA

Chile = ["Santiago","Concepción"]

#Argentina
G.add_node("Buenos Aires", pos=(-150,-90))#YA
G.add_node("La Plata", pos=(-160,-200))#YA

Argentina = ["Buenos Aires","La Plata"]

#Uruguay
G.add_node("Montevideo", pos=(-130,-100))#YA
G.add_node("Punta del Este", pos=(-110,-70))#YA

Uruguay = ["Montevideo","Punta del Este"]

SurÁmerica = [Colombia,  Ecuador, Perú, Brasil, Chile, Argentina, Uruguay]
SurÁmerica1 = ["Colombia", "Ecuador", "Perú", "Brasil", "Chile", "Argentina", "Uruguay"]

#NORTE ÁMERICA---------------------------------------------------------------------------

#Estados Unidos
G.add_node("Houston", pos=(-80, 85))#YA
G.add_node("Dallas", pos=(-90,100))#YA
G.add_node("Nueva Orleans", pos=(-100,110))#YA
G.add_node("Seattle", pos=(-110,120))#YA
G.add_node("San Francisco", pos=(-130,140))#YA
G.add_node("Las Vegas", pos=(-140,150))#YA
G.add_node("Los Ángeles", pos=(-150,160))#YA
G.add_node("Atlanta", pos=(-200,210))#YA
G.add_node("Orlando", pos=(-220, 230))#YA
G.add_node("Miami", pos=(-240,250 ))#YA
G.add_node("Washington", pos=(-180,190))#YA
G.add_node("New York", pos=(-170,80))#YA
G.add_node("Chicago", pos=(-210,80))#YA

EstadosUnidos = ["Houston","Dallas","Nueva Orleans","Seattle","San Francisco","Las Vegas","Los Ángeles","Atlanta","Orlando","Miami","Washington","New York","Chicago"]

#Panamá
G.add_node("Ciudad de Panamá", pos=(0, -70))#YA

Panamá = ["Ciudad de Panamá"]

#Costa Rica
G.add_node("Cartago", pos=(-300,80))#YA
G.add_node("San José", pos=(-320,100))#YA
G.add_node("Liberia", pos=(-310,60))

CostaRica = ["Cartago","San José","Liberia"]

#Cuba
G.add_node("La Habana", pos=(-310,-100))#YA

Cuba = ["La Habana"]

#México
G.add_node("Ciudad de México", pos=(-380,120))#YA
G.add_node("Guadalajara", pos=(-350,90))#YA
G.add_node("Monterrey", pos=(-330,180))#YA
G.add_node("Acapulco", pos=(-400,200))#YA
G.add_node("Cancún", pos=(-390,230))#YA

México = ["Ciudad de México","Guadalajara","Monterrey","Acapulco","Cancún"]

#Canadá
G.add_node("Toronto", pos=(-10,150))#YA
G.add_node("Montreal", pos=(-25, 135))#YA
G.add_node("Vancouver", pos=(-30,170))#YA
G.add_node("Winnipeg", pos=(-80,10))
G.add_node("Ottawa", pos=(-60,110))#YA#YA

Canadá = ["Toronto","Montreal","Vancouver","Winnipeg","Ottawa"]

NorteÁmerica = [EstadosUnidos, Panamá, CostaRica, Cuba, México, Canadá]
NorteÁmerica1 =["Estados Unidos", "Panamá", "Costa Rica", "Cuba", "México", "Canadá"]

#-----------------------------------------------------ARISTAS---------------------------------------------------------------------------
G.add_edge("Bogotá","Cartagena", weight = 1.20)
G.add_edge("Bogotá","Medellin", weight = 0.48)
G.add_edge("Bogotá","Miami", weight = 3.31)
G.add_edge("Bogotá", "Ciudad de Panamá", weight = 1.27)
G.add_edge("Ciudad de Panamá", "La Habana", weight = 2.28)
G.add_edge("Ciudad de Panamá", "Valencia", weight = 10.20)
G.add_edge("Bogotá","Atlanta",weight= 4.42)
G.add_edge("Atlanta","New York",weight=2.02)
G.add_edge("Miami","New York",weight=2.41)
G.add_edge("Roma","Milán",weight=1.06)
#G.add_edge("Milán","New York",weight=) ########
G.add_edge("Roma","Zúrich",weight=1.22)
#G.add_edge("New York","Zúrich",weight=) #####8.22
G.add_edge("Roma","Madrid",weight=2.10)
#G.add_edge("Madrid","Bogotá",weight=) ######10.30
#G.add_edge("Madrid","Medellin",weight=)######
G.add_edge("Venecia","Madrid",weight=2.16)
G.add_edge("Venecia","Zúrich",weight=0.58)
G.add_edge("Zúrich","Fráncfort",weight=0.52)
#G.add_edge("Fráncfort","Bogotá",weight=)#######11.48
G.add_edge("Madrid","París",weight=1.50)
G.add_edge("Londres","París",weight=0.56)
G.add_edge("Milán","Madrid",weight=1.59)
G.add_edge("Milán","París",weight=1.19)
G.add_edge("Milán","Viena",weight=1.20)
G.add_edge("Viena","Moscú",weight=2.35)
G.add_edge("Moscú","Múnich",weight=2.56)
G.add_edge("Múnich","Fráncfort",weight=0.53)
G.add_edge("Fráncfort","Milán",weight=1.09)
G.add_edge("Melbourne","Sídney",weight=1.23)
G.add_edge("Moscú","Abu Dabi",weight=5.07)#######
G.add_edge("Moscú","Dubái",weight=5.02)######
G.add_edge("Helsinki","Moscú",weight=1.41)
#G.add_edge("Helsinki","Hong Kong",weight=)######10.14
G.add_edge("Bogotá","Toronto",weight=5.55)######
G.add_edge("Toronto","Vancouver",weight=4.41)
#G.add_edge("Vancouver","Melbourne",weight=)######
#G.add_edge("Bogotá","Los Ángeles",weight=)######
#G.add_edge("Los Ángeles","Auckland",weight=)#####13.31
G.add_edge("Auckland","Melbourne",weight=3.48)
#G.add_edge("Bogotá","Múnich",weight=)#####
#G.add_edge("Bogotá","Abu Dabi",weight=)#####
#G.add_edge("Abu Dabi","Melbourne",weight=)#####14.59
G.add_edge("Toronto","Winnipeg",weight=2.23)
G.add_edge("Ottawa","Toronto",weight=0.58)
#G.add_edge("Ciudad de Panamá","Montreal",weight=)######
G.add_edge("Toronto","Montreal",weight=1.07)
#G.add_edge("San José","Montreal",weight=)######
G.add_edge("Ciudad de México","Montreal",weight=5.07)####
#G.add_edge("Cartagena","Ámsterdam",weight=)#####
G.add_edge("Ámsterdam","Moscú",weight=3.11)
G.add_edge("Moscú","Sochi",weight=2.10)
G.add_edge("París","Moscú",weight=3.34)
G.add_edge("Ciudad de Panamá","Cancún",weight=2.40)
#G.add_edge("Medellin","Cancún",weight=)#####
G.add_edge("Madrid","Valencia",weight=0.52)
#G.add_edge("New York","Estambul",weight=)######10.32
G.add_edge("Estambul","Valencia",weight=3.36)
G.add_edge("Fráncfort","Valencia",weight=2.13)
G.add_edge("Madrid","Barcelona",weight=1.07)
#G.add_edge("Cartagena","Ámsterdam",weight=)#####
G.add_edge("Ámsterdam","Barcelona",weight=2.03)
G.add_edge("París","Barcelona",weight=1.35)
G.add_edge("Madrid","Viena",weight=2.45)
#G.add_edge("Ciudad de Panamá","Madrid",weight=)#####10.39
G.add_edge("Ámsterdam","Viena",weight=1.42)
#G.add_edge("Ámsterdam","Montpellier",weight=)#####
G.add_edge("París","Montpellier",weight=1.16)
#G.add_edge("Santo Domingo","París",weight=)#####9.27
#G.add_edge("Londres","Versalles",weight=)#####
G.add_edge("Bogotá","Houston",weight=4.57)
G.add_edge("Houston","Chicago",weight=2.22)
#G.add_edge("Chicago","Versalles",weight=)#####
G.add_edge("Ámsterdam","Berlín",weight=1.14)
#G.add_edge("Toronto","Zúrich",weight=)#####8.36
G.add_edge("Zúrich","Berlín",weight=1.20)
G.add_edge("Múnich","Berlín",weight=1.06)
G.add_edge("Ámsterdam","Varsovia",weight=1.53)
G.add_edge("París","Varsovia",weight=2.11)
G.add_edge("Estambul","Varsovia",weight=2.13)
G.add_edge("Madrid","Zúrich",weight=2.03)
G.add_edge("Zúrich","Varsovia",weight=1.48)
G.add_edge("Londres","Varsovia",weight=2.20)
#G.add_edge("Varsovia","Kazán",weight=)#####
G.add_edge("Kazán","Moscú",weight=1.24)
#G.add_edge("Varsovia","París",weight=2.11)
G.add_edge("Varsovia","Estocolmo",weight=1.26)
G.add_edge("Varsovia","Dubái",weight=5.40)####
#G.add_edge("Toronto","Londres",weight=)####7.37
G.add_edge("Londres","Dublín",weight=1.04)
G.add_edge("Estambul","Dublín",weight=4.11)
#G.add_edge("Miami","Londres",weight=)####9.21
G.add_edge("Ámsterdam","Dublín",weight=1.27)
G.add_edge("Múnich","Antalya",weight=3.00)
G.add_edge("Estambul","Antalya",weight=1.07)
G.add_edge("Estambul","Madrid",weight=3.56)
G.add_edge("Londres","Estambul",weight=3.38)
G.add_edge("Ámsterdam","Bucarest",weight=2.44)
#G.add_edge("Múnich","Bogotá",weight=)#####
G.add_edge("Múnich","Bucarest",weight=1.58)
G.add_edge("Barcelona","Bucarest",weight=2.59)


######ARISTAS QUE NO ESTAN EN EL GIT
G.add_edge("Bogotá","Quito",weight=1.24)
G.add_edge("Ciudad de Panamá","Quito",weight=1.47)
#G.add_edge("Ámsterdam","Cracovia",weight=)####
#G.add_edge("Quito","Ámsterdam",weight=)####
#G.add_edge("Quito","París",weight=)####
G.add_edge("Madrid","Hamburgo",weight=2.43)
G.add_edge("Múnich","Hamburgo",weight=1.15)
G.add_edge("Fráncfort","Hamburgo",weight=1.01)
#G.add_edge("Atlanta","París",weight=)####
G.add_edge("París","Hamburgo",weight=1.25)
#G.add_edge("Hamburgo","Torun",weight=)####
#G.add_edge("Torun","Estambul",weight=)####
#G.add_edge("Estambul","Bogotá",weight=)####
G.add_edge("París","Mánchester",weight=1.14)
#G.add_edge("Toronto","Dublín",weight=)####7.04
G.add_edge("Dublín","Mánchester",weight=0.50)
G.add_edge("Ámsterdam","Birmingham",weight=1.04)
G.add_edge("Fráncfort","Birmingham",weight=1.28)
G.add_edge("Múnich","Birmingham",weight=1.50)
G.add_edge("Estambul","Birmingham",weight=3.47)
G.add_edge("Birmingham","Ámsterdam",weight=1.04)
#G.add_edge("Ámsterdam","Cork",weight=)####
#G.add_edge("Ciudad de Panamá","Ámsterdam",weight=)####11.28
G.add_edge("París","Ámsterdam",weight=1.00)
#G.add_edge("Londres","Cork",weight=)####
G.add_edge("Lisboa","Madrid",weight=1.09)
#G.add_edge("Toronto","Viena",weight=)####9.10
G.add_edge("Viena","Lisboa",weight=3.23)
#G.add_edge("New York","Lisboa",weight=)####
#G.add_edge("Madrid","Braga",weight=)####
#G.add_edge("Estambul","Braga",weight=)####
#G.add_edge("Braga","Fráncfort",weight=)####
#G.add_edge("Fráncfort","Shanghái",weight=)####11.33
G.add_edge("Ámsterdam","Atenas",weight=3.13)
#G.add_edge("Ciudad de Panamá","Estambul",weight=)####
G.add_edge("Estambul","Atenas",weight=1.11)
G.add_edge("París","Atenas",weight=3.08)
G.add_edge("Fráncfort","Atenas",weight=2.46)
G.add_edge("Múnich","Sibiu",weight=1.43)
#G.add_edge("Miami","Múnich",weight=)####

###MAS
G.add_edge("París","Helsinki",weight=2.52)
G.add_edge("Helsinki","Turku",weight=0.42)
G.add_edge("Zúrich","Estocolmo",weight=2.21)
G.add_edge("Estocolmo","Turku",weight=0.50)#FIN EUROPA
G.add_edge("París","Rabat",weight=2.47)
G.add_edge("Madrid","Tánger",weight=1.13)
G.add_edge("París","Tánger",weight=2.29)
#G.add_edge("París","Argel",weight=)####
#G.add_edge("Fráncfort","Argel",weight=)####
#G.add_edge("Argel","Orán",weight=)####
G.add_edge("Estambul","Orán",weight=3.47)
G.add_edge("Bogotá","Washington",weight=5.14)
#G.add_edge("Washington","Estambul",weight=)####10.59
G.add_edge("Estambul","El Cairo",weight=2.02)
G.add_edge("Fráncfort","El Cairo",weight=4.08)
G.add_edge("Estambul","Hurgada",weight=2.30)
G.add_edge("El Cairo","Hurgada",weight=1.00)
G.add_edge("Estambul","Jartum",weight=4.02)
#G.add_edge("Madrid","Abu Dabi",weight=)####
G.add_edge("Abu Dabi","Jartum",weight=3.37)
#G.add_edge("Londres","Abu Dabi",weight=)####7.22
#G.add_edge("Estambul","Abuya",weight=)####
#G.add_edge("París","Abuya",weight=)####6.03
#G.add_edge("París","Luanda",weight=)####8.35
#G.add_edge("Fráncfort","Johannesburgo",weight=)####11.16
#G.add_edge("Johannesburgo","Gaborone",weight=)####
G.add_edge("Bogotá","Lima",weight=2.51)
#G.add_edge("Sao Pablo","Lima",weight=)####
#G.add_edge("Sao Pablo","Johannesburgo",weight=)####
G.add_edge("Johannesburgo","Maun",weight=1.33)
G.add_edge("Bogotá","Santiago",weight=5.46)
#G.add_edge("Sao Pablo","Santiago",weight=)####
G.add_edge("Johannesburgo","Durban",weight=1.08)
G.add_edge("Estambul","Ankara",weight=0.55)
#G.add_edge("Fráncfort","Bombay",weight=)####8.41
#G.add_edge("Ámsterdam","Bombay",weight=)####9.02
#G.add_edge("Fráncfort","Nueva Delhi",weight=)####
#G.add_edge("Londres","Nueva Delhi",weight=)####
#G.add_edge("Houston","San Francisco",weight=)####
#G.add_edge("San Francisco","Pekín",weight=)####
G.add_edge("Dallas","Miami",weight=2.45)
#G.add_edge("Dallas","Pekín",weight=)####
G.add_edge("Houston","Chicago",weight=2.22)
#G.add_edge("Chicago","Shanghái",weight=)####14.37
#G.add_edge("Fráncfort","Pekín",weight=)####10.13
G.add_edge("Pekín","Shanghái",weight=1.52)
G.add_edge("Bogotá","Dallas",weight=5.23)
G.add_edge("Pekín","Shenzhen",weight=2.56)
#G.add_edge("Madrid","Shanghái",weight=)####
G.add_edge("Shanghái","Shenzhen",weight=2.00)

#ULTIMAS ARISTAS
#G.add_edge("Fráncfort","Astana",weight=)####
#G.add_edge("Estambul","Astana",weight=)####
#G.add_edge("Moscú","New York",weight=)####
G.add_edge("Moscú","Shymkent",weight=3.57)
#G.add_edge("Ciudad de Panamá","New York",weight=)####
G.add_edge("Moscú","Samarcanda",weight=3.57)
G.add_edge("Londres","Moscú",weight=3.41)
G.add_edge("Madrid","Moscú",weight=4.47)
G.add_edge("Moscú","Taskent",weight=4.01)
G.add_edge("Estambul","Taskent",weight=4.42)
#G.add_edge("Washington","Estambul",weight=)####10.59
#G.add_edge("París","Riad",weight=)####6.18
#G.add_edge("Riad","Meca",weight=)####
G.add_edge("Estambul","Riad",weight=3.32)
G.add_edge("Fráncfort","Riad",weight=5.51)
#G.add_edge("París","Riad",weight=)
G.add_edge("Riad","Abha",weight=1.34)
G.add_edge("El Cairo","Abha",weight=2.40)
#G.add_edge("Ciudad de México","Tokio",weight=)####
G.add_edge("Bogotá","Ciudad de México",weight=4.26)
#G.add_edge("Tokio","Yakarta",weight=)####7.41
#G.add_edge("Los Ángeles","Hong Kong",weight=)####15.02
G.add_edge("Hong Kong","Surabaya",weight=4.36)
#G.add_edge("New York","Hong Kong",weight=)####
#G.add_edge("Abu Dabi","Bangkok",weight=)####6.41
#G.add_edge("Madrid","Abu Dabi",weight=)####
#G.add_edge("Fráncfort","Bangkok",weight=)####11.42
G.add_edge("Bangkok","Phuket",weight=1.21)
#G.add_edge("Abu Dabi","Phuket",weight=)####6.42
#G.add_edge("Dallas","Seúl",weight=)####14.11
#G.add_edge("Los Ángeles","Seúl",weight=)####12.30
#G.add_edge("Dallas","Tokio",weight=)####13.22
G.add_edge("Tokio","Busan",weight=1.48)
#G.add_edge("Vancouver","Tokio",weight=)####9.51
#G.add_edge("Dallas","Daejeon",weight=)####
#G.add_edge("Los Ángeles","Daejeon",weight=)####
#G.add_edge("New York","Tokio",weight=)####
#G.add_edge("Tokio","Daejeon",weight=)####
#G.add_edge("Dallas","Kaesong",weight=)####
#G.add_edge("Atlanta","Kaesong",weight=)####
#G.add_edge("Tokio","Kaesong",weight=)####
#G.add_edge("Dallas","Haeju",weight=)####
#G.add_edge("Tokio","Haeju",weight=)####
G.add_edge("Tokio","Hiroshima",weight=1.22)
#G.add_edge("San Francisco","Tokio",weight=)####
#G.add_edge("Washington","Tokio",weight=)####14.01
#G.add_edge("Tokio","Kioto",weight=)####
G.add_edge("Tokio","Manila",weight=4.18)
G.add_edge("Hong Kong","Cebú",weight=2.38)
#G.add_edge("Toronto","Hong Kong",weight=)####16.08
#G.add_edge("Hong Kong","Perth",weight=)####7.58
G.add_edge("Santiago","Bogotá",weight=5.46)
#G.add_edge("Santiago","Auckland",weight=)####12.32
G.add_edge("Auckland","Sídney",weight=3.12)
G.add_edge("Sídney","Perth",weight=4.35)
G.add_edge("Auckland","Wellington",weight=1.06)
#G.add_edge("Los Ángeles","Sídney",weight=)####15.29
G.add_edge("Sídney","Wellington",weight=3.17)
#G.add_edge("Los Ángeles","Auckland",weight=)###13.31
G.add_edge("Auckland","Brisbane",weight=3.22)
#G.add_edge("Cusco","Lima",weight=)####
G.add_edge("Lima","Santiago",weight=3.33)
#G.add_edge("Bogotá","Cusco",weight=)####
G.add_edge("Bogotá","Guayaquil",weight=1.44)
#G.add_edge("Guayaquil","Ámsterdam",weight=)####12.44
G.add_edge("Santiago","Concepción",weight=1.02)
G.add_edge("Bogotá","Santiago",weight=5.46)
G.add_edge("Santiago","Buenos Aires",weight=1.56)
G.add_edge("Lima","Buenos Aires",weight=4.25)
#G.add_edge("Santiago","La Plata",weight=)####
G.add_edge("Lima","Montevideo",weight=4.37)
G.add_edge("Santiago","Montevideo",weight=2.31)
#G.add_edge("Bogotá","Buenos Aires",weight=)####6.19
G.add_edge("Buenos Aires","Punta del Este",weight=0.53)
#G.add_edge("Ciudad de Panamá","Nueva Orleans",weight=)####
#G.add_edge("New York","Nueva Orleans",weight=)####
G.add_edge("Los Ángeles","Seattle",weight=2.25)
#G.add_edge("San Francisco","Seattle",weight=)####
G.add_edge("Ciudad de Panamá","Orlando",weight=3.11)
G.add_edge("Dallas","Las Vegas",weight=2.37)
G.add_edge("Ciudad de Panamá","La Habana",weight=2.28)
G.add_edge("Ciudad de México","La Habana",weight=2.43)
#G.add_edge("Ciudad de México","Guadalajara",weight=)####
G.add_edge("Ciudad de Panamá","Ciudad de México",weight=3.30)
G.add_edge("Ciudad de México","Monterrey",weight=1.23)
G.add_edge("Houston","Monterrey",weight=1.20)
G.add_edge("Houston","Ciudad de Panamá",weight=4.03)
G.add_edge("Ciudad de México","Acapulco",weight=0.53)
G.add_edge("Bogotá","Cancún",weight=3.20)
G.add_edge("Cancún","Ciudad de México",weight=2.06)
G.add_edge("Toronto","Winnipeg",weight=2.23)
G.add_edge("Toronto","Ottawa",weight=0.58)
G.add_edge("Ottawa","Winnipeg",weight=2.37)
#G.add_edge("Bogotá","Cartago",weight=)####
G.add_edge("Ciudad de Panamá","Liberia",weight=1.22)


def Escala():
    pos = nx.get_node_attributes(G, 'pos')
    weight = nx.get_edge_attributes(G, 'weight')
    Edges = G.edges()
    Nodes = G.nodes()
    print("Ingrese el continente de salida y de llegada:")
    c = [Europa, Asia, Africa, SurÁmerica, NorteÁmerica, Oceanía]
    c1 = ["Europa","Asia", "Africa","Sur Ámerica","Norte Ámerica","Oceanía"]
    for i in range(len(c1)):
        print(i, ". Para ", c1[i])

    print("\n"*2)

    cont = int(input("Continente salida: "))
    cont1 = int(input("Continente llegada: "))
    print("\n"*2)
    print("Países de salida: ")

    if cont == 0:
        for i in range(len(Europa1)):
             print(i, ". Para ", Europa1[i])
        u = int(input("Ingrese el país de salida: "))
        print("\n")
        pais = Europa[u]
        for i in range(len(pais)):
            print(i,". Para ", pais[i])
        z = int(input("Ingrese la ciudad de salida: "))
        x = pais[z]
        print(x)


    if cont == 1:
        for i in range(len(Asia1)):
             print(i, ". Para ", Asia1[i])
        u = int(input("Ingrese el país de salida: "))
        print("\n")
        pais = Asia[u]
        for i in range(len(pais)):
            print(i,". Para ", pais[i])
        z = int(input("Ingrese la ciudad de salida: "))
        x = pais[z]
        print(x)


    if cont == 2:
        for i in range(len(Africa1)):
             print(i, ". Para ", Africa1[i])
        u = int(input("Ingrese el país de salida: "))
        print("\n")
        pais = Africa[u]
        for i in range(len(pais)):
            print(i,". Para ", pais[i])
        z = int(input("Ingrese la ciudad de salida: "))
        x = pais[z]
        print(x)

    if cont == 3:
        for i in range(len(SurÁmerica1)):
             print(i, ". Para ", SurÁmerica1[i])
        u = int(input("Ingrese el país de salida: "))
        print("\n")
        pais = SurÁmerica[u]
        for i in range(len(pais)):
            print(i,". Para ", pais[i])
        z = int(input("Ingrese la ciudad de salida: "))
        x = pais[z]
        print(x)

    if cont == 4:
        for i in range(len(NorteÁmerica1)):
             print(i, ". Para ", NorteÁmerica1[i])
        u = int(input("Ingrese el país de salida: "))
        pais = NorteÁmerica[u]
        print("\n")
        for i in range(len(pais)):
            print(i,". Para ", pais[i])
        z = int(input("Ingrese la ciudad de salida: "))
        x = pais[z]
        print(x)

    if cont == 5:
        for i in range(len(Oceanía1)):
             print(i, ". Para ", Oceanía1[i])
        u = int(input("Ingrese el país de salida: "))
        pais = Oceanía[u]
        print("\n")
        for i in range(len(pais)):
            print(i,". Para ", pais[i])
        z = int(input("Ingrese la ciudad de salida: "))
        x = pais[z]
        print(x)

    ######################
    if cont1 == 0:
        for i in range(len(Europa1)):
             print(i, ". Para ", Europa1[i])
        v = int(input("Ingrese el pais de destino: "))
        pais2 = Europa[v]
        print("\n")
        for i in range(len(pais2)):
            print(i,". Para ", pais2[i])
        w = int(input("Ingrese la ciudad de destino:"))
        y = pais2[w]
        print(y)

    if cont1 == 1:
        for i in range(len(Asia1)):
             print(i, ". Para ", Asia1[i])
        v = int(input("Ingrese el pais de destino: "))
        pais2 = Asia[v]
        print("\n")
        for i in range(len(pais2)):
            print(i,". Para ", pais2[i])
        w = int(input("Ingrese la ciudad de destino:"))
        y = pais2[w]
        print(y)

    if cont1 == 2:
        for i in range(len(Africa1)):
             print(i, ". Para ", Africa1[i])
        v = int(input("Ingrese el pais de destino: "))
        pais2 = Africa[v]
        print("\n")
        for i in range(len(pais2)):
            print(i,". Para ", pais2[i])
        w = int(input("Ingrese la ciudad de destino:"))
        y = pais2[w]
        print(y)

    if cont1 == 3:
        for i in range(len(SurÁmerica1)):
             print(i, ". Para ", SurÁmerica1[i])
        v = int(input("Ingrese el pais de destino: "))
        pais2 = SurÁmerica[v]
        print("\n")
        for i in range(len(pais2)):
            print(i,". Para ", pais2[i])
        w = int(input("Ingrese la ciudad de destino:"))
        y = pais2[w]
        print(y)

    if cont1 == 4:
        for i in range(len(NorteÁmerica1)):
             print(i, ". Para ", NorteÁmerica1[i])
        v = int(input("Ingrese el pais de destino: "))
        pais2 = NorteÁmerica[v]
        print("\n")
        for i in range(len(pais2)):
            print(i,". Para ", pais2[i])
        w = int(input("Ingrese la ciudad de destino:"))
        y = pais2[w]
        print(y)

    if cont1 == 5:
        for i in range(len(Oceanía1)):
             print(i, ". Para ", Oceanía1[i])
        v = int(input("Ingrese el pais de destino: "))
        pais2 = Oceanía[v]
        print("\n")
        for i in range(len(pais2)):
            print(i,". Para ", pais2[i])
        w = int(input("Ingrese la ciudad de destino:"))
        y = pais2[w]
        print(y)



    H = nx.Graph()

    if (x,y) in Edges and (x,y) in weight.keys():
        print("entrando al primer if")
        f = x,y
        z = weight.get(f)
        if z <= 5:
            time = weight.get((x,y))
            print(time)
            H.add_node(x, pos =(10,10))
            H.add_node(y, pos =(15,10))
            H.add_edge(x,y,weight=time)
            pos1 = nx.get_node_attributes(H, 'pos')
            weight1 = nx.get_edge_attributes(H,'weight')
            plt.figure()
            nx.draw_networkx(H,pos1)
            nx.draw_networkx_edge_labels(H,pos1,edge_labels = weight1)

            plt.show()
        else:
            print("entrando al primer else")
            for i in pos:
                H.add_node(i, pos = pos.get(i))
            for (a,b) in weight.keys():
                if (a,b) != (x,y) or (a,b) != (y,x):
                    j = a,b
                    H.add_edge(a,b, weight = weight.get(j))
            print((x,y) in H.edges())
            print((y,x) in H.edges())
            #print(H.edges())
            #print(H.nodes())

    if (y,x) in Edges and (y,x) in weight.keys():
        print("entrando al segundo if")
        f = y,x
        z = weight.get(f)
        print(type(z))
        if z <= 5:
            time = weight.get((y,x))
            print(time)
            H.add_node(x, pos =(10,10))
            H.add_node(y, pos =(15,10))
            H.add_edge(x,y,weight=time)
            print(H.nodes())
            pos1 = nx.get_node_attributes(H, 'pos')
            weight1 = nx.get_edge_attributes(H,'weight')
            print(pos1)
            print(weight1)
            print(H.edges())
            plt.figure()
            nx.draw_networkx(H,pos1)
            nx.draw_networkx_edge_labels(H,pos1,edge_labels = weight1)
            plt.show()
        else:
            print("entrando al segundo else")
            for i in pos:
                H.add_node(i, pos = pos.get(i))

            for (a,b) in weight.keys():
                if (a,b) != (x,y) or (a,b) != (y,x):
                    j = a,b
                    H.add_edge(a,b, weight = weight.get(j))

            pos1 = nx.get_node_attributes(H, 'pos')
            weight1 = nx.get_edge_attributes(H,'weight')
            print(pos1)
            print(weight1)
            path = nx.dijkstra_path(H,x,y)
            P = nx.Graph()
            x = 0
            y = 0
            for i in path:
                P.add_node(i, pos = (x,y))
                x += 20
            for i in range(len(path)):
                if i+1 < len(path):
                    print(i)
                    print(i+1)
                    u = path[i]
                    v = path[i+1]
                    print(u)
                    print(v)
                    if (u,v) in weight1.keys():
                        P.add_edge(u,v,weight = weight1.get((u,v)))

                    if (v,u) in weight1.keys():
                        P.add_edge(u,v,weight = weight1.get((v,u)))



            print(P.nodes())
            print(P.edges())
            pos2 = nx.get_node_attributes(P, 'pos')
            weight2 = nx.get_edge_attributes(P,'weight')
            plt.figure()
            nx.draw_networkx(P,pos2)
            nx.draw_networkx_edge_labels(P,pos2,edge_labels = weight2)
            plt.show()

    if (x,y) not in Edges or (y,x) not in Edges:
        for i in Nodes:
            H.add_node(i,pos = pos.get(i))

        for (a,b) in weight.keys():
            d = a,b
            H.add_edge(a,b,weight= weight.get(d))
        pos1 = nx.get_node_attributes(H, 'pos')
        weight1=nx.get_edge_attributes(H, 'weight')
        path = nx.dijkstra_path(H,x,y)
        P = nx.Graph()
        x = 0
        y = 0
        for i in path:
            P.add_node(i, pos = (x,y))
            x += 20
        for i in range(len(path)):
            if i+1 < len(path):
                print(i)
                print(i+1)
                u = path[i]
                v = path[i+1]
                #print(u)
                #print(v)
                if (u,v) in weight1.keys():
                    P.add_edge(u,v,weight = weight1.get((u,v)))

                if (v,u) in weight1.keys():
                    P.add_edge(u,v,weight = weight1.get((v,u)))



        print(P.nodes())
        print(P.edges())
        pos2 = nx.get_node_attributes(P, 'pos')
        weight2 = nx.get_edge_attributes(P,'weight')
        plt.figure()
        nx.draw_networkx(P,pos2)
        nx.draw_networkx_edge_labels(P,pos2,edge_labels = weight2)
        plt.show()



Escala()




"""
weight = nx.get_edge_attributes(G, 'weight')
print(weight)
pos = nx.get_node_attributes(G, 'pos')
print(pos)
nx.draw(G,pos,with_labels = True, node_size = 200)
nx.draw_networkx_edge_labels(G,pos,edge_labels = weight)
plt.show()"""