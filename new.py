import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate.host/convert"
    params = {
        "from": from_currency,
        "to": to_currency,
        "amount": amount
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if "result" in data and data["result"] is not None:
            return data["result"]
        else:
            print("Error: Could not get conversion result.")
            return None
    except requests.exceptions.RequestException as e:
        print("API request error:", e)
        return None

# --- User Input ---
try:
    amount = float(input("Enter amount: "))
    from_currency = input("From currency (e.g., USD): ").upper()
    to_currency = input("To currency (e.g., INR): ").upper()

    result = convert_currency(amount, from_currency, to_currency)

    if result is not None:
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    else:
        print("Conversion failed.")

except ValueError:
    print("Please enter a valid number for the amount.")
