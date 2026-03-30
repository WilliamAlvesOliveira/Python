import mysql.connector
from mysql.connector import Error
import customtkinter as ctk

def testar_conexao():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Dispensa"
        )
        if db.is_connected():
            print("Conexão com o banco de dados foi bem-sucedida!")
        db.close()
    except mysql.connector.Error as err:
        print(f"Erro: {err}")

if __name__ == "__main__":
    testar_conexao()
