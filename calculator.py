print("Welcone to Ola's EPIC tip calculator! \nIf you don't tip, you're clown.")
total = float(input("How much was the bill? \n"))
tip = float(input("How much would you like to tip? 10, 12 or 15 percent? \n"))
people = float(input("How many people are splitting the bill? \n"))
final = total / people * (1 + tip / 100)
final = total/people * (1 + tip/100)
print(f"Each person should pay {round(final, 2)} dollars.")
