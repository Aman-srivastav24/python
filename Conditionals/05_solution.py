import random
Weather =["Snowy","Rainy","Sunny"]
input = random.choice(Weather)
print("Input : ",input)

if input =="Sunny":
    print("Go For a Walk")
elif input =="Rainy":
    print("Read a book")
elif input == "Snowy":
    print("Build a SnowMan")

