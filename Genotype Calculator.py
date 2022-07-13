traitsquantity = input(
    "How many traits are you crossing? Ex. 1 is monohybrid and 2 is dihybrid.")

mother = 1
mothergenotype = ""

if mother <= int(traitsquantity):
    if len(str(mothergenotype)) % 2 == 1 or str(mothergenotype) == "":
        evaluate = input("Is the first allele of the MOTHER trait "
                         + str(mother) + " rec or dom?")
        mothergenotype = mothergenotype + " " + str(evaluate)
        evaluate = input("Is the second allele of the MOTHER trait "
                         + str(mother) + " rec or dom?")
        mothergenotype = mothergenotype + " " + str(evaluate)
        mother = int(mother) + 1

for element in range(len(mothergenotype)):
    if element != "rec" or "dom":
        mothergenotype = "Restart and print either 'dom' or 'rec'."

print(mothergenotype)
