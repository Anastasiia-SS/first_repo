def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price * (1 - discount)
        return apply_discount
    if discount < 0 or discount > 1:
        raise ValueError("Discount must be between 0 and 1")
    else:
        apply_discount()
        return price
    
print(discount_price(100, 0.1))  # Expected output: 80.0