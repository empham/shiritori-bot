# File: main.py
#
# Main code for shiritori bot
#
# Author: Emily Pham <emilyn3@hawaii.edu>

from dotenv import load_dotenv
import os
import discord

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('~play'):
        await message.channel.send("Let's Play!")
    if message.content.startswith('～遊びましょう'):
        await message.channel.send("いっしょに遊ぼうよ～")

client.run(TOKEN)

