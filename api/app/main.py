from fastapi import FastAPI
import uvicorn


app = FastAPI()

from pydantic import BaseModel

class Item(BaseModel):
    repo: str
    job: str


@app.post("/api/items")
async def data_post(item: Item):
    repo = item.repo
    job = item.job
    
    return {
        "Status": 200,
        "Result": {
            "repo": f"{repo} ret",
            "job": f"{job} retjob",
        }
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=28081)