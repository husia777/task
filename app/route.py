from fastapi import FastAPI, Query
from typing import Annotated
import requests
app = FastAPI()


@app.get("/")
async def converter(fromm: Annotated[str, Query(alias='from')], to: str, value: int):
    data = requests.get(
        f'https://v6.exchangerate-api.com/v6/906080ffef5930a673f492bc/pair/{fromm}/{to}'
    ).json()
    return data['conversion_rate'] * value
