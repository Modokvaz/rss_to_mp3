import feedparser
import requests
import os
from deep_translator import GoogleTranslator
from gtts import gTTS
from bs4 import BeautifulSoup

russian_text = ''

# set the URL of the RSS feed
rss_url = 'https://www.techtarget.com/searchnetworking/rss/Network-security-news-advice-and-technical-information.xml'

# retrieve the RSS feed
feed = feedparser.parse(rss_url)

# loop through each item in the feed
for item in feed['items']:
    # retrieve the URL of the news article
    news_url = item['link']

    # retrieve the HTML content of the news article
    response = requests.get(news_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # retrieve the first 5 lines of the news article
    lines = soup.find_all('p')[:5]
    content = ''
    for line in lines:
        content += line.get_text() + '\n'

    # news in english
    print('Link:', item['link'])

    # translate to russian
    translated = GoogleTranslator(source='auto', target='ru').translate(content)
    russian_text += (translated + '\n' + 'Следующая новость\n')
    print(translated)
    print()

# convert text to mp3, play mp3 file
language = 'ru'
output = gTTS(text = russian_text, lang=language, slow=False)
output.save("output.mp3")
os.system("start output.mp3")

