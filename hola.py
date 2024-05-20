from flask import Flask, render_template


app=Flask(__name__)


@app.route('/')
def principal():
    
    return render_template('test.html')#aca poner link a archivos front end, como la ruta esta en "/" es lo primero que vemos, todo en la carpeta templates, asi es el programa

@app.route('/starter')
def start():
    
    return render_template('father.html')#aca poner link a archivos front end, como la ruta esta en "/" es lo primero que vemos, todo en la carpeta templates, asi es el programa

@app.route('/son')
def son():
    
    return render_template('son.html')#aca poner link a archivos front end, como la ruta esta en "/" es lo primero que vemos, todo en la carpeta templates, asi es el programa


if __name__=='__main__':
    app.run(debug=True, port=5000)

