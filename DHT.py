#encoding: utf-8
from Torrent import Torrent

"""
A DHT substitui o servidor (tracker) que mantém informações 
sobre quais peers possuem o torrent selecionado
"""    

class DHTnode(object):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.previousNode = None
        self.nextNode = None
        self.id = self.createID()
        self.dict = {}
                  
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
            nodeBeforeNewNode = newNode.findNodeToInsert(node, newNode.id)
            newNode.insertAfter(nodeBeforeNewNode)
            self.updateResponsabilitiesAfterNewNode(newNode)
            return
        #caso nenhum nó exista, cria nova DHT
        self.initializeDHT()
        
    def leave(self):
        prevNode = self.getPrevious()
        nextNode = self.getNext()
        
        nextNode.setPrevious(prevNode)
        prevNode.setNext(nextNode)
        
        #responsabilidade das chaves irá para o próximo nó
        for k, v in self.dict.items():
            nextNode._storeAtThisNode(k, v)
        self.dict.clear()
        
    def store(self, key, value):
        """Encontra nó responsável por key e armazena key-valor"""
        node = self.findResponsibleNode(key)
        node._storeAtThisNode(key, value)

    def getPrevious(self):
        return self.previousNode

    def getNext(self):
        return self.nextNode

    def setPrevious(self, node):
        self.previousNode = node

    def setNext(self, node):
        self.nextNode = node

    def createID(self):
        ID = hash(f"{self.ip}{self.port}")
        ID = abs(ID)//1000000000000000
        return ID

    def initializeDHT(self):
        """Para no caso de uma DHT vazia, inicia com o nó node"""
        self.setNext(self)
        self.setPrevious(self)

    def findResponsibleNode(self, key):
        """Nó responsável é o primeiro nó com índice maior que a chave"""
        return self.findNodeToInsert(self, key).getNext()
    def _storeAtThisNode(self, key, value):
        self.dict.update({key: value})

    def retrieve(self, key):
        node = self.findResponsibleNode(key)
        if key not in self.dict.keys():
            return None
        return self.dict.get(key)
    
    def insertAfter(self, node):
        """Insere newNode após node e atualiza info dos nós"""
        newNode = self
        originalNext = node.getNext()
        originalPrevious = node
        
        node.setNext(newNode)
        originalNext.setPrevious(newNode)
        
        newNode.setPrevious(node)
        newNode.setNext(originalNext)
        
    def getContents(self):
        """Retorna pares key-value armazenados no nó"""
        return self.dict.items()
    
    def updateResponsabilitiesAfterNewNode(self, newNode):
        nodeBeforeNewNode = newNode.getPrevious()
        keysToKeep = [(k, v) for k, v in nodeBeforeNewNode.getContents() if k <= newNode.id]
        keysToTransfer = [(k, v) for k, v in nodeBeforeNewNode.getContents() if k > newNode.id]
        for k, v in keysToTransfer:
            newNode._storeAtThisNode(k, v)
        nodeBeforeNewNode.dict.clear()
        nodeBeforeNewNode.dict.update(keysToKeep)
        
        nodeAfterNewNode = newNode.getNext()
        keysToKeep = [(k, v) for k, v in nodeAfterNewNode.getContents() if k > newNode.id]
        keysToTransfer = [(k, v) for k, v in nodeAfterNewNode.getContents() if k <= newNode.id]
        for k, v in keysToTransfer:
            newNode._storeAtThisNode(k, v)
        nodeAfterNewNode.dict.clear()
        nodeAfterNewNode.dict.update(keysToKeep)
    
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
    
    def getSortedTopology(self):
        return self.getFirstNode().getTopology()
    
    def getFirstNode(self):
        currentNode, currentId = self, self.id
        nextNode = currentNode.getNext()
        while (currentId < nextNode.id):
            currentNode, currentId = nextNode, nextNode.id
            nextNode = currentNode.getNext()
        return nextNode

    def findNodeToInsert(self, node, ID):
        """Retorna o nó onde será inserido o novo nó"""
        currentNode = node.getFirstNode()
        #caso onde há apenas um nó na DHT
        if currentNode == currentNode.getNext():
            return currentNode
   
        #caso onde novo nó deve ser inserido antes do nó de menor id
        elif currentNode.id >= ID or currentNode.getPrevious().id <= ID:
            currentNode = currentNode.getPrevious()
            return currentNode
        else:
            #caso geral
            while currentNode.id <= ID:
                currentNode = currentNode.getNext()
        #caso de colisão
        correctNode =  currentNode.getPrevious()
        while correctNode.id == correctNode.getNext().id:
            correctNode = correctNode.getNext()
        return correctNode
        
    def __str__(self):
        return f"Node at ip {self.ip} port {self.port} id {self.id}"

        

    
    
