#Importación del framework y de MySQL
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#Inicialización del APP/servidor
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'#BD conecta al host
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbFlask'
app.secret_key = "clave_secreta"#Token para validación por cuestiones de seguridad al mandar datos entre la BD y la págia web
mysql = MySQL(app)



#Declaración de las ruta http://localhost:5000
@app.route('/')#Ruta raíz/principal o index
def index():
    CC = mysql.connection.cursor();
    CC.execute('select * from tbalbums')    
    conAlbums = CC.fetchall()#Consulta albums
    print(conAlbums)
    return render_template('index.html', listAlbums = conAlbums)

#Ruta http:localhost:5000/guardar - tipo POST para Insert
@app.route('/guardar', methods = ['POST'])
def guardar():
    if request.method == 'POST':
        #Pasamos a variables el contenido de los inputs
        Vtitulo = request.form['txtTitulo']
        Vartista = request.form['txtArtista']
        Vanio = request.form['txtAnio']
        #Conectar y ejecutar el insert
        #El objeto tipo cursor llamado CS
        CS = mysql.connection.cursor()   #(%s, %s, %s) --> Datos indefinidos que se pasan al siguiente parámetro de execute
        CS.execute('insert into tbalbums(titulo, artista, anio) values(%s, %s, %s)', (Vtitulo, Vartista, Vanio))
        mysql.connection.commit()
        #print(titulo, artista, anio)
    
    flash('El album fue agregado correctamente')
    return redirect(url_for('index'))#Redireccionamos a una url (la que llamamos index)

@app.route('/editar/<id>')
def editar(id):
    cursoId = mysql.connection.cursor()
    cursoId.execute('select * from tbalbums where id=%s', (id,))
    consultId = cursoId.fetchone()
    return render_template('editarAlbum.html', album = consultId)

@app.route('/actualizar/<id>', methods = ['POST'])
def actualizar(id):
    if request.method == 'POST':
        #Pasamos a variables el contenido de los inputs
        Vtitulo = request.form['txtTitulo']
        Vartista = request.form['txtArtista']
        Vanio = request.form['txtAnio']
        #Conectar y ejecutar el insert
        #El objeto tipo cursor llamado CS
        curAct = mysql.connection.cursor()   #(%s, %s, %s) --> Datos indefinidos que se pasan al siguiente parámetro de execute
        curAct.execute('update tbalbums set titulo = %s, artista = %s, anio = %s where id = %s',(Vtitulo, Vartista, Vanio, id))
        mysql.connection.commit()
    flash('Se actualizo el Album ' + Vtitulo)
    return redirect(url_for('index'))

@app.route('/eliminar/<id>')####
def eliminar(id):####
    cursoId = mysql.connection.cursor()
    cursoId.execute('select * from tbalbums where id=%s', (id,))
    consultId = cursoId.fetchone()
    return render_template('eliminarAlbum.html', album = consultId)

@app.route('/borrar/<id>', methods = ['POST'])
def borrar(id):
    if request.method == 'POST':
        curAct = mysql.connection.cursor()
        curAct.execute('delete from tbalbums where id = %s', (id,))
        mysql.connection.commit()
    flash('Se elimino el album ')
    return redirect(url_for('index'))


#Hacer que el servidor trabaje en el puerto especifícado: 5000 para este caso
#Ejecución del servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000, debug=True)
#El debug nos permite hacer cambios en el código sin tener que tumbar el servidor
