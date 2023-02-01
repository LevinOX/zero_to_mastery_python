import requests
from bs4 import BeautifulSoup
import pprint


# print(soup.body)
# soup.body.contents
# soup.find_all('search_string')
# soup.find('search_string')
# soup.a   <- catches the a-tag
# print(soup.find(id='text'))
# .titleline instead of .storylink
# print(soup.select('.score'))
# print(soup.select('#score_34565202'))

# print(links[0], votes[0])
# print(votes[0].get('id'))


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 100:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


def hn_xpages():
    hn_list = []
    ress = [requests.get('https://news.ycombinator.com/news'),
            requests.get('https://news.ycombinator.com/news?p=2')]
    for res in ress:
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.titleline > a')
        subtext = soup.select('.subtext')
        hn_list += create_custom_hn(links, subtext)

    return hn_list


pprint.pprint(hn_xpages())
