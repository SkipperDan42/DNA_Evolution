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
import random



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



def RandomBase(baseA, baseB):

    randomValue = random.randint(1, 100)
    if (randomValue == 1) or (randomValue == 100):
        baseR = gen.bases[random.randint(0, 3)]
    elif randomValue <= 50:
        baseR = baseA
    else:
        baseR = baseB

    return baseR



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