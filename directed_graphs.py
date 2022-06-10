# -*- coding: utf-8 -*-

"""--------------------YÖNLÜLER İÇİN----------------------------"""
import networkx as nx
import copy
G = nx.barabasi_albert_graph(10,1,seed = 1)
nodeCutG = G.to_directed()

#nx.draw(nodeCutG, with_labels = True)


bes = list()
dort = list()
uc = list()
iki = list()
bir = list()

inder = nx.in_degree_centrality(nodeCutG)
outder = nx.out_degree_centrality(nodeCutG)
ARADALIK1 = nx.betweenness_centrality(nodeCutG)
YAKINLIK1 = nx.closeness_centrality(nodeCutG)
OZVEKTOR1 = nx.eigenvector_centrality(nodeCutG)
PR1 = nx.pagerank(nodeCutG)


#Kaçlı ayırdığına bakıyoruz ve ona göre listelere atıyoruz 
for i in list(nodeCutG.nodes()):
    G3 = copy.deepcopy(nodeCutG)
    G3.remove_node(i)
    connectedT = nx.number_weakly_connected_components(G3)
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
    print(i,". Giriş Derecesi: ",inder[i])
    print(i,". Çıkış Derecesi: ",outder[i])
    print(i,". Aradalığı", ARADALIK1[i])
    print(i,". Yakınlığı", YAKINLIK1[i])
    print(i,". Özvektörü", OZVEKTOR1[i])
    print(i,". Pageranki", PR1[i])

print("   ")    
print("Dörtlülerin derece, aradalık, yakınlık, ozvektör ve pagerank değerleri")
for i in dort:
    print("  ")
    print("----",i,". değerleri","----")
    print(i,". Giriş Derecesi: ",inder[i])
    print(i,". Çıkış Derecesi: ",outder[i])
    print(i,". Aradalığı", ARADALIK1[i])
    print(i,". Yakınlığı", YAKINLIK1[i])
    print(i,". Özvektörü", OZVEKTOR1[i])
    print(i,". Pageranki", PR1[i])

print("   ")        
print("Üçlülerin derece, aradalık, yakınlık, ozvektör ve pagerank değerleri")
for i in uc:
    print("  ")
    print("----",i,". değerleri","----")
    print(i,". Giriş Derecesi: ",inder[i])
    print(i,". Çıkış Derecesi: ",outder[i])
    print(i,". Aradalığı", ARADALIK1[i])
    print(i,". Yakınlığı", YAKINLIK1[i])
    print(i,". Özvektörü", OZVEKTOR1[i])
    print(i,". Pageranki", PR1[i])

print("  ")
print("İkililerin derece, aradalık, yakınlık, ozvektör ve pagerank değerleri")
for i in iki:
    print("  ")
    print("----",i,". değerleri","----")
    print(i,". Giriş Derecesi: ",inder[i])
    print(i,". Çıkış Derecesi: ",outder[i])
    print(i,". Aradalığı", ARADALIK1[i])
    print(i,". Yakınlığı", YAKINLIK1[i])
    print(i,". Özvektörü", OZVEKTOR1[i])
    print(i,". Pageranki", PR1[i])

print("  ")
print("Birlilerin derece, aradalık, yakınlık, ozvektör ve pagerank değerleri")
for i in bir:
    print("  ")
    print("----",i,". değerleri","----")
    print(i,". Giriş Derecesi: ",inder[i])
    print(i,". Çıkış Derecesi: ",outder[i])
    print(i,". Aradalığı", ARADALIK1[i])
    print(i,". Yakınlığı", YAKINLIK1[i])
    print(i,". Özvektörü", OZVEKTOR1[i])
    print(i,". Pageranki", PR1[i])

