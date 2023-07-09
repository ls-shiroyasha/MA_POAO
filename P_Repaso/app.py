#Importación de los elementos necesarios del framework y de MySQL
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#Inicialización del APP/servidor
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'#BD conecta al host
app.config['MYSQL_USER']='root'#El usuario es root
app.config['MYSQL_PASSWORD']=''#No definimos contraseña
app.config['MYSQL_DB']='DB_Fruteria'#BD de la fruteria
app.secret_key = "clave_secreta"#Token para validación por cuestiones de seguridad al mandar datos entre la BD y la página web
mysql = MySQL(app)



#Declaración de las ruta http://localhost:5000
#Hacer que el servidor trabaje en el puerto especifícado: 5000 para este caso
#Ejecución del servidor en el puerto 5000
@app.route('/')#Ruta raíz/principal o index
def index():
    CC = mysql.connection.cursor();#Cursor para hacer conexión a mysql
    CC.execute('select * from tbFrutas')#Seleccionamos todos los datos de la tabla
    consultaDatos = CC.fetchall()#Consultar datos de toda la tabla    
    return render_template('index.html', listFrutas = consultaDatos)

#Ruta http:localhost:5000/guardar - tipo POST para Insert
@app.route('/guardar', methods = ['POST'])
def guardar():
    if request.method == 'POST':
        #Pasamos a variables el contenido de los inputs
        Vfruta = request.form['txtFruta']
        Vtemporada = request.form['txtTemporada']        
        Vprecio = request.form['txtPrecio']
        Vstock = request.form['txtStock']
        #Conectar y ejecutar el insert
        #El objeto tipo cursor llamado CS
        CS = mysql.connection.cursor()   #(%s, %s, %s) --> Datos indefinidos que se pasan al siguiente parámetro de execute
        CS.execute('insert into tbFrutas(Fruta, Temporada, Precio, Stock) values(%s, %s, %s, %s)', (Vfruta, Vtemporada, Vprecio, Vstock))
        mysql.connection.commit()            
    flash('Los datos se agregaron correctamente')    
    return redirect(url_for('registrar'))#Redireccionamos al index
    #return render_template('registros.html')
    #return redirect(url_for('index'))#Redireccionamos al index

@app.route('/editar/<id>')
def editar(id):
    cursoId = mysql.connection.cursor()
    cursoId.execute('select * from tbFrutas where id=%s', (id,))
    consultId = cursoId.fetchone()
    return render_template('editarRegistro.html', frut = consultId)

@app.route('/actualizar/<id>', methods = ['POST'])
def actualizar(id):
    if request.method == 'POST':
        #Pasamos a variables el contenido de los inputs
        Vfruta = request.form['txtFruta']
        Vtemporada = request.form['txtTemporada']        
        Vprecio = request.form['txtPrecio']
        Vstock = request.form['txtStock']
        #Conectar y ejecutar el insert
        #El objeto tipo cursor llamado CS
        curAct = mysql.connection.cursor()
        curAct.execute('update tbFrutas set Fruta = %s, Temporada = %s, Precio = %s, Stock = %s where id = %s',(Vfruta, Vtemporada, Vprecio, Vstock, id))
        mysql.connection.commit()
    flash('Se actualizo el registro')
    return redirect(url_for('registrar'))

@app.route('/registrar')#Ruta raíz/principal o index
def registrar():
    CC = mysql.connection.cursor();#Cursor para hacer conexión a mysql
    CC.execute('select * from tbFrutas')#Seleccionamos todos los datos de la tabla
    consultaDatos = CC.fetchall()#Consultar datos de toda la tabla    
    return render_template('registros.html', listFrutas = consultaDatos)

@app.route('/eliminar/<id>')####
def eliminar(id):####
    cursoId = mysql.connection.cursor()
    cursoId.execute('select * from tbFrutas where id=%s', (id,))
    consultId = cursoId.fetchone()
    return render_template('eliminarRegistro.html', frut = consultId)
    
@app.route('/borrar/<id>', methods = ['POST'])
def borrar(id):
    if request.method == 'POST':
        curAct = mysql.connection.cursor()
        curAct.execute('delete from tbFrutas where id = %s', (id,))
        mysql.connection.commit()
    flash('Se elimino el registro')
    return redirect(url_for('registrar'))

@app.route('/buscar')
def buscar():
    #CC = mysql.connection.cursor();#Cursor para hacer conexión a mysql
    #CC.execute('select * from tbFrutas')#Seleccionamos todos los datos de la tabla
    #consultaDatos = CC.fetchall()#Consultar datos de toda la tabla    
    return render_template('hacerBusqueda.html')

@app.route('/mostrar', methods = ['POST'])
def mostrar():
    if request.method == 'POST':        
        Vfruta = request.form['txtFruta']
        CC = mysql.connection.cursor()
        CC.execute('select * from tbFrutas where Fruta=%s', (Vfruta,))
        #CC.execute('select * tbFrutas where Fruta like = %s%', (Vfruta,))
        consultaDatos = CC.fetchall()        
    flash('Coincidencias para: ' + Vfruta)
    return render_template('hacerBusqueda.html', listFrutas = consultaDatos)


#Habilitamos que la app cargue en servidor en el puerto especificado
#El debug nos permite hacer cambios en el código sin tener que tumbar el servidor
if __name__ == '__main__':
    app.run(port=5000, debug=True)