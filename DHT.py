#encoding: utf-8
from Torrent import Torrent


"""
A DHT substitui o servidor (tracker) que mantém informações 
sobre quais peers possuem o torrent selecionado
"""    



def main():
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
    
    top = node1.getTopology()
    for node in top:
        print(node)

class Network:

    def __init__(self):
        self.nodeList = []
    
    def addNode(self, node):
        if node not in self.nodeList:
            self.nodeList.append(node)
    
    def try_connect(self, node):
        if node not in self.nodeList:
            raise Exception()
            

class DHTnode(object):


    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.previousNode = None
        self.nextNode = None
        self.id = self.createID()
        self.torrents = set()

    def getPrevious(self):
        return self.previousNode

    def getNext(self):
        return self.nextNode

    def setPrevious(self, node):
        self.previousNode = node

    def setNext(self, node):
        self.nextNode = node

    def createID(self):
        return hash(f"{self.ip}{self.port}")

    def initializeDHT(self):
        """Para no caso de uma DHT vazia, inicia com o nó node"""
        self.setNext(self)
        self.setPrevious(self)

    def findResponsibleNode(self, key):
        """Nó responsável é o primeiro nó com índice maior que a chave"""
        pass
        
    def isNodeResponsibleForKey(self, key):
        pass
    
    def getTopology(self):
        firstNode = self
        nodeList = [firstNode]
        if firstNode.getNext() == None:
            return [None]
        currentNode = firstNode.getNext()
        while (currentNode != firstNode):
            nodeList.append(currentNode)
            currentNode = currentNode.getNext()
        return nodeList
    
    def getFirstNode(self):
        currentNode, currentId = self, self.id
        nextNode = currentNode.getNext()
        while (currentId < nextNode.id):
            currentNode, currentId = nextNode, nextNode.id
            nextNode = currentNode.getNext()
        return nextNode
            
    
    def join(self, knownNodes, network):
        """Recebe nó que deseja se conectar e uma lista de nós conhecidos"""
        newNode = self
        for node in knownNodes:
            #tenta se conectar um a um, caso consiga se insere após o nó encontrado
            try:
                network.try_connect(node)
            except Exception as e:
                print(str(e))
                continue
            currentNode = node.getFirstNode()
            #caso onde há apenas um nó na DHT
            if currentNode.id == currentNode.getNext().id:
                newNode.insertAfter(currentNode)
                return
            #caso on id do nó a ser inserido é menor que o menor id presente na DHT
            if currentNode.id >= newNode.id:
                newNode.insertAfter(currentNode.getPrevious())
                return
            #caso on id do nó a ser inserido é maior que o maior id presente na DHT
            if currentNode.getPrevious().id < newNode.id:
                newNode.insertAfter(currentNode.getPrevious())
                return
            #caso geral
            while currentNode.id < newNode.id:
                currentNode = currentNode.getNext()
            newNode.insertAfter(currentNode.getPrevious())
            return
        #caso nenhum nó exista, cria nova DHT
        self.initializeDHT()
        #falta passar info
        
        
    def leave():
        prevNode = self.getPrevious()
        nextNode = self.getNext()
        
        nextNode.setPrevious(prevNode)
        prevNode.setnext(nextNode)
        #falta passar info
        
    def store(self, key, value):
        index = self.findResponsibleNode(key)

    def retrieve(self, key):
        pass        
    
    def insertAfter(self, node):
        """Insere newNode após node e atualiza info dos nós"""
        newNode = self
        originalNext = node.getNext()
        originalPrevious = node
        
        node.setNext(newNode)
        originalNext.setPrevious(newNode)
        
        newNode.setPrevious(node)
        newNode.setNext(originalNext)
        
    def __str__(self):
        return f"Node at ip {self.ip} port {self.port} id {self.id}"
        
if __name__ == "__main__":
    main()
        

    
    
