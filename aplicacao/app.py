from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/banco.db'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

BD = SQLAlchemy(APP)
MIGRATE = Migrate(APP, BD)

class Livro(BD.Model):
    __tablename__ = 'livros'
    id = BD.Column(BD.Integer, primary_key=True)
    titulo = BD.Column(BD.String(200), nullable=False)
    autor = BD.Column(BD.String(100), nullable=False)
    issn = BD.Column(BD.String(20), nullable=False)
    data_publicacao = BD.Column(BD.DateTime, nullable=False)
    paginas = BD.Column(BD.Integer, nullable=False)

@APP.route('/')
def index():
    return render_template('index.html')

@APP.route('/livros', methods=['GET', 'POST'])
def livros():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        autor = request.form.get('autor')
        issn = request.form.get('issn')
        data_publicacao = datetime.strptime(request.form.get('data_publicacao'), '%Y-%m-%d')
        paginas = int(request.form.get('paginas'))
        novo = Livro(titulo=titulo, autor=autor, issn=issn, data_publicacao=data_publicacao, paginas=paginas)
        BD.session.add(novo)
        BD.session.commit()
        return redirect(url_for('livros'))
    livros = Livro.query.all()
    return render_template('livros.html', livros=livros)

if __name__ == '__main__':
    with APP.app_context():
        BD.create_all()
    APP.run(debug=True, host='0.0.0.0')