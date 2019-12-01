#encoding: utf-8

from Network import Network
from DHT import DHTnode
from Torrent import Torrent

network = Network()

node1 = DHTnode("123.123.123.123","15000")
node2 = DHTnode("121.174.108.126","15010")
node3 = DHTnode("106.182.153.148","16000")
node4 = DHTnode("215.168.142.164","17010")
node5 = DHTnode("101.168.164.200","18000")
node6 = DHTnode("025.003.103.100","19000")
nodes = [node1, node2, node3, node4, node5, node6]

for node in nodes:
    network.addNode(node)
    
node1.join([], network)
node2.join([node1], network)
node3.join([node1, node2], network)
node4.join([node3, node2], network)
node5.join([node3, node1], network)

#popula com torrents de exemplo
torrents = [Torrent(f"arq{i}","./Arquivos/") for i in range(0, 20)]
for tor in torrents:
    node1.store(tor.getID(), tor)

#printa topologia atual
top = node1.getSortedTopology()
for node in top:
    print(f"Nó {node.ip}:")
    for k, _ in node.getContents():
        print(f"--{k}")

#cria nó da aplicação e insere na DHT
myNode = DHTnode("100.110.120.130","10000")
myNode.join([node1], network)

print("Insira algum identificador presente na DHT (impresso no terminal) para encontrar arquivo")
while(True):
    print("Que arquivo deseja localizar?")
    print("Insira 'q' e tecle Enter para sair")
    key = input()
    if key =="q":
        break
    key = int(key)
    value = myNode.retrieve(key)
    if value == None:
        print("Não encontrado")
    else:
        print(f"Encontrado: {value}")
    
    
    
    
    
