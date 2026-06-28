# pucpr_devops2026


# Aplicação de Livros - DevOps

Este repositório contém uma aplicação Flask para gerenciamento de livros, desenvolvida como parte da disciplina de DevOps. A aplicação possui um pipeline de CI/CD configurado no GitHub Actions, que executa testes e faz o build e push automático da imagem Docker para o Docker Hub.

## Executar com Docker (Recomendado)

A imagem está pública no Docker Hub. Para rodar a aplicação, basta executar:

```bash
docker pull paulotelss/meu-app:latest
docker run -p 5000:5000 paulotelss/meu-app:latest
```


Acesse no navegador: http://localhost:5000
Rotas disponíveis:

    / → Página inicial com informações dos integrantes.

    /livros → Lista de livros e formulário para cadastrar novos.

## Executar localmente (sem Docker)

Caso prefira rodar sem Docker:

    Clone o repositório:
    bash

    git clone https://github.com/paulotelss/pucpr_devops2026.git
    cd pucpr_devops2026

    Crie um ambiente virtual (opcional, mas recomendado):
    bash

    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    # ou
    venv\Scripts\activate     # Windows

    Instale as dependências:
    bash

    pip install -r requirements.txt

    Execute a aplicação:
    bash

    flask --app aplicacao.app:APP run --debug

    Acesse: http://localhost:5000

## Executar os testes unitários

Para rodar os testes localmente:
bash
```bash
pytest aplicacao/ -v
```
Os testes verificam as rotas / e /livros (GET e POST).
## Imagens Docker no Hub

    Última versão: paulotelss/meu-app:latest

    Versão com data (formato solicitado): paulotelss/paulo-giovani-teles-dias:27-06-26

## Tecnologias utilizadas

    Python 3.12 + Flask

    SQLAlchemy + SQLite (banco de dados local)

    Pytest (testes unitários)

    Docker (containerização)

    GitHub Actions (CI/CD)

## Pipeline CI/CD

O repositório possui um pipeline configurado em .github/workflows/ci_cd.yaml que:

    Roda os testes unitários.

    Constrói a imagem Docker.

    Envia a imagem para o Docker Hub.

## 👨‍💻 Integrantes

    Paulo Giovani Teles Dias


<img width="975" height="888" alt="Image" src="https://github.com/user-attachments/assets/898c8205-f59b-4bc6-adaf-a9ac088dd991" />


## 🎥 Demonstração da aplicação

[![Assista ao vídeo de demonstração](https://img.youtube.com/vi/tAEo436LuwY/0.jpg)](https://youtu.be/tAEo436LuwY)
