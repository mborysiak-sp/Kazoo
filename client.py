from discord.ext.commands import Bot
from os import environ

import settings


BOT_PREFIX = ";"
client = Bot(command_prefix=BOT_PREFIX)
extensions = ["cogs.music"]

if __name__ == "__main__":
    for extension in extensions:
        client.load_extension(extension)


@client.event
async def on_ready():
    print("Logged as {0.user}".format(client))


@client.command(hidden=True)
async def reload(ctx, extension):
    client.reload_extension(extension)


client.run(environ.get("DISCORD_TOKEN"), bot=True, reconnect=True)
