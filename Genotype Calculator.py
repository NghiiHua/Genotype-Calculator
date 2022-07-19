# input to start
# for quantity of traits being crossed
traitsquantity = input(
    "How many traits are you crossing? Ex. 1 is monohybrid and 2 is dihybrid.")

# initializing strings
# for mother
mother = 1
mothergenotype = ""

# create mother genotype
# repeat until all alleles for traits are determined
while mother <= int(traitsquantity):
    # determine between 1st or 2nd allele
    if len(str(mothergenotype)) % 2 == 0 or str(mothergenotype) == "":
        evaluate = input("Is the FIRST allele of the MOTHER trait "
                         + str(mother) + " rec or dom?")
        if evaluate == "dominant":
            mothergenotype == mothergenotype + "1"
        elif evaluate == "recessive":
            mothergenotype ==
        # create the mother genotype
        mothergenotype = mothergenotype + " " + str(evaluate)
        # ask for second allele of the trait
        evaluate = input("Is the SECOND allele of the MOTHER trait "
                         + str(mother) + " rec or dom?")
        # create the mother genotype
        mothergenotype = mothergenotype + " " + str(evaluate)
        # moving to next trait
        mother = int(mother) + 1
    else:
        # ask for second allele of the trait
        # considering alleles for more than one trait
        evaluate = input("Is the FIRST allele of the MOTHER trait "
                         + str(mother) + " rec or dom?")
        # create the mother genotype
        mothergenotype = mothergenotype + " " + str(evaluate)
        # moving to next trait
        mother = int(mother) + 1
