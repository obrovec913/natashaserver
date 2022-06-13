from nata import fasta 
from natanp import natanp
from fastapi import FastAPI


app = FastAPI()



@app.post("/natasha")
def dssas(text:str):
    return fasta(text)

@app.post("/natashanp")
def natanpp(text:str):
    return natanp(text)
