from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


#Configuração
engine = create_engine("mysql+pymysql://root:terceiro13@localhost:3306/cinema")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

#Entidades 
class Filmes(Base):
    __tablename__ = "filmes"

    titulo = Column(String,primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Filme: ({self.titulo}, ano={self.ano})"
    
# SQL

# Insert
data_insert = Filmes(titulo="O Poderoso Chefão", genero="Drama", ano=1972)
session.add(data_insert)
session.commit()

# Delete
session.query(Filmes).filter(Filmes.titulo == "O Poderoso Chefão").delete()
session.commit()

#update
session.query(Filmes).filter(Filmes.titulo == "O Poderoso Chefão").update({"ano": 1973})
session.commit()

# Select 
data = session.query(Filmes).all()
print(data)
print(data[0].titulo)



