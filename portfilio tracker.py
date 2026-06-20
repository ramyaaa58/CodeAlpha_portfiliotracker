import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "AMZN": 3300,
    "MSFT": 300
}

portfolio = {}
total_investment = 0

print("Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))

while True:
    try:
        count = int(input("Enter number of stocks you want to add: "))
        if count > 0:
            break
        else:
            print("Please enter a valid number greater than zero")
    except ValueError:
        print("Invalid input. Please enter a number")

for i in range(count):
    while True:
        stock = input("Enter stock name: ").upper()
        if stock in stock_prices:
            break
        else:
            print("Stock not available. Please choose from the list")

    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity > 0:
                break
            else:
                print("Quantity must be greater than zero")
        except ValueError:
            print("Invalid input. Please enter a number")

    portfolio[stock] = portfolio.get(stock, 0) + quantity

print("\nPortfolio Summary")
print("----------------------------------")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value
    print("Stock:", stock, "Quantity:", quantity, "Price:", price, "Value:", value)

print("----------------------------------")
print("Total Investment Value:", total_investment)

save = input("\nDo you want to save the report (yes or no): ").lower()

if save == "yes":
    file_type = input("Enter file type (txt or csv): ").lower()

    if file_type == "txt":
        with open("portfolio_report.txt", "w") as file:
            file.write("Stock Portfolio Report\n")
            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                value = price * quantity
                file.write(f"{stock} {quantity} {price} {value}\n")
            file.write(f"Total Investment: {total_investment}")
        print("Report saved as portfolio_report.txt")

    elif file_type == "csv":
        with open("portfolio_report.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                value = price * quantity
                writer.writerow([stock, quantity, price, value])
            writer.writerow(["Total", "", "", total_investment])
        print("Report saved as portfolio_report.csv")

    else:
        print("Invalid file type. Report not saved")

else:
    print("Report not saved")