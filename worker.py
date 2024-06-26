import discord
from discord.ext import commands
from secrets import BOT_TOKEN  # Import BOT_TOKEN from secrets.py

# Create a bot instance with command prefix '?'
bot = commands.Bot(command_prefix='?')

# Event listener for when the bot has connected to the server
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command listener for the '?hello' command
@bot.command()
async def hello(ctx):
    await ctx.send('Hi')  # Sends a message to the channel where the command was issued

# Use the BOT_TOKEN from the secrets file
bot.run(BOT_TOKEN)