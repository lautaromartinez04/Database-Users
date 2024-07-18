from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

class User(BaseModel):
    email:str
    password:str
class UsuarioBase(BaseModel):
    id: Optional[int] = None
    apellido: str = Field(min_length=2, max_length=20)
    nombre: str = Field(min_length=2, max_length=20)
    correo: EmailStr
    
    avatar: str
    pais: str 
    ciudad: str
    direccion: str
    telefono: str
    role:str
    class Config:
        from_attributes = True 
class Usuarios(UsuarioBase):
    password: str = Field(min_length=8)
    

    

