""" 
Example of how to create a engine with sqlalchemy. 

dialect+driver://username:password@host:port/database
                            
"""

from sqlalchemy import create_engine



engine = create_engine("mysql+pymysql://root:terceiro13@localhost:3306/cinema")
conn = engine.connect()
response = conn.execute("SELECT * FROM filmes")

for row in response:
    print(row)
    print(row.keys())