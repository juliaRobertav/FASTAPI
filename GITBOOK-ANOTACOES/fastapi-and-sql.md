# Fastapi & SQL

{% embed url="https://docs.sqlalchemy.org/en/14/dialects/mysql.html#asyncmy" %}

{% embed url="https://fastapidozero.dunossauro.com/" %}

{% embed url="https://kinsta.com/pt/blog/fastapi/" %}

{% embed url="https://github.com/dunossauro/fastapi-do-zero" %}

{% embed url="https://www.linode.com/pt-br/content/quickly-authenticate-users-with-fastapi-and-token-authentication/" %}

{% embed url="https://fastapi.tiangolo.com/tutorial/sql-databases/" %}

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
pip install asyncmy
```

