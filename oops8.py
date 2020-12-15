# multiple inheritance
# making one class from other more class like here is Coolprogrammer
class Employee:
    vpp = 1
    no_of_leaves = 10

    # constructor
    def __init__(self, naam, paisa, kaam):
        self.name = naam
        self.salary = paisa
        self.role = kaam

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    # class method
    @classmethod
    def changeleaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def altercon(cls,string):
        return cls(*string.split("-"))

    # method just to print
    # sometimes u need to run just the employee object on this and not for other objects
    @staticmethod
    def printgood(string):
        print("this is good "+string)



harry = Employee("harry", 1234, "gdv hg")
rohan = Employee("rohan", 3241, "ffrfrf")

class Player:
    vpp = 2
    no_of_games = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"Name is {self.name} and game is {self.game} "

# order of employee player matters. If an attribute is present in both class like name,
# then it will pick up the attri of first class mentioned. like here is employee
class CoolProgrammer(Player, Employee ):
#class CoolProgrammer(Employee, Player):
    language = "cpp"

    def printlan(self):
        print(self.language)



shubham = Player("Shubham", ["Cricket"])
# karan = CoolProgrammer("karan", 845665, "Coolprog")
karan = CoolProgrammer("karan", 845665)

print(karan.printdetails())
karan.printlan()
print(karan.vpp)