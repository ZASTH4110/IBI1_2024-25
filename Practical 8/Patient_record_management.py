class patients:
    def __init__(self, name, age, date_of_latest_admission, medical_history):
        self.name = name
        self.age = age
        self.date_of_latest_admission = date_of_latest_admission
        self.medical_history = medical_history
    def print_information_of_patient(self):
        print("Name:",self.name, "  Age:",self.age, "  Date of Latest Admission:",self.date_of_latest_admission, "  Medical History:",self.medical_history)

#example of creating a patient object and printing the information
patient1 = patients("John Doe", 30, "2023-10-01", "No known allergies")
patient1.print_information_of_patient()