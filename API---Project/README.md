##    -----             168051 – JOY MBOTE    ----
##    -----     DOCUMENTATION OF THE ASSIGNMENT  ------
## (Assignment: Build an Object-Oriented System in Python)
## -------------------HOSPITAL MANAGEMENT SYSTEM---------------------------------

I decided to build a hospital management system that provides an interactive system using OOP in Python. The system can manage doctors, patients and appointments. The system uses key concepts such as encapsulation for example it hides the doctors and patients’ id so as to keep the system secure.
It also uses the concepts of inheritance, polymorphism and abstraction which are shown in the code. For Inheritance, the doctor and patient classes both are subclasses of the class Person whereas for polymorphism doctor and patient override the ‘display_details’ method.
The classes used for this specific program include Person, Doctor, Patient and Appointment. The person class is the abstract base class from which the Doctor and Patient class get some of their attributes (name, age , gender) from. 
The Doctor class adds a new attributes that is ‘specialization’ and ‘ age,lability’ which tracks what kind of doctor is available for a certain appointment .It also provides the methods ‘set_availability’ and ‘check_availability' to be able to manage a doctors’ availability status.
Patient class adds symptoms and doctor_assigned as a new attribute to track what kind of symptoms the patient has, and to which doctor the a patient has been assigned to.IT implements the display_details method in order for patient details to be displayed.
The Appointment class can manage information to an appointment including patient, doctor, date and time. It contains methods: schedule, cancel, update appointments. When scheduling appointments the system checks if the doctor is available and assigns doctor to patient if possible.
For users to interact with the system the main() function is used. This function allows users to add doctors and patients, schedule, update and cancel appointments, display the doctor and patient information and lastly exiting the program. Function uses while loop to prompt the user for actions until the exit option is chosen.
All in all, the code demonstrates core OOP concepts, reusability of code like the use of the abstract class(Person) while ensuring methods have been inherited by the subclasses(Doctor and Patient) . The code displays hospital management scenario that can be easily adapted for more complex requirements.
