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



import functions as fun
import printers as prt
import dna_generator as gen



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
        motherBaseS = fun.RandomBase(motherBaseA, motherBaseB)
        # Father Sex Chromosome
        fatherBaseS = fun.RandomBase(fatherBaseA, fatherBaseB)
        # Child Chromosome A
        childBaseA = fun.RandomBase(motherBaseS, fatherBaseS)
        # Child Chromosome B
        childBaseB = fun.RandomBase(motherBaseS, fatherBaseS)

        childChromosomeA = childChromosomeA + childBaseA
        childChromosomeB = childChromosomeB + childBaseB

    return childChromosomeA, childChromosomeB



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
        motherChromosomeToRead = fun.checkChromosomeToRead(motherChromosomeA,
                                                            motherChromosomeB,
                                                            basesRead)
        fatherChromosomeToRead = fun.checkChromosomeToRead(fatherChromosomeA,
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
        motherGeneS = fun.RandomGene(motherChromosomeA[basesRead : basesRead
                                    + numberOfEncodedBases + geneLength],
                                 motherChromosomeA[basesRead: basesRead
                                    + numberOfEncodedBases + geneLength])
        # Father Sex Gene on Sex Chromosome
        fatherGeneS = fun.RandomGene(fatherChromosomeA[basesRead: basesRead
                                    + numberOfEncodedBases + geneLength],
                                 fatherChromosomeA[basesRead: basesRead
                                    + numberOfEncodedBases + geneLength])
        # Child Gene on Chromosome A
        childGeneA = fun.RandomGene(motherGeneS,fatherGeneS)
        # Child Gene on Chromosome B
        childGeneB = fun.RandomGene(motherGeneS,fatherGeneS)

        childChromosomeA = childChromosomeA + childGeneA
        childChromosomeB = childChromosomeB + childGeneB

        basesRead += geneLength + numberOfEncodedBases

    return childChromosomeA, childChromosomeB



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

    prt.PrintColourLabels()

    print("Mother Chromosome A    :", end = "")
    prt.PrintDNASequence(motherChromosomeA, True)
    print("Mother Chromosome B    :", end = "")
    prt.PrintDNASequence(motherChromosomeB, True)
    print("Father Chromosome A    :", end = "")
    prt.PrintDNASequence(fatherChromosomeA, True)
    print("Father Chromosome B    :", end = "")
    prt.PrintDNASequence(fatherChromosomeB, True)

    parentChromosomes = [motherChromosomeA, motherChromosomeB,
                         fatherChromosomeA, fatherChromosomeB]
    print("Child Chromosome A [SS]:", end = "")
    prt.PrintDNASequence(childChASignal, True, parentChromosomes)
    print("Child Chromosome B [SS]:", end = "")
    prt.PrintDNASequence(childChBSignal, True, parentChromosomes)
    print("Child Chromosome A [M] :", end = "")
    prt.PrintDNASequence(childChAMutation, True, parentChromosomes)
    print("Child Chromosome B [M] :", end = "")
    prt.PrintDNASequence(childChBMutation, True, parentChromosomes)


    print("\nMother:")
    prt.PrintFeatures(motherChromosomeA, motherChromosomeB)
    print("\nFather:")
    prt.PrintFeatures(fatherChromosomeA, fatherChromosomeB)
    print("\nChild [Signal Switching]:")
    prt.PrintFeatures(childChASignal, childChBSignal)
    print("\nChild [Random Mutation]:")
    prt.PrintFeatures(childChAMutation, childChBMutation)



#Either "all" or numeric value
runDNASimulator("all")



