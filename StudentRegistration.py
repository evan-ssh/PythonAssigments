def main():
    first_name = input("First name: ").title()
    last_name = input("Last name: ").title()
    birth_year = input("Birth year: ")

    print("Welcome", first_name,last_name)
    print("Youre registration is complete.")
    print(f"Temporary password is: {first_name}*{birth_year}")
main()