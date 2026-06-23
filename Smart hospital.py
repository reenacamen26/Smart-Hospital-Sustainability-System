def water_system():
    print("\n💧 Water Management System")

    water_usage = int(input("Enter water usage (liters): "))
    tank_level = int(input("Enter tank level (%): "))

    if water_usage > 500:
        usage_status = "High"
    else:
        usage_status = "Normal"

    if tank_level < 30:
        tank_status = "Low"
    else:
        tank_status = "Sufficient"

    suggestions = []

    if usage_status == "High":
        suggestions.append("Reduce water usage")
    if tank_status == "Low":
        suggestions.append("Refill water tank")
    if usage_status == "High" and tank_status == "Low":
        suggestions.append("Check for leakage")

    print("\n💧 Water Report")
    print("Usage Status :", usage_status)
    print("Tank Status  :", tank_status)
    print("Suggestions  :")
    for s in suggestions:
        print("-", s)


# ================= ELECTRICITY SYSTEM =================
def electricity_system():
    print("\n⚡ Electricity Management System")

    electricity_usage = int(input("Enter electricity usage (kWh): "))
    peak_hours = input("Is it peak hours? (yes/no): ")

    if electricity_usage > 1000:
        usage_status = "High"
    else:
        usage_status = "Normal"

    if peak_hours.lower() == "yes":
        peak_status = "Peak Time"
    else:
        peak_status = "Non-Peak"

    suggestions = []

    if usage_status == "High":
        suggestions.append("Reduce electricity usage")
    if peak_status == "Peak Time":
        suggestions.append("Shift work to non-peak hours")
    if usage_status == "High" and peak_status == "Peak Time":
        suggestions.append("Turn off unused equipment")

    print("\n⚡ Electricity Report")
    print("Usage Status :", usage_status)
    print("Time Status  :", peak_status)
    print("Suggestions  :")
    for s in suggestions:
        print("-", s)


# ================= WASTE MANAGEMENT SYSTEM =================
def waste_system():
    print("\n🗑️ Waste Management System")

    waste_type = input("Enter waste type (plastic / organic / medical): ")
    waste_amount = int(input("Enter waste amount (kg): "))

    if waste_type.lower() == "medical":
        category = "Hazardous"
    elif waste_type.lower() == "plastic":
        category = "Recyclable"
    else:
        category = "Biodegradable"

    if waste_amount > 50:
        level = "High"
    else:
        level = "Normal"

    suggestions = []

    if category == "Hazardous":
        suggestions.append("Dispose using special treatment")
    if category == "Recyclable":
        suggestions.append("Send for recycling")
    if category == "Biodegradable":
        suggestions.append("Use composting")
    if level == "High":
        suggestions.append("Reduce waste generation")

    print("\n🗑️ Waste Report")
    print("Category    :", category)
    print("Waste Level :", level)
    print("Suggestions :")
    for s in suggestions:
        print("-", s)


# ================= LEAK DETECTION SYSTEM =================
def leak_detection_system():
    print("\n🚰 Leak Detection System")

    water_usage = int(input("Enter water usage (liters): "))
    tank_drop = int(input("Enter sudden tank drop (%): "))

    if tank_drop > 20 and water_usage < 300:
        leak_status = "Leak Detected"
    else:
        leak_status = "No Leak"

    print("\n🚰 Leak Report")
    print("Leak Status :", leak_status)

    if leak_status == "Leak Detected":
        print("Suggestions :")
        print("- Check pipelines immediately")
        print("- Stop water supply temporarily")
    else:
        print("- No issues detected")


# ================= RESOURCE PLANNING SYSTEM =================
def resource_planning_system():
    print("\n📊 Resource Planning System")

    past_usage = int(input("Enter last month water usage (liters): "))
    growth = int(input("Enter expected increase (%): "))

    future_usage = past_usage + (past_usage * growth // 100)

    print("\n📊 Planning Report")
    print("Expected Usage :", future_usage)

    if future_usage > 1000:
        print("Suggestions :")
        print("- Increase storage capacity")
        print("- Plan additional supply")
    else:
        print("- Resources are sufficient")


# ================= MAIN MENU =================
while True:
    print("\n🏥 Smart Hospital Sustainability System")
    print("1. Water Management")
    print("2. Electricity Management")
    print("3. Waste Management")
    print("4. Leak Detection")
    print("5. Resource Planning")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        water_system()
    elif choice == "2":
        electricity_system()
    elif choice == "3":
        waste_system()
    elif choice == "4":
        leak_detection_system()
    elif choice == "5":
        resource_planning_system()
    elif choice == "6":
        print("Exiting system...")
        break
    else:
        print("Invalid choice! Try again.")
