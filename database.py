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