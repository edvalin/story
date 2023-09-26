isRaining = input("Is it raining today? ")
haveMoney = input("Have money? ")


if isRaining == "Yes":
    if haveMoney == "Yes":
        print("Take Uber")
    else:
        print("Take umbrella and walk")
else:
    print("Walk")