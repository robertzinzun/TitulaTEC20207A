from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer,String,Column,ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

db=SQLAlchemy()

class Edificio(db.Model):
    __tablename__='Edificios'
    idEdificio=Column(Integer,primary_key=True)
    nombre=Column(String,unique=True)
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        edificio=self.consultaIndividual()
        db.session.delete(edificio)
        db.session.commit()
    def consultaGeneral(self):
        return self.query.all()
    def consultaIndividual(self):
        return self.query.get(self.idEdificio)
    salas=relationship('Sala',backref='edificio',lazy='dynamic')

class Sala(db.Model):
    __tablename__='Salas'
    idSala=Column(Integer,primary_key=True)
    nombre=Column(String,unique=True)
    idEdificio=Column(Integer,ForeignKey('Edificios.idEdificio'))

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        sala = self.consultaIndividual()
        db.session.delete(sala)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self):
        return self.query.get(self.idSala)

class Usuario(UserMixin,db.Model):
    __tablename__='Usuarios'
    idUsuario=Column(Integer,primary_key=True)
    nombre=Column(String,nullable=False)
    sexo=Column(String,nullable=False)
    telefono=Column(String,nullable=False)
    email = Column(String, nullable=False)
    password_hash = Column(String(128), nullable=False)
    tipo = Column(String, nullable=False)
    estatus = Column(String, nullable=False)
    #Métodos para el cifrado de la contraseña
    @property
    def password(self):
        raise AttributeError('El atributo password no es un atributo de lectura')
    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)
    def validarPassword(self,password):
        return check_password_hash(self.password_hash,password)
    #metodos del CRUD
    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self.consultaIndividual())
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self):
        return self.query.get(self.idUsuario)
    #Metodos para el perfilamiento de los usuarios
    def is_authenticated(self):
        return True
    def is_anonymous(self):
        return False
    def is_active(self):
        if self.estatus=='A':
            return True
        else:
            return False
    def is_admin(self):
        if self.tipo=='A':
            return True
        else:
            return False
    def getTipo(self):
        return self.tipo
    def get_id(self):
        return self.idUsuario

class Alumnos():
    pass
class Docentes():
    pass
class Administrativos():
    pass
