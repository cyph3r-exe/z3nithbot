import discord

BOT_TOKEN = ""  # Replace with your actual bot token, but be aware of the security risks

intents = discord.Intents.default()  # Use default intents for now
intents.members = True
# Create a Discord client instance
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')

@client.event
async def on_message(message):
    if message.author == client.user:  # Ignore messages from the bot itself
        return

    if message.content.lower() == '?hello':
        await message.channel.send('Hi!')

# Run the bot using the token
client.run(BOT_TOKEN)
