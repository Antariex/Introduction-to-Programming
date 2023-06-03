def windchill(temperature, wind_speed):
    wind_chill_formula = 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
    return wind_chill_formula

def conversion(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperature_user = input("What is the temperature? ")
scale_user = input("Fahrenheit or Celsius (F/C)? ")

if scale_user.upper() == "C":
    temperature = conversion(float(temperature_user))
else:
    temperature = float(temperature_user)

wind_speed = 5
while wind_speed <= 60:
    wind_chill = windchill(temperature, wind_speed)
    wind_chill_rounded = round(wind_chill, 2)
    print(f"At temperature {temperature}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill_rounded}F")
    wind_speed += 5