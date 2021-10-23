from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# ### NASA Mars News

def scrape():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit https://redplanetscience.com/
    url = "https://redplanetscience.com/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the first content title
    content_title_all = soup.find('div', class_="content_title")

    # Get the text part of the content title
    news_title  = content_title_all.text
    
    # Get the first content description
    paragraph_all = soup.find('div', class_="article_teaser_body")

    # Get the text part of the content description
    news_p  = paragraph_all.text
    
    # Close the browser after scraping
    browser.quit()




# ### JPL Mars Space Images - Featured Image


    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit https://spaceimages-mars.com/
    url = "https://spaceimages-mars.com/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Find the image link to the Featured Mars Image
    relative_image_path = soup.find_all('img')[1]["src"]
    featured_image_url = url + relative_image_path

    # Close the browser after scraping
    browser.quit()





# ### Mars Facts

    url = 'https://galaxyfacts-mars.com/'

    tables = pd.read_html(url)
    tables

    df = tables[0]
    df

    df, df.columns = df[1:] , df.iloc[0]
    df

    df = df.set_index(keys = "Mars - Earth Comparison")
    df

    html_table = df.to_html()

    html_table = html_table.replace('\n', '')




# ### Mars Hemispheres

    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit https://marshemispheres.com/
    url_main = "https://marshemispheres.com/"
    #browser.visit(url)

    #time.sleep(1)

    #Obtain Cerberus Hemisphere Enhanced image and title
    url_cerberus = "https://marshemispheres.com/cerberus.html"
    browser.visit(url_cerberus)
    
    time.sleep(1)
    
    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    
    # BONUS: Find the src for the sloth image
    relative_image_path = soup.find_all('img')[4]["src"]
    cerberus_img = url_main + str(relative_image_path)
    
    browser.quit()
    
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #Obtain Schiaparelli Hemisphere Enhanced image and title
    url_schiaparelli = "https://marshemispheres.com/schiaparelli.html"
    browser.visit(url_schiaparelli)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # BONUS: Find the src for the sloth image
    relative_image_path = soup.find_all('img')[4]["src"]
    schiaparelli_img = url_main + str(relative_image_path)
    

    browser.quit()
    
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #Obtain Syrtis Major Hemisphere Enhanced image and title
    url_syrtis = "https://marshemispheres.com/syrtis.html"
    browser.visit(url_syrtis)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # BONUS: Find the src for the sloth image
    relative_image_path = soup.find_all('img')[4]["src"]
    syrtis_img = url_main + str(relative_image_path)
    

    browser.quit()
    
     
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #Obtain Valles Marineris Hemisphere Enhanced image and title
    url_valles = "https://marshemispheres.com/valles.html"
    browser.visit(url_valles)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # BONUS: Find the src for the sloth image
    relative_image_path = soup.find_all('img')[4]["src"]
    valles_img = url_main + str(relative_image_path)
    

    browser.quit()
   
    # Store data in a dictionary
    hemisphere_image_urls = [{"title": "Cerberus Hemisphere","img_url": cerberus_img},
                             {"title": "Schiaparelli Hemisphere" ,"img_url": schiaparelli_img },
                             {"title": "Syrtis Major Hemisphere" ,"img_url": syrtis_img},
                             {"title": "Valles Marineris Hemisphere","img_url": valles_img }]

    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "html_table": html_table,
        "cerberus_img": cerberus_img,
        "schiaparelli_img": schiaparelli_img,
        "syrtis_img": syrtis_img,
        "valles_img": valles_img}

    return mars_data



