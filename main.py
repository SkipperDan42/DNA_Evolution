import random
import dna_dictionaries as dna
import dna_generator as gen


def PrintFeatures(dnaSequence):
    print("Hair: " + dna.hair_textures[dnaSequence[2]] + \
                        dna.hair_types[dnaSequence[3]] + \
                        dna.hair_colours[dnaSequence[4:6]])
    print("Eyes: " + dna.eye_tones[dnaSequence[8]] + \
                    dna.eye_primary_colours[dnaSequence[9]] + \
                    dna.eye_secondary_colours[dnaSequence[10]])
    print("Skin: " + dna.skin_types[dnaSequence[13]] + \
                    dna.skin_tones[dnaSequence[14]] + \
                    dna.skin_colours[dnaSequence[15]])

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
    baseCount = 0

    for geneGroups in range(len(gen.allGenes)):

        geneLength = 2 + \
                     gen.bases.index(motherDNA[baseCount]) + \
                     gen.bases.index(motherDNA[baseCount + 1])

        motherGene = ""
        fatherGene = ""
        for basePairs in range(baseCount,
                               geneLength + baseCount,
                               1):
            motherGene = motherGene + motherDNA[basePairs]
            fatherGene = fatherGene + fatherDNA[basePairs]

        if random.randint(0,2) == 0:
            childGene = motherGene
        else:
            childGene = fatherGene

        childDNA = childDNA + childGene

        baseCount += geneLength

    return childDNA

motherDNA = gen.BuildSequenceFromGenes()
fatherDNA = gen.BuildSequenceFromGenes()

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