import pygame
import auction_classes as ac
import random
import time
from math import floor
pygame.init()


# display settings
display_width = 800
display_height = 600
clock = pygame.time.Clock()
clock.tick(30)

# render the window
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Auction")
background = pygame.image.load("animation_folder\\auction_hall.png")
background = pygame.transform.scale(background, (display_width, display_height))
# settings
running = True
current_product_instance = random.choice(ac.all_product_instances)
product_placement_x = 300
product_placement_y = 200
current_time = time.time()
prev_time = 0
time_limit = 10
# Main loop

def display_picture(image, x, y):
    gameDisplay.blit(image, (x, y))

def change_picture(current_picture):
    choice = random.choice(ac.all_product_instances)
    if (choice == current_picture):

        return change_picture(current_picture)
    return choice

def bid_money(buyer, current_product_price):
    # TODO set a time limimt
    global current_time, prev_time
    print(buyer.number)

    prev_time = 0
    if (buyer.money < current_product_price):
        current_time = time.time()
        return current_product_price
    money = -1
    while (money <= current_product_price):
        print(f"Your Money: {buyer.number}       Cost: {current_product_price}")
        money = int(input("Enter Your Bidding Price (-1 for cancel):\n"))
        if (money == -1):
            current_time = time.time()
            return current_product_price
    buyer.money -= money
    ac.auctioneer.current_buyer = buyer.number
    print(f"The product now costs {money}. The current bidder is currently number {buyer.number}")
    current_time = time.time()
    return money

print(current_product_instance.average_price)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                current_product_instance = change_picture(current_product_instance)
                print(current_product_instance.average_price)

            if event.key == pygame.K_1:
                current_product_instance.average_price = bid_money(ac.buyers_instances[0], current_product_instance.average_price)
            elif event.key == pygame.K_2:
                current_product_instance.average_price = bid_money(ac.buyers_instances[1], current_product_instance.average_price)
            elif event.key == pygame.K_3:
                current_product_instance.average_price = bid_money(ac.buyers_instances[2], current_product_instance.average_price)
            elif event.key == pygame.K_4:
                current_product_instance.average_price = bid_money(ac.buyers_instances[3], current_product_instance.average_price)
    # handle time

    diff = floor(time.time() - current_time)
    if (diff > prev_time):
        prev_time = diff
        print(diff)
    if (diff >= time_limit):
        running = False
    # display pictures
    display_picture(background, 0, 0)
    display_picture(ac.auctioneer.auctioneer_picture, 355, 300)
    display_picture(current_product_instance.image, product_placement_x, product_placement_y)
    for buyers in ac.buyers_instances:
        display_picture(buyers.auction_hand_picture, buyers.x, buyers.y)


    pygame.display.update()

pygame.quit()
