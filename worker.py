import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='?', intents=intents)

#Rules

rules = """
General Rules
1 Use of any inappropriate / irrelevant nicknames is strictly prohibited.
2 Use of any offensive profile picture is not permitted.
3 Selling any Hacks, Glitches or Bugs is strictly forbidden on the server.
4 Do not exploit any loopholes that you manage to discover in the server; Report them.
5 Moderators reserve the right to use their own discretion regardless of any rule.
6 These rules apply to DMs you send to members of this server.
7 Use of @everyone / @here tag is only for server staff.
8 Do not tag any fellow member of the server unnecessarily.
9 Sending any sort of NSFW explicit content is strictly prohibited
10 Acts of Groupism, Racism, Harassment or Hate Speech against any fellow member will not be tolerated.
11 Spamming / Excessive Tagging / Vertical Chatting is strictly prohibited on the server.
12 Any sort of advertisements is strictly prohibited in the server or in DMs of any member
13 Avoid interfering in matters which do not directly affect or involve you.
14 Avoid any religious / political / sexual discussions that may lead to heated arguments and/or hurt someone's beliefs and sentiments.
15 Use of any offensive language against any fellow member is not permitted
16 Moderators reserve the right to delete any post.
 
Voice Rules
1 No voice chat channel hopping.
2 No annoying, loud or high pitch noises.
3 Reduce the amount of background noise, if possible.
4 Moderators reserve the right to disconnect, mute, deafen, or move members to and from voice channels.

"""

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def hello(ctx):
    print('working')
    return await ctx.send('Hi')  


#Enter Bot token Here.
bot.run('')