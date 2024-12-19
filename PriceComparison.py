def main():
    print("Price Comparison")
    price_64 = float(input("Price of 64 oz size:"))
    price_32 = float(input("Price of 32 oz size:"))

    per_oz_64 = price_64 / 64
    per_oz_32 = price_32 / 32
    print(f"price per oz (64 oz): {per_oz_64:.2}")
    print(f"price per oz (64 oz): {per_oz_32:.2}")

if __name__ == "main":
    main()