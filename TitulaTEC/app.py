from flask import Flask,render_template,request,abort,redirect,url_for
from flask_login import LoginManager,current_user

from modelo.models import db
from modelo.models import Edificio,Sala, Usuario
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
#db=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://titulatec_user:hola.123@localhost/Titulatec2020'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#Configuración de la gestion Usuarios con Flask-Login
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view="inicio"
#rutas para el ingreso a la aplicacion

@login_manager.user_loader
def load_user(id):
    return Usuario.query.get(int(id))
@app.route('/')
def inicio():
    #return 'Bienvenido a FLASK'
    if current_user.is_athenticated:
        return render_template('principal.html')
    else:
        return render_template('index.html')

@app.route('/login')
def login():
    #return 'Procesando las credenciales.'
    usuario='Roberto Suarez Zinzun'
    return render_template('principal.html',usuario=usuario)

#fin de las rutas del acceso al sistema
@app.route('/registrarUsuario')
def registrarUsuario():
    return 'Registrando un usuario'

@app.route('/registrarProducto')
def regsitrarProducto():
    return 'registrando un producto'

@app.route('/cerrarSesion')
def cerrarSesion():
    return '<h1>Cerrando la Sesion, bye</h1><table border="1"><th>id</th></table>'

@app.route('/eliminarDocente/<int:idDocente>')
def eliminarDocente(idDocente):
    return 'Eliminando al Docente:'+str(idDocente)
@app.route('/consultarDocente/<id>')
def consultarDocente(id):
    return 'consultando los datos del docente:'+id
#Inicio del CRUD de alumnos
@app.route('/alumnos/new')
def nuevoAlumno():
    return render_template('Alumnos/altaAlumno.html')

@app.route('/alumnos/save',methods=['POST'])
def guardar_alumno():
    try:
        nombre=request.form['nombre']
    except:
        abort(500)
    return nombre
@app.route('/alumnos/edit')
def editarAlumno():
    return render_template('Alumnos/editarAlumno.html')

@app.route('/alumnos/delete')
def eliminarAlumno():
    return render_template('Alumnos/eliminarAlumno.html')

@app.route('/alumnos')
def consultarAlumnos():
    return render_template('Alumnos/ConsultaAlumnos.html')
#fin del CRUD alumnos

#CRUD Edificios
@app.route('/edificios/new')
def nuevoEdificio():
    return render_template('Edificios/altaEdificio.html')
@app.route('/edificios/save',methods=['POST'])
def agregarEdificio():
    try:
        e=Edificio()
        e.nombre=request.form['nombre']
        e.insertar()
        #return ''
        return redirect(url_for('consultarEdificios'))
    except:
        abort(500)
@app.route('/edificios')
def consultarEdificios():
    e=Edificio()
    edificios=e.consultaGeneral()
    return render_template('Edificios/consultaEdificios.html',edificios=edificios)

@app.route('/edificios/edit/<int:id>')
def editarEdificio(id):
    e = Edificio()
    e.idEdificio=id
    edificio=e.consultaIndividual()
    return render_template('Edificios/editarEdificio.html',edificio=edificio)
@app.route('/edificios/modificar',methods=['POST'])
def modificarEdificios():
    e=Edificio()
    e.idEdificio=request.form['id']
    e.nombre=request.form['nombre']
    e.actualizar()
    return redirect(url_for("consultarEdificios"))
@app.route('/edificios/delete/<int:id>')
def eliminarEdificio(id):
    e=Edificio()
    e.idEdificio=id
    e.eliminar()
    return redirect(url_for("consultarEdificios"))
#Fin CRUD
#crud de Salas
@app.route('/salas')
def consultarSalas():
    s=Sala()
    salas=s.consultaGeneral()
    return render_template('Salas/ConsultaSalas.html',salas=salas)
@app.route('/salas/new')
def nuevaSala():
    e = Edificio()
    return render_template('Salas/altaSalas.html',edificios=e.consultaGeneral())
@app.route('/salas/save',methods=['POST'])
def guardarSala():
    s=Sala()
    s.nombre=request.form['nombre']
    s.idEdificio=request.form['idEdificio']
    s.insertar()
    return redirect(url_for('consultarSalas'))
#fin crud salas
@app.errorhandler(404)
def error_404(e):
    return render_template('comunes/error_404.html'),404

@app.errorhandler(500)
def error_500(e):
    return render_template('comunes/error_500.html'),500

if __name__=='__main__':
    db.init_app(app)
    app.run(debug=True)