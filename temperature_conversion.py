# Step 2: Conversion logic
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Step 1: Accept user input
def temperature_converter():
    print("Temperature Converter")
    
    # Step 3: Allow users to choose the conversion direction
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    
    choice = input("Choose the conversion direction (1 or 2): ")
    
    if choice == '1':
        # Celsius to Fahrenheit
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")
        
    elif choice == '2':
        # Fahrenheit to Celsius
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")
        
    else:
        print("Invalid choice! Please choose 1 or 2.")

# Step 4: Test the program
if __name__ == "__main__":
    temperature_converter()
