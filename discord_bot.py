from get_weather import get_city_weather
import discord
from config import Config


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!hello':
        await message.channel.send('Hello!')

# client.run(Config.SECRET_KEY)
print(Config.SECRET_KEY)
