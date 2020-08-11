from discord.ext.commands import Bot
from utils import set_token
from api.handler import YoutubeHandler


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

    if message.content.startswith("p"):
        youtube_handler = YoutubeHandler()
        videos = youtube_handler.get_videos(message)
        await message.channel.send(videos)


client.run(TOKEN)
