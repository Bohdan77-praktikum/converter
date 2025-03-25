def cm_to_m(cm): return cm / 100
def m_to_cm(m): return m * 100
def cm_to_ml(cm): return cm * 10
def ml_to_cm(ml): return ml / 10
def m_to_km(m): return m / 1000
def km_to_m(km): return km * 1000
def m_to_foot(m): return m * 3.28084
def foot_to_m(foot): return foot / 3.28084
def km_to_mile(km): return km * 0.621371
def mile_to_km(mile): return mile / 0.621371
def cm_to_inch(cm): return cm / 2.54
def inch_to_cm(inch): return inch * 2.54
def litres_to_gallon(litres): return litres * 0.264172
def gallon_to_litres(gallon): return gallon / 0.264172
def kg_to_pound(kg): return kg * 2.20462
def pound_to_kg(pound):return pound / 2.20462
def kg_to_g(kg): return kg * 1000
def g_to_kg(g): return g / 1000
def g_to_pound(g): return g * 0.00220462
def pound_to_g(pound): return pound / 0.00220462
def celsius_to_fahrenheit(celsius): return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenhe): return (fahrenhe - 32) * 5/9

    
einheiten = ["cm","m","ml","km","foot","mile","inch","litres","gallon","pound","kg","g","celsius","fahrenheit"]

def converter_eval():
    conversion_dict = {
        "cm_to_m" : cm_to_m,
        "m_to_cm":  m_to_cm,
        "cm_to_ml": cm_to_ml,
        "ml_to_cm": ml_to_cm,
        "m_to_km": m_to_km,
        "km_to_m": km_to_m,
        "m_to_foot": m_to_foot,
        "foot_to_m": foot_to_m,
        "km_to_mile": km_to_mile,
        "mile_to_km": mile_to_km,
        "cm_to_inch":cm_to_inch,
        "inch_to_cm": inch_to_cm,
        "litres_to_gallon": litres_to_gallon,
        "gallon_to_litres": gallon_to_litres,
        "kg_to_pound": kg_to_pound,
        "pound_to_kg": pound_to_kg,
        "kg_to_g": kg_to_g,
        "g_to_kg": g_to_kg,
        "g_to_pound": g_to_pound,
        "pound_to_g": pound_to_g,
        "celsius_to_fahrenheit": celsius_to_fahrenheit,
        "fahrenheit_to_celsius": fahrenheit_to_celsius
    } 

    while True:
        from_unit = input("Geben Sie die Starteinheit ein/Enter the start unit: ").strip().lower()
        if from_unit in einheiten:
            print("Korreckt!")
        else:
            print("Falsh! Bitte eine gültige Einheit eingeben")
            continue 
        to_unit = input("Geben Sie die letzte Einheit ein/Enter the last unit: ").strip().lower()
        if to_unit in einheiten:
            print("Korreckt!")
        else:
            print("Falsh! Bitte eine gültige Einheit eingeben")
            continue
        value_str = input("Geben Sie einen Wert von ein/Enter a value of: ").strip().lower()
        try:
            value = float(value_str)
        except ValueError:
            print("Falsh!")
            value_str = input("Geben Sie einen Wert von ein/Enter a value of: ").strip().lower() 
            value = float(value_str)      
        func_name = f"{from_unit}_to_{to_unit}"
        if func_name in conversion_dict:
            result = conversion_dict[func_name](value)
            print(f"Ergibnes/Results: {result} {to_unit}")
        else:
            print ("No conversion found")
        if input ("Möchten Sie fortfahren? (ja/nein)").strip().lower() !="ja":
            break
if __name__ == "__main__":
    converter_eval()