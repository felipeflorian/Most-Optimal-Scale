import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

#USA
G.add_node("New york", pos=(-5,100))
G.add_node("Miami", pos=(-25, 75))
#G.add_node("Fort Lauderdale", pos=(-50, 50))
G.add_node("Atlanta", pos=(-150, 75))
G.add_node("Houston", pos=(-80, 85))
G.add_node("Cincinnati", pos=(-95, 70 ))
#G.add_node("LA", pos=(-35,30))
#G.add_node("Newark", pos=(0, 70))

#CANADA
G.add_node("Toronto", pos=(-10,150))
G.add_node("Montreal", pos=(-25, 135))

#COLOMBIA
G.add_node("Bogota", pos=(-100, -100))
G.add_node("Medellin", pos=(-60,-40))
G.add_node("Cartagena", pos=(60, -70))

#BRASIL
G.add_node("Rio", pos=(5, -100))

#PERU
G.add_node("Lima", pos=(-20, -100 ))

#PANAMA
G.add_node("CPanama", pos=(0, -70 ))


#EUROPA
#Italia
G.add_node("Roma", pos=())
G.add_node("Milán", pos=())
G.add_node("Venecia", pos=())

#Francia
G.add_node("París", pos=())
G.add_node("Montpellier", pos=())
G.add_node("Versalles", pos=())

#España
G.add_node("Madrid", pos=(80, 40))
G.add_node("Barcelona", pos=())
G.add_node("Valencia", pos=())

#Alemania
G.add_node("Berlín", pos=())
G.add_node("Roma", pos=())
G.add_node("Roma", pos=())

#ALEMANIA
G.add_node("Frankfurt", pos=(170, 80))
G.add_node("Munich", pos=(140,70))

#PAISES BAJOS
G.add_node("Amsterdam", pos=(80, 100))

#ITALIA
G.add_node("Roma", pos=(100, -60))
G.add_node("Milan", pos=(80, -30))

#AUSTRALIA
G.add_node("Sidney", pos=(300, -50))

#EMIRATOS ARABES
#G.add_node("Abu Dhabi", pos=(150, 60))

#RUSIA
G.add_node("Sochi", pos=(140, 120))
G.add_node("Moscu", pos=(150, 90))

#CHINA
G.add_node("Beijing", pos=(210, 60))
G.add_node("Xiamen", pos=(230,40))"""


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
