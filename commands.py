# File: commands.py
#
# code for all the commands
#
# Author: Emily Pham <emilyn3@hawaii.edu>

import discord

rules = '''\
1. You can't repeat a word
2. You can only use nouns
3. You can't end a word with an ん sound, since no words start with it.
4. You can use "words" that have の in them, as long as they are concrete enough \
to be considered a word. For example, things like 男おとこの 子こ would be acceptable.
5. Words normally written in hiragana or katakana are both okay. So, foreign words \
are a go (as long as they are actually considered words.)'''

async def print_rules(message):
        await message.channel.send('**Standard Rules**')
        await message.channel.send(rules)

async def play_shiritori(message):
    await message.channel.send("しりとり")