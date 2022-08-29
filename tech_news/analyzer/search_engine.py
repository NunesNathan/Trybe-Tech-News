from datetime import datetime
from tech_news.database import search_news


def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news = search_news(query)
    results = [(new["title"], new["url"]) for new in news]

    return results


def search_by_date(date):
    try:
        query = {"timestamp": {"$regex": datetime.strftime(
            datetime.strptime(date, "%Y-%m-%d"), "%d/%m/%Y"), "$options": "i"}}

        news = search_news(query)
        results = [(new["title"], new["url"]) for new in news]
    except ValueError:
        raise ValueError("Data inválida")

    return results


def search_by_tag(tag):
    query = {"tags": {"$regex": tag, "$options": "i"}}
    news = search_news(query)
    results = [(new["title"], new["url"]) for new in news]

    return results


def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}
    news = search_news(query)
    results = [(new["title"], new["url"]) for new in news]

    return results
