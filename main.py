import os
from re import A
import discord
from discord.ext import tasks, commands

import connection

# client = discord.Client()
bot = commands.Bot(command_prefix='!')
con = connection.instance(id='i-074936a74ded7d00c')

# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

async def send_cmd_help(ctx):
    cmd = ctx.command
    em = discord.Embed(title=f'Usage: {ctx.prefix}{cmd} {cmd.signature} ')
    em.color = discord.Color.blue()
    em.description = cmd.help
    return em

@tasks.loop(minutes=5.0)
def task(self):
    return

@bot.event
async def on_command_error(ctx, err):
    
    if isinstance(err, commands.CommandNotFound):
        pass
    elif isinstance(err, commands.MissingRequiredArgument):
        _help = await send_cmd_help(ctx)
        await ctx.send(embed=_help)
    else:
        print(err.__traceback__)

@bot.command()
async def echo(ctx, *, args):
    await ctx.send(args)

@bot.command()
async def ping(ctx):
    await ctx.send(con.describe_instance())

@bot.command()
async def start(ctx):
    res = con.start_instance()
    await ctx.send(res)

@bot.command()
async def stop(ctx):
    await ctx.send(con.stop_instance())

# client.run(os.getenv('HELIOS_BOT'))
bot.run(os.getenv('HELIOS_BOT'))