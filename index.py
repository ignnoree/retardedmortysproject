def ask_symptom(symptom):
    answer=""
    while answer != "yes" and answer !="no":
        answer = input(f"Do you have {symptom}? (yes/no): ").strip().lower()
    return answer == "yes"

has_fever = ask_symptom("a fever")
has_cough = ask_symptom("a cough")
has_headache = ask_symptom("a headache")
has_fatigue = ask_symptom("fatigue")

diagnosis = []


if has_fever:
    diagnosis.append("You have a fever.")
if has_cough:
    diagnosis.append("You have a cough.")
if has_headache:
    diagnosis.append("You have a headache.")
if has_fatigue:
    diagnosis.append("You are feeling fatigued.")


if has_fever and has_cough:
    diagnosis.append("Possibility of a common cold.")
if has_headache and has_fatigue:
    diagnosis.append("Possibility of general weakness.")
if has_fever and has_cough and has_headache and has_fatigue:
    diagnosis.append("Possible Influenza (Flu).")
if has_fever and not has_cough and not has_headache and not has_fatigue:
    diagnosis.append("Possibility of heatstroke.")
if not has_fever and not has_cough and not has_headache and not has_fatigue:
    diagnosis.append(" You seem to be healthy.")
if has_cough and not has_fever:
    diagnosis.append("Possibility of seasonal allergies.")


if has_headache and not has_fever and not has_cough:
    diagnosis.append("Possibility of a migraine.")

if has_fatigue and not has_fever and not has_cough and not has_headache:
    diagnosis.append("Possibility of lack of sleep or stress.")

if has_cough and has_fatigue and not has_fever:
    diagnosis.append("Possibility of bronchitis.")

if has_fever and has_headache and not has_cough:
    diagnosis.append("Possibility of sinus infection.")

if has_fever and has_fatigue and not has_cough and not has_headache:
    diagnosis.append("Possibility of early viral infection.")

print("\n📋 Diagnosis Results:")
for d in diagnosis:
    print("-", d)
