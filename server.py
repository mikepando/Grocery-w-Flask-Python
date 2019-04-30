from flask import Flask, render_template, request
import csv

app = Flask(__name__)
app.config["DEBUG"] = True
prices={"apples":0.79,"strawberries":1.99,"eggs":1.69,"milk":2.29,"soda":1.25}

@app.route("/generate_bill", methods=["POST"])
def generate_bill():
        apples=request.form["num_gsmith"]
        if int(apples) < 0:
            apples=0
        berries=request.form["num_strawberries"]
        if int(berries) < 0:
            berries=0
        eggs=request.form["num_eggs"]
        if int(eggs) < 0:
            eggs=0
        milk=request.form["num_milk"]
        if int(milk) < 0:
            milk=0
        soda=request.form["num_soda"]
        if int(soda) < 0:
            soda=0
        costApples=int(apples)*prices['apples']
        costBerries=int(berries)*prices['strawberries']
        costEggs=int(eggs)*prices['eggs']
        costMilk=int(milk)*prices['milk']
        costSoda=int(soda)*prices['soda']
        itemsToDisplay=[   # note there are four items in each list:
                                     # product name, price, number purchased, cost
    			["GrannySmith", prices['apples'], apples, costApples],
                ["Strawberries", prices["strawberries"], berries, costBerries],
                ["Eggs", prices["eggs"], eggs, costEggs],
                ["Milk", prices["milk"], milk, costMilk],
                ["Soda", prices["soda"], soda, costSoda]
                ]
        return render_template("bill.html",items=itemsToDisplay)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
