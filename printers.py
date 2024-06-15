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
import functions as fun



def PrintColourLabels():
    print("\033[0;33;255m" + "Chromosome Encoding" + "\033[0m", end=" | ")
    print("\033[0;32;255m" + "Gene Length Encoding" + "\033[0m", end="\n")
    print("\033[0;30;255m" + "From Neither" + "\033[0m", end=" | ")
    print("\033[0;31;255m" + "From Mother" + "\033[0m", end=" | ")
    print("\033[0;34;255m" + "From Father" + "\033[0m", end=" | ")
    print("\033[0;35;255m" + "From Both" + "\033[0m", end="\n")



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
                geneColour = fun.checkGeneMatchesParent(dna[basesRead: basesRead + basesToRead],
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
        chromosomeToRead = fun.checkChromosomeToRead(chromosomeA, chromosomeB,
                                                        basesRead)

        basesRead += encoder

        for i, gene in enumerate(geneGroup):
            basesToRead = len(list(geneGroup[gene].keys())[0])
            print(gene + ": " +
                  geneGroup[gene][chromosomeToRead[basesRead : basesRead + basesToRead]])

            basesRead += basesToRead