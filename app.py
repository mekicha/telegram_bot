import os
from HN import HackerNews
from Database import Database
import time 

basedir = os.path.abspath(os.path.dirname(__file__))
DB =  os.path.join(basedir, 'botdb.db')

db = Database(DB)
hn = HackerNews()

def main():
    tops = hn.get_top()[:10]
    latest = hn.get_latest()[:10]
    best = hn.get_best()[:10]
    save_stories(tops, "top")
    save_stories(latest, "latest")
    save_stories(best, "best")

def save_stories(stories_array, category):
    for story_item in stories_array:
        story = hn.get_story(story_item)
        db_story_id = db.select_story_id(story_item)
        if db_story_id is not None and db_story_id[0] == story_item:
            continue
        id = story["id"]
        url = story["url"]
        title = story["title"]
        types = story["type"]
        category = category
        story_tp = (id, title, types, url, category)
        db.insert_news(story_tp)
 

if __name__ == "__main__":
    main()
