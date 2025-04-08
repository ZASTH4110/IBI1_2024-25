def calculate_paracetamol_volume(weight_kg, strength):

    # Calculates the required volume of paracetamol (in ml) for a child.

    # Parameters:
    # - weight_kg: weight in kilograms (must be between 10 and 100 kg)
    # - strength: Paracetamol concentration, must be either "120 mg/5 ml" or "250 mg/5 ml"

    # Returns:
    # - Volume of paracetamol in ml needed for the correct dose
    # - Error message if input is invalid

    # Check if weight is within the valid range
    if weight_kg < 10 or weight_kg > 100:
        return "Error: Weight must be between 10 and 100 kg."

    # Check if strength is valid and calculate mg per ml
    if strength == "120 mg/5 ml":
        concentration = 120 / 5  # 24 mg per ml
    elif strength == "250 mg/5 ml":
        concentration = 250 / 5  # 50 mg per ml
    else:
        return "Error: Strength must be '120 mg/5 ml' or '250 mg/5 ml'."

    # Recommended dose is 15 mg per kg of body weight
    dosa_mg = 15 * weight_kg

    # Calculate volume required in ml
    volume_ml = dosa_mg / concentration

    return round(volume_ml, 2)  # Round to 2 decimal places


# Example calls
print(calculate_paracetamol_volume(30, "120 mg/5 ml"))  # Output: 18.75 ml
print(calculate_paracetamol_volume(45, "250 mg/5 ml"))  # Output: 13.5 ml
print(calculate_paracetamol_volume(110, "120 mg/5 ml"))   # Output: Error: Weight must be between 10 and 100 kg.