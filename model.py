

class Pokemon:

    def __init__(self, id:int, nom:str, type:str, niveau:int) -> None:
        self.id:int = id
        self.nom:str = nom
        self.type:str = type
        self.niveau:int = niveau
    
    def __str__(self) -> str:
        return f"N°{self.id} : {self.nom} (type {self.type}) Niveau {self.niveau}"
    
    

    