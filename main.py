# iniciar librerias de Python
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
# instancias
app = Flask(__name__)
bootstrap = Bootstrap(app)

# Diccionario
tres_columnas = {
    'columna0': {
        'img': 'img/icono01.png',
        'titulo': 'Core',
        'subtitulo': 'Everithings you need...',
        'precio': 'Free',
        'enlace': 'All core features',
        'boton': 'Included'
    },
    'columna01': {
        'img': 'img/icono02.png',
        'titulo': 'CoAdapt',
        'subtitulo': 'Customize you data....',
        'precio': '99',
        'enlace': 'All core features',
        'boton': 'Included'
    },
    'columna02': {
        'img': 'img/icono03.png',
        'titulo': 'Localize',
        'subtitulo': 'Add multiple languages....',
        'precio': '49',
        'enlace': 'Multilanguage......',
        'boton': 'Remove'
    }
}


# rutas
@app.route('/')
def home():
    return render_template('precios.html',
    **tres_columnas)


if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
