class Personalinfo:

def __init__ (self, name, dob, contact, email):

Self. name = name

Self. dob= dob

Self. Contact = Contact

Self. email = email

def display_personalinfo (self):

print ("Name:", self. Name)

print("DOB:", Self.dob)

print("Contact:", self.Contact)

print("Email:", Self. email)

class Education (Personalinfo):

def __init__(Self, name, dob, contact, email, degree, uni, year, cgpa)

personalinfo.__init__(self, name, dob, contact, email)

self. degres= degree

Self. uni= uni

Self.year= Year

Self.cgpa= cgpa

def display_education (self):

print("Degree:", Self. degree)

print("university:", self.uni)

print ("year", self. year)

print ("CGPA:", Self. cgpa)

class Candidate profile (Education):

def __init__ (self, name, dob, contact, email, degree, uni, year, cgpa, comp, role, exp, Skills):

Education.__init__ (self, name, dob, contact, email, degree, uni, year, cgpa)

Self. comp= comp

Self. role= role

Self. exp =exp

Self. skills= Skills

def display_complete (self):

print("\n CANDIDATE PROFILE")

Self. display_personal()

self. display_education()

Print("company:" ,self.comp)

print(" Role:", self.role).

print("Experience:", self.exp, "years")

print("Skills:", Self. Skills)

def check_eligibility (Self):

if self.exp>5 :

print(" Eligible for senior Role")

else

print("Eligible for Junior Role")

c1=Candidate profile ("Bhavana", "2007","8315407539", "bhavana@gmail.com","B.Tech", "ANITS", 2020, 9.1, "Google", "GM", 6,"Python")

c2=Candidata profile ("Jashmi", "2007", "9357045138", "Jachmi@gmail.com","B.Tech", "NSRIT", 2020, 9.0, "TCS", "Trainee",2,"C+")

c1.display_Complete()

c1.check_eligibility()

c2.display_Complete()

c2.check_eligibility()
