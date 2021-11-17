## Como instalar as dependências

```sh
pip install -r requirements.txt
```

## Como fazer as migrações

```sh
flask db init
flask db migrate
flask db upgrade
```

## Como rodar esse projeto

```sh
set FLASK_APP=app.py
set FLASK_ENV=development
set FLASK_DEBUG=True

flask run
```