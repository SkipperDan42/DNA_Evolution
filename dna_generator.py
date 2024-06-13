import random
import dna_dictionaries as dna
import gene_dictionaries as gene



#DEPRICATED - Pure Random Sequence with no Gene Markers
def BuildRandomSequence():
    dnaSequence = ""
    for i in range(12):
        dnaSequence = dnaSequence + bases[random.randint(0,3)]
    return dnaSequence


def BuildSequenceFromGenes(numberOfGenes):
    dnaSequence = ""
    global genesUsed
    global genesChosen

    if not genesChosen:
        genesChosen = True
        if numberOfGenes == "all":
            genesUsed = gene.allGenes
        elif numberOfGenes.strip().isdigit():
            numberOfGenes = int(numberOfGenes)
            if numberOfGenes > len(gene.allGenes):
                genesUsed = getRandomGenes(random.randint(1, len(gene.allGenes)))
            else:
                genesUsed = getRandomGenes(numberOfGenes)


    for geneGroup in genesUsed:
        geneGroupLength = getBasePairCounts(genesUsed[geneGroup])
        encoding = geneGroupLength

        for encodedBasePairs in range(getNumberOfEncodedBases()):
            for i in range(len(bases)-1,-1,-1):
                if i <= encoding:
                    dnaSequence = dnaSequence + bases[i]
                    encoding = encoding - i
                    break

        for geneBasePairs in range(geneGroupLength):
           dnaSequence = dnaSequence + bases[random.randint(0, 3)]

    return dnaSequence



def getRandomGenes(numberOfGenes):
    randomGenes = {}
    for number in range(numberOfGenes):
        geneLabel = random.choice(list(gene.allGenes.keys()))
        randomGenes.update({geneLabel: gene.allGenes[geneLabel]})

    return randomGenes




def getBasePairCounts(currentGenes):
    totalBasePairs = 0
    for gene in currentGenes:
        basePairs = 0
        dictLength = len(currentGenes[gene])

        while dictLength > 1:
            dictLength = dictLength / len(bases)
            basePairs += 1

        totalBasePairs = totalBasePairs + basePairs

    return totalBasePairs



def getNumberOfEncodedBases():
    return (getLongestGene() // (len(bases) - 1)) + 1



def getLongestGene():
    totalBasePairs = 0

    for genes in genesUsed:
        newGeneLength = getBasePairCounts(genesUsed[genes])
        if newGeneLength > totalBasePairs:
            totalBasePairs = newGeneLength

    return totalBasePairs



bases = ["A","C","G","T"]
genesUsed = {}
genesChosen = False

#print(BuildSequenceFromGenes())
#for genes in allGenes:
    #print(getBasePairCounts(allGenes[genes]))
#print(getNumberOfEncodedBases())