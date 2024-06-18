import json
import os
import requests
from datetime import datetime

# File to store stockpile and price data
DATA_FILE = "stockpile_data.json"

# Existing stockpile and price data
gas_stockpile = {
    "Fullerite-C28": 0,
    "Fullerite-C32": 0,
    "Fullerite-C50": 0,
    "Fullerite-C60": 0,
    "Fullerite-C70": 0,
    "Fullerite-C72": 0,
    "Fullerite-C84": 0,
    "Fullerite-C320": 0,
    "Fullerite-C540": 0,
}

mineral_stockpile = {
    "Isogen": 100000,
    "Megacyte": 20000,
    "Mexallon": 132324,
    "Nocxium": 4158,
    "Pyerite": 3033047,
    "Tritanium": 5357184,
    "Zydrine": 50000,
}

fuel_block_stockpile = {
    "Hydrogen Fuel Block": 5000,
    "Helium Fuel Block": 4000,
    "Nitrogen Fuel Block": 6000,
    "Oxygen Fuel Block": 7000,
}

gas_prices = {
    "Fullerite-C28": 10,
    "Fullerite-C32": 15,
    "Fullerite-C50": 12,
    "Fullerite-C60": 20,
    "Fullerite-C70": 25,
    "Fullerite-C72": 30,
    "Fullerite-C84": 35,
    "Fullerite-C320": 40,
    "Fullerite-C540": 45,
}

mineral_prices = {
    "Isogen": 100,
    "Megacyte": 200,
    "Mexallon": 300,
    "Nocxium": 400,
    "Pyerite": 500,
    "Tritanium": 600,
    "Zydrine": 700,
}

fuel_block_prices = {
    "Hydrogen Fuel Block": 10,
    "Helium Fuel Block": 20,
    "Nitrogen Fuel Block": 30,
    "Oxygen Fuel Block": 40,
}

gas_price_ids = {
    "Fullerite-C28": 30375,
    "Fullerite-C32": 30376,
    "Fullerite-C50": 30370,
    "Fullerite-C60": 30371,
    "Fullerite-C70": 30372,
    "Fullerite-C72": 30373,
    "Fullerite-C84": 30374,
    "Fullerite-C320": 30377,
    "Fullerite-C540": 30378,
}

mineral_price_ids = {
    "Isogen": 37,
    "Megacyte": 40,
    "Mexallon": 36,
    "Nocxium": 38,
    "Pyerite": 35,
    "Tritanium": 34,
    "Zydrine": 39,
}

fuel_block_price_ids = {
    "Hydrogen Fuel Block": 4246,
    "Helium Fuel Block": 4247,
    "Nitrogen Fuel Block": 4248,
    "Oxygen Fuel Block": 4249,
}

last_updated = {
    "gas_prices": None,
    "mineral_prices": None,
    "fuel_block_prices": None,
}

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            gas_stockpile.update(data.get("gas_stockpile", {}))
            mineral_stockpile.update(data.get("mineral_stockpile", {}))
            fuel_block_stockpile.update(data.get("fuel_block_stockpile", {}))
            gas_prices.update(data.get("gas_prices", {}))
            mineral_prices.update(data.get("mineral_prices", {}))
            fuel_block_prices.update(data.get("fuel_block_prices", {}))
            last_updated.update(data.get("last_updated", {}))

def save_data():
    data = {
        "gas_stockpile": gas_stockpile,
        "mineral_stockpile": mineral_stockpile,
        "fuel_block_stockpile": fuel_block_stockpile,
        "gas_prices": gas_prices,
        "mineral_prices": mineral_prices,
        "fuel_block_prices": fuel_block_prices,
        "last_updated": last_updated,
    }
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Fullerene Reaction Stockpile")
        print("2. Fullerene Input Prices")
        print("3. Production Information")
        print("4. Exit")
        
        choice = input("Please select an option (1-4): ")

        if choice == '1':
            fullerene_reaction_stockpile_menu()
        elif choice == '2':
            fullerene_input_prices_menu()
        elif choice == '3':
            production_information_menu()
        elif choice == '4':
            save_data()
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def fullerene_reaction_stockpile_menu():
    while True:
        print("\nFullerene Reaction Stockpile Menu")
        print("1. Gas Stockpile")
        print("2. Mineral Stockpile")
        print("3. Fuel Block Stockpile")
        print("4. Return to Main Menu")

        choice = input("Please select an option (1-4): ")

        if choice == '1':
            stockpile_menu("Gas Stockpile", gas_stockpile)
        elif choice == '2':
            stockpile_menu("Mineral Stockpile", mineral_stockpile)
        elif choice == '3':
            stockpile_menu("Fuel Block Stockpile", fuel_block_stockpile)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def stockpile_menu(title, stockpile):
    while True:
        print(f"\n{title} Menu")
        print("1. View Stockpile")
        print("2. Update Stockpile")
        print("3. Return to previous menu")

        choice = input("Please select an option (1-3): ")

        if choice == '1':
            view_stockpile(stockpile)
        elif choice == '2':
            update_stockpile(stockpile)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def view_stockpile(stockpile):
    print("\nStockpile:")
    for item, amount in stockpile.items():
        print(f"{item}: {amount}")

def update_stockpile(stockpile):
    print("\nUpdate Stockpile:")
    for item in stockpile:
        while True:
            choice = input(f"Do you want to edit the amount of {item}? (y/n/exit): ").strip().lower()
            if choice == 'y':
                try:
                    new_amount = int(input(f"Enter the new amount for {item}: "))
                    stockpile[item] = new_amount
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif choice == 'n':
                break
            elif choice == 'exit':
                return
            else:
                print("Invalid choice. Please enter 'y', 'n', or 'exit'.")

def fullerene_input_prices_menu():
    while True:
        print("\nFullerene Input Prices Menu")
        print("1. View Prices")
        print("2. Edit Prices")
        print("3. Update @ Jita Price")
        print("4. Return to Main Menu")
        
        choice = input("Please select an option (1-4): ")

        if choice == '1':
            view_fullerene_input_prices()
        elif choice == '2':
            edit_prices_menu()
        elif choice == '3':
            update_jita_prices()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def view_fullerene_input_prices():
    print("\nGas Prices:")
    for gas, price in gas_prices.items():
        print(f"{gas}: {price} ISK/unit")
    print(f"Last updated: {last_updated['gas_prices']}")

    print("\n\nMineral Prices:")
    for mineral, price in mineral_prices.items():
        print(f"{mineral}: {price} ISK/unit")
    print(f"Last updated: {last_updated['mineral_prices']}")

    print("\n\nFuel Block Prices:")
    for fuel_block, price in fuel_block_prices.items():
        print(f"{fuel_block}: {price} ISK/unit")
    print(f"Last updated: {last_updated['fuel_block_prices']}")

def edit_prices_menu():
    while True:
        print("\nEdit Prices Menu")
        print("1. Edit Gas Prices")
        print("2. Edit Mineral Prices")
        print("3. Edit Fuel Block Prices")
        print("4. Return to previous menu")
        
        choice = input("Please select an option (1-4): ")

        if choice == '1':
            edit_prices(gas_prices, "Gas Prices")
        elif choice == '2':
            edit_prices(mineral_prices, "Mineral Prices")
        elif choice == '3':
            edit_prices(fuel_block_prices, "Fuel Block Prices")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def edit_prices(prices, title):
    print(f"\nEdit {title}:")
    for item in prices:
        while True:
            choice = input(f"Do you want to edit the price of {item}? (y/n/exit): ").strip().lower()
            if choice == 'y':
                try:
                    new_price = float(input(f"Enter the new price for {item} (ISK/unit): "))
                    prices[item] = new_price
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif choice == 'n':
                break
            elif choice == 'exit':
                return
            else:
                print("Invalid choice. Please enter 'y', 'n', or 'exit'.")

def update_jita_prices():
    print("\nUpdating Prices from Jita Market...")
    update_prices(gas_prices, gas_price_ids, "gas_prices")
    update_prices(mineral_prices, mineral_price_ids, "mineral_prices")
    update_prices(fuel_block_prices, fuel_block_price_ids, "fuel_block_prices")

def update_prices(prices, price_ids, category):
    for item, item_id in price_ids.items():
        try:
            url = f"https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&type_id={item_id}"
            response = requests.get(url)
            response.raise_for_status()
            orders = response.json()
            sell_orders = [order for order in orders if not order['is_buy_order']]
            if not sell_orders:
                print(f"No sell orders found for {item}")
                continue
            lowest_price = min(order['price'] for order in sell_orders)
            prices[item] = lowest_price
            print(f"Updated {item} to {lowest_price:.2f} ISK/unit")
        except Exception as e:
            print(f"Failed to update {item} from {url}: {e}")
    last_updated[category] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def production_information_menu():
    while True:
        print("\nProduction Information Menu")
        print("1. View Production Info")
        print("2. Return to Main Menu")
        
        choice = input("Please select an option (1-2): ")

        if choice == '1':
            view_production_information()
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

def view_production_information():
    print("\nProduction Information:")
    for item, amount in mineral_stockpile.items():
        print(f"{item}: {amount} (Mineral)")

if __name__ == "__main__":
    load_data()
    main_menu()
