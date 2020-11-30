from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer,String,Column
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
        db.session.delete(self)
        db.session.commit()
    def consultaGeneral(self):
        return self.query.all()
    def consultaIndividual(self):
        return self.query.get(self.idEdificio)

class Alumnos():
    pass
class Docentes():
    pass
class Administrativos():
    pass
