THRESHOLD_FAHRENHEIT = 77

# Beispiel Sensordaten (Temperaturwerte in Celsius)
sensor_data_celsius = [22, 24, 26, 28, 32, 35, 44, 18, 15, 42, 27, 30]

# Funktion zur Umrechnung von Celsius in Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Aufgabe 1: Umrechnung der Temperaturwerte von Celsius in Fahrenheit mit map()
sensor_data_fahrenheit = list(map(celsius_to_fahrenheit, sensor_data_celsius))

# Aufgabe 2: Filtern der Daten über 77°F mit filter()
filtered_data = list(filter(lambda x: x > THRESHOLD_FAHRENHEIT, sensor_data_fahrenheit))

# Aufgabe 3: Tiefster Wert
lowest_temperature = min(filtered_data)
print((
    f"der tiefste Wert ist {lowest_temperature} °F / "
    f"{fahrenheit_to_celsius(lowest_temperature)} °C"
    ))
