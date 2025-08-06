
exchange_rates = {
    'USD': 1.0,
    'INR': 83.25,
    'EUR': 0.91,
    'GBP': 0.78,
    'JPY': 157.55,
    'AUD': 1.48,
    'CAD': 1.36
}

def convert_currency(amount, from_curr, to_curr):
    from_curr = from_curr.upper()
    to_curr = to_curr.upper()

    if from_curr not in exchange_rates or to_curr not in exchange_rates:
        print(" Unsupported currency code.")
        return

    # Convert to USD first, then to target
    usd_amount = amount / exchange_rates[from_curr]
    converted_amount = usd_amount * exchange_rates[to_curr]

    print(f"\n CONVERTED CURRENCY : {amount} {from_curr} = {converted_amount:.2f} {to_curr}")

# ------- Main Program --------
print("Offline Currency Converter (Static Rates)")
print("Supported currencies:", ", ".join(exchange_rates.keys()))

try:
    amount = float(input("Enter amount: "))
    from_currency = input("Convert from (e.g., USD): ")
    to_currency = input("Convert to (e.g., INR): ")
    convert_currency(amount, from_currency, to_currency)
except ValueError:
    print("Please enter a valid number for amount.")
