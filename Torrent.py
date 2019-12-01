class Torrent:
    """Classe para armazenar caminho do arquivo torrent"""
    def __init__(self, name, path):
        """name utilizado apenas para criar id"""
        self.id = self.createID()
        self.path = path
        
    def createID(self):
        return hash(name)
        
    def getID(self):
        return self.id
