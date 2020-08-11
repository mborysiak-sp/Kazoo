import os

import googleapiclient.discovery
import googleapiclient.errors

from result import Result


class YoutubeHandler:
    """Class for handling youtube api requests"""
    def __init__(self):
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        token = open("api_token.txt", "r").read()

        self.youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=token
        )

    def get_videos(self, query):
        """
        Method for getting a list of Result objects storing video data
        :param query: String containing query for searched videos
        :return: list of Result objects
        """
        request = self.youtube.search().list(
            part="snippet",
            maxResults=2,
            q=query
        )
        response = request.execute()

        results = []

        for item in response["items"]:
            results.append(Result(item))

        return results
