
inital = int(input("How many zombies to begin with? "))
infection = int(input("How many people does each zombie infect a day? "))
days = int(input("How many since the infection began? "))

zombietotal = inital * infection ** days

print("There are", zombietotal, "zombies outside")