{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "b538e68a",
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as bs\n",
    "import time\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ca755513",
   "metadata": {},
   "source": [
    "### NASA Mars News"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "bc1e93b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_info():\n",
    "    # Set up Splinter\n",
    "    executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "    browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "    # Visit https://redplanetscience.com/\n",
    "    url = \"https://redplanetscience.com/\"\n",
    "    browser.visit(url)\n",
    "\n",
    "    time.sleep(1)\n",
    "\n",
    "    # Scrape page into Soup\n",
    "    html = browser.html\n",
    "    soup = bs(html, \"html.parser\")\n",
    "\n",
    "    # Get the first content title\n",
    "    content_title_all = soup.find('div', class_=\"content_title\")\n",
    "\n",
    "    # Get the text part of the content title\n",
    "    news_title  = content_title_all.text\n",
    "    \n",
    "    # Get the first content description\n",
    "    paragraph_all = soup.find('div', class_=\"article_teaser_body\")\n",
    "\n",
    "    # Get the text part of the content description\n",
    "    news_p  = paragraph_all.text\n",
    "\n",
    "\n",
    "    # Store data in a dictionary\n",
    "    latest_news_data = {\"news_title\": news_title,\"news_briefing\": news_p}\n",
    "\n",
    "    # Close the browser after scraping\n",
    "    browser.quit()\n",
    "\n",
    "    # Return results\n",
    "    return latest_news_data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bbd75fc9",
   "metadata": {},
   "source": [
    "### JPL Mars Space Images - Featured Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "745e982f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_info_2():\n",
    "    # Set up Splinter\n",
    "    executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "    browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "    # Visit https://spaceimages-mars.com/\n",
    "    url = \"https://spaceimages-mars.com/\"\n",
    "    browser.visit(url)\n",
    "\n",
    "    time.sleep(1)\n",
    "\n",
    "    # Scrape page into Soup\n",
    "    html = browser.html\n",
    "    soup = bs(html, \"html.parser\")\n",
    "\n",
    "    # Find the image link to the Featured Mars Image\n",
    "    relative_image_path = soup.find_all('img')[1][\"src\"]\n",
    "    featured_image_url = url + relative_image_path\n",
    "\n",
    "    # Close the browser after scraping\n",
    "    browser.quit()\n",
    "\n",
    "    # Return results\n",
    "    return featured_image_url\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "74a7a1a8",
   "metadata": {},
   "source": [
    "### Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "a565503c",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://galaxyfacts-mars.com/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "5ca61631",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[                         0                1                2\n",
       " 0  Mars - Earth Comparison             Mars            Earth\n",
       " 1                Diameter:         6,779 km        12,742 km\n",
       " 2                    Mass:  6.39 ?? 10^23 kg  5.97 ?? 10^24 kg\n",
       " 3                   Moons:                2                1\n",
       " 4       Distance from Sun:   227,943,824 km   149,598,262 km\n",
       " 5          Length of Year:   687 Earth days      365.24 days\n",
       " 6             Temperature:     -87 to -5 ??C      -88 to 58??C,\n",
       "                       0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 ?? 10^23 kg (0.11 Earths)\n",
       " 3                Moons:          2 ( Phobos & Deimos )\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 ??C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers]"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tables = pd.read_html(url)\n",
    "tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "a5612012",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(tables)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "c79943f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mars - Earth Comparison</td>\n",
       "      <td>Mars</td>\n",
       "      <td>Earth</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Diameter:</td>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 ?? 10^23 kg</td>\n",
       "      <td>5.97 ?? 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Distance from Sun:</td>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Length of Year:</td>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Temperature:</td>\n",
       "      <td>-87 to -5 ??C</td>\n",
       "      <td>-88 to 58??C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                         0                1                2\n",
       "0  Mars - Earth Comparison             Mars            Earth\n",
       "1                Diameter:         6,779 km        12,742 km\n",
       "2                    Mass:  6.39 ?? 10^23 kg  5.97 ?? 10^24 kg\n",
       "3                   Moons:                2                1\n",
       "4       Distance from Sun:   227,943,824 km   149,598,262 km\n",
       "5          Length of Year:   687 Earth days      365.24 days\n",
       "6             Temperature:     -87 to -5 ??C      -88 to 58??C"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = tables[0]\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "7303335a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars - Earth Comparison</th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Diameter:</td>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 ?? 10^23 kg</td>\n",
       "      <td>5.97 ?? 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Distance from Sun:</td>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Length of Year:</td>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Temperature:</td>\n",
       "      <td>-87 to -5 ??C</td>\n",
       "      <td>-88 to 58??C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "0 Mars - Earth Comparison             Mars            Earth\n",
       "1               Diameter:         6,779 km        12,742 km\n",
       "2                   Mass:  6.39 ?? 10^23 kg  5.97 ?? 10^24 kg\n",
       "3                  Moons:                2                1\n",
       "4      Distance from Sun:   227,943,824 km   149,598,262 km\n",
       "5         Length of Year:   687 Earth days      365.24 days\n",
       "6            Temperature:     -87 to -5 ??C      -88 to 58??C"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df, df.columns = df[1:] , df.iloc[0]\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "6516d2cf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mars - Earth Comparison</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Diameter:</th>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 ?? 10^23 kg</td>\n",
       "      <td>5.97 ?? 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Distance from Sun:</th>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Length of Year:</th>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Temperature:</th>\n",
       "      <td>-87 to -5 ??C</td>\n",
       "      <td>-88 to 58??C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "0                                   Mars            Earth\n",
       "Mars - Earth Comparison                                  \n",
       "Diameter:                       6,779 km        12,742 km\n",
       "Mass:                    6.39 ?? 10^23 kg  5.97 ?? 10^24 kg\n",
       "Moons:                                 2                1\n",
       "Distance from Sun:        227,943,824 km   149,598,262 km\n",
       "Length of Year:           687 Earth days      365.24 days\n",
       "Temperature:                -87 to -5 ??C      -88 to 58??C"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = df.set_index(keys = \"Mars - Earth Comparison\")\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "c5d904e8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>Mars</th>\\n      <th>Earth</th>\\n    </tr>\\n    <tr>\\n      <th>Mars - Earth Comparison</th>\\n      <th></th>\\n      <th></th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>Diameter:</th>\\n      <td>6,779 km</td>\\n      <td>12,742 km</td>\\n    </tr>\\n    <tr>\\n      <th>Mass:</th>\\n      <td>6.39 ?? 10^23 kg</td>\\n      <td>5.97 ?? 10^24 kg</td>\\n    </tr>\\n    <tr>\\n      <th>Moons:</th>\\n      <td>2</td>\\n      <td>1</td>\\n    </tr>\\n    <tr>\\n      <th>Distance from Sun:</th>\\n      <td>227,943,824 km</td>\\n      <td>149,598,262 km</td>\\n    </tr>\\n    <tr>\\n      <th>Length of Year:</th>\\n      <td>687 Earth days</td>\\n      <td>365.24 days</td>\\n    </tr>\\n    <tr>\\n      <th>Temperature:</th>\\n      <td>-87 to -5 ??C</td>\\n      <td>-88 to 58??C</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "html_table = df.to_html()\n",
    "html_table"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "442c28f0",
   "metadata": {},
   "source": [
    "### Mars Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "c7a59826",
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_info_3():\n",
    "    # Set up Splinter\n",
    "    executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "    browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "    # Visit https://marshemispheres.com/\n",
    "    url_main = \"https://marshemispheres.com/\"\n",
    "    #browser.visit(url)\n",
    "\n",
    "    #time.sleep(1)\n",
    "\n",
    "    #Obtain Cerberus Hemisphere Enhanced image and title\n",
    "    url_cerberus = \"https://marshemispheres.com/cerberus.html\"\n",
    "    browser.visit(url_cerberus)\n",
    "    \n",
    "    time.sleep(1)\n",
    "    \n",
    "    # Scrape page into Soup\n",
    "    html = browser.html\n",
    "    soup = bs(html, \"html.parser\")\n",
    "    \n",
    "    # BONUS: Find the src for the sloth image\n",
    "    relative_image_path = soup.find_all('img')[4][\"src\"]\n",
    "    cerberus_img = url_main + str(relative_image_path)\n",
    "    \n",
    "    browser.quit()\n",
    "    \n",
    "    \n",
    "    executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "    browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "    #Obtain Schiaparelli Hemisphere Enhanced image and title\n",
    "    url_schiaparelli = \"https://marshemispheres.com/schiaparelli.html\"\n",
    "    browser.visit(url_schiaparelli)\n",
    "\n",
    "    time.sleep(1)\n",
    "\n",
    "    # Scrape page into Soup\n",
    "    html = browser.html\n",
    "    soup = bs(html, \"html.parser\")\n",
    "\n",
    "    # BONUS: Find the src for the sloth image\n",
    "    relative_image_path = soup.find_all('img')[4][\"src\"]\n",
    "    schiaparelli_img = url_main + str(relative_image_path)\n",
    "    \n",
    "\n",
    "    browser.quit()\n",
    "    \n",
    "    \n",
    "    executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "    browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "    #Obtain Syrtis Major Hemisphere Enhanced image and title\n",
    "    url_syrtis = \"https://marshemispheres.com/syrtis.html\"\n",
    "    browser.visit(url_syrtis)\n",
    "\n",
    "    time.sleep(1)\n",
    "\n",
    "    # Scrape page into Soup\n",
    "    html = browser.html\n",
    "    soup = bs(html, \"html.parser\")\n",
    "\n",
    "    # BONUS: Find the src for the sloth image\n",
    "    relative_image_path = soup.find_all('img')[4][\"src\"]\n",
    "    syrtis_img = url_main + str(relative_image_path)\n",
    "    \n",
    "\n",
    "    browser.quit()\n",
    "    \n",
    "     \n",
    "    executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "    browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "    #Obtain Valles Marineris Hemisphere Enhanced image and title\n",
    "    url_valles = \"https://marshemispheres.com/valles.html\"\n",
    "    browser.visit(url_valles)\n",
    "\n",
    "    time.sleep(1)\n",
    "\n",
    "    # Scrape page into Soup\n",
    "    html = browser.html\n",
    "    soup = bs(html, \"html.parser\")\n",
    "\n",
    "    # BONUS: Find the src for the sloth image\n",
    "    relative_image_path = soup.find_all('img')[4][\"src\"]\n",
    "    valles_img = url_main + str(relative_image_path)\n",
    "    \n",
    "\n",
    "    browser.quit()\n",
    "   \n",
    "    # Store data in a dictionary\n",
    "    hemisphere_image_urls = [{\"title\": \"Cerberus Hemisphere\",\"img_url\": cerberus_img},\n",
    "                             {\"title\": \"Schiaparelli Hemisphere\" ,\"img_url\": schiaparelli_img },\n",
    "                             {\"title\": \"Syrtis Major Hemisphere\" ,\"img_url\": syrtis_img},\n",
    "                             {\"title\": \"Valles Marineris Hemisphere\",\"img_url\": valles_img }]\n",
    "\n",
    "    # Return results\n",
    "    return hemisphere_image_urls\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
