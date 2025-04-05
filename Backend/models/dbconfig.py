import psycopg2,psycopg2.extras
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL=os.getenv("DB_URL")

def db_connection():
    try:
        conn=psycopg2.connect(DB_URL)
        cur=conn.cursor()
        return conn,cur
    except Exception as e:
        print(f"Error: {e}")
        return None,None