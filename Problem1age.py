



def whn100(a):
    if len(a) == 2:
        age = 100 - int(a)

    elif len(a) == 4:
        if int(a) >2020 :
            print("You are not yet born..")
            exit()

        elif 1920>int(a) :
            print("You are to old to be alive.")
            exit()
        else:
            age = int(a) + 100

    else:
        print("Invalid input")
    return age
def ageinyear(useryear,input_from_user):
    py = 2020
    if len(input_from_user) == 2:
        a = int(useryear) - py
        age=a+int(input_from_user)
        print(f"you will be {age} years")

    elif len(input_from_user) == 4:
        age = int(useryear)-int(input_from_user)
        print(f"you will be {age} years")

if __name__ == '__main__':
        input_from_user = input("Enter your age or year of birth : ")

        print(f"You will be of 100 years in {whn100(input_from_user)}")
        while True:
            userin = input("Do you wanna know what will be your age in any particular year.If yes type 'y' or 'n' :")
            if userin == "y":
                useryear = int(input("Enter year :"))
                ageinyear(useryear,input_from_user)
                break
            elif userin == "n":
                print("Thankyou")
                exit()
            else:
                continue

