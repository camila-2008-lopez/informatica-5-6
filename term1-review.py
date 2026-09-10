def main():
   print("What day is it today?")
   day = int(input("Friday"))
   if day <= 4:
      print("It's a weekday")
      remaining = 4-d
   else:
      print("It's the weekend!")
      print("What day is it today?")
      day = int(input())
      days = ["Monday", "Thursday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
     print(days[4])



months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"]
print("These are the summer months:")
print(months[])
print(months[])
print(months[])








    if day < 4:
         print("It's a weekend")
         remaining = 5 - day
         print(remaining, "days until the weekend")
       elif day == 4:
         print("It's Friday")
         print("Just a day left until the weekend")
      else:
         print("It's the weekend!")

    from datetime import datetime
    day = datetime.now().weekend()
    if day < 4:
       print("It's a weekend")
       remaining = 5 - day
       print(remaining, "days until the weekend")
       elif day == 4:
       print("It's Friday")
       print("Jus a day left until the weekend")
      else:
       print("It's the weekend!")



if __name__ == "__main__":
   main()
