from fastapi import FastAPI, HTTPException, status #Response, Path
# from typing import List, Optional
from models import Livro

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
async def get_livro(livro_id: int):
    try:
        livro = livros[livro_id]
        #livro.update({"id": livro_id})
        return livro
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não foi possível encontrar este livro.")
    

@app.post('/livros')
async def post_livro(livro: Livro):
    if livro.id not in livros:
        livros[livro.id] = livro
        return livro
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Já existe um livro com ID {livro.id}")
    
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='127.0.0.1', port=8000, debug=True, reload=True)