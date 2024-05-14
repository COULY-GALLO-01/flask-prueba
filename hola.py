from flask import Flask, render_template


app=Flask(__name__)


@app.route('/')
def principal():
    
    return render_template('index.html')#aca poner link a archivos front end, como la ruta esta en "/" es lo primero que vemos, todo en la carpeta templates, asi es el programa

@app.route('/test')
def secondary():
  
    return render_template('test.html')


if __name__=='__main__':
    app.run(debug=True, port=5000)

