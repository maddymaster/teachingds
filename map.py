def fahrenheit(T):
    return ((9/5)*T+32)
def celsius(T):
    return ((5/9)*(T-32))

temp = [0, 33, 41.1, 45.5, 21, 22, 33, 19, 18.4]

F_temps = map(celsius, temp)

print(F_temps)