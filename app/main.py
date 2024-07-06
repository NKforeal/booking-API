import uvicorn
from fastapi import FastAPI

from app.users.router import router as router_register
from app.bookings.router import router as router_bookings
from app.hotels.router import router as router_hotels

app = FastAPI()

app.include_router(router_register)
app.include_router(router_bookings)
app.include_router(router_hotels)

if __name__ == '__main__':
    uvicorn.run(app=app, port=8000)
