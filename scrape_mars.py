import datetime as dt
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
def scrape_all():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False) 
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    html = browser.html
    news_soup = soup(html, 'html.parser')

    slide_elem = news_soup.select_one('div.list_text')

    news_title = slide_elem.find('div', class_='content_title').get_text()

    news_paragraph = slide_elem.find('div', class_='article_teaser_body').get_text()

    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    html = browser.html
    img_soup = soup(html, 'html.parser')

    img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    featured_image = f'https://spaceimages-mars.com/{img_url_rel}'

    df = pd.read_html('https://galaxyfacts-mars.com')[0]

    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    mars_facts = df.to_html()

    # url = 'https://marshemispheres.com/'

    # browser.visit(url)

    # hemispheres_list_of_dicts = []

    # links = browser.find_by_css("a.product-item.img")


    # for i in range(len(links)):
    #     hemisphere = {}

    #     browser.find_by_css("a.product-item.img")[i].click()

    #     sample_elem = browser.links.find_by_text("Sample").first
    #     hemisphere["img_url"] = sample_elem["href"]
    #     hemisphere["title"] = browser.find_by_css("h2.title").text
    #     hemispheres_list_of_dicts.append(hemisphere)

    #     browser.back()


    hemispheres_list_of_dicts = [
        {"title": "Title of Hemisphere Image",
        "img_url": 'https://mediaproxy.salon.com/width/1200/https://media.salon.com/2021/01/life-on-mars-growing-0129211.jpg'},

        {"title": "Title of Hemisphere Image",
        "img_url": 'https://mediaproxy.salon.com/width/1200/https://media.salon.com/2021/01/life-on-mars-growing-0129211.jpg'},

        {"title": "Title of Hemisphere Image",
        "img_url": 'https://mediaproxy.salon.com/width/1200/https://media.salon.com/2021/01/life-on-mars-growing-0129211.jpg'},
        
        {"title": "Title of Hemisphere Image",
        "img_url": 'https://mediaproxy.salon.com/width/1200/https://media.salon.com/2021/01/life-on-mars-growing-0129211.jpg'},
    ]

    browser.quit()
    scraped_data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image,
        "facts": mars_facts,
        "hemispheres": hemispheres_list_of_dicts,
        "last_modified": dt.datetime.now()
    }

    return scraped_data