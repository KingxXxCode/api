from fastapi import FastAPI
"""write a FastAPI code that accepts 3 int parameters through fastapi and return the sum of the 3 int parameters """
app = FastAPI()
def sum(a,b,c):
    return a+b+c
@app.get("/sum/{a}/{b}/{c}")
async def root(a: int, b: int, c: int):
    return {"sum": sum(a,b,c)}  

