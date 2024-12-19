def main():
    miles_traveled = int(input(""))
    miles_per_hours = int(input(""))
    time_in_hours = miles_traveled / miles_per_hours
    time_in_minutes = miles_traveled % miles_per_hours

    print("Estimated Travel Time")
    print("Hours:", time_in_hours)
    print("Minutes:", time_in_minutes)

    
main()

