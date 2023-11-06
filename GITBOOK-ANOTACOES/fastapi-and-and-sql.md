# Fastapi && SQL

{% embed url="https://docs.sqlalchemy.org/en/14/dialects/mysql.html#asyncmy" %}

{% embed url="https://github.com/dunossauro/fastapi-do-zero" %}

```
core = núcleo do projeto

schemas = pega obj sql,do banco de dados ou do python e trasnforma em json e entrega da api
e recebe os dados da api e transforma em python ou banco de dados para que seja salvo
Chamado de serialização e deserializacao e é feito pelo pydantic
```

Install ->

```
pip install fastapi psycopg2-binary sqlalchemy asyncpg uvicorn
pip install pydantic-settings
```

