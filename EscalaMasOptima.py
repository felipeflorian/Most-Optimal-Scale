
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

Alemania = ["Zúrich","Berlín", "Hamburgo", "Fráncfort","Múnich"]


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


#Kenia
G.add_node("Nairobi",pos=(200,-300))

Kenia = ["Nairobi"]


#Zimbabue
G.add_node("Harare",pos=(320,300))

Zimbabue = ["Harare"]

Africa1 = ["Marruecos", "Argelia", "Egipto", "Sudán", "Nigeria","Angola", "Botsuana", "Sudáfrica","Kenia","Zimbabue"]
Africa = [Marruecos, Argelia, Egipto, Sudán, Nigeria, Angola, Botsuana, Sudáfrica,Kenia,Zimbabue]

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

China = ["Pekín", "Shanghái", "Shenzhen", "Hong Kong"]

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

CoreaDelNorte = ["Kaesong"]


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

#Samoa
G.add_node("Apia",pos=(600,150))

Samoa = ["Apia"]

Oceanía = [Australia, NuevaZelanda, Samoa]
Oceanía1 = ["Australia", "Nueva Zelanda", "Samoa"]

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
G.add_node("Sao Paulo", pos=(50,-90))#YA


Brasil = ["Río de Janeiro","Sao Paulo"]

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
G.add_node("Honolulu",pos = (-250,100))

EstadosUnidos = ["Houston","Dallas","Nueva Orleans","Seattle","San Francisco","Las Vegas","Los Ángeles","Atlanta","Orlando","Miami","Washington","New York","Chicago","Honolulu"]

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


G.add_edge("Helsinki","Moscú",weight=1.45)
G.add_edge("Moscú","Astana",weight=3.20)
G.add_edge("Astana","Pekín",weight=5.15)
G.add_edge("Pekín","Hong Kong",weight=3.45)

G.add_edge("Ciudad de Panamá","Miami",weight=5.35)
G.add_edge("Miami","Montreal",weight=3.21)

G.add_edge("Varsovia","Moscú",weight=2.00)
G.add_edge("Moscú","Kazán",weight=1.40)
G.add_edge("Lisboa","Milán",weight=2.40)
G.add_edge("Lisboa","Zúrich",weight=2.45)
G.add_edge("Bogotá","New York",weight=5.45)
G.add_edge("Lisboa","Madrid",weight=1.20)
G.add_edge("Lisboa","Fráncfort",weight=3.05)
G.add_edge("Lisboa","Estambul",weight=4.50)
G.add_edge("Bogotá","Cancún",weight=3.20)
G.add_edge("Cancún","Los Ángeles",weight=4.45)
G.add_edge("Lisboa","Múnich",weight=3.05)
G.add_edge("Ciudad de Panamá","New York",weight=5.15)
G.add_edge("Lisboa","Madrid",weight=1.09)
G.add_edge("Lisboa","Estambul",weight=4.31)
G.add_edge("Estambul","Abu Dabi",weight=4.16)
G.add_edge("Chicago","New York",weight=2.09)
G.add_edge("New York","Versalles",weight=6.50)
G.add_edge("Santo Domingo","Nueva York",weight=4.07)
G.add_edge("Nueva York","París",weight=6.50)

G.add_edge("Toronto","Lisboa",weight=7.00)
G.add_edge("Lisboa","Zúrich",weight=2.39)
G.add_edge("Lisboa","Moscú",weight=5.23)
G.add_edge("Washington","Toronto",weight=1.14)
G.add_edge("Lisboa","Estambul",weight=4.31)
G.add_edge("Tokio","Manila",weight=5.00)
G.add_edge("Manila","Yakarta",weight=5.20)
G.add_edge("Perth","Yakarta",weight=4.16)
G.add_edge("Yakarta","Hong Kong",weight=4.32)
G.add_edge("Atlanta","New York",weight=2.08)
G.add_edge("Lisboa","Paris",weight=2.20)
G.add_edge("Londres","Estambul",weight=3.38)
G.add_edge("Estambul","Nueva Delhi",weight=5.55)
G.add_edge("Miami","New York",weight=2.51)
G.add_edge("Lisboa","Múnich",weight=2.59)
G.add_edge("Toronto","Lisboa",weight=7.00)
G.add_edge("Lisboa","Viena",weight=3.23)
G.add_edge("New York","Londres",weight=6.40)
G.add_edge("Londres","Ámsterdam",weight=0.58)
G.add_edge("Fráncfort","Astana",weight=5.35)
G.add_edge("Astana","Taskent",weight=2.10)
G.add_edge("Astana","Nueva Delhi",weight=6.40)
G.add_edge("Nueva Delhi","Bombay",weight=2.10)
G.add_edge("Astaná","Pekín",weight=5.15)
G.add_edge("Madrid","Estambul",weight=3.56)
G.add_edge("Estambul","Nueva Delhi",weight=5.55)
G.add_edge("Nueva Delhi","Bangkok",weight=3.55)
G.add_edge("Bangkok","Shanghái",weight=4.06)
G.add_edge("Ámsterdam","Fráncfort",weight=0.58)
G.add_edge("París","Abuya",weight=6.03)
G.add_edge("Abuya","Luanda",weight=6.47)
G.add_edge("Tokio","Honolulu",weight=6.55)
G.add_edge("Honolulu","Vancouver",weight=5.55)
G.add_edge("Honolulu","Apia",weight=5.50)
G.add_edge("Apia","Brisbane",weight=5.47)
G.add_edge("Brisbane","Melbourne",weight=2.13)
G.add_edge("Los Ángeles","Honolulu",weight=5.37)
G.add_edge("Apia","Auckland",weight=4.05)
G.add_edge("Abu Dabi","Bombay",weight=2.58)
G.add_edge("Bombay","Bangkok",weight=4.17)
G.add_edge("Bangkok","Yakarta",weight=3.21)
G.add_edge("Yakarta","Perth",weight=4.16)
G.add_edge("Perth","Melbourne",weight=3.52)
G.add_edge("Tokio","Hong Kong",weight=4.12)
G.add_edge("Ciudad de México","Los Ángeles",weight=3.37)
G.add_edge("New York","Los Ángeles",weight=6.11)
G.add_edge("Tokio","Seúl",weight=2.04)
G.add_edge("Dallas","Los Ángeles",weight=2.59)
G.add_edge("Tokio","Shanghái",weight=2.43)
G.add_edge("Shanghái","Daejeon",weight=2.00)
G.add_edge("Tokio","Pekín",weight=3.07)
G.add_edge("Pekín","Kaesong",weight=1.45)
G.add_edge("Atlanta","Los Ángeles",weight=4.24)
G.add_edge("San Francisco","Honolulu",weight=5.27)
G.add_edge("Washington","San Francisco",weight=6.11)
G.add_edge("Toronto","San Francisco",weight=5.44)

G.add_edge("Ámsterdam","París",weight=1.00)
G.add_edge("París","Rabat",weight=2.47)

G.add_edge("Rabat","París",weight=2.47)
G.add_edge("París","El Cairo",weight=4.30)
G.add_edge("El Cairo","Jartum",weight=2.31)
G.add_edge("Jartum","Nairobi",weight=2.54) 
G.add_edge("Nairobi","Harare",weight=2.56) 
G.add_edge("Harare","Johannesburgo",weight=1.42)

G.add_edge("Sao Paulo","Bogotá",weight=5.53)
G.add_edge("San José","Montreal",weight=5.25)
G.add_edge("París","Riad",weight=6.18)
G.add_edge("Bogotá","Toronto",weight=5.55)
G.add_edge("Abu Dabi","Bangkok",weight=6.41)
G.add_edge("Madrid","Abu Dabi",weight=6.50)
G.add_edge("Abu Dabi","Phuket",weight=6.42)
G.add_edge("Bogotá","Buenos Aires",weight=6.19)
G.add_edge("Toronto","Dublín",weight=6.45)
G.add_edge("Estambul","Abuya",weight=6.50)
G.add_edge("Madrid","Abu Dabi",weight=6.50)
G.add_edge("París","Abuya",weight=6.03)
G.add_edge("Toronto","Londres",weight=6.55)

G.add_edge("Londres","Abu Dabi",weight=6.55)
G.add_edge("New York","Lisboa",weight=6.45)#IMPORTANTE
G.add_edge("Bogotá","Cartagena", weight = 1.20)
G.add_edge("Bogotá","Medellin", weight = 0.48)
G.add_edge("Bogotá","Miami", weight = 3.31)
G.add_edge("Bogotá", "Ciudad de Panamá", weight = 1.27)
G.add_edge("Ciudad de Panamá", "La Habana", weight = 2.28) 
G.add_edge("Bogotá","Atlanta",weight= 4.42)
G.add_edge("Atlanta","New York",weight=2.02)
G.add_edge("Miami","New York",weight=2.41)
G.add_edge("Roma","Milán",weight=1.06)
G.add_edge("Roma","Zúrich",weight=1.22)
G.add_edge("Roma","Madrid",weight=2.10)
G.add_edge("Venecia","Madrid",weight=2.16)
G.add_edge("Venecia","Zúrich",weight=0.58)
G.add_edge("Zúrich","Fráncfort",weight=0.52)
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
G.add_edge("Moscú","Abu Dabi",weight=5.07)
G.add_edge("Moscú","Dubái",weight=5.02)
G.add_edge("Helsinki","Moscú",weight=1.41)
G.add_edge("Toronto","Vancouver",weight=4.41)
G.add_edge("Auckland","Melbourne",weight=3.48)
G.add_edge("Toronto","Winnipeg",weight=2.23)
G.add_edge("Ottawa","Toronto",weight=0.58)
G.add_edge("Toronto","Montreal",weight=1.07)
G.add_edge("Ciudad de México","Montreal",weight=5.07)
G.add_edge("Ámsterdam","Moscú",weight=3.11)
G.add_edge("Moscú","Sochi",weight=2.10)
G.add_edge("París","Moscú",weight=3.34)
G.add_edge("Ciudad de Panamá","Cancún",weight=2.40)
G.add_edge("Medellin","Cancún",weight=3.15)
G.add_edge("Madrid","Valencia",weight=0.52)
G.add_edge("Estambul","Valencia",weight=3.36)
G.add_edge("Fráncfort","Valencia",weight=2.13)
G.add_edge("Madrid","Barcelona",weight=1.07)
G.add_edge("Ámsterdam","Barcelona",weight=2.03)
G.add_edge("París","Barcelona",weight=1.35)
G.add_edge("Madrid","Viena",weight=2.45)
G.add_edge("Ámsterdam","Viena",weight=1.42)
G.add_edge("Ámsterdam","Montpellier",weight=1.50)
G.add_edge("París","Montpellier",weight=1.16)
G.add_edge("Londres","Versalles",weight=1.20)
G.add_edge("Bogotá","Houston",weight=4.57)
G.add_edge("Houston","Chicago",weight=2.22)
G.add_edge("Ámsterdam","Berlín",weight=1.14)
G.add_edge("Zúrich","Berlín",weight=1.20)
G.add_edge("Múnich","Berlín",weight=1.06)
G.add_edge("Ámsterdam","Varsovia",weight=1.53)
G.add_edge("París","Varsovia",weight=2.11)
G.add_edge("Estambul","Varsovia",weight=2.13)
G.add_edge("Madrid","Zúrich",weight=2.03)
G.add_edge("Zúrich","Varsovia",weight=1.48)
G.add_edge("Londres","Varsovia",weight=2.20)
G.add_edge("Kazán","Moscú",weight=1.24)
G.add_edge("Varsovia","Estocolmo",weight=1.26)
G.add_edge("Varsovia","Dubái",weight=5.40)
G.add_edge("Londres","Dublín",weight=1.04)
G.add_edge("Estambul","Dublín",weight=4.11)
G.add_edge("Ámsterdam","Dublín",weight=1.27)
G.add_edge("Múnich","Antalya",weight=3.00)
G.add_edge("Estambul","Antalya",weight=1.07)
G.add_edge("Estambul","Madrid",weight=3.56)
G.add_edge("Londres","Estambul",weight=3.38)
G.add_edge("Ámsterdam","Bucarest",weight=2.44)
G.add_edge("Múnich","Bucarest",weight=1.58)
G.add_edge("Barcelona","Bucarest",weight=2.59)
G.add_edge("Bogotá","Quito",weight=1.24)
G.add_edge("Ciudad de Panamá","Quito",weight=1.47)
G.add_edge("Ámsterdam","Cracovia",weight=1.50)
G.add_edge("Madrid","Hamburgo",weight=2.43)
G.add_edge("Múnich","Hamburgo",weight=1.15)
G.add_edge("Fráncfort","Hamburgo",weight=1.01)
G.add_edge("París","Hamburgo",weight=1.25)
G.add_edge("Hamburgo","Torun",weight=1.15)
G.add_edge("Torun","Estambul",weight=2.35)
G.add_edge("París","Mánchester",weight=1.14)
G.add_edge("Dublín","Mánchester",weight=0.50)
G.add_edge("Ámsterdam","Birmingham",weight=1.04)
G.add_edge("Fráncfort","Birmingham",weight=1.28)
G.add_edge("Múnich","Birmingham",weight=1.50)
G.add_edge("Estambul","Birmingham",weight=3.47)
G.add_edge("Birmingham","Ámsterdam",weight=1.04)
G.add_edge("Ámsterdam","Cork",weight=1.50)
G.add_edge("París","Ámsterdam",weight=1.00)
G.add_edge("Londres","Cork",weight=1.20)
G.add_edge("Lisboa","Madrid",weight=1.09)
G.add_edge("Viena","Lisboa",weight=3.23)
G.add_edge("Madrid","Braga",weight=1.20)
G.add_edge("Estambul","Braga",weight=5.05)
G.add_edge("Braga","Fráncfort",weight=2.45)
G.add_edge("Ámsterdam","Atenas",weight=3.13)
G.add_edge("Estambul","Atenas",weight=1.11)
G.add_edge("París","Atenas",weight=3.08)
G.add_edge("Fráncfort","Atenas",weight=2.46)
G.add_edge("Múnich","Sibiu",weight=1.43)
G.add_edge("París","Helsinki",weight=2.52)
G.add_edge("Helsinki","Turku",weight=0.42)
G.add_edge("Zúrich","Estocolmo",weight=2.21)
G.add_edge("Estocolmo","Turku",weight=0.50)
G.add_edge("París","Rabat",weight=2.47)
G.add_edge("Madrid","Tánger",weight=1.13)
G.add_edge("París","Tánger",weight=2.29)
G.add_edge("Fráncfort","Argel",weight=2.30)
G.add_edge("Argel","Orán",weight=1.00)
G.add_edge("Estambul","Orán",weight=3.47)
G.add_edge("Bogotá","Washington",weight=5.14)
G.add_edge("Estambul","El Cairo",weight=2.02)
G.add_edge("Fráncfort","El Cairo",weight=4.08)
G.add_edge("Estambul","Hurgada",weight=2.30)
G.add_edge("El Cairo","Hurgada",weight=1.00)
G.add_edge("Estambul","Jartum",weight=4.02)
G.add_edge("Abu Dabi","Jartum",weight=3.37)
G.add_edge("Johannesburgo","Gaborone",weight=0.55)
G.add_edge("Bogotá","Lima",weight=2.51)
G.add_edge("Sao Paulo","Lima",weight=4.55)
G.add_edge("Johannesburgo","Maun",weight=1.33)
G.add_edge("Bogotá","Santiago",weight=5.46)
G.add_edge("Sao Paulo","Santiago",weight=4.05)
G.add_edge("Johannesburgo","Durban",weight=1.08)
G.add_edge("Estambul","Ankara",weight=0.55)
G.add_edge("Pekín","Shanghái",weight=1.52)
G.add_edge("Dallas","Miami",weight=2.45)
G.add_edge("Houston","Chicago",weight=2.22)
G.add_edge("Bogotá","Dallas",weight=5.23)
G.add_edge("Houston","San Francisco",weight=4.13)
G.add_edge("Pekín","Shenzhen",weight=2.56)
G.add_edge("Shanghái","Shenzhen",weight=2.00)
G.add_edge("Fráncfort","Astana",weight=5.35)
G.add_edge("Estambul","Astana",weight=4.45)
G.add_edge("Moscú","Shymkent",weight=3.57)
G.add_edge("Ciudad de Panamá","New York",weight=5.15)
G.add_edge("Moscú","Samarcanda",weight=3.57)
G.add_edge("Londres","Moscú",weight=3.41)
G.add_edge("Madrid","Moscú",weight=4.47)
G.add_edge("Moscú","Taskent",weight=4.01)
G.add_edge("Estambul","Taskent",weight=4.42)
G.add_edge("Riad","Meca",weight=1.35)
G.add_edge("Estambul","Riad",weight=3.32)
G.add_edge("Fráncfort","Riad",weight=5.51)
G.add_edge("Riad","Abha",weight=1.34)
G.add_edge("El cairo","Abha",weight=2.40)
G.add_edge("Bogotá","Ciudad de México",weight=4.26)
G.add_edge("Hong Kong","Surabaya",weight=4.36)
G.add_edge("Tokio","Busan",weight=1.48)
G.add_edge("Bangkok","Phuket",weight=1.21)
G.add_edge("Tokio","Daejeon",weight=2.50)
G.add_edge("Tokio","Kaesong",weight=2.40)
G.add_edge("Tokio","Hiroshima",weight=1.22)
G.add_edge("Tokio","Kioto",weight=1.10)
G.add_edge("Tokio","Manila",weight=4.18)
G.add_edge("Hong Kong","Cebú",weight=2.38)
G.add_edge("Santiago","Bogotá",weight=5.46)
G.add_edge("Auckland","Sídney",weight=3.12)
G.add_edge("Sídney","Perth",weight=4.35)
G.add_edge("Auckland","Wellington",weight=1.06)
G.add_edge("Sídney","Wellington",weight=3.17)
G.add_edge("Auckland","Brisbane",weight=3.22)
G.add_edge("Cusco","Lima",weight=1.26)
G.add_edge("Lima","Santiago",weight=3.33)
G.add_edge("Bogotá","Cusco",weight=3.22)
G.add_edge("Bogotá","Guayaquil",weight=1.44)
G.add_edge("Santiago","Concepción",weight=1.02)
G.add_edge("Bogotá","Santiago",weight=5.46)
G.add_edge("Santiago","Buenos Aires",weight=1.56)
G.add_edge("Lima","Buenos Aires",weight=4.25)
G.add_edge("Santiago","La Plata",weight=1.55)
G.add_edge("Lima","Montevideo",weight=4.37)
G.add_edge("Santiago","Montevideo",weight=2.31)
G.add_edge("Buenos Aires","Punta del Este",weight=0.53)
G.add_edge("Ciudad de Panamá","Nueva Orleans",weight=4.00)
G.add_edge("New York","Nueva Orleans",weight=3.33)
G.add_edge("Los Ángeles","Seattle",weight=2.25)
G.add_edge("San Francisco","Seattle",weight=2.11)
G.add_edge("Ciudad de Panamá","Orlando",weight=3.11)
G.add_edge("Dallas","Las Vegas",weight=2.37)
G.add_edge("Ciudad de Panamá","La Habana",weight=2.28)
G.add_edge("Ciudad de México","La Habana",weight=2.43)
G.add_edge("Ciudad de México","Guadalajara",weight=1.15)
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
G.add_edge("Bogotá","Cartago",weight=2.15)
G.add_edge("Ciudad de Panamá","Liberia",weight=1.22)
G.add_edge("Ciudad de Panamá","Dallas",weight=4.29)
G.add_edge("Río de Janeiro","Bogotá",weight=6.09)

def Escala():
    node_color = ['#7B241C', '#3333FF', '#34495E', '#FF3333', '#6C3483','#0E6655','#9C640C','#5F6A6A','#17202A','#D4AC0D','#C39BD3','#58D68D','#5D6D7E','#D98880','#5499C7','#24DB11']
    color = []
    pos = nx.get_node_attributes(G, 'pos')
    weight = nx.get_edge_attributes(G, 'weight')
    Edges = G.edges()
    Nodes = G.nodes()
    print("Ingrese el continente de salida y de llegada:")
    c = [Europa, Asia, Africa, SurÁmerica, NorteÁmerica, Oceanía]
    c1 = ["Europa","Asia", "Africa","Sur Ámerica","Norte y Centro Ámerica","Oceanía"]
    for i in range(len(c1)):
        print(i, ".Para ", c1[i])

    print("\n"*2)

    cont = int(input("Continente salida: "))
    print("\n")
    cont1 = int(input("Continente llegada: "))
    print("\n"*2)
    print("Países de salida: ")
    print("\n")
    if cont == 0:
        for i in range(len(Europa1)):
             print(i, ".Para ", Europa1[i])
        u = int(input("Ingrese el país de salida: "))
        print("\n")
        pais = Europa[u]
        for i in range(len(pais)):
            print(i,".Para ", pais[i])
        z = int(input("Ingrese la ciudad de salida: "))
        x = pais[z]



    if cont == 1:
        for i in range(len(Asia1)):
             print(i, ".Para ", Asia1[i])
        u = int(input("Ingrese el país de salida: "))
        print("\n")
        pais = Asia[u]
        for i in range(len(pais)):
            print(i,". Para ", pais[i])
        z = int(input("Ingrese la ciudad de salida: "))
        x = pais[z]



    if cont == 2:
        for i in range(len(Africa1)):
             print(i, ".Para ", Africa1[i])
        u = int(input("Ingrese el país de salida: "))
        print("\n")
        pais = Africa[u]
        for i in range(len(pais)):
            print(i,".Para ", pais[i])
        z = int(input("Ingrese la ciudad de salida: "))
        x = pais[z]


    if cont == 3:
        for i in range(len(SurÁmerica1)):
             print(i, ".Para ", SurÁmerica1[i])
        u = int(input("Ingrese el país de salida: "))
        print("\n")
        pais = SurÁmerica[u]
        for i in range(len(pais)):
            print(i,".Para ", pais[i])
        z = int(input("Ingrese la ciudad de salida: "))
        x = pais[z]


    if cont == 4:
        for i in range(len(NorteÁmerica1)):
             print(i, ".Para ", NorteÁmerica1[i])
        u = int(input("Ingrese el país de salida: "))
        pais = NorteÁmerica[u]
        print("\n")
        for i in range(len(pais)):
            print(i,".Para ", pais[i])
        z = int(input("Ingrese la ciudad de salida: "))
        x = pais[z]


    if cont == 5:
        for i in range(len(Oceanía1)):
             print(i, ".Para ", Oceanía1[i])
        u = int(input("Ingrese el país de salida: "))
        pais = Oceanía[u]
        print("\n")
        for i in range(len(pais)):
            print(i,".Para ", pais[i])
        z = int(input("Ingrese la ciudad de salida: "))
        x = pais[z]


    ######################
    if cont1 == 0:
        for i in range(len(Europa1)):
             print(i, ".Para ", Europa1[i])
        v = int(input("Ingrese el pais de destino: "))
        pais2 = Europa[v]
        print("\n")
        for i in range(len(pais2)):
            print(i,".Para ", pais2[i])
        w = int(input("Ingrese la ciudad de destino:"))
        y = pais2[w]


    if cont1 == 1:
        for i in range(len(Asia1)):
             print(i, ".Para ", Asia1[i])
        v = int(input("Ingrese el pais de destino: "))
        pais2 = Asia[v]
        print("\n")
        for i in range(len(pais2)):
            print(i,".Para ", pais2[i])
        w = int(input("Ingrese la ciudad de destino:"))
        y = pais2[w]


    if cont1 == 2:
        for i in range(len(Africa1)):
             print(i, ".Para ", Africa1[i])
        v = int(input("Ingrese el pais de destino: "))
        pais2 = Africa[v]
        print("\n")
        for i in range(len(pais2)):
            print(i,".Para ", pais2[i])
        w = int(input("Ingrese la ciudad de destino:"))
        y = pais2[w]


    if cont1 == 3:
        for i in range(len(SurÁmerica1)):
             print(i, ".Para ", SurÁmerica1[i])
        v = int(input("Ingrese el pais de destino: "))
        pais2 = SurÁmerica[v]
        print("\n")
        for i in range(len(pais2)):
            print(i,".Para ", pais2[i])
        w = int(input("Ingrese la ciudad de destino:"))
        y = pais2[w]


    if cont1 == 4:
        for i in range(len(NorteÁmerica1)):
             print(i, ".Para ", NorteÁmerica1[i])
        v = int(input("Ingrese el pais de destino: "))
        pais2 = NorteÁmerica[v]
        print("\n")
        for i in range(len(pais2)):
            print(i,".Para ", pais2[i])
        w = int(input("Ingrese la ciudad de destino:"))
        y = pais2[w]


    if cont1 == 5:
        for i in range(len(Oceanía1)):
             print(i, ".Para ", Oceanía1[i])
        v = int(input("Ingrese el pais de destino: "))
        pais2 = Oceanía[v]
        print("\n")
        for i in range(len(pais2)):
            print(i,".Para ", pais2[i])
        w = int(input("Ingrese la ciudad de destino:"))
        y = pais2[w]




    H = nx.Graph()

    if (x,y) in Edges and (x,y) in weight.keys():
        f = x,y
        z = weight.get(f)
        if z <= 7:
            time = weight.get((x,y))
            H.add_node(x, pos =(10,10))
            H.add_node(y, pos =(15,10))
            H.add_edge(x,y,weight=time)
            pos1 = nx.get_node_attributes(H, 'pos')
            weight1 = nx.get_edge_attributes(H,'weight')
            plt.figure()
            nx.draw_networkx(H,pos1, node_list = [x,y], node_color = [node_color[0],node_color[1]])
            nx.draw_networkx_edge_labels(H,pos1,edge_labels = weight1)

            plt.show()
        else:
            for i in pos:
                H.add_node(i, pos = pos.get(i))

            for (a,b) in weight.keys():
                if (a,b) != (x,y) or (a,b) != (y,x):
                    j = a,b
                    H.add_edge(a,b, weight = weight.get(j))

            pos1 = nx.get_node_attributes(H, 'pos')
            weight1 = nx.get_edge_attributes(H,'weight')
            path = nx.dijkstra_path(H,x,y)
            P = nx.Graph()
            x = 0
            y = 0
            for i in path:
                P.add_node(i, pos = (x,y))
                x += 20
            for i in range(len(path)):
                if i+1 < len(path):
                    u = path[i]
                    v = path[i+1]
                    if (u,v) in weight1.keys():
                        P.add_edge(u,v,weight = weight1.get((u,v)))

                    if (v,u) in weight1.keys():
                        P.add_edge(u,v,weight = weight1.get((v,u)))


            n = P.nodes()
            nodesP = []
            for u in n:
                nodesP.append(u)
            for v in range(len(nodesP)):
                color.append(node_color[v])

            pos2 = nx.get_node_attributes(P, 'pos')
            weight2 = nx.get_edge_attributes(P,'weight')
            plt.figure()
            nx.draw_networkx(P,pos2,nodelist=nodesP,node_color= color)
            nx.draw_networkx_edge_labels(P,pos2,edge_labels = weight2)
            plt.show()



    if (y,x) in Edges and (y,x) in weight.keys():
        f = y,x
        z = weight.get(f)

        if z <= 5:
            time = weight.get((y,x))
            print(time)
            H.add_node(x, pos =(10,10))
            H.add_node(y, pos =(15,10))
            H.add_edge(x,y,weight=time)
            pos1 = nx.get_node_attributes(H, 'pos')
            weight1 = nx.get_edge_attributes(H,'weight')
            plt.figure()
            nx.draw_networkx(H,pos1,node_list = [x,y], node_color = [node_color[0],node_color[1]])
            nx.draw_networkx_edge_labels(H,pos1,edge_labels = weight1)
            plt.show()
        else:
            for i in pos:
                H.add_node(i, pos = pos.get(i))

            for (a,b) in weight.keys():
                if (a,b) != (x,y) or (a,b) != (y,x):
                    j = a,b
                    H.add_edge(a,b, weight = weight.get(j))

            pos1 = nx.get_node_attributes(H, 'pos')
            weight1 = nx.get_edge_attributes(H,'weight')
            path = nx.dijkstra_path(H,x,y)
            P = nx.Graph()
            x = 0
            y = 0
            for i in path:
                P.add_node(i, pos = (x,y))
                x += 20
            for i in range(len(path)):
                if i+1 < len(path):
                    u = path[i]
                    v = path[i+1]
                    if (u,v) in weight1.keys():
                        P.add_edge(u,v,weight = weight1.get((u,v)))

                    if (v,u) in weight1.keys():
                        P.add_edge(u,v,weight = weight1.get((v,u)))

            n = P.nodes()
            nodesP = []
            for u in n:
                nodesP.append(u)
            for v in range(len(nodesP)):
                color.append(node_color[v])

            pos2 = nx.get_node_attributes(P, 'pos')
            weight2 = nx.get_edge_attributes(P,'weight')
            plt.figure()
            nx.draw_networkx(P,pos2,nodelist=nodesP,node_color= color)
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
        z = 300
        for i in path:
            P.add_node(i, pos = (x,y))
            x += 200
            y += z




        for i in range(len(path)):
            if i+1 < len(path):
                u = path[i]
                v = path[i+1]
                if (u,v) in weight1.keys():
                    P.add_edge(u,v,weight = weight1.get((u,v)))

                if (v,u) in weight1.keys():
                    P.add_edge(u,v,weight = weight1.get((v,u)))


        n = P.nodes()
        nodesP = []
        for u in n:
            nodesP.append(u)
        for v in range(len(nodesP)):
            color.append(node_color[v])

        pos2 = nx.get_node_attributes(P, 'pos')
        weight2 = nx.get_edge_attributes(P,'weight')

        plt.figure()

        nx.draw_networkx(P,pos2,nodelist=nodesP,node_color= color)
        nx.draw_networkx_edge_labels(P,pos2,edge_labels = weight2)
        plt.show()



Escala()
