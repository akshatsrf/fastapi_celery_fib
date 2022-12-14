from fastapi import FastAPI
from tasks import fib,app1
from celery.result import AsyncResult
app = FastAPI()

@app.get('/{number}')
async def send_number(number: int):
    res = fib.delay(number)
    return res.get()

# @app.get('/result')
# async def get_fib(id):
#     result = AsyncResult(id, app=app1)
#     return result.get()

@app.get('/without_celery/{number}')
async def send_number_without_celery(number: int):
    return fib(number)