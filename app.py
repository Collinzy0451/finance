from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__,
            template_folder='app/templates',
            static_folder='app/static')
app.secret_key = '1a9f4e5d6c2b41f9a7e3c0d8f4e2b6c3'

@app.route('/')
def home():
    return render_template('index.html')


# login page
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if email == "master123@yahoo.com" and password == "master456":
            session['logged_in'] = True
            return redirect("/dashboard")  # or /profile or landing page
        else:
            error = "Invalid email or password"
    return render_template("login.html", error=error)


#  register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return render_template("register.html", success="Registration successful! Please log in.")
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route("/dashboard")
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    
    return render_template("dashboard.html")


@app.route("/profile")
def profile():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template("profile.html")

@app.route('/transactions')
def transactions():
    sample_transactions = [
        {
            "id": "TXN001",
            "date": "2025-04-10",
            "time": "10:22 AM",
            "type": "Deposit to Investment Wallet",
            "amount": 1500.00,
            "status": "Completed",
            "description": "Initial investment capital"
        },
        {
            "id": "TXN002",
            "date": "2025-04-11",
            "time": "02:45 PM",
            "type": "Stock Purchase",
            "amount": 500.00,
            "status": "Completed",
            "description": "Bought 5 shares of TSLA"
        },
        {
            "id": "TXN003",
            "date": "2025-04-12",
            "time": "09:18 AM",
            "type": "Profit Withdrawal",
            "amount": 120.00,
            "status": "Completed",
            "description": "Withdrew trading profit to savings"
        },
        {
            "id": "TXN004",
            "date": "2025-04-13",
            "time": "03:30 PM",
            "type": "Investment Return",
            "amount": 200.00,
            "status": "Completed",
            "description": "ROI from mutual fund"
        },
        {
            "id": "TXN005",
            "date": "2025-04-13",
            "time": "06:10 PM",
            "type": "Savings Wallet Deposit",
            "amount": 300.00,
            "status": "Completed",
            "description": "Transfer from main balance to savings"
        },
        {
            "id": "TXN006",
            "date": "2025-04-14",
            "time": "11:15 AM",
            "type": "Stock Purchase",
            "amount": 250.00,
            "status": "Completed",
            "description": "Bought 2 shares of AAPL"
        },
        {
            "id": "TXN007",
            "date": "2025-04-14",
            "time": "04:22 PM",
            "type": "Deposit to Savings Wallet",
            "amount": 100.00,
            "status": "Completed",
            "description": "Added funds to savings"
        },
        {
            "id": "TXN008",
            "date": "2025-04-15",
            "time": "08:05 AM",
            "type": "Profit Withdrawal",
            "amount": 80.00,
            "status": "Completed",
            "description": "Withdrew trading profits"
        },
        {
            "id": "TXN009",
            "date": "2025-04-15",
            "time": "01:42 PM",
            "type": "Investment",
            "amount": 1000.00,
            "status": "Completed",
            "description": "Invested in index fund"
        },
        {
            "id": "TXN010",
            "date": "2025-04-15",
            "time": "05:50 PM",
            "type": "Deposit",
            "amount": 700.00,
            "status": "Completed",
            "description": "Top-up for upcoming investment"
        }
    ]
    return render_template("transactions.html", transactions=sample_transactions)

@app.route('/withdraw')
def withdraw():
    return render_template('withdraw.html')

@app.route('/deposit')
def deposit():
    return render_template('deposit.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # You can now save this to a database, email it, or log it
    print(f"Message received from {name} ({email}): {message}")

    flash("Thank you for reaching out! We'll get back to you soon.")
    return redirect('/')  # Or wherever you want to redirect after submitting


# @app.route('/balance')
# def balance():
#     return render_template('balance.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/stocks')
def stocks():
    return render_template('stocks.html')



if __name__ == '__main__':
    app.run(port=7000, debug=True)
