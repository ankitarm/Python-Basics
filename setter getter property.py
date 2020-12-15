class Emplopyee:
    def __init__(self, fname, lname):
        self.fname =fname
        self.lname = lname
        self.email = f"{fname}{lname}@gmail.com"

    # function
    def explain(self):
        return f"this employee is {self.fname} {self.lname}"

    @property
    def pemail(self):
        return f"{self.fname}{self.lname}@gmail.com"

    @pemail.setter     #attribute that i want to take as input.setter
    def email(self, string):
        names = string.split("@")[0]
        fname = names.split(".")[0]
        lname = names.split(".")[1]



ht = Emplopyee("Anku", "Meshu")
print(ht.explain())
print(ht.pemail)  # need not be called as function --() because using property decorators
ht.fname="nikku"
print(ht.pemail)
