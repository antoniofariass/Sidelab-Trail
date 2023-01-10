from infra.configs.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Filmes(Base):
    __tablename__ = "filmes"

    titulo = Column(String,primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    atores = relationship("Atores", backref="filme",lazy="subquery")
    
    def __repr__(self) -> str:
        return f"Filme: ({self.titulo}, ano={self.ano})"
    