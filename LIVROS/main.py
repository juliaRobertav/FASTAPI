from fastapi import FastAPI, HTTPException, status, Response, Path
from models import Curso


app = FastAPI()  

cursos = {
    1: {
        "nome": "Python",
        "aulas": 20,
        "horas": 80,
        "instrutor": "Cleber"
    },
    2: {
        "nome": "Java",
        "aulas": 15,
        "horas": 60,
        "instrutor": "Leonardo"
    }
}

@app.get('/cursos')
async def get_cursos():
    return cursos


#é necessário fazer a tipagem de dados


@app.get('/cursos/{curso_id}') 
async def get_curso(curso_id : int = Path(default=None, title='ID do curso', description='Deve ser entre 1 e 2', gt=0, lt=3)):
    try:
        curso = cursos[curso_id]
        curso.update({"id": curso_id})
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso Não Encontrado')
    
    
@app.post('/cursos', status_code=status.HTTP_201_CREATED, response_model=Curso)
async def post_curso(curso: Curso):
    next_id = len(cursos) + 1
    if next_id not in cursos:
        curso.id = next_id
        cursos.append(curso)
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Já existe um curso com o ID {curso.id}")
 

@app.put('/cursos/{curso_id}')    
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos [curso_id] = curso
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Esse Curso Não Existe.")
 

@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Esse Curso Não Existe.")


@app.get('/calculadora')
async def calcular(a, b, c):
    soma = a + b + c
    return {"resultado": soma}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)