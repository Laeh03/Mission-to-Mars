#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[5]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[ ]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[ ]:


slide_elem.find('div', class_='content_title')


# In[ ]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[ ]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[ ]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[ ]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[ ]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[ ]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[ ]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[ ]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[ ]:


df.to_html()


# In[ ]:


browser.quit()


# In[6]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[7]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
url_hemisphere = browser.html
bs = soup(url_hemisphere, "html.parser")

hemispheres = bs.find_all("div", class_="item")

# Loop through the list of all hemispheres information
for i in hemispheres:
    title = i.find("h3").text
    hemispheres_img = i.find("a", class_="itemLink product-item")["href"]

    # Visit the link that contains the full image website
    browser.visit(url + hemispheres_img)

    # HTML Object
    image_html = browser.html
    web_info = soup(image_html, "html.parser")

    # Create image url
    img_url = url + web_info.find("img", class_="wide-image")["src"]

    hemisphere_image_urls.append({"title" : title, "img_url" : img_url})


# In[8]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[9]:


# 5. Quit the browser
browser.quit()


# In[ ]:




