import discord
import emotes
from dotenv import dotenv_values

config = dotenv_values('.env')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

async def glorp_react(message, keyword, emote):
    if keyword in message.content.lower() and emote not in message.content:
        await message.add_reaction(emote)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


async def glorp_connections(message):
    # Replace squares from connections puzzle with glorp of same color
    tmp = message.author.mention + "'s\n" + message.content
    tmp = tmp.replace(emotes.GREEN_SQ, emotes.GLORP)
    tmp = tmp.replace(emotes.BLUE_SQ, emotes.BLORP)
    tmp = tmp.replace(emotes.YELLOW_SQ, emotes.YLORP)
    connections_result = tmp.replace(emotes.PURPLE_SQ, emotes.PLORP)
    await message.channel.send(connections_result)

    # Delete original message and ping the person who sent it
    await message.delete()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # React with glorp emojis
    await glorp_react(message, 'rlorp', emotes.RLORP)
    await glorp_react(message, 'olorp', emotes.OLORP)
    await glorp_react(message, 'ylorp', emotes.YLORP)
    await glorp_react(message, 'glorp', emotes.GLORP)
    await glorp_react(message, 'blorp', emotes.BLORP)
    await glorp_react(message, 'plorp', emotes.PLORP)

    # Replace Connections scores with glorp equivalent
    if message.content.startswith("Connections\nPuzzle #"):
        await glorp_connections(message)

client.run(config.get('TOKEN'))