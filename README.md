# myfy-auth-service
Serviço de autenticação do MVP da sprint de arquitetura de software da minha pós-graduação 

---
## Como executar 

1. Instalar dependências (as mesmas estão descritas no arquivo `requirements.txt`).
```
$ pip install -r requirements.txt
```

2. Dispnibilizar a API
```
$ flask run --host 0.0.0.0 --port 5000
```

> A documentação da APi pode ser visualizada acessando http://localhost:5000 (se a porta usada para iniciar o flask foi a 5000)

## Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker build -t myfy-auth-service .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$ docker run -p 5000:5000 myfy-auth-service
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador.

