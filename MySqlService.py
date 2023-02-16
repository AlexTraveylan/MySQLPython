import mysql.connector as mc
from model import Pokemon
# pip install mysql-connector-pyton

class PokemonService:

    def __init__(self) -> None:
        try: 
            self.conn = mc.connect(host = 'localhost', database = 'pythonmysql', user = 'root', password = 'root')
            self.cursor = self.conn.cursor()
        except mc.Error as err:
            raise ValueError(err)

    def close(self) -> None:
        if(self.conn.is_connected()):
            self.cursor.close()
            self.conn.close()
        else:
            raise ValueError("Aucune connexion ouverte à fermer")

    def getAll(self):
        req = 'SELECT * FROM pokemon'
        try:
            self.cursor.execute(req)  
            bddPokemons = self.cursor.fetchall()

            pokemons: list[Pokemon] = []
            for pokemon in bddPokemons:
                pokemons.append(Pokemon(*pokemon))

        except mc.Error as err:
            raise ValueError(err)

        return pokemons

    def create(self, nom:str, type:str, niveau:int):
        req = 'INSERT INTO pokemon (nom, type, niveau) VALUES (%s,%s,%s)'
        infos = (nom, type, niveau)
        try:
            self.cursor.execute(req, infos)
            self.conn.commit()
        except mc.Error as err:
            raise ValueError(err)
    
    def lvlup(self, pokemon:Pokemon):
        req = "UPDATE pokemon SET niveau = %s WHERE id=%s"
        info = (min(100, pokemon.niveau + 1), pokemon.id)
        print(info)
        try:
            self.cursor.execute(req, info)
            self.conn.commit()
        except mc.Error as err:
            raise ValueError(err)
    
    def delete(self, pokemon:Pokemon):
        req = "DELETE FROM pokemon WHERE id=%s"
        info = [pokemon.id]
        try:
            self.cursor.execute(req, info)
            self.conn.commit()
            return True
        except:
            return False
