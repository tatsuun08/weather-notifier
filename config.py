from dotenv import load_dotenv
import os


# .envファイルをロード
load_dotenv()

class Config:
    DISCORD_TORKEN = os.getenv('DISCORDBOT_TORKEN')