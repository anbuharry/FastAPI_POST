from fastapi import FastAPI
from pydantic import BaseModel


class GreetingModel(BaseModel):
	texts: str
	
app = FastAPI(title="date_picker_fastapi")

@app.post('/date_range')
async def date(text: GreetingModel):
	print(text.texts)
	return {"status" : 200}
