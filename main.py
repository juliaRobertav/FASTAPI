from fastapi import FastAPI

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

@app.get('/cursos') 
async def get_cursos():
    return cursos

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)
