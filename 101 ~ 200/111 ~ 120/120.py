volatility = int(btc['max_price']) - int(btc['min_price'])
if int(btc['opening_price']) + volatility > int(btc['max_price']) :
    print("상승장")
else :
    print("하락장")
