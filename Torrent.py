from util import hashFunction

class Torrent:
    """Classe para armazenar caminho do arquivo torrent"""
    def __init__(self, name, path):
        """name utilizado apenas para criar id"""
        self.path = path
        self.name = name
        self.id = self.createID()
        
    def createID(self):
        return hashFunction(self.name)
        
    def getID(self):
        return self.id
        
        
    def __str__(self):
        return f"Torrent Nome: {self.name}; ID: {self.id}"
