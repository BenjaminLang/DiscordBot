import discord
import asyncio
import json
from discord.ext.commands import Bot
from discord.ext import commands
import platform

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
discordBot = Bot(description="TestBot", command_prefix="!", pm_help = True)

def getToken():
	data = json.load(open('token.json'))
	return data["token"]

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
@discordBot.event
async def on_ready():
	print('Logged in as')
	print(discordBot.user.name)
	print(discordBot.user.id)

# This is a basic example of a call and response command. You tell it do "this" and it does it.
@discordBot.command()
async def ping(*args):
	await discordBot.say(":ping_pong: Pong!")

@discordBot.command()
async def pong(*args):
	await discordBot.say(":ping_pong: Ping!")

discordBot.run(getToken())
