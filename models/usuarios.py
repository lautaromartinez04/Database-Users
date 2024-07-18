from config.database import Base
from sqlalchemy import Column, Integer, String, Float, Text

class Usuarios(Base):

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key = True)
    apellido = Column(String(20))
    nombre= Column(String(20))
    correo= Column(String(100))
    password=Column(String(1000))
    avatar=Column(Text)
    pais= Column(String(50)) 
    ciudad= Column(String(50))  
    direccion= Column(String(50)) 
    telefono= Column(String(20)) 
    role= Column(String(50)) 

   