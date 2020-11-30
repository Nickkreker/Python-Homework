from fastapi import FastAPI
from fastapi.responses import JSONResponse
import unicorn
import httpx

app = FastAPI()

async def get_data(number):
    async with httpx.AsyncClient() as client:
        data = await client.get('https://jsonplaceholder.typicode.com/todos/{0}'.format(number))
        return data

@app.get('/todo/{number}')
async def main(number):
    data = await get_data(number)
    
    data.headers.pop('content-encoding')
    return JSONResponse(content=data.json(),
                        status_code=data.status_code,
                        headers=data.headers)

if __name__ == '__main__':
    unicorn.run(app, port=8000, host='0.0.0.0')
