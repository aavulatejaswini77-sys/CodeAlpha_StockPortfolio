# Stock Portfolio Tracker

# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 300
}

portfolio = {}
total_investment = 0

print("Welcome to Stock Portfolio Tracker!")

# Get number of stocks
number = int(input("How many stocks do you want to add? "))

for i in range(number):
    stock = input("Enter stock name (AAPL/TSLA/GOOG/MSFT): ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock] * quantity
        portfolio[stock] = quantity

        total_investment += investment

        print("Investment:", investment)

    else:
        print("Stock not available!")

# Display portfolio
print("\n----- Your Portfolio -----")

for stock, quantity in portfolio.items():
    print(stock, "Quantity:", quantity)

print("Total Investment:", total_investment)

# Save portfolio to a file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Tracker\n")

    for stock, quantity in portfolio.items():
        file.write(stock + " - Quantity: " + str(quantity) + "\n")

    file.write("Total Investment: " + str(total_investment))

print("\nPortfolio saved successfully!")
