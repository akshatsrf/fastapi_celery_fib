from celery import Celery

app1 = Celery('tasks',
             broker='amqp://uwvixavr:MtPVnhDmZKcIWbfyAGDzCU8SBieiSAWD@turkey.rmq.cloudamqp.com/uwvixavr',
             backend='db+mysql://sql6513307:rC6MLbdySn@sql6.freesqldatabase.com:3306/sql6513307')

@app1.task
def fib(n: int):
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)
