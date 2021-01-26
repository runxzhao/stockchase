from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

def getStock(stockQuote):
    stock = yf.Ticker(stockQuote)
    print(stock.history(period='1d'))
    if stock.history(period='1d').empty:
        return "Please give a valid symbol"
    openp = str(stock.history(period = '1d').Open[0])
    high = str(stock.history(period = '1d').High[0])
    low = str(stock.history(period = '1d').Low[0])
    close = str(stock.history(period = '1d').Close[0])
    #return high +", "+low +", "+openp+", "+close
    return {"open": openp, "high":high, "low":low, "close":close}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    sq = request.args.get('msg')
    return getStock(sq)

if __name__ == "__main__":
       
    app.run()
