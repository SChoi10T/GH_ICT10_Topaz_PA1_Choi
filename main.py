# Temperature Converter: Fahrenheit to Celsius
from pyscript import display, document # pyright: ignore[reportMissingImports]

def temperature_conversion(e):
    document.getElementById('output').innerHTML = ""

    fahrenheit = float(document.getElementById('temperature').value)
    
    celsius = (fahrenheit - 32) * 5/9

    temperature = round(celsius, 1)

    if temperature <= 37.8:
        display(f'Your temperature is: {temperature} °C, you don't have a fever.', target='output')
    elif temperature > 37.8:
        display(f'Your temperature is: {temperature} °C, you have a fever.', target='output')
    else:
        display(f'Invalid input', target='output')


