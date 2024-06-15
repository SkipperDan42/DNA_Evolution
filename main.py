import random
import dna_generator as gen



def PrintDNASequence(dna, withColour=False, parentDNA = []):
    encoder = gen.getNumberOfEncodedBases()
    basesRead = 0

    for geneGroupLabel in gen.genesUsed:
        geneGroup = gen.genesUsed[geneGroupLabel]

        if withColour:
            print("\033[0;33;255m" + dna[basesRead] + "\033[0m", end=" - ")
            print("\033[0;32;255m" + dna[basesRead + 1: basesRead + encoder]
                  + "\033[0m", end=" - ")
        else:
            print(dna[basesRead], end=" - ")
            print(dna[basesRead + 1: basesRead + encoder], end=" - ")

        basesRead += encoder

        for i, gene in enumerate(geneGroup):
            basesToRead = len(list(geneGroup[gene].keys())[0])
            dnaLen = len(dna)
            geneColour = ""
            if withColour and (len(parentDNA) == 4):
                geneColour = checkGeneMatchesParent(dna[basesRead: basesRead + basesToRead],
                                                    parentDNA[0][basesRead: basesRead + basesToRead],
                                                    parentDNA[1][basesRead: basesRead + basesToRead],
                                                    parentDNA[2][basesRead: basesRead + basesToRead],
                                                    parentDNA[3][basesRead: basesRead + basesToRead])
                if geneColour == "B":
                    geneColour = "\033[0;35;255m"
                elif geneColour == "M":
                    geneColour = "\033[0;31;255m"
                elif geneColour == "F":
                    geneColour = "\033[0;34;255m"
                elif geneColour == "N":
                    geneColour = "\033[0;30;255m"

            if (basesRead + basesToRead) == len(dna):
                print(geneColour + dna[basesRead: basesRead + basesToRead] + "\033[0m", end="\n")
            else:
                print(geneColour + dna[basesRead: basesRead + basesToRead] + "\033[0m", end=" - ")

            basesRead += basesToRead


def PrintFeatures(chromosomeA, chromosomeB):

    encoder = gen.getNumberOfEncodedBases()
    basesRead = 0

    for geneGroupLabel in gen.genesUsed:
        geneGroup = gen.genesUsed[geneGroupLabel]

        #Choose which Chromosome to read
        chromosomeToRead = checkChromosomeToRead(chromosomeA, chromosomeB,
                                                 basesRead)

        basesRead += encoder

        for i, gene in enumerate(geneGroup):
            basesToRead = len(list(geneGroup[gene].keys())[0])
            print(gene + ": " +
                  geneGroup[gene][chromosomeToRead[basesRead : basesRead + basesToRead]])

            basesRead += basesToRead



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
        baseR = gen.bases[random.randint(0, 3)]
    elif randomValue <= 50:
        baseR = baseA
    else:
        baseR = baseB

    return baseR



def SignalSwitching(motherChromosomeA, motherChromosomeB,
                    fatherChromosomeA, fatherChromosomeB):

    numberOfEncodedBases = gen.getNumberOfEncodedBases()
    childChromosomeA = ""
    childChromosomeB = ""
    basesRead = 0

    for geneGroups in range(len(gen.genesUsed)):

        """
        Takes the first encoded base to decide which chromosome to read for
        each parent.
        """
        motherChromosomeToRead = checkChromosomeToRead(motherChromosomeA,
                                                       motherChromosomeB,
                                                       basesRead)
        fatherChromosomeToRead = checkChromosomeToRead(fatherChromosomeA,
                                                       fatherChromosomeB,
                                                       basesRead)

        """
        Retrieves the value of the gene length by getting the index values of 
        the encoded base pairs.
        """
        geneLength = 0
        for base in range(1,numberOfEncodedBases):
            geneLength += gen.bases.index(motherChromosomeA[basesRead + base])

        #Mother Gene on Sex Chromosome
        motherGeneS = RandomGene(motherChromosomeA[basesRead : basesRead
                                    + numberOfEncodedBases + geneLength],
                                 motherChromosomeA[basesRead: basesRead
                                    + numberOfEncodedBases + geneLength])
        # Father Sex Gene on Sex Chromosome
        fatherGeneS = RandomGene(fatherChromosomeA[basesRead: basesRead
                                    + numberOfEncodedBases + geneLength],
                                 fatherChromosomeA[basesRead: basesRead
                                    + numberOfEncodedBases + geneLength])
        # Child Gene on Chromosome A
        childGeneA = RandomGene(motherGeneS,fatherGeneS)
        # Child Gene on Chromosome B
        childGeneB = RandomGene(motherGeneS,fatherGeneS)

        childChromosomeA = childChromosomeA + childGeneA
        childChromosomeB = childChromosomeB + childGeneB

        basesRead += geneLength + numberOfEncodedBases

    return childChromosomeA, childChromosomeB



def RandomGene(geneA, geneB):

    geneR = ""
    randomValue = random.randint(1, 100)
    if randomValue <= 50:
        geneR = geneA
    else:
        geneR = geneB

    """
    Transcription errors must take place after the gene has been selected.
    """
    if (randomValue == 1) or (randomValue == 100):
        randomBase = random.randint(0, len(geneR))
        baseLocation = randomBase
        geneR = geneR[0: baseLocation] + \
                gen.bases[random.randint(0, 3)] + \
                geneR[baseLocation + 1: len(geneR)]

    return geneR



"""
Decides which chromosome must be read from the encoded base.
"""
def checkChromosomeToRead(chromosomeA, chromosomeB, basesRead):

    if chromosomeA[basesRead] == "A" or chromosomeA[basesRead] == "T":
        chromosomeToRead = chromosomeA
    else:
        chromosomeToRead = chromosomeB

    return chromosomeToRead



def checkGeneMatchesParent(childChromosome,
                           motherChromosomeA, motherChromosomeB,
                           fatherChromosomeA, fatherChromosomeB,
                           encoder, basesRead, basesToRead):

    motherChromosomeToRead = checkChromosomeToRead(motherChromosomeA,
                                                   motherChromosomeB,
                                                   basesRead - encoder)
    fatherChromosomeToRead = checkChromosomeToRead(fatherChromosomeA,
                                                   fatherChromosomeB,
                                                   basesRead - encoder)

    if ((childChromosome[basesRead: basesRead + basesToRead] ==
        motherChromosomeToRead[basesRead: basesRead + basesToRead])
        and (childChromosome[basesRead: basesRead + basesToRead] ==
        fatherChromosomeToRead[basesRead: basesRead + basesToRead])):
        return "B"
    elif (childChromosome[basesRead: basesRead + basesToRead] ==
        motherChromosomeToRead[basesRead: basesRead + basesToRead]):
        return "M"
    elif (childChromosome[basesRead: basesRead + basesToRead] ==
        fatherChromosomeToRead[basesRead: basesRead + basesToRead]):
        return "F"
    else:
        return "N"



def runDNASimulator(numberOfGenes):

    motherChromosomeA, motherChromosomeB = gen.BuildSequenceFromGenes(numberOfGenes)
    fatherChromosomeA, fatherChromosomeB = gen.BuildSequenceFromGenes(numberOfGenes)

    childChASignal, childChBSignal = SignalSwitching(motherChromosomeA,
                                                     motherChromosomeB,
                                                     fatherChromosomeA,
                                                     fatherChromosomeB)

    childChAMutation, childChBMutation = RandomDNAMutation(motherChromosomeA,
                                                           motherChromosomeB,
                                                           fatherChromosomeA,
                                                           fatherChromosomeB)
    """
    print("Mother Chromosome A    :" + motherChromosomeA)
    print("Mother Chromosome B    :" + motherChromosomeB)
    print("Father Chromosome A    :" + fatherChromosomeA)
    print("Father Chromosome B    :" + fatherChromosomeB)
    """

    print("Mother Chromosome A    :", end = "")
    PrintDNASequence(motherChromosomeA, True)
    print("Mother Chromosome B    :", end = "")
    PrintDNASequence(motherChromosomeB, True)
    print("Father Chromosome A    :", end = "")
    PrintDNASequence(fatherChromosomeA, True)
    print("Father Chromosome B    :", end = "")
    PrintDNASequence(fatherChromosomeB, True)

    parentChromosomes = [motherChromosomeA, motherChromosomeB,
                         fatherChromosomeA, fatherChromosomeB]
    print("Child Chromosome A [SS]:", end = "")
    PrintDNASequence(childChASignal, True, parentChromosomes)
    print("Child Chromosome B [SS]:", end = "")
    PrintDNASequence(childChBSignal, True, parentChromosomes)
    print("Child Chromosome A [M] :", end = "")
    PrintDNASequence(childChAMutation, True, parentChromosomes)
    print("Child Chromosome B [M] :", end = "")
    PrintDNASequence(childChBMutation, True, parentChromosomes)


    print("\nMother:")
    PrintFeatures(motherChromosomeA, motherChromosomeB)
    print("\nFather:")
    PrintFeatures(fatherChromosomeA, fatherChromosomeB)
    print("\nChild [Signal Switching]:")
    PrintFeatures(childChASignal, childChBSignal)
    print("\nChild [Random Mutation]:")
    PrintFeatures(childChAMutation, childChBMutation)



#Either "all" or numeric value
runDNASimulator("4")



