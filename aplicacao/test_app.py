import pytest
from aplicacao.app import APP, BD, Livro
from datetime import datetime

@pytest.fixture
def client():
    APP.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })
    with APP.app_context():
        BD.create_all()
        yield APP.test_client()
        BD.drop_all()

def test_index_status(client):
    assert client.get("/").status_code == 200

def test_index_conteudo(client):
    assert "Paulo Giovani Teles Dias" in client.get("/").text

def test_index_titulo(client):
    # Verifica se o link para livros está presente (nova versão)
    assert "Ver lista de livros" in client.get("/").text

def test_livros_get(client):
    assert client.get("/livros").status_code == 200

def test_livros_post(client):
    dados = {
        'titulo': 'Dom Casmurro',
        'autor': 'Machado de Assis',
        'issn': '1234-5678',
        'data_publicacao': '1899-01-01',
        'paginas': '256'
    }
    resp = client.post("/livros", data=dados, follow_redirects=True)
    assert "Dom Casmurro" in resp.text