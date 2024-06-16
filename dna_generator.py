# Copyright 2024 D North
# Source: <https://github.com/SkipperDan42/DNA_Evolution>
#
# This file is part of DNA_Evolution.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# For a copy of the GNU General Public License see
# <http://www.gnu.org/licenses/>.



import random
import gene_dictionaries as gene



"""
DEPRICATED - Pure Random Sequence with no Gene Markers
"""
def BuildRandomSequence(numberOfBases):
    dnaSequence = ""
    for i in range(numberOfBases):
        dnaSequence = dnaSequence + bases[random.randint(0,3)]
    return dnaSequence


"""
Builds a DNA sequence including the desired number of Gene Clusters.
These gene clusters may be of different lengths and each contain different 
numbers of genes.
"""
def BuildSequenceFromGenes(numberOfGeneClusters):

    chromosomeA = ""
    chromosomeB = ""

    global genesUsed
    global genesChosen

    if not genesChosen:
        genesChosen = True
        if numberOfGeneClusters == "all":
            genesUsed = gene.allGeneClusters
        elif numberOfGeneClusters.strip().isdigit():
            numberOfGeneClusters = int(numberOfGeneClusters)
            if numberOfGeneClusters > len(gene.allGeneClusters):
                genesUsed = getRandomGenes(random.randint(1, len(gene.allGeneClusters)))
            else:
                genesUsed = getRandomGenes(numberOfGeneClusters)


    for geneGroup in genesUsed:
        geneGroupLength = getBasePairCounts(genesUsed[geneGroup])
        encoding = geneGroupLength

        """
        Codes which Chromosome the Gene will be read from.
        """
        randomValue = random.randint(0, 3)
        if randomValue == 0:
            chromosomeA = chromosomeA + "A"
            chromosomeB = chromosomeB + "A"
        elif randomValue == 1:
            chromosomeA = chromosomeA + "C"
            chromosomeB = chromosomeB + "C"
        elif randomValue == 2:
            chromosomeA = chromosomeA + "G"
            chromosomeB = chromosomeB + "G"
        else:
            chromosomeA = chromosomeA + "T"
            chromosomeB = chromosomeB + "T"

        """
        Codes the value of the gene length using by adding together the
        index values of the encoded base pairs.
        """
        for encodedBasePairs in range(getNumberOfEncodedBases() - 1):

            for i in range(len(bases)-1,-1,-1):
                if i <= encoding:
                    chromosomeA = chromosomeA + bases[i]
                    chromosomeB = chromosomeB + bases[i]
                    encoding = encoding - i
                    break

        for geneBasePairs in range(geneGroupLength):
           chromosomeA = chromosomeA + bases[random.randint(0, 3)]
           chromosomeB = chromosomeB + bases[random.randint(0, 3)]

    return chromosomeA, chromosomeB



def getRandomGenes(numberOfGenes):
    randomGenes = {}
    for number in range(numberOfGenes):
        geneLabel = random.choice(list(gene.allGeneClusters.keys()))
        randomGenes.update({geneLabel: gene.allGeneClusters[geneLabel]})

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


"""
Gets the length of the longest gene to calculate the number of required bases
to encode the genes.
Adds 2 to the value: 1 for using floor division
                     1 for the Chromosome encoding
"""
def getNumberOfEncodedBases():
    return (getLongestGene() // (len(bases) - 1)) + 2



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