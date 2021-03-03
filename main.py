from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origin=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class todolist(BaseModel):
    item:int
    chore:str


class delitem(BaseModel):
    item:int


class Name(BaseModel):
    person_name:str
    age:int

@app.get("/")
def basic():
    return "Hello world"



@app.get("/info")
def info():
    #info={"Name":"Noel","srn":"PES2UG20CS446","fun fact":"You are alive(for now)"}
    #return info
    name="Noel"
    SRN="PES2UG20CS446"
    funfact="You are alive(for now)"
    return(name,SRN,funfact)
    
 


    
@app.get("/date")
def return_date():
    res={"date":"today"}
    return "today is 4th"



@app.post("/name")
def name(name_var: Name):
    name_encoded=jsonable_encoder(name_var)
    pname= name_encoded['person_name']
    with open("names.txt","a") as f:
            f.write('{}\n'.format(pname))
            f.write("\n")
        
    age= name_encoded['age']
    print(age)
    print(type(age))
    return "Hello "+pname
todo={}
@app.post("/todolist")
def ITEM(item_var: todolist):
    
    item_encoded=jsonable_encoder(item_var)
    itemno= item_encoded['item']
    choreno= item_encoded['chore']
    #with open("todo.txt","a") as file:
       # file.write('{}{}\n'.format(itemno,choreno))
    todo[itemno]=choreno
    print (todo)
    return(todo)
@app.put("/todolist")
def ITEM(item_var: todolist):
    item_encoded=jsonable_encoder(item_var)
    itemno= item_encoded['item']
    choreno= item_encoded['chore']
    todo.update({itemno:choreno})
    return(todo)
@app.delete("/todolist")
def ITEM(item_var: delitem):
    item_encoded=jsonable_encoder(item_var)
    itemno= item_encoded['item']
    del todo[itemno]
    return(todo)
@app.get("/todolist")
def mystuff():
    return(todo)
