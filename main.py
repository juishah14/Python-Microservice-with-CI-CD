import uvicorn
from fastapi import FastAPI
from library import apod, earth_natural_imagery, nasa_library, asteroid_info

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the NASA API!"}


@app.get("/apod")
async def search_apod():
    # Retrieve the Astronomy Picture of the Day
    result = apod()
    return {"result": result}


@app.get("/earth-natural-imagery")
async def search_earth():
    # Retrieve metadata on the most recent date of natural color imagery
    result = earth_natural_imagery()
    return {"result": result}


@app.get("/nasa-library/{query}")
async def search_nasa(query: str):
    # Perform a search of the Nasa Image and Video library
    result = nasa_library(query)
    return {"result": result}


@app.get("/asteroid-info/{start_date}/{end_date}")
async def search_asteroid(start_date: str, end_date: str):
    # Retrieve a list of Asteroids on thier closest approach date to Earth
    result = asteroid_info(start_date, end_date)
    return {"result": result}


# basically http://localhost:8080/
if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
