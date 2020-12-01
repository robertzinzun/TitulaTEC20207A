from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer,String,Column,ForeignKey
from sqlalchemy.orm import relationship
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
    salas=relationship('Sala',backref='edificio')

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


class Alumnos():
    pass
class Docentes():
    pass
class Administrativos():
    pass
