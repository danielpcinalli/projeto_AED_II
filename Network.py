class Network:

    def __init__(self):
        self.nodeList = []
    
    def addNode(self, node):
        if node not in self.nodeList:
            self.nodeList.append(node)
    
    def try_connect(self, node):
        if node not in self.nodeList:
            raise Exception()
