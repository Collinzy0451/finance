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

        if email == "tomtracy1@gmail.com" and password == "Thomcy1000@":
            session['logged_in'] = True
            session['user'] = 'main'
            return redirect("/dashboard")

        elif email == "mohkalqaddi1987@gmail.com" and password == "master456":
            session['logged_in'] = True
            session['user'] = 'alt'
            return redirect("/dashboard2")

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
            "date": "2025-04-03",
            "time": "10:22 AM",
            "type": "Initial investment deposit via bank transfer",
            "amount": 90000.00,
            "status": "Completed",
            "description": "Initial investment capital"
        },
        {
            "id": "TXN002",
            "date": "2025-04-17",
            "time": "02:45 PM",
            "type": "Investment Profit credit",
            "amount": 4200.23,
            "status": "Completed",
            "description": "Monthly profit from investments"
        },
        {
            "id": "TXN003",
            "date": "2025-05-01",
            "time": "09:18 AM",
            "type": "Investment deposit via bank transfer",
            "amount": 85000.00,
            "status": "Completed",
            "description": "Additional investment for portfolio diversification"
        },
        {
            "id": "TXN004",
            "date": "2025-05-10",
            "time": "03:30 PM",
            "type": "Performance Bonus credit",
            "amount": 15833.20,
            "status": "Completed",
            "description": "Quarterly performance bonus for exceeding targets"
        },
        {
            "id": "TXN005",
            "date": "2025-05-22",
            "time": "06:10 PM",
            "type": "Investment deposit via Crypto",
            "amount": 83120.04,
            "status": "Completed",
            "description": "Investment in cryptocurrency portfolio"
        },
        {
            "id": "TXN006",
            "date": "2025-06-02",
            "time": "11:15 AM",
            "type": "Portfolio growth credit",
            "amount": 26325.12,
            "status": "Completed",
            "description": "Portfolio growth credit for reaching Gold Tier status"
        },
        {
            "id": "TXN007",
            "date": "2025-06-15",
            "time": "04:22 PM",
            "type": "Debit for accumulated administrative fees",
            "amount": 2530.30,
            "status": "Completed",
            "description": "Accumulated administrative fees for account maintenance"
        },
        {
            "id": "TXN008",
            "date": "2025-06-30",
            "time": "11:05 AM",
            "type": "Deposit via bank transfer",
            "amount": 45000.00,
            "status": "Completed",
            "description": "Deposit for upcoming investment opportunities"
        },
        {
            "id": "TXN009",
            "date": "2025-07-15",
            "time": "01:42 PM",
            "type": "Cumulative Compounded Gains Allocation",
            "amount": 540375.33,
            "status": "Completed",
            "description": "Cumulative gains from investments allocated to portfolio"
        },
        
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


# Alt routes
@app.route("/dashboard2")
def dashboard2():
    if not session.get('logged_in') or session.get('user') != 'alt':
        return redirect(url_for('login'))
    return render_template("dashboard2.html")

@app.route("/profile2")
def profile2():
    if not session.get('logged_in') or session.get('user') != 'alt':
        return redirect(url_for('login'))
    return render_template("profile2.html")

@app.route("/withdraw2")
def withdraw2():
    if not session.get('logged_in') or session.get('user') != 'alt':
        return redirect(url_for('login'))
    return render_template("withdraw2.html")

@app.route("/deposit2")
def deposit2():
    if not session.get('logged_in') or session.get('user') != 'alt':
        return redirect(url_for('login'))
    return render_template("deposit2.html")

@app.route("/transactions2")
def transactions2():
    if not session.get('logged_in') or session.get('user') != 'alt':
        return redirect(url_for('login'))
    return render_template("transactions2.html")

@app.route("/pop")
def pop():
    return render_template("pop.html")
 



if __name__ == '__main__':
    app.run(port=7000, debug=True)
