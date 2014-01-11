from PyCryptsy import PyCryptsy

secret_key = "49976dfba78486e0ac6e69efb7fa12d83bbc5b1bbd3bcc9ad14289602329b037640aa9a09d27967a"
public_key = "fdb5b5004245daf95e9d5f969dd8cc1b342c25b5"
api = PyCryptsy(public_key,secret_key)

markets = api.Query("getmarkets",{})
transactions = api.Query("allmytrades",{})

def funds():
    """
    parses JSON response into a list of unique markets
    """
    for item in markets["return"]:
        print item

def trades():
    """
    parses JSON response into a list of unique trades
    """
    for item in transactions["return"]:
        print item["tradetype"], item["marketid"], (float(item["total"]) - float(item["fee"]))

def unique_markets():
    """
    find all of the user's unique markets
    """
    m = []

    for item in transactions["return"]:
        if item["marketid"] not in m:
            m.append(item["marketid"])

    for market in markets["return"]:
        if market["marketid"] in m:
            print market["label"], market["marketid"]


print trades()
print unique_markets()
# final_total = ((btc_trades * btc_usd_exchange_rate) + (ltc_trades * ltc_usd_exchange_rate)) - fees