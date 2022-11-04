import uvicorn
from fastapi import FastAPI
from library.logic import search_wiki
from library.logic import wiki as wikilogic
from library.logic import phrase as wikiphrases

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API.  Call /search or /wiki or /phrase"}


@app.get("/search/{value}")
async def search(value: str):
    """Page to search in wikipedia"""

    result = search_wiki(value)
    return {"result": result}


@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retrieve wikipedia page"""

    result = wikilogic(name)
    return {"result": result}


@app.get("/phrase/{name}")
async def phrase(name: str):
    """Retrieve wikipedia page and return phrases"""

    result = wikiphrases(name)
    return {"result": result}


# basically http://localhost:8080/
if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
