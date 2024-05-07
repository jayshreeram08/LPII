class MedicalDiagnosisSystem:
    def __init__(self):
        self.rules = {
            'flu': ['fever', 'cough', 'sore throat', 'runny nose'],
            'cold': ['cough', 'sore throat', 'stuffy nose'],
            'stomach flu': ['nausea', 'vomiting', 'diarrhea']
        }

    def diagnose(self, symptoms):
        diagnoses = []
        for illness, illness_symptoms in self.rules.items():
            if all(symptom in symptoms for symptom in illness_symptoms):
                diagnoses.append(illness)
        return diagnoses

def main():
    print("Welcome to the Simple Medical Diagnosis System")
    print("Please enter your symptoms separated by commas:")
    user_input = input()
    symptoms = [symptom.strip().lower() for symptom in user_input.split(',')]

    system = MedicalDiagnosisSystem()
    diagnosis = system.diagnose(symptoms)

    if diagnosis:
        print("Based on your symptoms, you may have the following:")
        for illness in diagnosis:
            print(illness)
    else:
        print("Your symptoms do not match any common illnesses in our system.")

if __name__ == "__main__":
    main()