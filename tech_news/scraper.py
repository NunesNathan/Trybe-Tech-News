import time
import requests
from parsel import Selector

from tech_news.database import create_news


def fetch(url):
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3)
        time.sleep(1)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css("a.cs-overlay-link::attr(href)").getall()


def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css(".next::attr(href)").get()


def scrape_noticia(html_content):
    selector = Selector(html_content)
    return {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".author a::text").get(),
        "comments_count": len(selector.css("#comments").getall()),
        "summary": "".join(
            selector.css(".entry-content > p:nth-of-type(1) *::text").getall()
        ).strip(),
        "tags": selector.css(".post-tags a::text").getall(),
        "category": selector.css("div.meta-category .label::text").get()
    }


def get_tech_news(amount):
    BASE_URL = "https://blog.betrybe.com"
    news = []

    while len(news) < amount:
        content = fetch(BASE_URL)
        links = scrape_novidades(content)

        for i in range(min(amount - len(news), len(links))):
            news.append(scrape_noticia(fetch(links[i])))

        BASE_URL = scrape_next_page_link(content)

    create_news(news)
    return news
