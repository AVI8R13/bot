from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("BOT_TOKEN")
giphyKey = os.getenv("GIPHY_KEY")