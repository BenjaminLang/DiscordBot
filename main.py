import discord
import asyncio
import json
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import dbInterface

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
discordBot = Bot(description="TestBot", command_prefix="!", pm_help = True)
Users = dict()

def getToken():
	data = json.load(open('token.json'))
	return data["token"]

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
@discordBot.event
async def on_ready():
	print('Logged in as')
	print(discordBot.user.name)
	print(discordBot.user.id)

	for member in discordBot.get_all_members():
		Users[member.name] = dbInterface.History(member.name, member.id)

@discordBot.event
async def on_message(message):
	if message.author == discordBot.user:
		return

	print(message.content)
	print(message.author)
	Users[message.author].logMessage(message.content)

	await discordBot.process_commands(message)

# This is a basic example of a call and response command. You tell it do "this" and it does it.
@discordBot.command()
async def ping(*args):
	await discordBot.say(":ping_pong: Pong!")

@discordBot.command()
async def pong(*args):
	await discordBot.say(":ping_pong: Ping!")

@discordBot.command()
async def history(message, num):
	await discordBot.say(Users[message.author].getLastMessages(num))

discordBot.run(getToken())
