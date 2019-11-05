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
G.add_node("Paris", pos=(150,60))#YA
G.add_node("Montpellier", pos=(170,60))#YA
G.add_node("Versalles", pos=(190,80))#YA

Francia = ["Paris","Montpellier","Versalles"]


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

Sudáfica = ["Johannesburgo", "Durban"]

Africa = ["Marruecos", "Argelia", "Egipto", "Sudán", "Nigeria","Angola", "Botsuana", "Sudáfrica"]


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


Asia = [Rusia, Turquía, India, China,Kazajistán, Uzbekistán, Arabia Saudita, EmiratosÁrabesUnidos, Indonesia,Tailandia, CoreaDelSur, CoreaDelNorte, Japón, Filipinas]


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


Oceanía = [Tasmania, Australia, Nueva Zelanda]


#SUR AMÉRICA---------------------------------------------------------------------------

#Colombia
G.add_node("Bogotá", pos=(-100, -100))#YA
G.add_node("Medellin", pos=(-60,-40))#YA
G.add_node("Cartagena", pos=(60, -70))#YA


#Ecuador
G.add_node("Quito", pos=(-200,-50))#YA
G.add_node("Guayaquil", pos=(-250,-90))#YA

#Perú
G.add_node("Lima", pos=(-20, -100))#YA
G.add_node("Cusco", pos=(-50,-130))#YA

#Brasil
G.add_node("Río de Janeiro", pos=(5, -100))#YA
G.add_node("Sao Pablo", pos=(50,-90))#YA

#Chile
G.add_node("Santiago", pos=(-140,-80))#YA
G.add_node("Concepción", pos=(-180,-100))#YA

#Argentina
G.add_node("Buenos Aires", pos=(-150,-90))#YA
G.add_node("La Plata", pos=(-160,-200))#YA

#Uruguay
G.add_node("Montevideo", pos=(-130,-100))#YA
G.add_node("Punta del Este", pos=(-110,-70))#YA



SurÁmerica = [Colombia,  Ecuador, Perú, Brasil, Chile, Argentina, Uruguay]


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


#Panamá
G.add_node("Ciudad de Panamá", pos=(0, -70))#YA

#Costa Rica
G.add_node("Cartago", pos=(-300,80))#YA
G.add_node("San José", pos=(-320,100))#YA
G.add_node("Liberia", pos=(-310,60))

#Cuba
G.add_node("La Habana", pos=(-310,-100))#YA

#México
G.add_node("Ciudad de México", pos=(-380,120))#YA
G.add_node("Guadalajara", pos=(-350,90))#YA
G.add_node("Monterrey", pos=(-330,180))#YA
G.add_node("Acapulco", pos=(-400,200))#YA
G.add_node("Cancún", pos=(-390,230))#YA

#Canadá
G.add_node("Toronto", pos=(-10,150))#YA
G.add_node("Montreal", pos=(-25, 135))#YA
G.add_node("Vancouver", pos=(-30,170))#YA
G.add_node("Winnipeg", pos=(-80,10))
G.add_node("Ottawa", pos=(-60,110))#YA#YA




NorteÁmerica = [EstadosUnidos, Panamá, CostaRica, Cuba, México, Canadá]


#-----------------------------------------------------ARISTAS---------------------------------------------------------------------------
G.add_edge("Bogotá","Cartagena", weight = 1.21 )
G.add_edge("Bogotá","Medellin", weight = 0.45)
G.add_edge("Bogotá","Miami", weight = 3.45)
G.add_edge("Bogotá", "Ciudad de Panamá", weight = 1.45)
G.add_edge("Ciudad de Panamá", "La Habana", weight = ) #Cuba
G.add_edge("Ciudad de Panamá", "Valencia", weight = ) #Venezuela
G.add_edge("Bogotá","Atlanta",weight=)
G.add_edge("Atlanta","New York",weight=)
G.add_edge("Miami","New York",weight=)
G.add_edge("Roma","Milán",weight=)
G.add_edge("Milán","New York",weight=)
G.add_edge("Roma","Zúrich",weight=)
G.add_edge("New York","Zúrich",weight=)
G.add_edge("Roma","Madrid",weight=)
G.add_edge("Madrid","Bogotá",weight=)
G.add_edge("Madrid","Medellin",weight=)
G.add_edge("Venecia","Madrid",weight=)
G.add_edge("Venecia","Zúrich",weight=)
G.add_edge("Zúrich","Fráncfort",weight=)
G.add_edge("Fráncfort","Bogotá",weight=)
G.add_edge("Madrid","Paris",weight=)
G.add_edge("Londres","Paris",weight=)
G.add_edge("Milán","Madrid",weight=)
G.add_edge("Milán","Paris",weight=)
G.add_edge("Milán","Viena",weight=)
G.add_edge("Viena","Moscú",weight=)
G.add_edge("Moscú","Múnich",weight=)
G.add_edge("Múnich","Fráncfort",weight=)
G.add_edge("Fráncfort","Milán",weight=)
G.add_edge("Melbourne","Sídney",weight=)
G.add_edge("Moscú","Abu Dabi",weight=)
G.add_edge("Moscú","Dubái",weight=)
G.add_edge("Helsinki","Moscú",weight=)
G.add_edge("Helsinki","Hong Kong",weight=)
G.add_edge("Bogotá","Toronto",weight=)
G.add_edge("Toronto","Vancouver",weight=)
G.add_edge("Vancouver","Melbourne",weight=)
G.add_edge("Bogotá","Los Ángeles",weight=)
G.add_edge("Los Ángeles","Auckland",weight=)
G.add_edge("Auckland","Melbourne",weight=)
G.add_edge("Bogotá","Múnich",weight=)
G.add_edge("Bogotá","Abu Dabi",weight=)
G.add_edge("Abu Dabi","Melbourne",weight=)
G.add_edge("Toronto","Winnipeg",weight=)
G.add_edge("Ottawa","Toronto",weight=)
G.add_edge("Ciudad de Panamá","Montreal",weight=)
G.add_edge("Toronto","Montreal",weight=)
G.add_edge("San José","Montreal",weight=)
G.add_edge("Ciudad de México","Montreal",weight=)
G.add_edge("Cartagena","Ámsterdam",weight=)
G.add_edge("Ámsterdam","Moscú",weight=)
G.add_edge("Moscú","Sochi",weight=)
G.add_edge("Paris","Moscú",weight=)
G.add_edge("Ciudad de Panamá","Cancún",weight=)
G.add_edge("Medellin","Cancún",weight=)
G.add_edge("Madrid","Valencia",weight=)
G.add_edge("New York","Estambul",weight=)
G.add_edge("Estambul","Valencia",weight=)
G.add_edge("Fráncfort","Valencia",weight=)
G.add_edge("Madrid","Barcelona",weight=)
G.add_edge("Cartagena","Ámsterdam",weight=)
G.add_edge("Ámsterdam","Barcelona",weight=)
G.add_edge("Paris","Barcelona",weight=)
G.add_edge("Madrid","Viena",weight=)
G.add_edge("Ciudad de Panamá","Madrid",weight=)
G.add_edge("Ámsterdam","Viena",weight=)
G.add_edge("Ámsterdam","Montpellier",weight=)
G.add_edge("Paris","Montpellier",weight=)
G.add_edge("Santo Domingo","Paris",weight=)
G.add_edge("Londres","Versalles",weight=)
G.add_edge("Bogotá","Houston",weight=)
G.add_edge("Houston","Chicago",weight=)
G.add_edge("Chicago","Versalles",weight=)
G.add_edge("Ámsterdam","Berlín",weight=)
G.add_edge("Toronto","Zúrich",weight=)
G.add_edge("Zúrich","Berlín",weight=)
G.add_edge("Múnich","Berlín",weight=)
G.add_edge("Ámsterdam","Varsovia",weight=)
G.add_edge("Paris","Varsovia",weight=)
G.add_edge("Estambul","Varsovia",weight=)
G.add_edge("Madrid","Zúrich",weight=)
G.add_edge("Zúrich","Varsovia",weight=)
G.add_edge("Londres","Varsovia",weight=)
G.add_edge("Varsovia","Kazán",weight=)
G.add_edge("Kazán","Moscú",weight=)
G.add_edge("Varsovia","Paris",weight=)
G.add_edge("Varsovia","Estocolmo",weight=)
G.add_edge("Varsovia","Dubái",weight=)
G.add_edge("Toronto","Londres",weight=)
G.add_edge("Londres","Dublín",weight=)
G.add_edge("Estambul","Dublín",weight=)
G.add_edge("Miami","Londres",weight=)
G.add_edge("Ámsterdam","Dublín",weight=)
G.add_edge("Múnich","Antalya",weight=)
G.add_edge("Estambul","Antalya",weight=)
G.add_edge("Estambul","Madrid",weight=)
G.add_edge("Londres","Estambul",weight=)
G.add_edge("Ámsterdam","Bucarest",weight=)
G.add_edge("Múnich","Bogotá",weight=)
G.add_edge("Múnich","Bucarest",weight=)
G.add_edge("Barcelona","Bucarest",weight=)


######ARISTAS QUE NO ESTAN EN EL GIT
G.add_edge("Bogotá","Quito",weight=)
G.add_edge("Ciudad de Panamá","Quito",weight=)
G.add_edge("Ámsterdam","Cracovia",weight=)
G.add_edge("Quito","Ámsterdam",weight=)
G.add_edge("Quito","Paris",weight=)
G.add_edge("Madrid","Hamburgo",weight=)
G.add_edge("Múnich","Hamburgo",weight=)
G.add_edge("Fráncfort","Hamburgo",weight=)
G.add_edge("Atlanta","Paris",weight=)
G.add_edge("Paris","Hamburgo",weight=)
G.add_edge("Hamburgo","Torun",weight=)
G.add_edge("Torun","Estambul",weight=)
G.add_edge("Estambul","Bogotá",weight=)
G.add_edge("Paris","Mánchester",weight=)
G.add_edge("Toronto","Dublín",weight=)
G.add_edge("Dublín","Mánchester",weight=)
G.add_edge("Ámsterdam","Birmingham",weight=)
G.add_edge("Fráncfort","Birmingham",weight=)
G.add_edge("Múnich","Birmingham",weight=)
G.add_edge("Estambul","Birmingham",weight=)
G.add_edge("Birmingham","Ámsterdam",weight=)
G.add_edge("Ámsterdam","Cork",weight=)
G.add_edge("Ciudad de Panamá","Ámsterdam",weight=)
G.add_edge("Paris","Ámsterdam",weight=)
G.add_edge("Londres","Cork",weight=)
G.add_edge("Lisboa","Madrid",weight=)
G.add_edge("Toronto","Viena",weight=)
G.add_edge("Viena","Lisboa",weight=)
G.add_edge("New York","Lisboa",weight=)
G.add_edge("Madrid","Braga",weight=)
G.add_edge("Estambul","Braga",weight=)
G.add_edge("Braga","Fráncfort",weight=)
G.add_edge("Fráncfort","Shanghái",weight=)
G.add_edge("Ámsterdam","Atenas",weight=)
G.add_edge("Ciudad de Panamá","Estambul",weight=)
G.add_edge("Estambul","Atenas",weight=)
G.add_edge("Paris","Atenas",weight=)
G.add_edge("Fráncfort","Atenas",weight=)
G.add_edge("Múnich","Sibiu",weight=)
G.add_edge("Miami","Múnich",weight=)

###MAS
G.add_edge("Paris","Helsinki",weight=)
G.add_edge("Helsinki","Turku",weight=)
G.add_edge("Zúrich","Estocolmo",weight=)
G.add_edge("Estocolmo","Turku",weight=)#FIN EUROPA
G.add_edge("Paris","Rabat",weight=)
G.add_edge("Madrid","Tánger",weight=)
G.add_edge("Paris","Tánger",weight=)
G.add_edge("Paris","Argel",weight=)
G.add_edge("Fráncfort","Argel",weight=)
G.add_edge("Argel","Orán",weight=)
G.add_edge("Estambul","Orán",weight=)
G.add_edge("Bogotá","Washington",weight=)
G.add_edge("Washington","Estambul",weight=)
G.add_edge("Estambul","El Cairo",weight=)
G.add_edge("Fráncfort","El Cairo",weight=)
G.add_edge("Estambul","Hurgada",weight=)
G.add_edge("El Cairo","Hurgada",weight=)
G.add_edge("Estambul","Jartum",weight=)
G.add_edge("Madrid","Abu Dabi",weight=)
G.add_edge("Abu Dabi","Jartum",weight=)
G.add_edge("Londres","Abu Dabi",weight=)
G.add_edge("Estambul","Abuya",weight=)
G.add_edge("Paris","Abuya",weight=)
G.add_edge("Paris","Luanda",weight=)
G.add_edge("Fráncfort","Johannesburgo",weight=)
G.add_edge("Johannesburgo","Gaborone",weight=)
G.add_edge("Bogotá","Lima",weight=)
G.add_edge("Sao Pablo","Lima",weight=)
G.add_edge("Sao Pablo","Johannesburgo",weight=)
G.add_edge("Johannesburgo","Maun",weight=)
G.add_edge("Bogotá","Santiago",weight=)
G.add_edge("Sao Pablo","Santiago",weight=)
G.add_edge("Johannesburgo","Durban",weight=)
G.add_edge("Estambul","Ankara",weight=)
G.add_edge("Fráncfort","Bombay",weight=)
G.add_edge("Ámsterdam","Bombay",weight=)
G.add_edge("Fráncfort","Nueva Delhi",weight=)
G.add_edge("Londres","Nueva Delhi",weight=)
G.add_edge("Houston","San Francisco",weight=)
G.add_edge("San Francisco","Pekín",weight=)
G.add_edge("Dallas","Miami",weight=)
G.add_edge("Dallas","Pekín",weight=)
G.add_edge("Houston","Chicago",weight=)
G.add_edge("Chicago","Shanghái",weight=)
G.add_edge("Fráncfort","Pekín",weight=)
G.add_edge("Pekín","Shanghái",weight=)
G.add_edge("Bogotá","Dallas",weight=)
G.add_edge("Pekín","Shenzhen",weight=)
G.add_edge("Madrid","Shanghái",weight=)
G.add_edge("Shanghái","Shenzhen",weight=)

#ULTIMAS ARISTAS
G.add_edge("Fráncfort","Astana",weight=)
G.add_edge("Estambul","Astana",weight=)
G.add_edge("Moscú","New York",weight=)
G.add_edge("Moscú","Shymkent",weight=)
G.add_edge("Ciudad de Panamá","New York",weight=)
G.add_edge("Moscú","Samarcanda",weight=)
G.add_edge("Londres","Moscú",weight=)
G.add_edge("Madrid","Moscú",weight=)
G.add_edge("Moscú","Taskent",weight=)
G.add_edge("Estambul","Taskent",weight=)
G.add_edge("Washington","Estambul",weight=)
G.add_edge("Paris","Riad",weight=)
G.add_edge("Riad","Meca",weight=)
G.add_edge("Estambul","Riad",weight=)
G.add_edge("Fráncfort","Riad",weight=)
G.add_edge("Paris","Riad",weight=)
G.add_edge("Riad","Abha",weight=)
G.add_edge("El cairo","Abha",weight=)
G.add_edge("Ciudad de México","Tokio",weight=)
G.add_edge("Bogotá","Ciudad de México",weight=5)
G.add_edge("Tokio","Yakarta",weight=)
G.add_edge("Los Ángeles","Hong Kong",weight=)
G.add_edge("Hong Kong","Surabaya",weight=)
G.add_edge("New York","Hong Kong",weight=)
G.add_edge("Abu Dabi","Bangkok",weight=)
G.add_edge("Madrid","Abu Dabi",weight=)
G.add_edge("Fráncfort","Bangkok",weight=)
G.add_edge("Bangkok","Phuket",weight=)
G.add_edge("Abu Dabi","Phuket",weight=)
G.add_edge("Dallas","Seúl",weight=)
G.add_edge("Los Ángeles","Seúl",weight=)
G.add_edge("Dallas","Tokio",weight=)
G.add_edge("Tokio","Busan",weight=)
G.add_edge("Vancouver","Tokio",weight=)
G.add_edge("Dallas","Daejeon",weight=)
G.add_edge("Los Ángeles","Daejeon",weight=)
G.add_edge("New York","Tokio",weight=)
G.add_edge("Tokio","Daejeon",weight=)
G.add_edge("Dallas","Kaesong",weight=)
G.add_edge("Atlanta","Kaesong",weight=)
G.add_edge("Tokio","Kaesong",weight=)
G.add_edge("Dallas","Haeju",weight=)
G.add_edge("Tokio","Haeju",weight=)
G.add_edge("Tokio","Hiroshima",weight=)
G.add_edge("San Francisco","Tokio",weight=)
G.add_edge("Washington","Tokio",weight=)
G.add_edge("Tokio","Kioto",weight=)
G.add_edge("Tokio","Manila",weight=)
G.add_edge("Hong Kong","Cebú",weight=)
G.add_edge("Toronto","Hong Kong",weight=)
G.add_edge("Hong Kong","Perth",weight=)
G.add_edge("Santiago","Bogotá",weight=)
G.add_edge("Santiago","Auckland",weight=)
G.add_edge("Auckland","Sídney",weight=)
G.add_edge("Sídney","Perth",weight=)
G.add_edge("Auckland","Wellington",weight=)
G.add_edge("Los Ángeles","Sídney",weight=)
G.add_edge("Sídney","Wellington",weight=)
G.add_edge("Los Ángeles","Auckland",weight=)
G.add_edge("Auckland","Brisbane",weight=)
G.add_edge("Cusco","Lima",weight=)
G.add_edge("Lima","Santiago",weight=)
G.add_edge("Bogotá","Cusco",weight=)
G.add_edge("Bogotá","Guayaquil",weight=)
G.add_edge("Guayaquil","Ámsterdam",weight=)
G.add_edge("Santiago","Concepción",weight=)
G.add_edge("Bogotá","Santiago",weight=)
G.add_edge("Santiago","Buenos Aires",weight=)
G.add_edge("Lima","Buenos Aires",weight=)
G.add_edge("Santiago","La Plata",weight=)
G.add_edge("Lima","Montevideo",weight=)
G.add_edge("Santiago","Montevideo",weight=)
G.add_edge("Bogotá","Buenos Aires",weight=)
G.add_edge("Buenos Aires","Punta del Este",weight=)
G.add_edge("Ciudad de Panamá","Nueva Orleans",weight=)
G.add_edge("New York","Nueva Orleans",weight=)
G.add_edge("Los Ángeles","Seattle",weight=)
G.add_edge("San Francisco","Seattle",weight=)
G.add_edge("Ciuda de Panamá","Orlando",weight=)
G.add_edge("Dallas","Las Vegas",weight=)
G.add_edge("Ciudad de Panamá","La Habana",weight=)
G.add_edge("Ciudad de México","La Habana",weight=)
G.add_edge("Ciudad de México","Guadalajara",weight=)
G.add_edge("Ciudad de Panamá","Ciudad de México",weight=)
G.add_edge("Ciudad de México","Monterrey",weight=)
G.add_edge("Houston","Monterrey",weight=)
G.add_edge("Houston","Ciudad de Panamá",weight=)
G.add_edge("Ciudad de México","Acapulco",weight=)
G.add_edge("Bogotá","Cancún",weight=)
G.add_edge("Cancún","Ciudad de México",weight=)
G.add_edge("Toronto","Winnipeg",weight=)
G.add_edge("Toronto","Ottawa",weight=)
G.add_edge("Ottawa","Winnipeg",weight=)
G.add_edge("Bogotá","Cartago",weight=)
G.add_edge("Ciudad de Panamá","Liberia",weight=)







#weight = nx.get_edge_attributes(G, 'weight')
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G,with_labels = True, node_size = 200)
#nx.draw_networkx_edge_labels(G,pos,edge_labels = weight)
plt.show()

