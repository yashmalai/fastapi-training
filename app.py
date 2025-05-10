from fastapi import FastAPI, Body, Header, Response, Depends
from fastapi.params import Param
import uvicorn
import asyncio
from models import Creature
from data import get_creatures

app = FastAPI()

@app.get("/cr")
def get_all() -> list[Creature]:
    return get_creatures()

# функция зависимости:
def user_dep(name: str = Param, password: str = Param):
    return {"name": name, "valid": True}

# функция пути/конечная точка веб-приложения:
@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user

# @app.get('/hi/{who}') # извлечь переменную под названием who в указанном местоположении в URL
# def url(who):
#     return f'helo {who}'

# @app.get('/hu') # who — это параметр запроса name==value
# def param(who):
#     return f'helo {who}'

# @app.post('/hu')
# def json_body(who:str = Body(embed=True)): # получаем значение who из тела запроса в формате JSON name=value
#     return f'helo {who}'

# @app.get('/hy')
# def header_post(who:str = Header()): # получаем значение who из HTTP-заголовка name:value
#     return f'helo {who}'

# @app.get("/agent")
# def get_agent(user_agent:str = Header()):
#     return user_agent

# @app.get("/happy")
# def happy(status_code=200):
#     return ":)"

# @app.get("/header/{name}/{value}")
# def header(name: str, value: str, response:Response):
#     response.headers[name] = value
#     return "normal body"

# @app.get("/hi")
# async def greet():
#     await asyncio.sleep(1)
#     return "Hello? World?"

# if __name__ == '__main__':
#     uvicorn.run('app:app', reload=True)