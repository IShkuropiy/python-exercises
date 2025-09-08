def main ():

    MAX_DOSE = 25  # mg per kg body weight
    COURSE = 28
    WEEKS = COURSE // 7  # 4 weeks

    print("Griseofulvin Dosage for Guinea Pigs")
    print(f"Max safe dose: {MAX_DOSE} mg/kg/day")
    print(f"Course length: {COURSE} days ({WEEKS} weeks)")

    # Get initial weight
    weight_g = float(input("Enter starting weight in grams: "))

    # Loop through each week
    for week in range(1, WEEKS + 1):
        # Convert grams to kg
        weight_kg = weight_g / 1000.0
        # Calculate daily dose
        daily_dose_mg = weight_kg * MAX_DOSE
    
    print(f"\nWeek {week}:")
    print(f"  Weight: {weight_g:.1f} g")
    print(f"  Daily dose: {daily_dose_mg:.2f} mg")
    
    # Ask for new weight at the end of the week, except after the last week
    if week != WEEKS:
        new_weight = input("Enter updated weight for next week in grams: ")
        # Validate input
        try:
            weight_g = float(new_weight)
        except ValueError:
            print("Invalid input. Using previous weight.")

main()
