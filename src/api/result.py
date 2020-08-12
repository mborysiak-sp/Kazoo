
class Result:

    def __init__(self, yt_item):
        self.id = yt_item["id"]["videoId"]
        self.title = yt_item["snippet"]["title"]
        self.url = self.get_url(self.id)

    def __str__(self):
        return f"ID: {self.id} Title: {self.title} URL: {self.url}\n"

    def get_url(self, id):
        return "https://www.youtube.com/watch?v=" + id
