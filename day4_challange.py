# Cyber Activity Risk Analyzer


register_number = input("Enter your Register Number: ")


D = int(register_number[-1])
print("\nRegister Digit (D):", D)


activity_scores = [10, 45, 78, 120, -5, 30, 99, 150]   


low_risk = []
medium_risk = []
high_risk = []
critical_risk = []

valid_count = 0
ignored_count = 0


for score in activity_scores:
    
    # Ignore invalid data
    if score < 0:
        ignored_count = ignored_count + 1
        continue
    
    valid_count = valid_count + 1
    
    if score <= 30:
        low_risk.append(score)
    elif score <= 60:
        medium_risk.append(score)
    elif score <= 100:
        high_risk.append(score)
    else:
        critical_risk.append(score)


print("\nBefore Personalized Filtering:")
print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)


removed_count = 0

# If D is EVEN → remove Low Risk
if D % 2 == 0:
    print("\nD is EVEN → Removing Low Risk scores")
    removed_count = len(low_risk)
    low_risk = []

# If D is ODD → remove Critical Risk
else:
    print("\nD is ODD → Removing Critical Risk scores")
    removed_count = len(critical_risk)
    critical_risk = []

print("\nAfter Personalized Filtering:")
print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)

print("\nSummary Report")
print("Total Valid Entries:", valid_count)
print("Ignored Entries:", ignored_count)
print("Removed Due to Personalization:", removed_count)
