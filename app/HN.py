import requests

class HackerNews:
    def __init__(self):
        self.url = "https://hacker-news.firebaseio.com/v0/"

    def get_top(self):
        url = self.url + "topstories.json"
        return self.get_results(url)

    def get_latest(self):
        url = self.url + "newstories.json"
        return self.get_results(url)

    def get_best(self):
        url = self.url + "beststories.json"
        return self.get_results(url)
    
    def get_story(self, story_id):
        url = self.url +"item/{}.json".format(story_id)
        return self.get_results(url)
    def get_results(self, url):
        r = requests.get(url)
        return r.json()
