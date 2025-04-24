
def medi_route_system():
    print("=== MEDI-ROUTE: Smart Hospital Bed & Department Allocation Expert System ===\n")

    # Inputs from doctor or nurse
    name = input("Patient Name: ")
    age = int(input("Age: "))
    symptom = input("Primary Symptom (fever/breathing/pain/accident/pregnancy/other): ").lower()
    severity = input("Severity Level (mild/moderate/severe/critical): ").lower()
    comorbidities = input("Any comorbidities? (diabetes/asthma/heart/kidney/none): ").lower()
    contagious = input("Is the condition contagious (e.g., flu/COVID)? (yes/no): ").lower()
    vitals = input("Are vital signs stable? (yes/no): ").lower()

    print(f"\n🔍 Patient: {name}")
    print("--- SYSTEM RECOMMENDATION ---")

    # Isolation & Infection Control
    if contagious == "yes":
        print("🏥 Allocate: Isolation Ward")
        if severity in ["severe", "critical"]:
            print("🫁 Required: Oxygen supply or ventilator support")
        else:
            print("💊 Monitor: Provide supportive care & isolation protocols")

    # Pregnancy Case
    elif symptom == "pregnancy":
        print("🏥 Allocate: Maternity Ward")
        if severity in ["severe", "critical"]:
            print("🚨 Emergency Obs Unit: Immediate obstetric attention required")

    # Pediatric Case
    elif age < 12:
        print("🏥 Allocate: Pediatric Ward")
        if severity == "critical":
            print("🚨 Pediatric ICU: Intensive monitoring required")

    # Trauma or Accident
    elif symptom == "accident":
        if severity in ["severe", "critical"]:
            print("🏥 Allocate: Emergency + Trauma Surgery")
        else:
            print("🩹 Minor Trauma: General ward with orthopedic consult")

    # Breathing issue or heart
    elif symptom == "breathing" or comorbidities in ["asthma", "heart"]:
        if severity in ["severe", "critical"]:
            print("🏥 Allocate: ICU with Cardio-Pulmonary Support")
        else:
            print("🫁 Allocate: Pulmonology Ward")

    # General
    else:
        if severity == "mild":
            print("🩺 OPD Consultation or Home Treatment")
        elif severity == "moderate":
            print("🏥 Allocate: General Ward")
        elif severity == "severe":
            print("🚨 Allocate: High Dependency Unit (HDU)")
        elif severity == "critical":
            print("🚨 Allocate: ICU – Full Monitoring Required")

    # Final Recommendation
    if vitals == "no":
        print("🔴 Alert: Unstable vitals — immediate intervention needed!")

    print("\n✅ Please register patient for further medical evaluation.")

# Run the system
medi_route_system()