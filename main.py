import random
import dna_dictionaries

def BuildRandomSequence():
    bases = ["A","C","G","T"]
    dnaSequence = ""

    for i in range(12):
        dnaSequence = dnaSequence + bases[random.randint(0,3)]

    return dnaSequence

def PrintFeatures(dnaSequence):
    print("Hair Colour: " + dna_dictionaries.hair_colours[dnaSequence[0:3]])
    print("Hair Type: " + dna_dictionaries.hair_types[dnaSequence[3:6]])
    print("Eye Colour: " + dna_dictionaries.eye_colours[dnaSequence[6:9]])
    print("Skin Colour: " + dna_dictionaries.skin_colours[dnaSequence[9:12]])

def RandomMutation(motherDNA, fatherDNA):

    childDNA = ""

    for i in range(0,len(motherDNA)):
        motherGene = motherDNA[i]
        fatherGene = fatherDNA[i]

        if random.randint(0,1) == 0:
            childGene = motherGene
        else:
            childGene = fatherGene

        childDNA = childDNA + childGene

    return childDNA

def SignalSwitching(motherDNA, fatherDNA):

    childDNA = ""

    for i in range(0,len(motherDNA),3):
        motherGene = motherDNA[i] + motherDNA[i + 1] + motherDNA[i + 2]
        fatherGene = fatherDNA[i] + fatherDNA[i + 1] + motherDNA[i + 2]

        if random.randint(0,2) == 0:
            childGene = motherGene
        else:
            childGene = fatherGene

        childDNA = childDNA + childGene

    return childDNA

motherDNA = BuildRandomSequence()
fatherDNA = BuildRandomSequence()

childDNASignal = SignalSwitching(motherDNA, fatherDNA)
childDNAMutation = RandomMutation(motherDNA, fatherDNA)

print(motherDNA)
print(fatherDNA)
#print(childDNASignal)
#print(childDNAMutation)

print("\nMother:")
PrintFeatures(motherDNA)

print("\nFather:")
PrintFeatures(fatherDNA)

print("\nChild [Signal Switching]:")
PrintFeatures(childDNASignal)

print("\nChild [Random Mutation]:")
PrintFeatures(childDNAMutation)