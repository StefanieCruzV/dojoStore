from flask import Flask, render_template, request, redirect
import os
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    # print(request.form["strawberry"])
    # print(request.form["raspberry"])
    # print(request.form["apple"])
    # print(request.form["first_name"])
    # print(request.form["last_name"])
    # print(request.form["student_id"])
    totalfruits= int(request.form["raspberry"])+int(request.form["apple"])+int(request.form["strawberry"])
    print(f"Charging {request.form['last_name']} for {totalfruits} fruits")
    

   # print(request.form)
    return render_template("checkout.html",values=request.form, apple=request.form["apple"])
  

@app.route('/fruits')
def fruits():
    fruits= os.listdir('static/img')
    print(fruits)
    return render_template("fruit.html",fruits=fruits)


if __name__ == "__main__":
    app.run(debug=True)
