import datetime as dt

def scrape_all():

    news_title = 'Testing'
    news_paragraph = 'Testing'
    featured_image = 'https://linktoimage.png'
    mars_facts = 'Testing'
    news_title = 'Testing'
    hemispheres_list_of_dicts = [
        {"title": "Title of Hemisphere Image",
        "img_url": 'https://linktoimage.png'},

        {"title": "Title of Hemisphere Image",
        "img_url": 'https://linktoimage.png'},

        {"title": "Title of Hemisphere Image",
        "img_url": 'https://linktoimage.png'},
        
        {"title": "Title of Hemisphere Image",
        "img_url": 'https://linktoimage.png'},
    ]

    scraped_data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image,
        "facts": mars_facts,
        "hemispheres": hemispheres_list_of_dicts,
        "last_modified": dt.datetime.now()
    }

    return scraped_data