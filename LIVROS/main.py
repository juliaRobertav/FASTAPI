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


@app.get('/livros')
async def get_livros():
    return livros

@app.get('/livros/{livro_id}')
async def get_livro(livro_id: int ):
    try:
        livro = livros[livro_id]
        #livro.update({"id": livro_id})
        return livro
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não foi possível encontrar este livro.")
    

@app.post('/livros', status_code=status.HTTP_201_CREATED)
async def post_livro(livro: Livro):
    next_id: int = len(livros) + 1
    livros[next_id] = livro
    del livro.id
    return livro


@app.put('/livros/{livro_id}')
async def put_livro(livro_id: int, livro:Livro):
    if livro_id in livros:
        livros[livro_id] = livro
        del livro.id
        return livro
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe um curso com o ID {livro_id}")
        

@app.delete('/livros/{livro_id}')    
async def delete_livro(livro_id: int):
    if livro_id in livros:
        del livros[livro_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe um curso com ID {livro_id}")

@app.get('/api/livros')
async def get_livros():
    request = requests.get("https://www.googleapis.com/books/v1/volumes?q=search-terms&key=AIzaSyB0xZUK8Zaag-Mf-_0Q_h8Y2Y9QH_FcjtI")
    response = request.json()
    return response


    
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
