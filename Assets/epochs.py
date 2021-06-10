from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import urllib.request as req

URL = "https://www.google.com/search?q=bottles&sxsrf=ALeKk01KaArfjt74c70pOCMGcfHRk-VPYw:1623328321788&source=lnms&tbm=isch&sa=X&ved=2ahUKEwja8eSfiY3xAhUOzjgGHRngCLIQ_AUoAXoECAEQAw"

# Install the newest version of the chrome driver
browser = webdriver.Chrome(ChromeDriverManager().install())

# Defining the automation page
browser.get(URL)


# Making a quick log function
def log(log):
    print(f"(basic): {log}")


# Making a special log function
def executing(log):
    print(f"(executing): {log}")


# Seperating the image retrieving code from the rest of epoch.py
def getImages(startpoint):
    for x in range(2):
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)

    images = browser.find_elements_by_tag_name("img")
    imagesBySource = []
    constImages = []

    executing("time.sleep(3)")
    log(len(images))
    time.sleep(3)

    for x in range(startpoint, len(images)):
        imageSrc = images[x].get_attribute("src")
        imagesBySource.append(imageSrc)

    for x in range(len(imagesBySource)):
        if imagesBySource[x] != None:
            constImages.append(imagesBySource[x])

    for x in range(len(constImages)):
        req.urlretrieve(constImages[x], f"main/main{x}.png")


getImages(50)
