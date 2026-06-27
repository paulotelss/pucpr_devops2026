FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY aplicacao/ ./aplicacao/
ENV FLASK_APP=aplicacao.app:APP
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]