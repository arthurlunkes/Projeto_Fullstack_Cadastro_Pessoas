from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

# Função para criar conexão no banco
def conectar():
  con = psycopg2.connect(host=os.environ["host"], 
                         database=os.environ["database"],
                         user=os.environ["user"], 
                         password=os.environ["password"])
  return con

# Função para inserir dados no banco
def inserir(sql):
    con = conectar()
    cur = con.cursor()
    try:
        cur.execute(sql)
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        cur.close()
        return 1
    cur.close()

# Função para consultas no banco
def consultar(sql):
  con = conectar()
  cur = con.cursor()
  cur.execute(sql)
  recset = cur.fetchall()
  con.close()
  return recset