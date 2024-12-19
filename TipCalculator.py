def main():
    print("Tip calculator")
    cost_meal = float(input("Cost of meal: "))
    tip_percent = float(input("Tip percent: ") ) 
    tip = cost_meal * tip_percent / 100
    total_amount = cost_meal + tip

    print("Tip amount:", tip)
    print("Total amount", total_amount)

if __name__ == "main":
    main()