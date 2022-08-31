# File: main.py
#
# Main code for shiritori bot
#
# Author: Emily Pham <emilyn3@hawaii.edu>

from commands import play_shiritori
from commands import print_rules
from dotenv import load_dotenv

import os
import discord

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('~play'):
        await message.channel.send("Let's Play!")
        await play_shiritori(client, message)
    elif message.content.startswith('～遊びましょう'):
        await message.channel.send("いっしょに遊ぼうよ～")
    elif message.content.startswith('~rules'):
        await print_rules(message)


client.run(TOKEN)