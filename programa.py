from flask import Flask, render_template


class Programa:

     def __init__(self):

       self.app=Flask(__name__)

       self.app.add_url_rule('/nuevo', view_func=self.agregar)

    #Iniciar el servidor 
       self.app.run(debug=True)

     def agregar(self):
        return render_template('nuevoEstudiante.html')


miprograma=Programa()