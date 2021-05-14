# Eurovision-Youtube-Views
First things first. I really like Eurovision Song Contest. And durings the months leading up to May, it's always really exciting to listen to all the competing songs as they are released. The songs are published on Eurovision's Youtube channel, and I like to keep track of how many views each song get. So I decided to make a little script.

## Guide
1. Install the following python modules:
- Selenium
- BeautifulSoup
- Pandas
- Progress
2. You need a chromedriver in order to run Selenium. See: https://chromedriver.chromium.org/downloads
3. Run `python load_data.py` to scrape the songs into "songs.csv"
4. Run `python visualize.py` to see the leaderboard!

## TODO:
- Add data for likes/dislikes
