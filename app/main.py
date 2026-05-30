from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import engine, SessionLocal
from app.models import Base, User, Restaurant, Order

app = FastAPI(title="Food Delivery MVP", version="1.0.0")

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@app.on_event("startup")
def startup(): Base.metadata.create_all(bind=engine)

@app.get("/")
def root(): return {"message": "Food Delivery API is running"}

@app.get("/users", response_model=list[dict])
def get_users(db: Session = Depends(get_db)):
    return [{"id": u.id, "name": u.name, "role": u.role} for u in db.query(User).all()]

@app.get("/restaurants", response_model=list[dict])
def get_restaurants(db: Session = Depends(get_db)):
    return [{"id": r.id, "name": r.name, "rating": r.rating} for r in db.query(Restaurant).all()]

@app.post("/orders", response_model=dict)
def create_order(order_data: dict, db: Session = Depends(get_db)):
    if not all(k in order_data for k in ("user_id", "restaurant_id", "total_amount", "delivery_address")):
        raise HTTPException(400, "Missing required fields")
    new_order = Order(**order_data)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return {"id": new_order.id, "status": new_order.status, "total": new_order.total_amount}