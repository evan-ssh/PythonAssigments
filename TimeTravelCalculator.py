def main():
 miles_traveled = int(input("Enter miles: "))
 miles_per_hours = int(input("Enter miles per hour: "))
 time_in_hours = miles_traveled / miles_per_hours
 time_in_minutes = miles_traveled % miles_per_hours

 print("Estimated Travel Time")
 print(f"Hours:{time_in_hours:.0f}" )
 print("Minutes:", time_in_minutes)

main()

