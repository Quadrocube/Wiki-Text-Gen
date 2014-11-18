# Get links
from init import setup
import requests as req
from bs4 import BeautifulSoup
from urllib import parse
from urllib.parse import urljoin
import pickle
import sys


def is_in_domain(url, domain):
    return (parse.urlsplit(url).netloc.startswith(domain)
            or parse.urlsplit(url).netloc == '')


def is_valid_scheme(url):
    return (parse.urlsplit(url).scheme == 'http'
            or parse.urlsplit(url).scheme == '')


def is_article(url):
    return (parse.urlsplit(url).fragment == ''
            and parse.urlsplit(url).query == ''
            and ':' not in url)


def bust_new_links(html):
    soup = BeautifulSoup(html)
    links = [urljoin("http://" + domain, new_url) for new_url
             in map(lambda x: x['href'], soup.findAll('a', href=True))
             if is_in_domain(new_url, domain)
             and is_valid_scheme(new_url)
             and is_article(new_url)]
    return links


def crawl(url, link_count):
    visited_links = set()
    link_queue = [url]
    while link_queue and len(visited_links) < link_count:
        link = link_queue.pop(0)
        if (link in visited_links):
            continue
        page = req.get(link)
        if not page.ok:
            continue
        visited_links.add(link)
        for new_link in bust_new_links(req.get(link).text):
            link_queue.append(new_link)
    return visited_links

if __name__ == '__main__':
    link_count = int(sys.argv[1])
    domain = sys.argv[2]
    _, _, links_dir = setup(domain)
    result = crawl("http://" + domain, link_count)
    with open(links_dir + domain + '.p', 'wb') as f:
        pickle.dump(result, f)

    print(len(result))
