#write a program using to covert from celcius to fahrenheit
def covert():
    celcius=int(input("Temperature in celcius :"))
    print(f"{celcius}°C to °F = {round(celcius*(9/5)+32)} °F")
covert()   #my thought


def f_to_c(f):
    return 5*(f-32)/9
f = int(input("Enter Temperature in F :"))
c = f_to_c(f)
print(f"{round(c ,2)} °C") #harry's Style

#round function 