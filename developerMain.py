import random
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



def RandomMutation(motherDNA, fatherDNA, test = False, countList=None):

    if countList is None:
        countList = [0, 0]
    childDNA = ""

    for i in range(0,len(motherDNA)):
        motherBase = motherDNA[i]
        fatherBase = fatherDNA[i]

        randomValue = random.randint(1,100)
        if randomValue <= 50:
            childBase = motherBase
            countList[0] += 1
        else:
            childBase = fatherBase
            countList[1] += 1

        if (randomValue == 1) or (randomValue == 100):
            childBase = gen.bases[random.randint(0,3)]

        childDNA = childDNA + childBase

    if test:
        return childDNA, countList
    else:
        return childDNA



def SignalSwitching(motherDNA, fatherDNA, test = False, countList=None):

    if countList is None:
        countList = [0, 0]
    numberOfEncodedBases = gen.getNumberOfEncodedBases()
    childDNA = ""
    baseCount = 0

    for geneGroups in range(len(gen.genesUsed)):

        geneLength = 0

        for base in range(numberOfEncodedBases):
            geneLength += gen.bases.index(motherDNA[baseCount + base])

        randomValue = random.randint(1, 100)
        if randomValue <= 50:
            childGene = motherDNA[baseCount :
                        baseCount + geneLength + numberOfEncodedBases]
            countList[0] += 1
        else:
            childGene = fatherDNA[baseCount :
                        baseCount + geneLength + numberOfEncodedBases]
            countList[1] += 1

        if (randomValue == 1) or (randomValue == 100):
            randomBase = random.randint(0, geneLength)
            baseLocation = baseCount + numberOfEncodedBases + randomBase
            childDNA = childDNA[0 : baseLocation] + \
                       gen.bases[random.randint(0, 3)] + \
                       childDNA[baseLocation + 1 : len(childDNA)]

        childDNA = childDNA + childGene

        baseCount += geneLength + numberOfEncodedBases

    if test:
        return childDNA, countList
    else:
        return childDNA



def runDNASimulator(numberOfGenes):

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



#Either "all" or numeric value
#runDNASimulator("1")