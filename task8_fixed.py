def calculate_total(prices, discount=0):
    total = 0
    for price in prices:
        total += price
    total = total - total * discount / 100
    return total
def describe_order(city, customer, country="Azerbaijan"):
    return customer + " ordered from " + city + ", " + country
order_total = calculate_total([10, 20, 30], 10)
print("Total: " + str(order_total))
print(describe_order("Baku", customer="Ali"))
