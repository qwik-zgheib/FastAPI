from fastapi import FastAPI;

app = FastAPI();

@app.get('/')
async def read_root():
    return {'data': {'name': 'qwik'} };

@app.get('/about')
async def read_about():
    return {'data': 'About page' };