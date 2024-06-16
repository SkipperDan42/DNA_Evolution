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



import dna_generator as gen
import dna_functions as fun



"""
Prints the labels for all colours used.
"""
def PrintColourLabels():
    print(yellow + "Chromosome Encoding" + reset, end=" | ")
    print(green + "Gene Length Encoding" + reset, end="\n")
    print(black + "From Neither" + reset, end=" | ")
    print(red + "From Mother" + reset, end=" | ")
    print(blue + "From Father" + reset, end=" | ")
    print(purple + "From Both" + reset, end="\n")



"""
This will print out the DNA Sequence.
The function automatically formats the output to have hyphens between each
gene and encoding.
-   The function can be asked to print with colour by passing the parameter 
    True.
-   The function can additionally show (in colour) whether the gene is
    present in the mother or father gene by passing all 4 of the parent
    chromosomes in a list as a parameter.
"""
def PrintDNASequence(dna, withColour=False, parentDNA = []):

    # Defines the length of the encoding for all genes using the
    # longest gene present.
    encoder = gen.getNumberOfEncodedBases()

    # Define the number of bases that have been read (the counter)
    basesRead = 0

    # Loop through all gene clusters (collection of genes) to be used
    for geneClusterLabel in gen.genesUsed:
        geneCluster = gen.genesUsed[geneClusterLabel]

        # Check whether the sequence should be printed with colours
        if withColour:
            print(yellow + dna[basesRead] + reset, end=" - ")
            print(green + dna[basesRead + 1: basesRead + encoder]
                  + reset, end=" - ")
        else:
            print(dna[basesRead], end=" - ")
            print(dna[basesRead + 1: basesRead + encoder], end=" - ")

        # After the encoding has been read increase the value of bases read
        basesRead += encoder

        # Loop through all genes within the geneCluster
        for gene in geneCluster:

            # Check how many bases long the current gene is
            basesToRead = len(list(geneCluster[gene].keys())[0])
            geneColour = ""

            # If the user has specified to print with colour, and the
            # list of parent chromosomes is 4 chromosomes long
            if withColour and (len(parentDNA) == 4):

                # Check if the current gene exists in either chromosome
                # of either parent and set the colour accordingly
                geneColour = fun.checkGeneMatchesParent(dna[basesRead: basesRead + basesToRead],
                                                    parentDNA[0][basesRead: basesRead + basesToRead],
                                                    parentDNA[1][basesRead: basesRead + basesToRead],
                                                    parentDNA[2][basesRead: basesRead + basesToRead],
                                                    parentDNA[3][basesRead: basesRead + basesToRead])
                if geneColour == "B":
                    geneColour = purple
                elif geneColour == "M":
                    geneColour = red
                elif geneColour == "F":
                    geneColour = blue
                elif geneColour == "N":
                    geneColour = black

            # If the end of the dna has been reached print without seperator
            if (basesRead + basesToRead) == len(dna):
                print(geneColour + dna[basesRead: basesRead + basesToRead] + reset, end="\n")
            else:
                print(geneColour + dna[basesRead: basesRead + basesToRead] + reset, end=" - ")

            # Update the value of bases read at the end of the loop
            basesRead += basesToRead



def PrintFeatures(chromosomeA, chromosomeB):

    encoder = gen.getNumberOfEncodedBases()
    basesRead = 0

    for geneGroupLabel in gen.genesUsed:
        geneGroup = gen.genesUsed[geneGroupLabel]

        #Choose which Chromosome to read
        chromosomeToRead = fun.checkChromosomeToRead(chromosomeA, chromosomeB,
                                                        basesRead)

        basesRead += encoder

        for i, gene in enumerate(geneGroup):
            basesToRead = len(list(geneGroup[gene].keys())[0])
            print(gene + ": " +
                  geneGroup[gene][chromosomeToRead[basesRead : basesRead + basesToRead]])

            basesRead += basesToRead


#These are all the Escape Codes used by the printer functions
yellow = "\033[0;33;255m"
green = "\033[0;32;255m"
black = "\033[0;30;255m"
red = "\033[0;31;255m"
blue = "\033[0;34;255m"
purple = "\033[0;35;255m"
reset = "\033[0m"