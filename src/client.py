from discord.ext.commands import Bot
from utils import get_token
from api.handler import YoutubeHandler


BOT_PREFIX = "["
TOKEN = get_token("token.txt")

client = Bot(command_prefix=BOT_PREFIX)


@client.event
async def on_ready():
    print("Logged as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(client.command_prefix + "p"):
        youtube_handler = YoutubeHandler()
        result = ""
        for video in youtube_handler.get_videos(message.content):
            result = result + str(video)
        await message.channel.send(result)


client.run(TOKEN)
