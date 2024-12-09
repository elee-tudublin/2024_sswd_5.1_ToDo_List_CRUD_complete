# import the model class
from app.models.todo import *
from starlette.config import Config
from supabase import create_client, Client

import httpx, json

import json


# Load environment variables from .env
config = Config(".env")

db_url: str = config("SUPABASE_URL")
db_key: str = config("SUPABASE_KEY")

supabase: Client = create_client(db_url, db_key)