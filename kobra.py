#!/usr/bin/env python

import discord
import asyncio
import json
import sys
import os

from utilities import *

# Client
client = discord.Client()

# Events
@client.event
async def on_ready():
    print(client.user.name + " is ready to go!")

@client.event
async def on_message(message):
    mention = False

    if len(message.mentions) > 0:
        for x in message.mentions:
            if x.id == client.user.id:
                mention = True

    if not mention or message.author.bot:
        return

    await client.send_message(message.channel, "Hello!")

# Init
if __name__ == "__main__":
    if not os.path.isfile("./keychain.json"):
        fatal("keychain.json is missing; fill out keychain.json.example and remove .example from the name!")
    
    if not os.path.isfile("./settings.json"):
        fatal("settings.json is missing... what did you do?!")

    # Load Keychain
    with open("./keychain.json", "r") as f:
        keys = json.loads(f.read())

    # Run with 
    client.run(keys["token"])
