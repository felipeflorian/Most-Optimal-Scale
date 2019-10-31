import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()


#EUROPA---------------------------------------------------------------------------

#Italia
G.add_node("Roma", pos=(100, -60))
G.add_node("Milán", pos=(80, -30))
G.add_node("Venecia", pos=(130,-70))

#Francia
G.add_node("París", pos=(150,60))
G.add_node("Montpellier", pos=(170,60))
G.add_node("Versalles", pos=(190,80))

#España
G.add_node("Madrid", pos=(80, 40))
G.add_node("Barcelona", pos=())
G.add_node("Valencia", pos=())

#Alemania
G.add_node("Berlín", pos=(170, 80))
G.add_node("Roma", pos=(140,70))
G.add_node("Roma", pos=())

#Polonia
G.add_node("Torun", pos=())
G.add_node("Cracovia", pos=())
G.add_node("Varsovia", pos=())

#Reino Unido
G.add_node("Londres", pos=())
G.add_node("Mánchester", pos=())
G.add_node("Oxford", pos=())

#Irlanda
G.add_node("Dublín", pos=())
G.add_node("Cork", pos=())
G.add_node("Kilkenny", pos=())

#Portugal
G.add_node("Lisboa", pos=())
G.add_node("Braga", pos=())
G.add_node("Lagos", pos=())

#Grecia
G.add_node("Atenas", pos=())
G.add_node("Olimpia", pos=())
G.add_node("Corinto", pos=())

#Rumanía
G.add_node("Bucarest", pos=())
G.add_node("Sibiu", pos=())
G.add_node("Constanza", pos=())

#Austria
G.add_node("Viena", pos=())
G.add_node("Hallstatt", pos=())
G.add_node("Villach", pos=())

#Ucrania
G.add_node("Kiev", pos=())
G.add_node("Poltava", pos=())
G.add_node("Járkov", pos=())

#Finlandia
G.add_node("Helsinki", pos=())
G.add_node("Pori", pos=())
G.add_node("Turku", pos=())

#Noruega
G.add_node("Oslo", pos=())
G.add_node("Tromso", pos=())
G.add_node("Bergen", pos=())

#Suecia
G.add_node("Estocolmo", pos=())
G.add_node("Malmö", pos=())
G.add_node("Upsala", pos=())


#AFRICA---------------------------------------------------------------------------

#Marruecos
G.add_node("Rabat", pos=())
G.add_node("Tánger", pos=())
G.add_node("Mequinez", pos=())

#Argelia
G.add_node("Argel", pos=())
G.add_node("Orán", pos=())
G.add_node("Tlemecén", pos=())

#Libia
G.add_node("Trípoli", pos=())
G.add_node("Bengasi", pos=())
G.add_node("Misurata", pos=())

#Egipto
G.add_node("El Cairo", pos=())
G.add_node("Guiza", pos=())
G.add_node("Hurganda", pos=())

#Sudán
G.add_node("Jartum", pos=())
G.add_node("Kasala", pos=())
G.add_node("Omdurmán", pos=())

#Nigeria
G.add_node("Lagos", pos=())
G.add_node("Abuya", pos=())
G.add_node("Abeokuta", pos=())

#Malí
G.add_node("Bamako", pos=())
G.add_node("Tombuctú", pos=())
G.add_node("Gao", pos=())

#Somalia
G.add_node("Mogadiscio", pos=())
G.add_node("Kismaayo", pos=())
G.add_node("Hargeisa", pos=())

#Kenia
G.add_node("Nairobi", pos=())
G.add_node("Mombasa", pos=())
G.add_node("Malindi", pos=())

#Republica Democratica del Congo
G.add_node("Kinshasa", pos=())
G.add_node("Bukavu", pos=())
G.add_node("Boma", pos=())

#Angola
G.add_node("Luanda", pos=())
G.add_node("Huambo", pos=())
G.add_node("Lubango", pos=())

#Zimbabue
G.add_node("Harare", pos=())
G.add_node("Bulawayo", pos=())
G.add_node("Chinhoyi", pos=())

#Botsuana
G.add_node("Serowe", pos=())
G.add_node("Gaborone", pos=())
G.add_node("Maun", pos=())

#Sudáfrica
G.add_node("Johannesburgo", pos=())
G.add_node("Durban", pos=())
G.add_node("Pretoria", pos=())

#Madagascar
G.add_node("Toliara", pos=())
G.add_node("Antananarivo", pos=())
G.add_node("Antsiranana", pos=())

#Costa de Marfíl
G.add_node("Abiyán", pos=())
G.add_node("Yamasukro", pos=())
G.add_node("Man", pos=())


#ASIA---------------------------------------------------------------------------

#Rusia
G.add_node("Moscú", pos=(150, 90))
G.add_node("Kazán", pos=())
G.add_node("Sochi", pos=(140, 120))

#Turquía
G.add_node("Estambul", pos=())
G.add_node("Ankara", pos=())
G.add_node("Antalya", pos=())

#India
G.add_node("Jaipur", pos=())
G.add_node("Bombay", pos=())
G.add_node("Nueva Delhi", pos=())

#Pakistán
G.add_node("Islamabad", pos=())
G.add_node("Multán", pos=())
G.add_node("Lahore", pos=())

#Afganistan
G.add_node("Kabul", pos=())
G.add_node("Kandahar", pos=())
G.add_node("Ganzi", pos=())

#China
G.add_node("Pekín", pos=(210, 60))
G.add_node("Shanghái", pos=(230,40))
G.add_node("Shenzhen", pos=())

#Irak
G.add_node("Bagdad", pos=())
G.add_node("Mosul", pos=())
G.add_node("Erbil", pos=())

#Irán
G.add_node("Teherán", pos=())
G.add_node("Yazd", pos=())
G.add_node("Tabriz", pos=())

#Kazajistán
G.add_node("Astaná", pos=())
G.add_node("Shymkent", pos=())
G.add_node("Pavlodar", pos=())

#Uzbekistán
G.add_node("Samarcanda", pos=())
G.add_node("Bujara", pos=())
G.add_node("Taskent", pos=())

#Siría
G.add_node("Hama", pos=())
G.add_node("Alepo", pos=())
G.add_node("Lataquia", pos=())

#Arabia Saudita
G.add_node("Meca", pos=())
G.add_node("Riad", pos=())
G.add_node("Abha", pos=())

#Emiratos Árabes Unidos
G.add_node("Dubái", pos=())
G.add_node("Abu Dabi", pos=())
G.add_node("Ajman", pos=())

#Vietnam
G.add_node("Hanói", pos=())
G.add_node("Hue", pos=())
G.add_node("Nha Trang", pos=())

#Indonesia
G.add_node("Yakarta", pos=())
G.add_node("Surabaya", pos=())
G.add_node("Denpasar", pos=())

#Malasia
G.add_node("Malaca", pos=())
G.add_node("Putrajaya", pos=())
G.add_node("Kuantan", pos=())

#Myanmar
G.add_node("Pegu", pos=())
G.add_node("Rangún", pos=())
G.add_node("Mandalay", pos=())

#Nepal
G.add_node("Katmandú", pos=())
G.add_node("Patan", pos=())
G.add_node("Nagarkot", pos=())

#Tailandia
G.add_node("Bangkok", pos=())
G.add_node("Ayutthaya", pos=())
G.add_node("Phuket", pos=())

#Corea del Sur
G.add_node("Seúl", pos=())
G.add_node("Busan", pos=())
G.add_node("Daejeon", pos=())

#Corea del Norte
G.add_node("Kaesong", pos=())
G.add_node("Pionyang", pos=())
G.add_node("Haeju", pos=())

#Japon
G.add_node("Tokio", pos=())
G.add_node("Hiroshima", pos=())
G.add_node("Kioto", pos=())

#Filipinas
G.add_node("Manila", pos=())
G.add_node("Cebú", pos=())
G.add_node("Dávao", pos=())

#Yemen
G.add_node("Saná", pos=())
G.add_node("Adén", pos=())
G.add_node("Dhamar", pos=())


#OCEANÍA---------------------------------------------------------------------------

#Tasmania
G.add_node("Hobart", pos=())

#Australia Occidental
G.add_node("Perth", pos=())

#Australia Meridional
G.add_node("Adelaida", pos=())

#Nueva Gales del Sur
G.add_node("Sídney", pos=(300, -50))

#Victoria
G.add_node("Melbourne", pos=())

#Queensland
G.add_node("Brisbane", pos=())

#Nueva Zelanda
G.add_node("Wellington", pos=())
G.add_node("Christchurch", pos=())
G.add_node("Auckland", pos=())


#SUR AMÉRICA---------------------------------------------------------------------------

#Colombia
G.add_node("Bogotá", pos=(-100, -100))
G.add_node("Medellin", pos=(-60,-40))
G.add_node("Cali", pos=(60, -70))

#Venezuela
G.add_node("Caracas", pos=())
G.add_node("Ciudad Bolívar", pos=())
G.add_node("Maracaibo", pos=())

#Ecuador
G.add_node("Quito", pos=())
G.add_node("Cuenca", pos=())
G.add_node("Guayaquil", pos=())

#Perú
G.add_node("Lima", pos=(-20, -100))
G.add_node("Cusco", pos=())
G.add_node("Iquitos", pos=())

#Brasil
G.add_node("Río de Janeiro", pos=(5, -100))
G.add_node("Brasilia", pos=())
G.add_node("São Pablo", pos=())

#Chile
G.add_node("Santiago de Chile", pos=())
G.add_node("Valparaíso", pos=())
G.add_node("Concepción", pos=())

#Argentina
G.add_node("Buenos Aires", pos=())
G.add_node("Rosario", pos=())
G.add_node("La Plata", pos=())

#Uruguay
G.add_node("Montevideo", pos=())
G.add_node("Punta del Este", pos=())
G.add_node("Salto", pos=())

#Paraguay
G.add_node("Asunción", pos=())
G.add_node("Luque", pos=())
G.add_node("Encarnación", pos=())

#Bolivia
G.add_node("La Paz", pos=())
G.add_node("Sucre", pos=())
G.add_node("Cochabamba", pos=())

#Guyana
G.add_node("Georgetown", pos=())


#NORTE ÁMERICA---------------------------------------------------------------------------

#Estados Unidos
G.add_node("Houston", pos=(-80, 85))
G.add_node("Dallas", pos=())
G.add_node("Nueva Orleans", pos=())
G.add_node("Seattle", pos=())
G.add_node("Portland", pos=())
G.add_node("San Francisco", pos=())
G.add_node("Las Vegas", pos=())
G.add_node("Los Ángeles", pos=(-35,30))
G.add_node("Phoenix", pos=())
G.add_node("Kansas City", pos=())
G.add_node("Springfield", pos=())
G.add_node("Montgomery", pos=())
G.add_node("Atlanta", pos=())
G.add_node("Jacksonville", pos=())
G.add_node("Orlando", pos=(-95, 70))
G.add_node("Tampa", pos=())
G.add_node("Miami", pos=(-25, 75))
G.add_node("Charlotte", pos=())
G.add_node("Washington DC", pos=())
G.add_node("Nueva York", pos=(-5,100))
G.add_node("Portland", pos=())
G.add_node("Atlanta", pos=(-150, 75))
G.add_node("Nashville", pos=())
G.add_node("Indianápolis", pos=())
G.add_node("Mineápolis", pos=())
G.add_node("Chicago", pos=())
G.add_node("Alaska", pos=())

#Panamá
G.add_node("Ciudad de Panamá", pos=(0, -70))

#Costa Rica
G.add_node("Cartago", pos=())
G.add_node("San José", pos=())
G.add_node("Liberia", pos=())

#Nicaragua
G.add_node("Granada", pos=())
G.add_node("León", pos=())
G.add_node("Managua", pos=())

#Cuba
G.add_node("La Habana", pos=())
G.add_node("Santiago de Cuba", pos=())
G.add_node("Trinidad", pos=())

#Guatemala
G.add_node("Ciudad de Guatemala", pos=())
G.add_node("Petén", pos=())
G.add_node("Izabal", pos=())

#Honduras
G.add_node("Tegucigalpa", pos=())
G.add_node("La Ceiba", pos=())
G.add_node("Puerto Cortés", pos=())

#República Dominicana
G.add_node("Santo Domingo", pos=())
G.add_node("Puerto Plata", pos=())
G.add_node("La Romana", pos=())

#Puerto Rico
G.add_node("San Juan", pos=())
G.add_node("Ponce", pos=())
G.add_node("Guaynabo", pos=())

#México
G.add_node("Mérida", pos=())
G.add_node("Ciudad de México", pos=())
G.add_node("Guadalajara", pos=())
G.add_node("Monterrey", pos=())
G.add_node("Hermosillo", pos=())
G.add_node("Tijuana", pos=())
G.add_node("Acapulco", pos=())
G.add_node("Cancún", pos=())

#Canadá
G.add_node("Toronto", pos=(-10,150))
G.add_node("Vancouver", pos=())
G.add_node("Montereal", pos=(-25, 135))
G.add_node("Ottawa", pos=())
G.add_node("Winnipeg", pos=())

#Groenlandia
G.add_node("Nuuk", pos=())
G.add_node("Kangerlussuaq", pos=())
G.add_node("Narsarsuaq", pos=())




#-----------------------------------------------------ARISTAS---------------------------------------------------------------------------
G.add_edge("Bogota","Cartagena", weight = 1.21 )
G.add_edge("Bogota","Medellin", weight = 0.45)
G.add_edge("Bogota","Miami", weight = 3.17)
G.add_edge("Bogota","Toronto", weight = 5.35)
G.add_edge("Bogota","Frankfurt", weight = 11.14)
G.add_edge("Bogota","CPanama", weight = 1.31)
G.add_edge("Bogota","Lima",weight = 2.38 )
G.add_edge("Bogota","Atlanta", weight=4.26)
G.add_edge("Bogota","Cincinnati", weight = 5.7)
G.add_edge("Bogota","Houston",weight = 4.39)
#G.add_edge("Bogota","LA")
G.add_edge("Bogota","Munich",weight=11.29)
G.add_edge("Cartagena","Amsterdam",weight=11.29)
G.add_edge("Amsterdam","Madrid",weight =2.10)
G.add_edge("Medellin","Madrid",weight = 9.58)
G.add_edge("Miami","New york",weight=2.29)
G.add_edge("New york","Madrid",weight=7.17)
G.add_edge("Toronto","Paris",weight=7.34)
G.add_edge("Toronto","Montreal",weight=1.8)
G.add_edge("Montreal","Paris",weight=6.58)
G.add_edge("CPanama","Amsterdam",weight=6.58)
G.add_edge("CPanama","Rio",weight=6.43)
G.add_edge("Medellin","Lima",weight=2.49)
G.add_edge("Lima","Rio",weight=4.54)
G.add_edge("Houston","Sidney",weight=16.52)
G.add_edge("Atlanta","New york",weight=1.49)
G.add_edge("Cincinnati", "New york",weight=1.44)
G.add_edge("Miami","Milan",weight=9.54)
G.add_edge("New york","Milan",weight=8.7)
G.add_edge("Frankfurt","Roma",weight=1.48)



weight = nx.get_edge_attributes(G, 'weight')
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G,pos,  with_labels = True, node_size = 200)
#nx.draw_networkx_edge_labels(G,pos,edge_labels = weight)
plt.show()
