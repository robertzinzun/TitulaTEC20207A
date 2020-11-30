from flask import Flask,render_template,request,abort,redirect,url_for
from modelo.models import db
from modelo.models import Edificio
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
#db=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://titulatec_user:hola.123@localhost/Titulatec2020'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#rutas para el ingreso a la aplicacion


@app.route('/')
def inicio():
    #return 'Bienvenido a FLASK'
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

#Fin CRUD


@app.errorhandler(404)
def error_404(e):
    return render_template('comunes/error_404.html'),404

@app.errorhandler(500)
def error_500(e):
    return render_template('comunes/error_500.html'),500

if __name__=='__main__':
    db.init_app(app)
    app.run(debug=True)