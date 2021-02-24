
#3.12
price = float(input("Enter the price of a meal: ")) #define input as float so user can input whole number or decimal

tip = price * 0.16 

total = price + tip #separate variables onto individual lines

print("A 16% tip would be:", "{:.2f}".format( tip )) #format output so that it gives 2 decimal places

print("The total including tip would be:", "{:.2f}".format( total )) #separate print commands onto individual lines
