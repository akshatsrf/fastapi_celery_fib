from celery import Celery

app1 = Celery('tasks',
             broker='amqp://uwvixavr:MtPVnhDmZKcIWbfyAGDzCU8SBieiSAWD@turkey.rmq.cloudamqp.com/uwvixavr',
             backend='db+sqlite:///db.sqlite3')

@app1.task
def fib(n: int):
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)
