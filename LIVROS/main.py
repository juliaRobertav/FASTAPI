from fastapi import FastAPI, HTTPException, status, Response 
from models import Livro
import requests
import json


app = FastAPI()


livros = {
    1: {
        "nome": "A Culpa é das Estrelas",
        "gênero": "drama",
        "autor": "John Green",
        "editora": "Intriseca"
    },
    2: {
        "nome": "Coraline",
        "gênero": "terror",
        "autor": "Neil Gaiman",
        "editora": "Intriseca"
    },
    3: {
        "nome": "O Gato Preto",
        "gênero": "terror",
        "autor": "Edgar Allan Poe",
        "editora": "Camelot Editora"
    },
    4: {
        "nome": "Até o Verão Terminar",
        "gênero": "romance",
        "autor": "Colleen Hoover",
        "editora": "Grupo Editorial Record"
    } 
}


#método get
@app.get('/livros')
async def get_livros():
    return livros

@app.get('/livros/{livro_nomes}')
async def get_nome(livro_nomes: str):
    for livro in livros:
        if livros[livro]["nome"] == livro_nomes:
            nome_livro = livros[livro]
    return(nome_livro)
    
    
#método get para livro específico
@app.get('/livros/{livro_id}')
async def get_livro(livro_id: str ):
    try:
        livro = livros[livro_id]
        #livro.update({"id": livro_id})
        return livro
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não foi possível encontrar este livro.")
    
    
#método post
@app.post('/livros', status_code=status.HTTP_201_CREATED)
async def post_livro(livro: Livro):
    next_id: int = len(livros) + 1
    if next_id not in livros:
        livro.id = next_id
        livros[next_id] = livro
        return livro
    else:
         raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Ja existe o livro com id {livro.id}")


#método put
@app.put('/livros/{livro_id}')
async def put_livro(livro_id: int, livro:Livro):
    if livro_id in livros:
        livros[livro_id] = livro
        del livro.id
        return livro
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe um curso com o ID {livro_id}")
  
        
#método delete
@app.delete('/livros/{livro_id}')    
async def delete_livro(livro_id: int):
    if livro_id in livros:
        del livros[livro_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe um curso com ID {livro_id}")


#consumindo api do google books
@app.get('/api/livros')
async def get_livros():
    request = requests.get("https://www.googleapis.com/books/v1/volumes?q=A+culpa+é+das+estrelas") #basta colocar o nome do autor ou livro caso queira algum específico 
    response = request.json()
    return response


#consumindo api de filmes e séries
@app.get('/biblioteca')
async def get_biblioteca():
    request_series = requests.get('http://10.234.92.19:8000')
    series = json.loads(request_series.content)
    
    request_filmes = requests.get('http://10.21.59.33:8000')
    filmes = json.loads(request_filmes.content)
    return livros, series, filmes
    
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)