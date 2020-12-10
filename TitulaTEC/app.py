from flask import Flask,render_template,request,abort,redirect,url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required

from modelo.models import db, Opcion
from modelo.models import Edificio,Sala, Usuario
import json
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.secret_key='TitulaT3c'
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
    if current_user.is_authenticated:
        return render_template('principal.html')
    else:
        return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    #return 'Procesando las credenciales.'
    u=Usuario()
    usuario=u.validar(request.form['email'],request.form['password'])
    if usuario!=None:
        login_user(usuario)
        return render_template('principal.html')
    else:
        return 'Usuario invalido'

@app.route('/cerrarSesion')
@login_required
def cerrarSesion():
    if current_user.is_authenticated:
        logout_user()
    else:
        abort(404)
    return redirect(url_for("inicio"))
#fin de las rutas del acceso al sistema
@app.route('/registrarUsuario')
def registrarUsuario():
    return render_template('Usuarios/altaUsuario.html')
@app.route('/guardarUsuario',methods=['post'])
def guardarUsuario():
    usuario=Usuario()
    usuario.nombre=request.form['nombre']
    usuario.telefono = request.form['telefono']
    usuario.email = request.form['email']
    usuario.tipo = request.form['tipo']
    usuario.estatus = request.form['estatus']
    usuario.sexo = request.form['sexo']
    usuario.password=request.form['password']
    usuario.insertar()
    return render_template('index.html')
@app.route('/registrarProducto')
def regsitrarProducto():
    return 'registrando un producto'

@app.route('/eliminarDocente/<int:idDocente>')
@login_required
def eliminarDocente(idDocente):
    return 'Eliminando al Docente:'+str(idDocente)
@app.route('/consultarDocente/<id>')
@login_required
def consultarDocente(id):
    return 'consultando los datos del docente:'+id
#Inicio del CRUD de alumnos
@app.route('/alumnos/new')
@login_required
def nuevoAlumno():
    return render_template('Alumnos/altaAlumno.html')

@app.route('/alumnos/save',methods=['POST'])
@login_required
def guardar_alumno():
    try:
        nombre=request.form['nombre']
    except:
        abort(500)
    return nombre
@app.route('/alumnos/edit')
@login_required
def editarAlumno():
    return render_template('Alumnos/editarAlumno.html')

@app.route('/alumnos/delete')
@login_required
def eliminarAlumno():
    return render_template('Alumnos/eliminarAlumno.html')

@app.route('/alumnos')
def consultarAlumnos():
    return render_template('Alumnos/ConsultaAlumnos.html')
#fin del CRUD alumnos

#CRUD Edificios
@app.route('/edificios/new')
@login_required
def nuevoEdificio():

    return render_template('Edificios/altaEdificio.html')

@app.route('/edificios/save',methods=['POST'])
@login_required
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
@login_required
def editarEdificio(id):
    e = Edificio()
    e.idEdificio=id
    edificio=e.consultaIndividual()
    return render_template('Edificios/editarEdificio.html',edificio=edificio)
@app.route('/edificios/modificar',methods=['POST'])
@login_required
def modificarEdificios():
    e=Edificio()
    e.idEdificio=request.form['id']
    e.nombre=request.form['nombre']
    e.actualizar()
    return redirect(url_for("consultarEdificios"))
@app.route('/edificios/delete/<int:id>')
@login_required
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
@login_required
def nuevaSala():
    e = Edificio()
    return render_template('Salas/altaSalas.html',edificios=e.consultaGeneral())
@app.route('/salas/save',methods=['POST'])
@login_required
def guardarSala():
    s=Sala()
    s.nombre=request.form['nombre']
    s.idEdificio=request.form['idEdificio']
    s.insertar()
    return redirect(url_for('consultarSalas'))
#fin crud salas

#CRUD Opciones (Ajax)
@app.route("/opciones")
def opciones():
    return render_template('Opciones/opciones.html')

@app.route('/opciones/consultaGeneral')
def consultarOpciones():
    opcion=Opcion()
    lista=[]
    for o in opcion.consultaGeneral():
        lista.append({"idOpcion":o.idOpcion,"nombre":o.nombre,"descripcion":o.descripcion})
    return json.dumps(lista)
@app.route('/opciones/guardar/<data>',methods=['get'])
def guaradarOpcion(data):
    opcion=Opcion()
    datos=json.loads(data)
    opcion.nombre=datos['nombre']
    opcion.descripcion=datos['descripcion']
    opcion.insertar()
    return 'Opcion agregada con exito'
@app.route('/opciones/<int:id>')
def consultarOpcion(id):
    opcion=Opcion()
    opcion.idOpcion=id
    opcion=opcion.consultaIndividual()
    dicOpcion={"idOpcion":opcion.idOpcion,"nombre":opcion.nombre,"descripcion":opcion.descripcion}
    return json.dumps(dicOpcion)
@app.route('/opciones/modificar/<data>',methods=['get'])
def modifcarOpcion(data):
    opcion = Opcion()
    datos = json.loads(data)
    opcion.idOpcion=datos['idOpcion']
    opcion.nombre = datos['nombre']
    opcion.descripcion = datos['descripcion']
    opcion.actualizar()
    return 'Opcion modificada con exito'
@app.route('/opciones/delete/<int:id>')
def eliminarOpcion(id):
    opcion = Opcion()
    opcion.idOpcion=id
    opcion.eliminar()
    return 'Opcion eliminada con exito'


@app.errorhandler(404)
def error_404(e):
    return render_template('comunes/error_404.html'),404

@app.errorhandler(500)
def error_500(e):
    return render_template('comunes/error_500.html'),500

if __name__=='__main__':
    db.init_app(app)
    app.run(debug=True)