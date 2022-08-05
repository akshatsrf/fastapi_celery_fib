from fastapi import FastAPI
from tasks import fib,app1
from celery.result import AsyncResult
app = FastAPI()

@app.post('/{number}')
async def send_number(number: int):
    res = fib.delay(number)
    return res.id

@app.get('/result')
async def get_fib(id):
    result = AsyncResult(id, app=app1)
    return result.get()
    