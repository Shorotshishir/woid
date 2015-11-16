# coding: utf-8

from unipath import Path
import sys
import os

PROJECT_DIR = Path(os.path.abspath(__file__)).parent.parent
sys.path.append(PROJECT_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'woid.settings')

import django
django.setup()


from twisted.internet import task
from twisted.internet import reactor

from woid.apps.services import crawlers


FIVE_MINUTES = 5 * 60
THIRTY_MINUTES = 30 * 60

def main_loop():
    crawlers.RedditCrawler().update_top_stories()
    crawlers.HackerNewsCrawler().update_top_stories()
    crawlers.MediumCrawler().update_top_stories()

def lazy_loop():
    #crawlers.GithubCrawler().update_top_stories()
    crawlers.NyTimesCrawler().update_top_stories()

def main():
    #main_loop_task = task.LoopingCall(main_loop)
    #main_loop_task.start(FIVE_MINUTES)

    main_loop_task = task.LoopingCall(lazy_loop)
    main_loop_task.start(THIRTY_MINUTES)

    reactor.run()


if __name__ == '__main__':
    main()
