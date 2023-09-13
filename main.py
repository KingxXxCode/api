from typing import Annotated, Union

from fastapi import FastAPI, Query
import json
app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[Union[list[str], None], Query()] = None):
    query_items = parse_input(q) 
    return query_items


def parse_input(input_data):
    try:
        # Convert the input JSON-like string into a Python dictionary
        data = json.loads(input_data[0])
        
        # Extract and return the dictionary
        return data
    except Exception as e:
        # Handle any exceptions that may occur during parsing
        return {"error": str(e)}

