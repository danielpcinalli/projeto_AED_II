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

#tor1 = Torrent("tor1","path")
d = {}
alp = "qwertyuiopasdfghjklzxcvbnm"
nums = [x*1000+4000 for x in range(0,5)]

for k, v in zip(nums, alp):
    node1.store(k, v)



top = node1.getSortedTopology()
for node in top:
    print(f"Nó {node.id}:")
    for k, _ in node.getContents():
        print(f"--{k}")

node3.leave()    
print("---------------")
top = node1.getSortedTopology()
for node in top:
    print(f"Nó {node.id}:")
    for k, _ in node.getContents():
        print(f"--{k}")
        
node3.join([node1, node2], network)
print("---------------")
top = node1.getSortedTopology()
for node in top:
    print(f"Nó {node.id}:")
    for k, _ in node.getContents():
        print(f"--{k}")
