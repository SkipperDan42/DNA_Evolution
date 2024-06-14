import random
import dna_generator as gen



def PrintDNASequence(dna):
    None



def PrintFeatures(chromosomeA, chromosomeB):

    encoder = gen.getNumberOfEncodedBases()
    read = 0

    for geneGroupLabel in gen.genesUsed:
        geneGroup = gen.genesUsed[geneGroupLabel]

        #Choose which Chromosome to read
        chromosomeToRead = ""
        if chromosomeA[read] == "A" or chromosomeA[read] == "T":
            chromosomeToRead = chromosomeA
        else:
            chromosomeToRead = chromosomeB

        read += encoder

        for i, gene in enumerate(geneGroup):
            toRead = len(list(geneGroup[gene].keys())[0])
            print(gene + ": " +
                  geneGroup[gene][chromosomeToRead[read : read + toRead]])

            read = toRead



def RandomDNAMutation(motherChromosomeA, motherChromosomeB,
                      fatherChromosomeA, fatherChromosomeB):

    childChromosomeA = ""
    childChromosomeB = ""

    for i in range(0,len(motherChromosomeA)):
        motherBaseA = motherChromosomeA[i]
        motherBaseB = motherChromosomeB[i]
        fatherBaseA = fatherChromosomeA[i]
        fatherBaseB = fatherChromosomeB[i]

        # Mother Sex Chromosome
        motherBaseS = RandomBase(motherBaseA, motherBaseB)
        # Father Sex Chromosome
        fatherBaseS = RandomBase(fatherBaseA, fatherBaseB)
        # Child Chromosome A
        childBaseA = RandomBase(motherBaseS, fatherBaseS)
        # Child Chromosome B
        childBaseB = RandomBase(motherBaseS, fatherBaseS)

        childChromosomeA = childChromosomeA + childBaseA
        childChromosomeB = childChromosomeB + childBaseB

    return childChromosomeA, childChromosomeB



def RandomBase(baseA, baseB):

    randomValue = random.randint(1, 100)
    if (randomValue == 1) or (randomValue == 100):
        baseS = gen.bases[random.randint(0, 3)]
    elif randomValue <= 50:
        baseS = baseA
    else:
        baseS = baseB

    return baseS



def SignalSwitching(motherDNA, fatherDNA):

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
        else:
            childGene = fatherDNA[baseCount :
                        baseCount + geneLength + numberOfEncodedBases]

        if (randomValue == 1) or (randomValue == 100):
            randomBase = random.randint(0, geneLength)
            baseLocation = baseCount + numberOfEncodedBases + randomBase
            childDNA = childDNA[0 : baseLocation] + \
                       gen.bases[random.randint(0, 3)] + \
                       childDNA[baseLocation + 1 : len(childDNA)]

        childDNA = childDNA + childGene
        baseCount += geneLength + numberOfEncodedBases

    return childDNA



def runDNASimulator(numberOfGenes):

    motherChromosomeA, motherChromosomeB = gen.BuildSequenceFromGenes(numberOfGenes)
    fatherChromosomeA, fatherChromosomeB = gen.BuildSequenceFromGenes(numberOfGenes)
    """
    childChASignal, childChBSignal = SignalSwitching(motherChromosomeA,
                                                     motherChromosomeB,
                                                     fatherChromosomeA,
                                                     fatherChromosomeB)
    """
    childChAMutation, childChBMutation = RandomDNAMutation(motherChromosomeA,
                                                           motherChromosomeB,
                                                           fatherChromosomeA,
                                                           fatherChromosomeB)

    print("Mother Chromosome A    :" + motherChromosomeA)
    print("Mother Chromosome B    :" + motherChromosomeB)
    print("Father Chromosome A    :" + fatherChromosomeA)
    print("Father Chromosome B    :" + fatherChromosomeB)

    #print("Child Chromosome A [SS]:" + childChASignal)
    #print("Child Chromosome B [SS]:" + childChBSignal)
    print("Child Chromosome A [M] :" + childChAMutation)
    print("Child Chromosome B [M] :" + childChBMutation)

    print("\nMother:")
    PrintFeatures(motherChromosomeA, motherChromosomeB)

    print("\nFather:")
    PrintFeatures(fatherChromosomeA, fatherChromosomeB)

    #print("\nChild [Signal Switching]:")
    #PrintFeatures(childChASignal, childChBSignal)

    print("\nChild [Random Mutation]:")
    PrintFeatures(childChAMutation, childChBMutation)



#Either "all" or numeric value
runDNASimulator("4")



