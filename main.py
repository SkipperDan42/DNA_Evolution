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


import dna_functions as fun
import printers as prt
import dna_generator as gen



"""
This is the Random Mutation method of DNA replication.
-   In Random Mutation the replication process reads each base from each of the
    parent chromosomes and randomly selects one as the base for the child 
    chromosome.
-   This can result in very different DNA, as while every base exists in one of
    the parent chromosomes, the genes they make up can now be very different
    to those in the parents.
-   This can result negative mutations (though these are not included in this
    simulation).
-   Random mutation also occurs through Transcription Errors.
"""
def RandomDNAMutation(motherChromosomeA, motherChromosomeB,
                      fatherChromosomeA, fatherChromosomeB):

    # Declaring the child chromosomes to be built
    childChromosomeA = ""
    childChromosomeB = ""

    # Loop through all bases in the DNA of parents (same length)
    for i in range(0,len(motherChromosomeA)):
        motherBaseA = motherChromosomeA[i]
        motherBaseB = motherChromosomeB[i]
        fatherBaseA = fatherChromosomeA[i]
        fatherBaseB = fatherChromosomeB[i]

        """
        The Sex Chromosomes of each parent are assumed to be a mix of the 
        2 chromosomes that each parent has (in reality sex cells have
        23 chromosomes - half of the total 46 (23 pairs) of a person).
        """
        # Add a base to the Mothers Sex Chromosome
        # from either of her Chromosomes
        motherBaseS = fun.RandomBase(motherBaseA, motherBaseB)
        # Add a base to the Fathers Sex Chromosome
        # from either of his Chromosomes
        fatherBaseS = fun.RandomBase(fatherBaseA, fatherBaseB)

        # Randomly generate this base for each of the Child
        # Chromosomes from the Sex Chromosomes of each parent.
        childBaseA = fun.RandomBase(motherBaseS, fatherBaseS)
        childBaseB = fun.RandomBase(motherBaseS, fatherBaseS)

        # Add this gene cluster to the Child Chromosomes
        childChromosomeA = childChromosomeA + childBaseA
        childChromosomeB = childChromosomeB + childBaseB

    # Once loop is complete return the child chromosomes
    return childChromosomeA, childChromosomeB



"""
This is the Signal Switching method of DNA replication.
-   In Signal Switching the replication process reads the entire gene from
    one of the parent chromosomes. This still produces randomised results but 
    ensures that the genes of child chromosome are identical to those on one of
    the parent chromosomes.
-   This reduces the likelihood of negative mutations.
-   True random mutation still occurs through Transcription Errors.
"""
def SignalSwitching(motherChromosomeA, motherChromosomeB,
                    fatherChromosomeA, fatherChromosomeB):

    #Defines the length of the encoding for all genes using the longest
    #gene present.
    numberOfEncodedBases = gen.getNumberOfEncodedBases()

    #Declaring the child chromosomes to be built
    childChromosomeA = ""
    childChromosomeB = ""

    #Define the number of bases that have been read (the counter)
    basesRead = 0

    #Loop through all gene clusters (collection of genes) to be used
    for geneCluster in range(len(gen.genesUsed)):

        #Resets and retrieves the value of the gene length by getting the
        #index values of the encoded base pairs.
        geneLength = 0
        for base in range(1,numberOfEncodedBases):
            geneLength += gen.bases.index(motherChromosomeA[basesRead + base])

        """
        The Sex Chromosomes of each parent are assumed to be a mix of the 
        2 chromosomes that each parent has (in reality sex cells have
        23 chromosomes - half of the total 46 (23 pairs) of a person).
        """
        #Randomly generate this gene cluster for the Mothers Sex Chromosome
        motherGeneS = fun.RandomGene(motherChromosomeA[basesRead : basesRead
                                    + numberOfEncodedBases + geneLength],
                                 motherChromosomeB[basesRead: basesRead
                                    + numberOfEncodedBases + geneLength])

        # Randomly generate this gene cluster for the Fathers Sex Chromosome
        fatherGeneS = fun.RandomGene(fatherChromosomeA[basesRead: basesRead
                                    + numberOfEncodedBases + geneLength],
                                 fatherChromosomeB[basesRead: basesRead
                                    + numberOfEncodedBases + geneLength])

        """
        MUST ADD WAY TO ENSURE GENE ENCODING ON 
        CHILD IS THE SAME FOR BOTH CHROMOSOMES
        """
        # Randomly generate this gene cluster for each of the Child
        # Chromosomes from the Sex Chromosomes of each parent.
        childGeneA = fun.RandomGene(motherGeneS,fatherGeneS)
        childGeneB = fun.RandomGene(motherGeneS,fatherGeneS)

        # Add this gene cluster to the Child Chromosomes
        childChromosomeA = childChromosomeA + childGeneA
        childChromosomeB = childChromosomeB + childGeneB

        # Increase the number of bases read to the end of this gene cluster
        basesRead += geneLength + numberOfEncodedBases

    # Once loop is complete return the child chromosomes
    return childChromosomeA, childChromosomeB


"""This function runs the program by running all other functions."""
def runDNASimulator(numberOfGenes):

    #Randomly create two chromosomes for the mother and father
    motherChromosomeA, motherChromosomeB = gen.BuildSequenceFromGenes(numberOfGenes)
    fatherChromosomeA, fatherChromosomeB = gen.BuildSequenceFromGenes(numberOfGenes)

    #Run the Signal Switching method to create two child chromosomes
    childChASignal, childChBSignal = SignalSwitching(motherChromosomeA,
                                                     motherChromosomeB,
                                                     fatherChromosomeA,
                                                     fatherChromosomeB)

    #Run the Random Mutations method to create the child chromosomes
    childChAMutation, childChBMutation = RandomDNAMutation(motherChromosomeA,
                                                           motherChromosomeB,
                                                           fatherChromosomeA,
                                                           fatherChromosomeB)

    #This code is non-essential but kept for potential relavance
    #It simply prints the DNA sequences as is, with no formatting or colour
    """
    print("Mother Chromosome A    :" + motherChromosomeA)
    print("Mother Chromosome B    :" + motherChromosomeB)
    print("Father Chromosome A    :" + fatherChromosomeA)
    print("Father Chromosome B    :" + fatherChromosomeB)
    """

    #This prints labels for the colours used
    prt.PrintColourLabels()

    #This prints labels for and the parent chromosomes with colours
    print("Mother Chromosome A    :", end = "")
    prt.PrintDNASequence(motherChromosomeA, True)
    print("Mother Chromosome B    :", end = "")
    prt.PrintDNASequence(motherChromosomeB, True)
    print("Father Chromosome A    :", end = "")
    prt.PrintDNASequence(fatherChromosomeA, True)
    print("Father Chromosome B    :", end = "")
    prt.PrintDNASequence(fatherChromosomeB, True)

    #This prints labels for and the child chromosomes with colours and markers
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

    #This prints the features of each person
    print("\nMother:")
    prt.PrintFeatures(motherChromosomeA, motherChromosomeB)
    print("\nFather:")
    prt.PrintFeatures(fatherChromosomeA, fatherChromosomeB)
    print("\nChild [Signal Switching]:")
    prt.PrintFeatures(childChASignal, childChBSignal)
    print("\nChild [Random Mutation]:")
    prt.PrintFeatures(childChAMutation, childChBMutation)



#Either "all" or numeric value (as String)
runDNASimulator("5")



