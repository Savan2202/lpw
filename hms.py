class Patient:
    def __init__(self, patient_id, name, age, gender):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def __str__(self):
        return f"Appointment ID: {self.appointment_id}, Patient: {self.patient.name}, Doctor: {self.doctor}, Date: {self.date}, Time: {self.time}"


class HospitalManagementSystem:
    def __init__(self):
        self.patients = {}
        self.appointments = {}
        self.doctors = ["Dr. Smith", "Dr. Johnson", "Dr. Lee"]  
        self.patient_count = 0
        self.appointment_count = 0

    def add_patient(self, name, age, gender):
        self.patient_count += 1
        patient = Patient(self.patient_count, name, age, gender)
        self.patients[self.patient_count] = patient
        print(f"Patient added: {patient}")
    
    def schedule_appointment(self, patient_id, doctor, date, time):
        if patient_id not in self.patients:
            print("Patient not found!")
            return
        self.appointment_count += 1
        appointment = Appointment(self.appointment_count, self.patients[patient_id], doctor, date, time)
        self.appointments[self.appointment_count] = appointment
        print(f"Appointment scheduled: {appointment}")

    def view_patients(self):
        if not self.patients:
            print("No patients found.")
            return
        print("Patients:")
        for patient in self.patients.values():
            print(patient)

    def view_appointments(self):
        if not self.appointments:
            print("No appointments found.")
            return
        print("Appointments:")
        for appointment in self.appointments.values():
            print(appointment)


def main():
    hms = HospitalManagementSystem()

    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. Schedule Appointment")
        print("3. View Patients")
        print("4. View Appointments")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            gender = input("Enter patient gender: ")
            hms.add_patient(name, age, gender)

        elif choice == '2':
            patient_id = int(input("Enter patient ID: "))
            doctor = input("Enter doctor name: ")
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            hms.schedule_appointment(patient_id, doctor, date, time)

        elif choice == '3':
            hms.view_patients()

        elif choice == '4':
            hms.view_appointments()

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()