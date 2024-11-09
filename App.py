import streamlit as st

# Set fixed exchange rates for currencies (approximate values)
EXCHANGE_RATES = {
    "ANG": 1.0,       # Base currency
    "USD": 0.56,
    "EUR": 0.51,
    "GBP": 0.44,
    "CAD": 0.75
}

# Set up wine data
wines = {
    "Sparkling": [
        ("Cava Palau Brut", 24.50),
        ("Cava Palau Semi Sec", 24.50),
        ("Cava Palau Rosado", 25.50),
        ("Cielo Prosecco Spumante (Vegan)", 29.00),
        ("Cielo Prosecco Rose Spumante", 29.00),
        ("Champagne Baron Fuente Tradition Brut", 79.00),
        ("Champagne Taittinger Brut Reserve", 165.00),
        ("Champagne Taittinger Prestige Rose", 199.00),
    ],
    "White": [
        ("Ca del Lago Pinot Grigio", 19.50),
        ("Ca del Lago Chardonnay", 19.50),
        ("Villa San Martino Le Rive Pinot Grigio", 22.00),
        ("Cielo Pinot Grigio Veneto", 18.50),
        ("Torre Oria Viura - Sauvignon Blanc", 19.85),
        ("Invidious Viura - Sauvignon Vdt Castilla", 19.75),
        ("Paul Mas Chardonnay 250 ml", 13.00),
    ],
    "Rose": [
        ("Ca del Lago Pinot Grigio Blush", 19.50),
        ("Mirada Bobal Rosado Organic Vdt Castilla", 27.95),
        ("Torre Oria Pinot Noir Rosato", 30.00),
    ],
    "Red": [
        ("Invidious Tempranillo - Syrah Vdt Castilla", 19.75),
        ("Luccarelli Red Blend (Puglia, Italy)", 24.50),
        ("Neropasso Rosso IGT Veneto", 42.50),
        ("Antico Casale Valpolicella Ripasso", 35.00),
        ("Antiche Terre Amarone Valpolicella", 74.00),
    ]
}

# Streamlit app layout
st.title("Videmi Wine Ordering System")
st.write("Select the wine and quantity you would like to order, and view the total cost in your preferred currency.")

# Currency selection
currency = st.selectbox("Choose your currency:", options=["ANG", "USD", "EUR", "GBP", "CAD"])

# Initialize a dictionary to track quantities
quantities = {wine_name: 0 for category in wines for wine_name, _ in wines[category]}

# Order form
total_ang = 0
for category, wine_list in wines.items():
    with st.expander(f"{category} Wines"):
        for wine_name, price_ang in wine_list:
            qty = st.number_input(f"{wine_name} (ANG {price_ang:.2f})", min_value=0, max_value=100, step=1, key=f"{wine_name}_{currency}")
            quantities[wine_name] = qty
            total_ang += qty * price_ang

# Currency conversion
conversion_rate = EXCHANGE_RATES[currency]
total_converted = total_ang * conversion_rate

# Display order summary in selected currency
st.write("## Order Summary")
for category, wine_list in wines.items():
    for wine_name, price_ang in wine_list:
        qty = quantities[wine_name]
        if qty > 0:
            price_converted = price_ang * conversion_rate
            st.write(f"{wine_name}: {qty} bottles @ {currency} {price_converted:.2f} each = {currency} {qty * price_converted:.2f}")

st.write("### Total Cost:", f"{currency} {total_converted:.2f}")

# Confirmation button
if st.button("Place Order"):
    st.success(f"Your order has been placed! Total: {currency} {total_converted:.2f}")
    # Add order processing functionality here, if needed.
