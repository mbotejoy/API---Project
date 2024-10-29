from abc import ABC, abstractmethod

# Base abstract class
class Person(ABC):
    def __init__(self, name, age, gender, id):
        self.name = name
        self.age = age
        self.gender = gender
        # Private attribute
        self.__id = id

    # Abstract method
    @abstractmethod
    def display_details(self):
        pass

    def id_info(self):
        return self.__id

# Doctor is a subclass of class Person     
class Doctor(Person):
    def __init__(self, name, age, gender, id, specialization):
        super().__init__(name, age, gender, id)
        self.specialization = specialization
        self.__availability = True  # Doctor is initially available

    # Overridden method (Polymorphism)
    def display_details(self):
        availability_status = "Available" if self.check_availability() else "Not Available"
        print(f"Doctor Name: {self.name}, Age: {self.age}, Gender: {self.gender}, "
              f"Specialization: {self.specialization}, Availability: {availability_status}")

    def set_availability(self, is_available):
        self.__availability = is_available

    def check_availability(self):
        return self.__availability

# Patient subclass of Person   
class Patient(Person):
    def __init__(self, name, age, gender, id, symptoms):
        super().__init__(name, age, gender, id)
        self.symptoms = symptoms
        self.doctor_assigned = None

    def display_details(self):
        doctor_name = self.doctor_assigned.name if self.doctor_assigned else "None"
        print(f"Patient Name: {self.name}, Age: {self.age}, Gender: {self.gender}, "
              f"Symptoms: {self.symptoms}, Doctor Assigned: {doctor_name}")

    def assign_doctor(self, doctor):
        if doctor.check_availability():
            self.doctor_assigned = doctor
            doctor.set_availability(False)
            print(f"Doctor {doctor.name} assigned to {self.name}")
        else:
            print(f"Doctor {doctor.name} is not available.")

#Appointment class
class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def schedule_appointment(self):
        if self.doctor.check_availability():
            self.patient.assign_doctor(self.doctor)
            print(f"Appointment with ID {self.appointment_id} scheduled on {self.date} at {self.time} with Dr. {self.doctor.name}")
        else:
            print(f"Doctor {self.doctor.name} is not available.")

    def cancel_appointment(self):
        if self.patient.doctor_assigned == self.doctor:
            self.doctor.set_availability(True)
            self.patient.doctor_assigned = None
            print(f"Appointment {self.appointment_id} has been canceled.")
        else:
            print("No appointment found to cancel.")

    def update_appointment(self, new_date, new_time):
        self.date = new_date
        self.time = new_time
        print(f"Appointment {self.appointment_id} updated to {self.date} at {self.time}")

# Interactive System using the method main
def main():
    doctors = []
    patients = []
    appointments = []

    while True:
        print("\nHospital Management System")
        print("1. Add Doctor")
        print("2. Add Patient")
        print("3. Schedule Appointment")
        print("4. Update Appointment")
        print("5. Cancel Appointment")
        print("6. Display All Doctors")
        print("7. Display All Patients")
        print("8. Exit")

        choice = input("Enter your choice: ")

#Code to input doctors's details into the system
        if choice == "1":
            name = input("Enter doctor's name: ")
            age = input("Enter age: ")
            gender = input("Enter gender: ")
            id = input("Enter ID: ")
            specialization = input("Enter specialization: ")
            doctors.append(Doctor(name, age, gender, id, specialization))
            print("Doctor added successfully!")

#Code for user to input patient's details
        elif choice == "2":
            name = input("Enter patient's name: ")
            age = input("Enter age: ")
            gender = input("Enter gender: ")
            id = input("Enter ID: ")
            symptoms = input("Enter symptoms: ")
            patients.append(Patient(name, age, gender, id, symptoms))
            print("Patient added successfully!")

#Code used to be able to use to add an appointment
        elif choice == "3":
            patient_name = input("Enter patient's name: ")
            doctor_name = input("Enter doctor's name: ")
            date = input("Enter date of appointment (YYYY-DD-MM): ")
            time = input("Enter time of the appointment (HH-MM): ")

            patient = next((p for p in patients if p.name == patient_name), None)
            doctor = next((d for d in doctors if d.name == doctor_name), None)

            if patient and doctor:
                appointment_id = len(appointments) + 1
                appointment = Appointment(appointment_id, patient, doctor, date, time)
                appointment.schedule_appointment()
                appointments.append(appointment)
            else:
                print("Invalid patient or doctor name.")

#Updating the appointment
        elif choice == "4":
            appointment_id = int(input("Enter appointment ID to update: "))
            new_date = input("Enter new date for the appointment: ")
            new_time = input("Enter new time for the appointment: ")
            appointment = next((a for a in appointments if a.appointment_id == appointment_id), None)
            if appointment:
                appointment.update_appointment(new_date, new_time)
                print("Updated Successfully")
            else:
                print("Invalid appointment ID.")

#Cancelling the appointment
        elif choice == "5":
            appointment_id = int(input("Enter appointment ID to cancel: "))
            appointment = next((a for a in appointments if a.appointment_id == appointment_id), None)
            if appointment:
                appointment.cancel_appointment()
                appointments.remove(appointment)
            else:
                print("Invalid appointment ID.")

#Displaying a list of doctors
        elif choice == "6":
            print("List of Doctors:")
            for doctor in doctors:
                doctor.display_details()

#Displaying a list of Patients
        elif choice == "7":
            print("List of Patients:")
            for patient in patients:
                patient.display_details()

#Code to Exit program
        elif choice == "8":
            print("Exiting the system. Have a great day!")
            break

        else:
            print("Invalid choice. Please try again.")
            #Output to be displayed if no number is inserted that is available from the list is chosen
            
#Calling of the main function
if __name__ == "__main__":
    main()
