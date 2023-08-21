from fastapi import FastAPI, HTTPException, status

app = FastAPI()  

cursos = {
    1: {
        "id": 1,
        "nome": "Python",
        "aulas": 20,
        "horas": 80,
        "instrutor": "Cleber"
    },
    2: {
        "id": 2,
        "nome": "Java",
        "aulas": 15,
        "horas": 60,
        "instrutor": "Leonardo"
    }
}

@app.get('/cursos/{curso_id}') 
async def get_cursos(curso_id : int):
    try:
        curso = cursos[curso_id]
        curso.update({"id": curso_id})
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso Não Encontrado')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)

