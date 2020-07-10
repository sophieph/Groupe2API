import sqlite3

class Database:
    def __init__(self):
        self.connection = None

    # Creation 
    def get_connection(self):
        if self.connection is None:
            try:
                self.connection = sqlite3.connect('./db/pokemon.db')
            except sqlite3.Error as error:
                print("Error while creating a sqlite table", error)
        return self.connection

    def deconnection(self):
        if self.connection is not None:
            self.connection.close()

    def insert_user(self, username, email, password):
        cursor = self.get_connection().cursor()
        cursor.execute(("INSERT INTO user (username, email"
                       ",password) VALUES (?, ?, ?)"),
                       (username, email, password))
        self.get_connection().commit()

    def get_user(self, username):
        cursor = self.get_connection().cursor()
        cursor.execute(("SELECT username "
                        "FROM user WHERE username = ?"), (username,))
        id_username = cursor.fetchone()

        if id_username is None:
            return None
        else:
            return id_username[0]
    

    def get_user_id(self, username):
        cursor = self.get_connection().cursor()
        cursor.execute(("SELECT id "
                        "FROM user WHERE username = ?"), (username,))
        id_username = cursor.fetchone()

        if id_username is None:
            return None
        else:
            return id_username[0]

    def insert_favorites(self, pokemon, user_id):
        cursor = self.get_connection().cursor()
        cursor.execute(("INSERT INTO favourite (pokemon"
                       ",user_id) VALUES (?, ?)"),
                       (pokemon, user_id))
        self.get_connection().commit()

    def get_pokemon(self, pokemon):
        cursor = self.get_connection().cursor()
        cursor.execute(("SELECT pokemon "
                        "FROM favourite WHERE pokemon = ?"), (pokemon,))
        id_pokemon = cursor.fetchone()

        if id_pokemon is None:
            return None
        else:
            return id_pokemon[0]

    def get_all_pokemon(self, user_id):
        cursor = self.get_connection().cursor()
        cursor.execute(("SELECT pokemon "
                        "FROM favourite WHERE user_id = ?"), (user_id,))
        pokemon_list = cursor.fetchall()
        len_pokemon_list = len(pokemon_list)
        if len_pokemon_list == 0:
            return None
        else:
            return [pokemon[0] for pokemon in pokemon_list]