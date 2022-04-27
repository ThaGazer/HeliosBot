import os
import discord
from discord.ext import commands
import boto3

# client = discord.Client()
bot = commands.Bot(command_prefix='$')

# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

@bot.command()
async def test(ctx, *, args):
    await ctx.send(args)

# client.run(os.getenv('KEVIN_BOT'))
bot.run(os.getenv('KEVIN_BOT'))