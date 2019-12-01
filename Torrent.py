from util import hashFunction

class Torrent:
    """Classe para armazenar caminho do arquivo torrent"""
    def __init__(self, name, path, ips):
        """name utilizado apenas para criar id"""
        self.path = path
        self.name = name
        self.id = self.createID()
        self.ips = ips
        
    def createID(self):
        return hashFunction(self.name)
        
    def getID(self):
        return self.id
        
        
    def __str__(self):
        s = f"Torrent Nome: {self.name}; ID: {self.id}\nIPS:\n"
        
        for ip in self.ips:
            s = f"{s}--{ip}\n"
        return s
