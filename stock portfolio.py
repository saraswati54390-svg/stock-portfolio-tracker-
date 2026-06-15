print("📈 Stock Portfolio Tracker")

portfolio = {}
total_value = 0

while True:
    stock_name = input("\nEnter Stock Name (or 'done' to finish): ")

    if stock_name.lower() == "done":
        break

    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price per Share: ₹"))

    value = quantity * price
    portfolio[stock_name] = value
    total_value += value

print("\n📊 Portfolio Summary")
print("-" * 30)

for stock, value in portfolio.items():
    print(f"{stock}: ₹{value}")

print("-" * 30)
print(f"💰 Total Portfolio Value: ₹{total_value}")
