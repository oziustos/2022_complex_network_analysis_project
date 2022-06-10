# -*- coding: utf-8 -*-
"""--------------------YÖNSÜZLER İÇİN----------------------------"""
import networkx as nx
import copy
nodeCutG = nx.barabasi_albert_graph(10,1,seed = 1)

bes = list()
dort = list()
uc = list()
iki = list()
bir = list()

DERECE1 = nx.degree_centrality(nodeCutG)
ARADALIK1 = nx.betweenness_centrality(nodeCutG)
YAKINLIK1 = nx.closeness_centrality(nodeCutG)
OZVEKTOR1 = nx.eigenvector_centrality(nodeCutG)
PR1 = nx.pagerank(nodeCutG)

#G = nx.petersen_graph()
#connectedP = nx.number_connected_components(nodeCutG)
#nx.draw(G, with_labels = True)



#Kaçlı ayırdığına bakıyoruz ve ona göre listelere atıyoruz 
for i in list(nodeCutG.nodes()):
    G3 = copy.deepcopy(nodeCutG)
    G3.remove_node(i)
    connectedT = nx.number_connected_components(G3)
    if connectedT == 5:
        bes.append(i)
    elif connectedT == 4:
        dort.append(i)
    elif connectedT == 3:
        uc.append(i)
    elif connectedT == 2:
        iki.append(i)
    else:
        bir.append(i)


#İstenen aradalık derece yakınlık özvektör ve pagerank değerlerini yazdırıyoruz
print("Beşlilerin derece, aradalık, yakınlık, ozvektör ve pagerank değerleri")
for i in bes:
    print("  ")
    print("----",i,". değerleri","----")
    print(i,". Derecesi: ",DERECE1[i])
    print(i,". Aradalığı", ARADALIK1[i])
    print(i,". Yakınlığı", YAKINLIK1[i])
    print(i,". Özvektörü", OZVEKTOR1[i])
    print(i,". Pageranki", PR1[i])

print("   ")    
print("Dörtlülerin derece, aradalık, yakınlık, ozvektör ve pagerank değerleri")
for i in dort:
    print("  ")
    print("----",i,". değerleri","----")
    print(i,". Derecesi: ",DERECE1[i])
    print(i,". Aradalığı", ARADALIK1[i])
    print(i,". Yakınlığı", YAKINLIK1[i])
    print(i,". Özvektörü", OZVEKTOR1[i])
    print(i,". Pageranki", PR1[i])

print("   ")        
print("Üçlülerin derece, aradalık, yakınlık, ozvektör ve pagerank değerleri")
for i in uc:
    print("  ")
    print("----",i,". değerleri","----")
    print(i,". Derecesi: ",DERECE1[i])
    print(i,". Aradalığı", ARADALIK1[i])
    print(i,". Yakınlığı", YAKINLIK1[i])
    print(i,". Özvektörü", OZVEKTOR1[i])
    print(i,". Pageranki", PR1[i])

print("  ")
print("İkililerin derece, aradalık, yakınlık, ozvektör ve pagerank değerleri")
for i in iki:
    print("  ")
    print("----",i,". değerleri","----")
    print(i,". Derecesi: ",DERECE1[i])
    print(i,". Aradalığı", ARADALIK1[i])
    print(i,". Yakınlığı", YAKINLIK1[i])
    print(i,". Özvektörü", OZVEKTOR1[i])
    print(i,". Pageranki", PR1[i])

print("  ")
print("Birlilerin derece, aradalık, yakınlık, ozvektör ve pagerank değerleri")
for i in bir:
    print("  ")
    print("----",i,". değerleri","----")
    print(i,". Derecesi: ",DERECE1[i])
    print(i,". Aradalığı", ARADALIK1[i])
    print(i,". Yakınlığı", YAKINLIK1[i])
    print(i,". Özvektörü", OZVEKTOR1[i])
    print(i,". Pageranki", PR1[i])






