from flask import Flask, render_template, request, redirect, flash, url_for, session

app = Flask(__name__)
app.secret_key = "sweetsecret"

# In-memory sweet data
sweets = {
    "1001": {"id": "1001", "name": "Kaju Katli", "category": "Nut Based", "price": 50.0, "quantity": 20}
    
}

@app.before_request
def initialize_cart():
    if "cart" not in session:
        session["cart"] = {}

# Home Page with listinng , search and sort
@app.route("/", methods=["GET"])
def index():
    query = request.args
    search_id = query.get("id", "").lower()
    search_name = query.get("name", "").lower()
    search_category = query.get("category", "").lower()
    search_price = query.get("price", "")
    sort_by = query.get("sort_by", "")

    filtered = list(sweets.values())

    if search_id:
        filtered = [s for s in filtered if search_id in s["id"].lower()]
    if search_name:
        filtered = [s for s in filtered if search_name in s["name"].lower()]
    if search_category:
        filtered = [s for s in filtered if search_category in s["category"].lower()]
    if search_price:
        try:
            max_price = float(search_price)
            filtered = [s for s in filtered if s["price"] <= max_price]
        except:
            pass

    if sort_by in ["id", "name", "category", "price", "quantity"]:
        filtered.sort(key=lambda x: x[sort_by])

    return render_template("index.html", sweets=filtered)

# Adding sweets
@app.route("/add", methods=["POST"])
def add():
    data = request.form
    sweet_id = data["id"]
    if sweet_id in sweets:
        flash("Sweet ID already exists.", "error")
    else:
        sweets[sweet_id] = {
            "id": sweet_id,
            "name": data["name"],
            "category": data["category"],
            "price": float(data["price"]),
            "quantity": int(data["quantity"])
        }
        flash("Sweet added successfully!", "success")
    return redirect(url_for("index"))

# Deleting the Sweet
@app.route("/delete/<id>")
def delete(id):
    if id in sweets:
        del sweets[id]
        flash("Sweet deleted.", "success")
    else:
        flash("Sweet not found.", "error")
    return redirect(url_for("index"))

# Editing the exsiting Sweet 
@app.route("/edit/<id>")
def edit(id):
    if id not in sweets:
        flash("Sweet not found.", "error")
        return redirect(url_for("index"))
    return render_template("edit.html", sweet=sweets[id])

# Update Sweet
@app.route("/update/<id>", methods=["POST"])
def update(id):
    if id in sweets:
        data = request.form
        sweets[id]["name"] = data["name"]
        sweets[id]["category"] = data["category"]
        sweets[id]["price"] = float(data["price"])
        sweets[id]["quantity"] = int(data["quantity"])
        flash("Sweet updated.", "success")
    else:
        flash("Sweet not found.", "error")
    return redirect(url_for("index"))

# Purchase the sweets
@app.route("/purchase/<id>", methods=["POST"])
def purchase(id):
    qty = int(request.form["quantity"])
    if id in sweets and sweets[id]["quantity"] >= qty:
        sweets[id]["quantity"] -= qty

        cart = session.get("cart", {})
        if id in cart:
            cart[id]["qty"] += qty
        else:
            cart[id] = {
                "name": sweets[id]["name"],
                "category": sweets[id]["category"],
                "qty": qty,
                "price": sweets[id]["price"]
            }
        session["cart"] = cart
        session.modified = True  
        flash("Purchase successful.", "success")
    else:
        flash("Not enough stock or sweet not found.", "error")
    return redirect(url_for("index"))

# Restock if not available
@app.route("/restock/<id>", methods=["POST"])
def restock(id):
    qty = int(request.form["quantity"])
    if id in sweets:
        sweets[id]["quantity"] += qty
        flash("Restocked successfully.", "success")
    else:
        flash("Sweet not found.", "error")
    return redirect(url_for("index"))

# Add to Cart 
@app.route("/cart/add/<id>", methods=["POST"])
def add_to_cart(id):
    qty = int(request.form["quantity"])
    if id in sweets and sweets[id]["quantity"] >= qty:
        cart = session.get("cart", {})
        if id in cart:
            cart[id]["qty"] += qty
        else:
            cart[id] = {
                "name": sweets[id]["name"],
                "category": sweets[id]["category"],
                "qty": qty,
                "price": sweets[id]["price"]
            }
        session["cart"] = cart
        session.modified = True
        flash("Added to cart!", "success")
    else:
        flash("Sweet not found or insufficient stock.", "error")
    return redirect(url_for("index"))

# View Cart Page
@app.route("/cart")
def view_cart():
    cart = session.get("cart", {})
    total = sum(item["qty"] * item["price"] for item in cart.values())
    return render_template("cart.html", cart=cart, total=total)

# Checkout Page for enerating bill and view cart items
@app.route("/checkout")
def checkout():
    cart = session.get("cart", {})
    total = sum(item["qty"] * item["price"] for item in cart.values())
    items = list(cart.values())
    session["cart"] = {}
    flash("Checkout completed!", "success")
    return render_template("bill.html", items=items, total=total)

if __name__ == "__main__":
    app.run(debug=True)
