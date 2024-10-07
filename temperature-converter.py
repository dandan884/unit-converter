def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def validate_input(value):
    try:
        temp = float(value)
        return True, temp
    except ValueError:
        return False, None

def main():
    while True:
        print("\nTemperature Unit Converter")
        print("1. Convert from Celsius")
        print("2. Convert from Fahrenheit")
        print("3. Convert from Kelvin")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '4':
            print("Goodbye!")
            break
        
        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
            continue
        
        temp_value = input("Enter the temperature value: ")
        is_valid, temp = validate_input(temp_value)
        
        if not is_valid:
            print("Invalid temperature value. Please enter a number.")
            continue
        
        if choice == '1':    # From Celsius
            fahrenheit = celsius_to_fahrenheit(temp)
            kelvin = celsius_to_kelvin(temp)
            print(f"{temp}°C is equal to:")
            print(f"{fahrenheit:.2f}°F")
            print(f"{kelvin:.2f}K")
            
        elif choice == '2':  # From Fahrenheit
            celsius = fahrenheit_to_celsius(temp)
            kelvin = fahrenheit_to_kelvin(temp)
            print(f"{temp}°F is equal to:")
            print(f"{celsius:.2f}°C")
            print(f"{kelvin:.2f}K")
            
        elif choice == '3':  # From Kelvin
            celsius = kelvin_to_celsius(temp)
            fahrenheit = kelvin_to_fahrenheit(temp)
            print(f"{temp}K is equal to:")
            print(f"{celsius:.2f}°C")
            print(f"{fahrenheit:.2f}°F")

if __name__ == "__main__":
    main()
