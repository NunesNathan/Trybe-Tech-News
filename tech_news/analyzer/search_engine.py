from tech_news.database import search_news


def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news = search_news(query)
    results = [(new["title"], new["url"]) for new in news]

    return results


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_tag(tag):
    query = {"tags": {"$regex": tag, "$options": "i"}}
    news = search_news(query)
    results = [(new["title"], new["url"]) for new in news]

    return results


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}
    news = search_news(query)
    results = [(new["title"], new["url"]) for new in news]

    return results
