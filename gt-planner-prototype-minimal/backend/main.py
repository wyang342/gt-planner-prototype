from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

from data import default_curriculums
from fastapi.responses import JSONResponse


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


# open the dot files
f1 = open('./dots/g1.gv')
f2 = open('./dots/g2.gv')
f3 = open('./dots/g3.gv')
f4 = open('./dots/g4.gv')

# read the dot files
d1 = f1.read()
d2 = f2.read()
d3 = f3.read()
d4 = f4.read()
dots = [d1, d2, d3, d4]

origins = ['http://localhost:8080']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/graph/{item_id}")
def read_examples(item_id: int, q: Optional[str] = None):
    # return {"item_id": item_id, "q": q}
    return {"item_id": dots[item_id]}

@app.get("/graph/{item_id}")
def get_graph(item_id: int, q: Optional[str] = None):
    # draw_scheme
    # extract dot lines from graphviz obj
    # maybe to_str
    # or look into file-writing source code (by exploring filename argument)
    return

@app.get("/curr/{major}")
def get_curr(major: str):
    return JSONResponse(default_curriculums[major])

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


# not sure if these will ever get called
f1.close()
f2.close()
f3.close()
f4.close()