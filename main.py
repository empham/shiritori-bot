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

rules = '''\
1. You can't repeat a word
2. You can only use nouns
3. You can't end a word with an ん sound, since no words start with it.
4. You can use "words" that have の in them, as long as they are concrete enough \
to be considered a word. For example, things like 男おとこの 子こ would be acceptable.
5. Words normally written in hiragana or katakana are both okay. So, foreign words \
are a go (as long as they are actually considered words.)'''

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('~play'):
        await message.channel.send("Let's Play!")
    elif message.content.startswith('～遊びましょう'):
        await message.channel.send("いっしょに遊ぼうよ～")
    elif message.content.startswith('~rules'):
        await message.channel.send('**Standard Rules**')
        await message.channel.send(rules)


client.run(TOKEN)

