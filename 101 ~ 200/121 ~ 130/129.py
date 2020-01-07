prices = ["129,300", "1,000", "2,300"]
for price in prices :
    temp = price.replace(',', '')
    print(int(temp))
