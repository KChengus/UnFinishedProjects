from selenium import webdriver
import requests
import io
from selenium.webdriver.common.by import By
from PIL import Image
from time import sleep
import os

PATH = "D:\\Downloads\\random\\chromedriver.exe"
sleepTimeShort = 0.2
sleepTimeLong = 1
wd = webdriver.Chrome(PATH)

googleUrl = "https://www.google.com/search?q="
googleImagesUrlSuffix = "&tbm=isch"

googleSearches = ["saab"]
imagesMaxAmount = 10

def googleToImages(search):
    wd.get(googleUrl + search + googleImagesUrlSuffix)
    sleep(sleepTimeLong)

def getImageFromGoogle(imageMaxAmount, photosAmountFromBefore):
    images_url = set()
    thumpnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")[photosAmountFromBefore:]
    skipImagesAmount = 0
    for thumpnail in thumpnails:
        try:
            thumpnail.click()
            sleep(sleepTimeShort)
        except Exception as e:
            skipImagesAmount+=1
            print(e)
            continue
        images = wd.find_elements(By.CLASS_NAME, "n3VNCb")
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

if __name__ == "__main__":
    for googleSearch in googleSearches:
        imageDirectoryPath = f"imgs\\{googleSearch}"

        googleToImages(googleSearch)
        
        if not os.path.isdir(imageDirectoryPath):
            os.mkdir(imageDirectoryPath)
        
        photosAmountFromBefore = len(os.listdir(imageDirectoryPath))
        if (photosAmountFromBefore > 0):
            photosAmountFromBefore = int(os.listdir(imageDirectoryPath)[-1][0])
        urlOfImages, skipImagesAmount = getImageFromGoogle(imagesMaxAmount, photosAmountFromBefore)
        if len(urlOfImages) > 0:
            for i, urlOfImage in enumerate(urlOfImages):
                download_image(imageDirectoryPath + "\\", urlOfImage, str(i + 1 + photosAmountFromBefore + skipImagesAmount) + ".png")
        sleep(sleepTimeLong)
    wd.quit()