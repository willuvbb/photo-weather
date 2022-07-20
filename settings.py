# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

FLICKR_API_KEY = os.environ.get("FLICKR_API_KEY")
FLICKR_SECRET_KEY = os.environ.get("FLICKR_SECRET_KEY")
