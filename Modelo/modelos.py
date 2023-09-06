from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Usuario(Base):
    __tablename__="Usuarios"

    id = Column(Integer(), primary_key=True)
    nombre_usuario = Column(String(50), nullable=False, unique=True)
    contrasena = Column(String(50), nullable=False)
    sesion_iniciada = Column(Boolean(), nullable=False)
    #contextos = relationship("Contexto", backref="Usuarios")

class Contexto(Base):
    __tablename__ = "Contextos"

    id = Column(Integer(), primary_key=True)
    nombre_contexto = Column(String(100), nullable=False, unique=False)
    #tipo = Column(String(50), nullable=False, unique=True)
    contenido = Column(String(550), nullable=False, unique=False)
    usuario_contextos = relationship("Usuario", backref="Contextos")
    usuario_id = Column(Integer, ForeignKey('Usuarios.id'))  
