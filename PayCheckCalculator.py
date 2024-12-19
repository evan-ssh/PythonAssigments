def main():
    print("Pay Check Calculator")
    hours_worked = float(input("Hours Worked: "))
    hourly_rate = float(input("Hourly Pay Rate: "))
    tax_rate = get_tax()
    gross_pay = grosspay(hours_worked, hourly_rate)
    taxed_amount = taxpay(tax_rate, gross_pay)
    tax_in_percent = tax_rate * 100
    take_home_pay = gross_pay - taxed_amount
    print("Gross Pay:", gross_pay)
   
    print("Tax rate:", tax_in_percent)
    print("Tax amount:", taxed_amount)
    print("Take Home Pay:", take_home_pay)


def taxpay(tax_rate, gross_pay):
    taxed_amount = gross_pay * tax_rate
    return taxed_amount

def grosspay(hours_worked, hourly_rate):
    gross_pay = hours_worked * hourly_rate
    return gross_pay

def get_tax():
    tax = int(input("Tax Rate:"))
    tax_rate = tax/100
    return tax_rate


if __name__ == "__main__":
    main()

