#Importación de los elementos necesarios del framework y de MySQL
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#Inicialización del APP/servidor
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'#BD conecta al host
app.config['MYSQL_USER']='root'#El usuario es root
app.config['MYSQL_PASSWORD']=''#No definimos contraseña
app.config['MYSQL_DB']='DB_Floreria'#BD de la fruteria
app.secret_key = "clave_secreta"#Token para validación por cuestiones de seguridad al mandar datos entre la BD y la página web
mysql = MySQL(app)

#Declaración de las ruta http://localhost:5000
#Hacer que el servidor trabaje en el puerto especifícado: 5000 para este caso
#Ejecución del servidor en el puerto 5000
@app.route('/')#Ruta raíz/principal o index
def index():
    CC = mysql.connection.cursor();#Cursor para hacer conexión a mysql
    CC.execute('select * from tbFlores')#Seleccionamos todos los datos de la tabla
    consultaDatos = CC.fetchall()#Consultar datos de toda la tabla
    print(consultaDatos)
    return render_template('index.html')


#Ruta http:localhost:5000/guardar - tipo POST para Insert
@app.route('/guardar', methods = ['POST'])
def guardar():
    if request.method == 'POST':
        #Pasamos a variables el contenido de los inputs
        VNombre = request.form['txtNombre']
        VCantidad = request.form['txtCantidad']        
        Vprecio = request.form['txtPrecio']        
        #Conectar y ejecutar el insert
        #El objeto tipo cursor llamado CS
        CS = mysql.connection.cursor()   #(%s, %s, %s) --> Datos indefinidos que se pasan al siguiente parámetro de execute
        CS.execute('insert into tbFlores(Nombre, Cantidad, Precio) values(%s, %s, %s)', (VNombre, VCantidad, Vprecio))
        mysql.connection.commit()            
    flash('Los datos se agregaron correctamente')    
    return redirect(url_for('index'))#Redireccionamos al index

@app.route('/editar/<id>')
def editar(id):
    cursoId = mysql.connection.cursor()
    cursoId.execute('select * from tbFlores where id=%s', (id,))
    consultId = cursoId.fetchone()
    return render_template('editar.html', flor = consultId)

@app.route('/actualizar/<id>', methods = ['POST'])
def actualizar(id):
    if request.method == 'POST':
        #Pasamos a variables el contenido de los inputs
        Vnombre = request.form['txtNombre']
        Vcantidad = request.form['txtCantidad']        
        Vprecio = request.form['txtPrecio']        
        #Conectar y ejecutar el insert
        #El objeto tipo cursor llamado CS
        curAct = mysql.connection.cursor()
        curAct.execute('update tbFlores set Nombre = %s, Cantidad = %s, Precio = %s where id = %s',(Vnombre, Vcantidad, Vprecio, id))
        mysql.connection.commit()
    flash('Se actualizo el registro')
    return redirect(url_for('index'))

@app.route('/eliminar/<id>')####
def eliminar(id):####
    cursoId = mysql.connection.cursor()
    cursoId.execute('select * from tbFlores where id=%s', (id,))
    consultId = cursoId.fetchone()
    return render_template('eliminarFlor.html', flor = consultId)

@app.route('/borrar/<id>', methods = ['POST'])
def borrar(id):
    if request.method == 'POST':
        curAct = mysql.connection.cursor()
        curAct.execute('delete from tbFlores where id = %s', (id,))
        mysql.connection.commit()
    flash('Se elimino la flor')
    return redirect(url_for('index'))

@app.route('/buscar')
def buscar():
    return render_template('Busqueda.html')

@app.route('/mostrar', methods = ['POST'])
def mostrar():
    if request.method == 'POST':        
        Vflor = request.form['txtFlor']
        CC = mysql.connection.cursor()
        CC.execute('select * from tbFlores where Nombre=%s', (Vflor,))        
        consultaDatos = CC.fetchall()        
    flash('Coincidencias para: ' + Vflor)
    return render_template('Busqueda.html', listFlores = consultaDatos)


#Habilitamos que la app cargue en servidor en el puerto especificado
#El debug nos permite hacer cambios en el código sin tener que tumbar el servidor
if __name__ == '__main__':
    app.run(port=5000, debug=True)