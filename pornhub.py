import discord
import asyncio
import time
import os
from discord.utils import get
from discord.voice_client import VoiceClient
from discord.ext import commands, tasks

client = commands.Bot(command_prefix='porn!')

players = {}

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('with them balls like its fifa'))
    print ('online')

@client.event
async def on_command_error(message, error):
    await message.send(error)

@client.command()
async def ping(ctx):
    await ctx.author.send(f'Pong! {round(client.latency * 100)}ms')