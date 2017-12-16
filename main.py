import discord
import asyncio
import json
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import dbInterface

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
discordBot = Bot(description="TestBot", command_prefix="!", pm_help=True)
Users = dict()


def getToken():
    data = json.load(open('token.json'))
    return data["token"]


# This is what happens everytime the bot launches.
@discordBot.event
async def on_ready():
    print('Logged in as')
    print(discordBot.user.name)
    print(discordBot.user.id)

    for member in discordBot.get_all_members():
        Users[member.name] = dbInterface.History(member.name, member.id)
        Users[member.name].logMessage("ASDF")


@discordBot.event
async def on_message(message):
    if message.author == discordBot.user:
        return

    Users[message.author.name].logMessage(message.content)

    await discordBot.process_commands(message)


@discordBot.command()
async def ping(*args):
    await discordBot.say(":ping_pong: Pong!")


@discordBot.command()
async def pong(*args):
    await discordBot.say(":ping_pong: Ping!")


@discordBot.command(pass_context=True)
async def history(ctx, num):
    await discordBot.say(Users[ctx.message.author.name].getLastMessages(num))


discordBot.run(getToken())
