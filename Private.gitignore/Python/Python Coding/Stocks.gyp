from yahoo_fin import stock_info as si


try:
    si.get_live_price("aapl")
    print(si)
    fprice1 = int(input("\nPlease enter the beginning period stock price: "))
    fprice2 = int(input("\nPlease enter the ending period stock price: "))
    fmoney = int(input("\nPlease enter the amount invested: "))
    discount = .85
    if fprice1 > fprice2:
        fcheap = fprice2 * discount
        fmax = fprice1
    else:
        fcheap = fprice1 * discount
        fmax = fprice2

    fshares = int (fmoney / fcheap) 
    int(round(fshares))

    print("\n" + str(fcheap) + " is the price of the stock after the discount. \n" )
    print(str(fshares) + " is the number of shares purchased. \n" )

    fprofit = int((fmax * fshares) - (fcheap * fshares))
    print(str(fprofit) + " $ is the profit you made over the last 6 months. \n" )
except:
    print("\n Unknown error, please abort program and try again.\n")
