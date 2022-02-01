import os
import pygame
import random


auction_hand_width = 75
auction_hand_height = 150
auction_hand_position = [(100, 300), (200, 400), (500, 300), (600, 400)]
auctioneer_width = 75
auctioneer_height = 100

class People:
    def __init__(self, name, age, social_class, money):
        self.name = name
        self.age = age
        self.social_class = social_class
        self.money = money

class Buyer(People):
    def __init__(self, name, age, social_class, money, x, y, number):
        super().__init__(name, age, social_class, money)
        self.x = x
        self.y = y
        self.number = number

    bought_items = {}
    # hand picture
    auction_hand_picture = pygame.image.load("animation_folder\\auction_hand.png")
    auction_hand_picture = pygame.transform.scale(auction_hand_picture, (auction_hand_width, auction_hand_height))
    x = y = 0
    # If the bidding price is within their money range, return True otherwise False

    def bid(self, bid_price):
        if (self.money >= bid_price):
            return True
        else:
            return False

    def buy(self, price, product):
        self.bought_items[product] = price
        self.money += price

class Auctioneer():
    def __init__(self, money):
        self.available_items = list()
        auctioneer_picture = pygame.image.load("animation_folder\\auctioneer.png")
        self.auctioneer_picture = pygame.transform.scale(auctioneer_picture, (auctioneer_width, auctioneer_height))
        self.money = money
        self.current_buyer = None
    def sold(self, price):
        self.money += price

    def sold_item(self, item):
        self.available_items.remove(item)

#Upper Class.
#Lower Class.
#Working Class.
#Poor.


class Product:
    def __init__(self, product, average_price, image):
        self.product = product
        self.average_price = average_price
        self.image = image

# auctioneer
auctioneer_money = 10 ** 5
auctioneer = Auctioneer(auctioneer_money)

# Buyers text file. The number of rows represents the num of buyers
# Each row has four columns. (Name Age Class Money)
buyers_instances = list()
with open("text_folder\\people.txt", "r") as f:
    for i, buyers_attribute in enumerate(f.readlines()):
        buyers_attribute = buyers_attribute.split(" ")
        if (len(buyers_attribute) == 4):
            name, age, social_class, money = buyers_attribute
            buyer = Buyer(name, int(age), social_class, int(money),
                          auction_hand_position[i][0], auction_hand_position[i][1], i + 1)
            buyers_instances.append(buyer)



# product instance initializer
all_product_instances = list()
product_file = "text_folder\\product.txt"
product_and_price = {}
auction_item_dimension_width = 200
auction_item_dimension_height = 100


with open(product_file, "r") as f:
    for prod in f.readlines():
        product_name, average_price = prod.split()

        product_and_price[product_name] = average_price

for product_name, price in product_and_price.items():
    name = product_name.replace("_", " ")
    path = "picture_folder\\" + product_name + ".png"
    image = pygame.image.load(path)
    image = pygame.transform.scale(image, (auction_item_dimension_width, auction_item_dimension_height))
    product_instance = Product(name, int(price), image)
    all_product_instances.append(product_instance)




