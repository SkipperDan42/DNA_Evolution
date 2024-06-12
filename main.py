import random
import dna_dictionaries as dna
import dna_generator as gen


def PrintFeatures(dnaSequence):

    encoder = gen.getNumberOfEncodedBases() - 1
    read = 0

    for geneGroupLabel in gen.allGenes:
        geneGroup = gen.allGenes[geneGroupLabel]
        read += encoder

        for i, gene in enumerate(geneGroup):
            toRead = len(list(geneGroup[gene].keys())[0])
            print(gene + ": " +
                  geneGroup[gene][dnaSequence[read : read + toRead]])

            read = toRead

    #primary = toRead
    #read += toRead
    #toRead = len(list(dna.eye_secondary_colours.keys())[0])
    #if dna.eye_primary_colours[dnaSequence[read - primary : read]] \
    #        in dna.eye_secondary_colours[dnaSequence[read : read + toRead]]:
    #    print("Eyes Secondary Colour: N/A")
    #else:
    #    print("Eyes Secondary Colour: " +
    #          dna.eye_secondary_colours[dnaSequence[read : read + toRead]])


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

        geneLength = 0

        for base in range(gen.getNumberOfEncodedBases()):
            geneLength += gen.bases.index(motherDNA[baseCount + base]) + 1

        if random.randint(0,10) >= 5:
            childGene = motherDNA[baseCount : baseCount + geneLength]
        else:
            childGene = fatherDNA[baseCount : baseCount + geneLength]

        childDNA = childDNA + childGene

        baseCount += geneLength

    return childDNA

motherDNA = gen.BuildSequenceFromGenes()
fatherDNA = gen.BuildSequenceFromGenes()

childDNASignal = SignalSwitching(motherDNA, fatherDNA)
childDNAMutation = RandomMutation(motherDNA, fatherDNA)

print("Mother    :" + motherDNA)
print("Father    :" + fatherDNA)
print("Child [SS]:" + childDNASignal)
print("Child  [M]:" + childDNAMutation)

print("\nMother:")
PrintFeatures(motherDNA)

print("\nFather:")
PrintFeatures(fatherDNA)

print("\nChild [Signal Switching]:")
PrintFeatures(childDNASignal)

print("\nChild [Random Mutation]:")
PrintFeatures(childDNAMutation)