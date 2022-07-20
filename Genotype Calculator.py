# input to start
# for quantity of traits being crossed
traitsquantity = input(
    "How many traits are you crossing? Ex. 1 is monohybrid and 2 is dihybrid.")

# initializing strings
# for mother
mother = 1
mothergenotype = ""


# function to evaluate input
# create the mother genotype
def check_mother(evaluate):
    global mothergenotype
    # assign values depending on rec or dom
    if evaluate == "dom":
        mothergenotype = mothergenotype + "1 "
    elif evaluate == "rec":
        mothergenotype = mothergenotype + "0 "
    # error input
    else:
        mothergenotype = mothergenotype + "error"


# create mother genotype
# repeat until all alleles for traits are determined
while mother <= int(traitsquantity):
    # determine between 1st or 2nd allele
    if len(str(mothergenotype)) % 2 == 0 or str(mothergenotype) == "":
        evaluate = input("Is the FIRST allele of the MOTHER trait "
                         + str(mother) + " rec or dom?")
        # run checking function
        check_mother(evaluate)
        # ask for second allele of the trait
        evaluate = input("Is the SECOND allele of the MOTHER trait "
                         + str(mother) + " rec or dom?")
        check_mother(evaluate)
        # move to next trait
        mother = int(mother) + 1
    else:
        # ask for second allele of the trait
        # consider alleles for more than one trait
        evaluate = input("Is the FIRST allele of the MOTHER trait "
                         + str(mother) + " rec or dom?")
        # run checking function
        check_mother(evaluate)
        # move to next trait
        mother = int(mother) + 1

# initializing strings
# for father
father = 1
fathergenotype = ""


# function to evaluate input
# create the father genotype
def check_father(evaluate):
    global fathergenotype
    # assign values depending on rec or dom
    if evaluate == "dom":
        fathergenotype = fathergenotype + "1 "
    elif evaluate == "rec":
        fathergenotype = fathergenotype + "0 "
    # error input
    else:
        fathergenotype = fathergenotype + "error"


# create father genotype
# repeat until all alleles for traits are determined
while father <= int(traitsquantity):
    # determine between 1st or 2nd allele
    if len(str(fathergenotype)) % 2 == 0 or str(fathergenotype) == "":
        evaluate = input("Is the FIRST allele of the FATHER trait "
                         + str(father) + " rec or dom?")
        # run checking function
        check_father(evaluate)
        # ask for second allele of the trait
        evaluate = input("Is the SECOND allele of the FATHER trait "
                         + str(father) + " rec or dom?")
        check_father(evaluate)
        # move to next trait
        father = int(father) + 1
    else:
        # ask for second allele of the trait
        # consider alleles for more than one trait
        evaluate = input("Is the FIRST allele of the FATHER trait "
                         + str(father) + " rec or dom?")
        # run checking function
        check_father(evaluate)
        # move to next trait
        father = int(father) + 1

# change string into list
mothergenotype = mothergenotype.split(" ")
# remove last value in list
# which is always " "
mothergenotype = mothergenotype[:-1]

# change string into list
fathergenotype = fathergenotype.split(" ")
# remove last value in list
# which is always " "
fathergenotype = fathergenotype[:-1]
print(fathergenotype)
print(mothergenotype)

listsplit = 0
counter = 0
combined = ""
potentials = []

while counter < len(mothergenotype):
    while listsplit < len(fathergenotype):
        combined = combined.join(mothergenotype[counter:counter+1])
        combined = combined.join(fathergenotype[listsplit:listsplit+1])
        potentials.append(combined)
        listsplit = listsplit + 1
    counter = counter + 1
    listsplit = 0
print(potentials)

list = ["ok ", "okz ", "okay "]
list_2 = ["bruh ", "pls "]
string = "string"
string = string.join(list)
string = string.join(list_2)
print(string)
