traitsquantity = input(
    "How many traits are you crossing? Ex. 1 is monohybrid and 2 is dihybrid.")

mother = 1
mothergenotype = ""


def evaluate_input(evaluate):
    if input != "recessive" or "dominant":
        print("Please print 'dominant' or 'recessive'.")
    else:
        mothergenotype == mothergenotype + str(evaluate)


while mother <= int(traitsquantity):
    if len(str(mothergenotype)) % 2 == 0:
        evaluate = input("Is the first allele of the MOTHER trait "
                         + str(mother) + " recessive or dominant?")
        evaluate_input(evaluate)
        evaluate = input("Is the second allele of the MOTHER trait "
                         + str(mother) + " recessive or dominant?")
        evaluate_input(evaluate)
        mother = int(mother) + 1
    if mother > int(traitsquantity):
        break
