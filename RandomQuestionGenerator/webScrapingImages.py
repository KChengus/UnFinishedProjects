from selenium import webdriver
import requests
import io
from selenium.webdriver.common.by import By
from PIL import Image
from time import sleep
import os

# change path to where your chromedriver is
PATH = "/Users/kevincheng/Documents/Programming/RandomThings/chromedriver"
#PATH = "D:\\Downloads\\random\\chromedriver.exe"
sleepTimeShort = 0.2
sleepTimeLong = 1


googleUrl = "https://www.google.com/search?q="
googleImagesUrlSuffix = "&tbm=isch"

imagesMaxAmount = 5

def googleToImages(search, wDriver):
    wDriver.get(googleUrl + search + googleImagesUrlSuffix)
    sleep(sleepTimeLong)

def getImageFromGoogle(imageMaxAmount, photosAmountFromBefore, wDriver):
    images_url = set()
    thumpnails = wDriver.find_elements(By.CLASS_NAME, "Q4LuWd")[photosAmountFromBefore:]
    skipImagesAmount = 0
    for thumpnail in thumpnails:
        try:
            thumpnail.click()
            sleep(sleepTimeShort)
        except Exception as e:
            skipImagesAmount+=1
            print(e)
            continue
        images = wDriver.find_elements(By.CLASS_NAME, "n3VNCb")
        for image in images:
            if (image.get_attribute("src") and image.get_attribute("src").startswith("http")):
                images_url.add(image.get_attribute("src"))
                break
        if len(images_url) >= imageMaxAmount:
            break
    return images_url, skipImagesAmount


def download_image(download_path, url, file_name):
    try: 
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        
        image = Image.open(image_file)
        file_path = download_path + file_name
        with open(file_path, "wb") as f:
            image.save(f)

        print("Success")
    except Exception as e:
        print("Error --", e)

def run(googleSearch):
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    wDriver = webdriver.Chrome(PATH, options=op)

    # google searches is a list of strings that are google searches
    

    imageDirectoryPath = f"imgs/{googleSearch}"

    googleToImages(googleSearch, wDriver)
    
    if not os.path.isdir(imageDirectoryPath):
        os.mkdir(imageDirectoryPath)

    photosAmountFromBefore = len(os.listdir(imageDirectoryPath))
    if (photosAmountFromBefore > 0):
        photosAmountFromBefore = int(os.listdir(imageDirectoryPath)[-1][0])
    urlOfImages, skipImagesAmount = getImageFromGoogle(imagesMaxAmount, photosAmountFromBefore, wDriver)
    
    wDriver.quit()
    
    if len(urlOfImages) > 0:
        for i, urlOfImage in enumerate(urlOfImages):
            download_image(imageDirectoryPath + "/", urlOfImage, str(i + 1 + photosAmountFromBefore + skipImagesAmount) + ".png")
    sleep(sleepTimeLong)

    
if __name__ == "__main__":
    run(["toalett"])
