#encoding: utf-8
from Torrent import Torrent


"""
A DHT substitui o servidor (tracker) que mantém informações 
sobre quais peers possuem o torrent selecionado
"""    

class DHTnode:


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
        return hash(f"{ip}{port}")

    def initializeDHT(self, node):
        """Para no caso de uma DHT vazia, inicia com o nó node"""
        node.setNext = node
        node.setPrevious = node

    def findResponsibleNode(self, key):
        """Nó responsável é o primeiro nó com índice maior que a chave"""
        pass
        
    def isNodeResponsibleForKey(self, key):
        pass
    
    def getTopology(self):
        firstNode = self
        currentNode = firstNode.getNext()
        nodeList = [firstNode]
        while (currentNode != firstNode):
            nodeList.append(currentNode)
            currentNode = currentNode.getNext()
        return nodeList
    
    def join(self, newNode, knownNodes):
        """Recebe nó que deseja se conectar e uma lista de nós conhecidos"""
        for node in knownNodes:
            #tenta se conectar um a um, caso consiga se insere após o nó encontrado
            return
        #caso nenhum nó exista, cria nova DHT
        self.initializeDHT(newNode)
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
    
    def insertAfter(self, newNode, node):
        """Insere newNode após node e atualiza info dos nós"""
        originalNext = node.getNext()
        originalPrevious = node
        
        node.setNext(newNode)
        originalNext.setPrevious(newNode)
        
        newNode.setPrevious(node)
        newNode.setNext(originalNext)
        
        
        
        
        

    
    
