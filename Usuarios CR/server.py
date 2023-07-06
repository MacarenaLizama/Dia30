from flask import Flask, render_template, redirect, request
from usuarios import Usuarios

app = Flask(__name__)

@app.route("/")
def home():
    return redirect ("/usuarios")

@app.route("/usuarios")
def mostrar_usuarios():
    lista_usuarios = Usuarios.obtener_todos()
    return render_template("usuarios.html", lista_usuarios=lista_usuarios)

@app.route("/nuevo/usuario")
def nuevo_usuario():
    return render_template("nuevo_usuario.html")

@app.route( "/crear/usuario", methods = ['POST'] )
def crear_usuario():
    nuevo_usuario = {
        "nombre"    : request.form['nombre'],
        "apellido"  : request.form['apellido'],
        "email" :   request.form['email']
    }
    Usuarios.agregar_usuario( nuevo_usuario )
    return redirect( "/" )

if __name__=="__main__":
    app.run( debug = True, port= 5001)

