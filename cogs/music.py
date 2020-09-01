import youtube_dl
import googleapiclient.discovery
import googleapiclient.errors

from os import environ
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.utils import get



class Result:

    def __init__(self, yt_item):
        self.id = yt_item["id"]["videoId"]
        self.title = yt_item["snippet"]["title"]
        self.url = self.get_url(self.id)

    def __str__(self):
        return f"ID: {self.id} Title: {self.title} URL: {self.url}\n"

    def get_url(self, id):
        return "https://www.youtube.com/watch?v=" + id


class YoutubeHandler:
    """Class for handling youtube youtube requests"""

    def __init__(self):
        environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        token = environ.get("YOUTUBE_TOKEN")

        self.youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=token
        )

    def get_videos(self, query, count):
        """
        Method for getting a list of Result objects storing video data
        :param query: String containing query for searched videos
        :param count: Count of requested videos
        :return: list of Result objects
        """
        request = self.youtube.search().list(
            part="snippet",
            maxResults=count,
            q=query
        )
        response = request.execute()

        results = []

        for item in response["items"]:
            results.append(Result(item))
            print(item)

        return results

    def get_download_link(self, url):
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            r = ydl.extract_info(url, download=False)
            return r['formats'][-1]['url']


class Music(commands.Cog, name="Music"):
    def __init__(self, client):
        self.client = client
        self.ctx = {}
        self.youtube_handler = YoutubeHandler()

    @commands.command(aliases=['p'])
    async def play(self, ctx):
        channel = ctx.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        url = str(ctx.message.content).split(" ")[1]

        if not voice.is_playing():
            voice.play(FFmpegPCMAudio(executable="C:\\ffmpeg.exe", source=self.youtube_handler.get_download_link(url)))


def setup(client):
    client.add_cog(Music(client))
