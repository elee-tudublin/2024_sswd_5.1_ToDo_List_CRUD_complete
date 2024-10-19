# Home router

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from starlette.config import Config

router = APIRouter()

# Load environment variables from .env
config = Config(".env")

# set location for templates
templates = Jinja2Templates(directory="app/view_templates")

# handle http get requests for the site root /
# return the index.html page
@router.get("/", response_class=HTMLResponse)
async def index(request: Request):

    # get current date and time
    serverTime: datetime = datetime.now().strftime("%d/%m/%y %H:%M:%S")

    # note passing of parameters to the page
    return templates.TemplateResponse("./home/index.html", {"request": request, "serverTime": serverTime })

@router.get("/advice", response_class=HTMLResponse)
async def advice(request: Request):
    
    # Define a request_client instance
    requests_client = request.app.requests_client

    # Connect to the API URL and await the response
    response = await requests_client.get(config("ADVICE_URL"))

    data = response.json()

    # Send the json data from the response in the TemplateResponse data parameter 
    return templates.TemplateResponse("./home/advice.html", {"request": request, "data": data })

@router.get("/apod", response_class=HTMLResponse)
async def apod(request: Request):
    requests_client = request.app.requests_client
    response = await requests_client.get(config("NASA_APOD_URL") + config("NASA_API_KEY"))
    return templates.TemplateResponse("./home/apod.html", {"request": request, "data": response.json() })


@router.post("/clicked", response_class=HTMLResponse)
async def clicked(request: Request):
    # note passing of parameters to the page
    return templates.TemplateResponse("./home/partials/clicked_button.html", {"request": request })

@router.get("/server_time", response_class=HTMLResponse)
async def index(request: Request):

    # get current date and time
    serverTime: datetime = datetime.now().strftime("%d/%m/%y %H:%M:%S")

    # send response
    return serverTime

# https://www.getorchestra.io/guides/mastering-query-parameters-in-fastapi-a-detailed-tutorial
@router.get("/params", response_class=HTMLResponse)
async def params(request: Request, name : str | None = ""):
    return templates.TemplateResponse("./home/params.html", {"request": request, "name": name })
