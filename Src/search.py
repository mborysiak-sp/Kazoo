from youtube_search import YoutubeSearch


def search(query):
    print(YoutubeSearch(query, max_results=5).to_dict())
