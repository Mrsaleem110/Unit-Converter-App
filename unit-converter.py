import streamlit as st

def convert_units(value, from_unit, to_unit, category):
    # Dictionary of unit conversion factors for Length, Mass, and Temperature
    conversion_factors = {
        'Length': {
            'meters': 1,
            'kilometers': 0.001,
            'centimeters': 100,
            'millimeters': 1000,
            'inches': 39.3701,
            'feet': 3.28084,
        },
        'Mass': {
            'grams': 1,
            'kilograms': 0.001,
            'milligrams': 1000,
            'pounds': 0.00220462,
        },
        'Temperature': {
            'celsius': (lambda c: c),
            'fahrenheit': (lambda c: (c * 9/5) + 32),
            'kelvin': (lambda c: c + 273.15),
        },
        'Time': {
            'seconds': 1,
            'minutes': 60,
            'hours': 3600,
            'days': 86400,
            'weeks': 604800,
            'months': 2592000,  # Approximate
            'years': 31536000,
        }
    }
    
    # Check if the selected category is available in the conversion dictionary
    if category == "Temperature":
        # Temperature conversion is a little different since it's not a factor-based conversion
        if to_unit == "fahrenheit":
            return conversion_factors['Temperature']['fahrenheit'](value)
        elif to_unit == "kelvin":
            return conversion_factors['Temperature']['kelvin'](value)
        return value  # Default to return as celsius
    else:
        # For other categories (Length, Mass, Time), use factor-based conversion
        return value * conversion_factors[category][to_unit] / conversion_factors[category][from_unit]

# Streamlit App
def main():
    st.title("📏Unit Converter")

    # Dropdown for selecting category (e.g., Length, Mass, Temperature, Time)
    category = st.selectbox("Choose category", ["Length", "Mass", "Temperature", "Time"])

    # Get available units based on selected category
    if category == "Length":
        units = ["meters", "kilometers", "centimeters", "millimeters", "inches", "feet"]
    elif category == "Mass":
        units = ["grams", "kilograms", "milligrams", "pounds"]
    elif category == "Temperature":
        units = ["celsius", "fahrenheit", "kelvin"]
    elif category == "Time":
        units = ["seconds", "minutes", "hours", "days", "weeks", "months", "years"]

    # Input fields
    from_unit = st.selectbox(f"From {category}", units)
    to_unit = st.selectbox(f"To {category}", units)

    # Value to convert
    value = st.number_input(f"Enter value in {from_unit}", value=1.0)

    if st.button("Convert"):
        # Perform conversion
        result = convert_units(value, from_unit, to_unit, category)
        if result is not None:
            st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
        else:
            st.write("Conversion error, please check input units.")

# Run the app
if __name__ == "__main__":
    main()
