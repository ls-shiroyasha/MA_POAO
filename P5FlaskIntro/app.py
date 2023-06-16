#Importación del framework y de MySQL
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

#Inicialización del APP/servidor
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'#BD conecta al host
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbFlask'
mysql = MySQL(app)


#Declaración de las ruta http://localhost:5000
@app.route('/')#Ruta raíz/principal o index
def index():
    return render_template('index.html')

#Ruta http:localhost:5000/guardar - tipo POST para Insert
@app.route('/guardar', methods = ['POST'])
def guardar():
    if request.method == 'POST':
        titulo = request.form['txtTitulo']
        artista = request.form['txtArtista']
        anio = request.form['txtAnio']
        print(titulo, artista, anio)
    return 'Los datos llegaron'


@app.route('/eliminar')
def eliminar():
    return "Se elimino en la BD"


#Hacer que el servidor trabaje en el puerto especifícado: 5000 para este caso
#Ejecución del servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000, debug=True)
#El debug nos permite hacer cambios en el código sin tener que tumbar el servidor
