import models
from fastapi import FastAPI, Depends
import math
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, engine


app =  FastAPI()
models.Base.metadata.create_all(bind=engine)

class point(BaseModel):
    x : int 
    y : int  

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home(db: Session = Depends(get_db)):
    return db.query(models.Point).all()

@app.post("/post-Address")
def create_address(point:point, db: Session = Depends(get_db)):
    point_model = models.Point()
    point_model.x = point.x
    point_model.y = point.y

    db.add(point_model)
    db.commit()
    return point

@app.get("/get-point")
def get_point(point_dis:int,db: Session = Depends(get_db)):
    a=[]
    q=[0,0]
    # return db.query(models.Point).all()
    p1 = db.query(models.Point).all()
    for i in p1:
        p=[]
        p = [i.x,i.y]
    # return p1
        if point_dis >= math.dist(p,q):
            a.append(p)
    if len(a)==0:
        return {"msg":"No Point Present"}
    return a

