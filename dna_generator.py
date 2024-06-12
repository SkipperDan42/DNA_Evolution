import random
import dna_dictionaries as dna

def BuildRandomSequence():
    dnaSequence = ""

    for i in range(12):
        dnaSequence = dnaSequence + bases[random.randint(0,3)]

    return dnaSequence


def BuildSequenceFromGenes():
    dnaSequence = ""

    for geneGroup in allGenes:
        geneGroupLength = getBasePairCounts(allGenes[geneGroup])
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

def getLongestGene():
    totalBasePairs = 0

    for genes in allGenes:
        newGeneLength = getBasePairCounts(allGenes[genes])
        if newGeneLength > totalBasePairs:
            totalBasePairs = newGeneLength

    return totalBasePairs

def getNumberOfEncodedBases():
    return (getLongestGene() // (len(bases) - 1)) + 1

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

bases = ["A","C","G","T"]

hairGenes = {"texture": dna.hair_textures,
             "type":    dna.hair_types,
             "colour":  dna.hair_colours}

eyeGenes = {"tone":      dna.eye_tones,
            "primary":   dna.eye_primary_colours,
            "secondary": dna.eye_secondary_colours}

skinGenes = {"type":   dna.skin_types,
             "tone":   dna.skin_tones,
             "colour": dna.skin_colours}

allGenes = {"hair": hairGenes,
            "eye":  eyeGenes,
            "skin": skinGenes}

#print(BuildSequenceFromGenes())

for genes in allGenes:
    print(getBasePairCounts(allGenes[genes]))

print(getNumberOfEncodedBases())