from discord.ext.commands import Bot
from .utils import set_token

BOT_PREFIX = ("[", "]")
TOKEN = set_token()

client = Bot(command_prefix=BOT_PREFIX)


@client.event
async def on_ready():
    print("Logged as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(":p"):
        msg = "Hello {0.author.mention}".format(message)
        await message.channel.send(msg)


client.run(TOKEN)
