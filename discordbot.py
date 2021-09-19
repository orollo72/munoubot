from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def 暇(ctx):
    await ctx.send('暇ならゲームしろ')
    
    
token = getenv('DISCORD_BOT_TOKEN')
bot.run(ODg5MDU0Nzg2MzYyNjc1MjQy.YUbqyg.1j7xjV5JUeAoBboKc0-BQbQP-Y0)
