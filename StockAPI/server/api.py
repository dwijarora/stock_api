from fastapi import FastAPI
from server.models.values_model import ValuesModel

from server.services.read_stocks import readStocks
from server.services.read_values import readValues
app = FastAPI()

@app.get("/")
async def read_root():
    return "Api Working"


@app.get("/readStocks/")
async def read_stocks():
    return readStocks()


@app.post("/readValues/")
async def read_values(model: ValuesModel):
    return readValues(model)
