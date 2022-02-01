import os

directory ="C:\\Users\\Kevin\\PycharmProjects\\pythonProject\\Auction\\picture_folder"
product_file = "text_folder\\product.txt"
picture_folder = "picture_folder"
picture_files = [file_name[:-4] for file_name in os.listdir(directory)]

products = list()
with open(product_file, "r") as f:

    for line in f.readlines():

        products.append(line.split()[0])
    print(products)

with open(product_file, 'a') as f:
    for picture_file in picture_files:
        if picture_file not in products:
            average_price = int(input("Type the Average Price for " + picture_file + '\n'))
            f.write('\n' + picture_file + ' ' + str(average_price))

print("Done")