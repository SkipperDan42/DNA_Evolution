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
                           fatherChromosomeA, fatherChromosomeB):

    if (((childChromosome == motherChromosomeA) or
         (childChromosome == motherChromosomeB)) and
        ((childChromosome == fatherChromosomeA) or
         (childChromosome == fatherChromosomeB))):
        return "B"
    elif ((childChromosome == motherChromosomeA) or
         (childChromosome == motherChromosomeB)):
        return "M"
    elif ((childChromosome == fatherChromosomeA) or
         (childChromosome == fatherChromosomeB)):
        return "F"
    else:
        return "N"