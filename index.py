from flask import Flask,render_template
import pyodbc

app = Flask(__name__)


#Conexion a base de datos
#conexion = pyodbc.connect('Driver = {OBDC Driver 17 for SQL Server};'
#                        'server = localhost;'
#                        'database = devuser;'
#                        'uid = devuser'
#                        )

#Funciones invocadoras de Pages 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/pag1')
def pag1():
    return render_template('pag1.html')

if __name__ == '__main__':
    app.run(debug=True)