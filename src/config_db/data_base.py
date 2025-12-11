from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import os

db = SQLAlchemy()

def init_db(app):
    host='localhost',
    user='root',
    password='root',
    database='twosc'
    mysql.connector.connet()
        
    
        