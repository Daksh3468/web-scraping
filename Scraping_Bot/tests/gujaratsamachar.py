# This file is meant to instantiate the site class
from sites.gujaratsamachar import GujaratSamachar 

def run_gujaratsamachar():
  with GujaratSamachar(keeprunning=False) as bot:
      bot.landing_page()
      bot.news_title()
      bot.img()
      bot.date_and_time()
      data=bot.article()
      return data
      