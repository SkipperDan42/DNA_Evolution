import random
import dna_dictionaries as dna
import dna_generator as gen



def PrintFeatures(dnaSequence):

    encoder = gen.getNumberOfEncodedBases() - 1
    read = 0

    for geneGroupLabel in gen.genesUsed:
        geneGroup = gen.genesUsed[geneGroupLabel]
        read += encoder

        for i, gene in enumerate(geneGroup):
            toRead = len(list(geneGroup[gene].keys())[0])
            print(gene + ": " +
                  geneGroup[gene][dnaSequence[read : read + toRead]])

            read = toRead



def RandomMutation(motherDNA, fatherDNA):

    childDNA = ""

    for i in range(0,len(motherDNA)):
        motherBase = motherDNA[i]
        fatherBase = fatherDNA[i]

        randomValue = random.randint(1,100)
        if randomValue <= 50:
            childBase = motherBase
        else:
            childBase = fatherBase

        if (randomValue == 1) or (randomValue == 100):
            childBase = TranscriptionError(childBase)

        childDNA = childDNA + childBase

    return childDNA



def SignalSwitching(motherDNA, fatherDNA):

    childDNA = ""
    baseCount = 0

    for geneGroups in range(len(gen.genesUsed)):

        geneLength = 0

        for base in range(gen.getNumberOfEncodedBases()):
            geneLength += gen.bases.index(motherDNA[baseCount + base]) + 1

        if random.randint(1,50) <= 25:
            childGene = motherDNA[baseCount : baseCount + geneLength]
        else:
            childGene = fatherDNA[baseCount : baseCount + geneLength]

        

        childDNA = childDNA + childGene

        baseCount += geneLength

    return childDNA



def TranscriptionError(dna):

    newDNA = ""

    for base in range(len(dna)):
        if True:
            newDNA += gen.bases[random.randint(0,3)]
        else:
            newDNA += base

    return newDNA



#Either "all" or numeric value
numberOfGenes = "1"

motherDNA = gen.BuildSequenceFromGenes(numberOfGenes)
fatherDNA = gen.BuildSequenceFromGenes(numberOfGenes)

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