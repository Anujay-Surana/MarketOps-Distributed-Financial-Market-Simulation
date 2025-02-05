from flask import Flask, render_template, request, jsonify
import grpc
import proto.market_pb2 as market_pb2
import proto.market_pb2_grpc as market_pb2_grpc

app = Flask(__name__)
channel = grpc.insecure_channel("localhost:50051")
market_stub = market_pb2_grpc.MarketServiceStub(channel)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/instruments", methods=["GET", "POST"])
def instruments():
    if request.method == "POST":
        symbol = request.form["symbol"]
        type_ = request.form["type"]
        price = float(request.form["price"])
        instrument = market_pb2.Instrument(symbol=symbol, type=type_, price=price)
        response = market_stub.AddInstrument(instrument)
        return jsonify({"success": response.success, "message": response.message})

    instruments = market_stub.ListInstruments(market_pb2.Empty()).instruments
    return render_template("instruments.html", instruments=instruments)

@app.route("/orders", methods=["POST"])
def place_order():
    symbol = request.form["symbol"]
    type_ = request.form["type"]
    price = float(request.form["price"])
    quantity = int(request.form["quantity"])
    order = market_pb2.Order(symbol=symbol, type=type_, price=price, quantity=quantity)
    response = market_stub.PlaceOrder(order)
    return jsonify({"success": response.success, "message": response.message})

@app.route("/orderbook/<symbol>")
def order_book(symbol):
    symbol_request = market_pb2.Symbol(symbol=symbol)
    orderbook = market_stub.QueryOrderBook(symbol_request)
    return render_template("orders.html", orderbook=orderbook)

if __name__ == "__main__":
    app.run(debug=True)
