#!/usr/bin/env python
#-*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()


#EUROPA---------------------------------------------------------------------------

#Italia
G.add_node("Roma", pos=(100, -60))
G.add_node("Milán", pos=(80, -30))
G.add_node("Venecia", pos=(130,-70))

Italia = ["Roma","Milán","Venecia"]


#Francia
G.add_node("París", pos=(150,60))
G.add_node("Montpellier", pos=(170,60))
G.add_node("Versalles", pos=(190,80))

Francia = ["Paris","Montpellier","Versalles"]


#España
G.add_node("Madrid", pos=(80, 40))
G.add_node("Barcelona", pos=(100,30))
G.add_node("Valencia", pos=(110,-10))

España = ["Madrid", "Barcelona", "Valencia"]


#Alemania
G.add_node("Berlín", pos=(170, 80))
G.add_node("Hamburgo", pos=(165, 90))
G.add_node("Fráncfort", pos=(150, 100))

Alemania = ["Berlín", "Hamburgo", "Fráncfort"]


#Polonia
G.add_node("Torun", pos=(190,130))
G.add_node("Cracovia", pos=(130,150))
G.add_node("Varsovia", pos=(150,140))

Polonia = ["Torun", "Cracovia", "Varsovia"]


#Inglaterra
G.add_node("Londres", pos=(100,500))
G.add_node("Mánchester", pos=(115,480))
G.add_node("Oxford", pos=(130,490))

Inglaterra = ["Londres", "Mánchester", "Oxford"]


#Irlanda
G.add_node("Dublín", pos=(150,300))
G.add_node("Cork", pos=(120,250))
G.add_node("Kilkenny", pos=(140,320))

Irlanda = ["Dublín", "Cork", "Kilkenny"]


#Portugal
G.add_node("Lisboa", pos=(70,130))
G.add_node("Braga", pos=(90,140))
G.add_node("Lagos", pos=(80,150))

Portugal = ["Lisboa", "Braga", "Lagos"]


#Grecia
G.add_node("Atenas", pos=(160,210))
G.add_node("Olimpia", pos=(140,240))
G.add_node("Corinto", pos=(130,250))

Grecia = ["Atenas", "Olimpia", "Corinto"]


#Rumanía
G.add_node("Bucarest", pos=(130,50))
G.add_node("Sibiu", pos=(150,70))
G.add_node("Constanza", pos=(140,60))

Rumanía = ["Bucarest", "Sibiu", "Constanza"]


#Austria
G.add_node("Viena", pos=(150,300))
G.add_node("Hallstatt", pos=(160,350))
G.add_node("Villach", pos=(130,320))

Austria = ["Viena", "Hallstatt", "Villach"]


#Ucrania
G.add_node("Kiev", pos=(140,220))
G.add_node("Poltava", pos=(130,200))
G.add_node("Járkov", pos=(150,210))

Ucrania = ["Kiev", "Poltava", "Járkov"]


#Finlandia
G.add_node("Helsinki", pos=(180,310))
G.add_node("Pori", pos=(190,320))
G.add_node("Turku", pos=(170,290))

Finlandia = ["Helsinki", "Pori", "Turku"]


#Noruega
G.add_node("Oslo", pos=(160,-30))
G.add_node("Tromso", pos=(150,-10))
G.add_node("Bergen", pos=(160,-40))

Noruega = ["Oslo", "Tromso", "Bergen"]


#Suecia
G.add_node("Estocolmo", pos=(100,600))
G.add_node("Malmö", pos=(120,550))
G.add_node("Upsala", pos=(140,500))

Suecia = ["Estocolmo", "Malmö", "Upsala"]


Europa = ["Italia", "Francia", "España", "Alemania", "Polonia", "Inglaterra", "Irlanda", "Portugal", "Grecia", "Rumanía", "Austria", "Ucrania", "Finlandia", "Noruega", "Suecia"]


#AFRICA---------------------------------------------------------------------------

#Marruecos
G.add_node("Rabat", pos=(130,-250))
G.add_node("Tánger", pos=(140,-230))
G.add_node("Mequinez", pos=(100,-250))

Marruecos = ["Rabat", "Tánger", "Mequinez"]


#Argelia
G.add_node("Argel", pos=(160,-200))
G.add_node("Orán", pos=(180,-215))
G.add_node("Tlemecén", pos=(150,-230))

Argelia = ["Argel", "Orán", "Tlemecén"]


#Egipto
G.add_node("El Cairo", pos=(120,-90))
G.add_node("Guiza", pos=(140,-70))
G.add_node("Hurganda", pos=(150,-100))

Egipto = ["El Cairo", "Guiza", "Hurganda"]


#Sudán
G.add_node("Jartum", pos=(140,-60))
G.add_node("Kasala", pos=(120,-70))
G.add_node("Omdurmán", pos=(160,-90))

Sudán = ["Jartum", "Kasala", "Omdurmán"]


#Nigeria
G.add_node("Lagos", pos=(180,-60))
G.add_node("Abuya", pos=(170,-30))
G.add_node("Abeokuta", pos=(190,-50))

Nigeria = ["Lagos", "Abuya", "Abeokuta"]


#Malí
G.add_node("Bamako", pos=(140,-150))
G.add_node("Tombuctú", pos=(150,-170))
G.add_node("Gao", pos=(160,-190))

Malí = ["Bamako", "Tombuctú", "Gao"]


#Somalia
G.add_node("Mogadiscio", pos=(180,-30))
G.add_node("Kismaayo", pos=(170,-50))
G.add_node("Hargeisa", pos=(150,-70))

Somalia = ["Mogadiscio", "Kismaayo", "Hargeisa"]


#Kenia
G.add_node("Nairobi", pos=(150,-150))
G.add_node("Mombasa", pos=(160,-170))
G.add_node("Malindi", pos=(170,-160))

Kenia = ["Nairobi", "Mombasa", "Malindi"]


# #Republica Democrática del Congo
# G.add_node("Kinshasa", pos=(200,-230))
# G.add_node("Bukavu", pos=(210,-220))
# G.add_node("Boma", pos=(220,-200))
#
# Republica Democrática del Congo



#Angola
G.add_node("Luanda", pos=(210,-30))
G.add_node("Huambo", pos=(200,-50))
G.add_node("Lubango", pos=(230,-80))

Angola = ["Luanda", "Huambo", "Lubango"]


#Botsuana
G.add_node("Serowe", pos=(180,-180))
G.add_node("Gaborone", pos=(190,-200))
G.add_node("Maun", pos=(170,-230))

Botsuana = ["Serowe", "Gaborone", "Maun"]


#Sudáfrica
G.add_node("Johannesburgo", pos=(210,-210))
G.add_node("Durban", pos=(200,-200))
G.add_node("Pretoria", pos=(220,-240))

Sudáfica = ["Johannesburgo", "Durban", "Pretoria"]


#Madagascar
G.add_node("Toliara", pos=(230,-250))
G.add_node("Antananarivo", pos=(250,-270))
G.add_node("Antsiranana", pos=(260,-280))

Madagascar = ["Toliara", "Antananarivo", "Antsiranana"]


#Costa de Marfíl
G.add_node("Abiyán", pos=(280,-260))
G.add_node("Yamasukro", pos=(270,-300))
G.add_node("Man", pos=(260,-290))

CostadeMarfíl = ["Abiyán", "Yamasukro", "Man"]


Africa = ["Marruecos", "Argelia", "Egipto", "Sudán", "Nigeria", "Malí", "Somalia", "Kenia", "Angola", "Botsuana", "Sudáfrica", "Madagascar", "Costa de Marfíl"]


#ASIA---------------------------------------------------------------------------

#Rusia
G.add_node("Moscú", pos=(150, 90))
G.add_node("Kazán", pos=(180,100))
G.add_node("Sochi", pos=(140, 120))

Rusia = ["Moscú","Kazán", "Sochi"]


#Turquía
G.add_node("Estambul", pos=(100,300))
G.add_node("Ankara", pos=(120,350))
G.add_node("Antalya", pos=(115,325))

Turquía = ["Estambul", "Ankara", "Antalya"]


#India
G.add_node("Jaipur", pos=(130,150))
G.add_node("Bombay", pos=(140,180))
G.add_node("Nueva Delhi", pos=(120,160))

India = ["Jaipur", "Bombay", "Nueva Delhi"]


#Pakistán
G.add_node("Islamabad", pos=(160,170))
G.add_node("Multán", pos=(140,140))
G.add_node("Lahore", pos=(120,120))

Pakistán = ["Islamabad", "Multán", "Lahore"]


#Afganistan
G.add_node("Kabul", pos=(200,210))
G.add_node("Kandahar", pos=(210,220))
G.add_node("Ganzi", pos=(190,200))

Afganistan = ["Kabul", "Kandahar", "Ganzi"]


#China
G.add_node("Pekín", pos=(210, 60))
G.add_node("Shanghái", pos=(230,40))
G.add_node("Shenzhen", pos=(220,50))

China = ["Pekín", "Shanghái", "Shenzhen"]


#Irak
G.add_node("Bagdad", pos=(270,240))
G.add_node("Mosul", pos=(290,220))
G.add_node("Erbil", pos=(260,210))

Irak = ["Bagdad", "Mosul", "Erbil"]


#Irán
G.add_node("Teherán", pos=(190,400))
G.add_node("Yazd", pos=(170,410))
G.add_node("Tabriz", pos=(180,390))

Irán = ["Teherán", "Yazd", "Tabriz"]


#Kazajistán
G.add_node("Astaná", pos=(200,310))
G.add_node("Shymkent", pos=(220,300))
G.add_node("Pavlodar", pos=(210,280))

Kazajistán = ["Astaná", "Shymkent", "Pavlodar"]


#Uzbekistán
G.add_node("Samarcanda", pos=(300,400))
G.add_node("Bujara", pos=(310,420))
G.add_node("Taskent", pos=(330,390))

Uzbekistán = ["Samarcanda", "Bujara", "Taskent"]


#Arabia Saudita
G.add_node("Meca", pos=(200,40))
G.add_node("Riad", pos=(220,20))
G.add_node("Abha", pos=(230,0))

ArabiaSaudita = ["Meca", "Riad", "Abha"]


#Emiratos Árabes Unidos
G.add_node("Dubái", pos=(210,80))
G.add_node("Abu Dabi", pos=(230,100))
G.add_node("Ajman", pos=(210,50))

EmiratosÁrabesUnidos = ["Dubái", "Abu Dabi", "Ajman"]


#Vietnam
G.add_node("Hanói", pos=(390,45))
G.add_node("Hue", pos=(370,70))
G.add_node("Nha Trang", pos=(350,20))

Vietnam = ["Hanói", "Hue", "Nha Trang"]


#Indonesia
G.add_node("Yakarta", pos=(300,470))
G.add_node("Surabaya", pos=(320,450))
G.add_node("Denpasar", pos=(300,420))

Indonesia = ["Yakarta", "Surabaya", "Denpasar"]


#Malasia
G.add_node("Malaca", pos=(280,100))
G.add_node("Putrajaya", pos=(260,120))
G.add_node("Kuantan", pos=(240,140))

Malasia = ["Malaca", "Putrajaya", "Kuantan"]


#Myanmar
G.add_node("Pegu", pos=(300,-10))
G.add_node("Rangún", pos=(310,-30))
G.add_node("Mandalay", pos=(320,-20))

Myanmar = ["Pegu", "Rangún", "Mandalay"]


#Nepal
G.add_node("Katmandú", pos=(350,-80))
G.add_node("Patan", pos=(370,-60))
G.add_node("Nagarkot", pos=(340,-40))

Nepal = ["Katmandú", "Patan", "Nagarkot"]


#Tailandia
G.add_node("Bangkok", pos=(300,120))
G.add_node("Ayutthaya", pos=(310,100))
G.add_node("Phuket", pos=(280,80))

Tailandia = ["Bangkok", "Ayutthaya", "Phuket"]


#Corea del Sur
G.add_node("Seúl", pos=(380,100))
G.add_node("Busan", pos=(400,120))
G.add_node("Daejeon", pos=(420,140))

CoreaDelSur = ["Seúl", "Busan", "Daejeon"]


#Corea del Norte
G.add_node("Kaesong", pos=(450,130))
G.add_node("Pionyang", pos=(460,150))
G.add_node("Haeju", pos=(480,170))

CoreaDelNorte = ["Kaesong", "Pionyang", "Haeju"]


#Japon
G.add_node("Tokio", pos=(500, 300))
G.add_node("Hiroshima", pos=(480,320))
G.add_node("Kioto", pos=(490,280))

Japón = ["Tokio", "Hiroshima", "Kioto"]


#Filipinas
G.add_node("Manila", pos=(380,0))
G.add_node("Cebú", pos=(350,-20))
G.add_node("Dávao", pos=(360,-10))

Filipinas = ["Manila", "Cebú", "Dávao"]


Asia = ["Rusia", "Turquía", "India", "Pakistán", "Afganistan", "China", "Irak", "Irán", "Kazajistán", "Uzbekistán", "Arabia Saudita", "Emiratos Árabes Unidos", "Vietnam", "Indonesia", "Malasia", "Myanmar", "Nepal", "Tailandia", "Corea del Sur", "Corea del Norte", "Japón", "Filipinas"]


#OCEANÍA---------------------------------------------------------------------------

#Tasmania
G.add_node("Hobart", pos=(600, 0))

Tasmania = ["Hobart"]


#Australia
G.add_node("Perth", pos=(620,40))
G.add_node("Adelaida", pos=(610,60))
G.add_node("Sídney", pos=(650, 50))
G.add_node("Melbourne", pos=(680, 80))
G.add_node("Brisbane", pos=(670,40))

Australia = ["Perth", "Adelaida", "Sídney", "Melbourne", "Brisbane"]


#Nueva Zelanda
G.add_node("Wellington", pos=(580,100))
G.add_node("Christchurch", pos=(560,70))
G.add_node("Auckland", pos=(550,110))

NuevaZelanda = ["Wellington", "Christchurch", "Auckland"]


Oceanía = ["Tasmania", "Australia", "Nueva Zelanda"]


#SUR AMÉRICA---------------------------------------------------------------------------

#Colombia
G.add_node("Bogotá", pos=(-100, -100))
G.add_node("Medellin", pos=(-60,-40))
G.add_node("Cali", pos=(60, -70))

#Venezuela
G.add_node("Caracas", pos=(-120,-100))
G.add_node("Ciudad Bolívar", pos=(-140,-80))
G.add_node("Valencia", pos=(-160,-70))

#Ecuador
G.add_node("Quito", pos=(-200,-50))
G.add_node("Cuenca", pos=(-230,-70))
G.add_node("Guayaquil", pos=(-250,-90))

#Perú
G.add_node("Lima", pos=(-20, -100))
G.add_node("Cusco", pos=(-50,-130))
G.add_node("Iquitos", pos=(-70,-170))

#Brasil
G.add_node("Río de Janeiro", pos=(5, -100))
G.add_node("Brasilia", pos=(30,-120))
G.add_node("São Pablo", pos=(50,-90))

#Chile
G.add_node("Santiago de Chile", pos=(-140,-80))
G.add_node("Valparaíso", pos=(-160,-50))
G.add_node("Concepción", pos=(-180,-100))

#Argentina
G.add_node("Buenos Aires", pos=(-150,-90))
G.add_node("Rosario", pos=(-170,-100))
G.add_node("La Plata", pos=(-160,-200))

#Uruguay
G.add_node("Montevideo", pos=(-130,-100))
G.add_node("Punta del Este", pos=(-110,-70))
G.add_node("Salto", pos=(-160,-90))

#Paraguay
G.add_node("Asunción", pos=(-200,-100))
G.add_node("Luque", pos=(-220,-60))
G.add_node("Encarnación", pos=(-240,-90))

#Bolivia
G.add_node("La Paz", pos=(-300,-310))
G.add_node("Sucre", pos=(-340,-300))
G.add_node("Cochabamba", pos=(-320,-280))


SurÁmerica = ["Colombia", "Venezuela", "Ecuador", "Perú", "Brasil", "Chile", "Argentina", "Uruguay", "Paraguay", "Bolivia"]


#NORTE ÁMERICA---------------------------------------------------------------------------

#Estados Unidos
G.add_node("Houston", pos=(-80, 85))
G.add_node("Dallas", pos=(-90,100))
G.add_node("Nueva Orleans", pos=(-100,110))
G.add_node("Seattle", pos=(-110,120))
G.add_node("Portland", pos=(-120,130))
G.add_node("San Francisco", pos=(-130,140))
G.add_node("Las Vegas", pos=(-140,150))
G.add_node("Los Ángeles", pos=(-150,160))
G.add_node("Phoenix", pos=(-160,170))
G.add_node("Kansas City", pos=(-170,180))
G.add_node("Springfield", pos=(-180,190))
G.add_node("Montgomery", pos=(-190,200))
G.add_node("Atlanta", pos=(-200,210))
G.add_node("Jacksonville", pos=(-210,220))
G.add_node("Orlando", pos=(-220, 230))
G.add_node("Tampa", pos=(-230,240))
G.add_node("Miami", pos=(-240,250 ))
G.add_node("Charlotte", pos=(-200,200))
G.add_node("Washington DC", pos=(-180,190))
G.add_node("Nueva York", pos=(-170,80))
G.add_node("Portland", pos=(-190,90))
G.add_node("Atlanta", pos=(-150, 75))
G.add_node("Nashville", pos=(-140,100))
G.add_node("Indianápolis", pos=(-180,30))
G.add_node("Mineápolis", pos=(-200,70))
G.add_node("Chicago", pos=(-210,80))
G.add_node("Alaska", pos=(-240,90))

#Panamá
G.add_node("Ciudad de Panamá", pos=(0, -70))

#Costa Rica
G.add_node("Cartago", pos=(-300,80))
G.add_node("San José", pos=(-320,100))
G.add_node("Liberia", pos=(-310,60))

#Nicaragua
G.add_node("Granada", pos=(-400,-30))
G.add_node("León", pos=(-410,-50))
G.add_node("Managua", pos=(-380,0))

#Cuba
G.add_node("La Habana", pos=(-310,-100))
G.add_node("Santiago de Cuba", pos=(-320,-80))
G.add_node("Trinidad", pos=(-280,-120))

#Guatemala
G.add_node("Ciudad de Guatemala", pos=(-290,10))
G.add_node("Petén", pos=(-300,40))
G.add_node("Izabal", pos=(-330,70))

#Honduras
G.add_node("Tegucigalpa", pos=(-310,-210))
G.add_node("La Ceiba", pos=(-340,-230))
G.add_node("Puerto Cortés", pos=(-320,-260))

#República Dominicana
G.add_node("Santo Domingo", pos=(-410,-30))
G.add_node("Puerto Plata", pos=(-430,-50))
G.add_node("La Romana", pos=(-460,-70))

#Puerto Rico
G.add_node("San Juan", pos=(-400,50))
G.add_node("Ponce", pos=(-420,70))
G.add_node("Guaynabo", pos=(-400,90))

#México
G.add_node("Ciudad de México", pos=(-380,120))
G.add_node("Guadalajara", pos=(-350,90))
G.add_node("Monterrey", pos=(-330,180))
G.add_node("Tijuana", pos=(-350,160))
G.add_node("Acapulco", pos=(-400,200))
G.add_node("Cancún", pos=(-390,230))

#Canadá
G.add_node("Toronto", pos=(-10,150))
G.add_node("Vancouver", pos=(-30,170))
G.add_node("Montereal", pos=(-25, 135))
G.add_node("Ottawa", pos=(-60,110))
G.add_node("Winnipeg", pos=(-80,10))

#Groenlandia
G.add_node("Nuuk", pos=(-400,500))
G.add_node("Kangerlussuaq", pos=(-410,400))
G.add_node("Narsarsuaq", pos=(-450,450))


NorteÁmerica = ["Estados Unidos", "Panamá", "Costa Rica", "Nicaragua", "Cuba", "Guatemala", "Honduras", "Republica Dominicana", "Puerto Rico", "México", "Canadá", "Groenlandia"]


#-----------------------------------------------------ARISTAS---------------------------------------------------------------------------
G.add_edge("Bogota","Cartagena", weight = 1.21 )
G.add_edge("Bogota","Medellin", weight = 0.45)
G.add_edge("Bogota","Miami", weight = 3.17)
#g.add_edge("Bogota", "Ciudad de Panamá", weight = )
#g.add_edge("Ciudad de Panamá", "La Habana", weight = ) #Cuba
#g.add_edge("Ciudad de Panamá", "Valencia", weight = ) #Venezuela




#weight = nx.get_edge_attributes(G, 'weight')
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G,with_labels = True, node_size = 200)
#nx.draw_networkx_edge_labels(G,pos,edge_labels = weight)
plt.show()

