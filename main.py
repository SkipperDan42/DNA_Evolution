import random
import dna_dictionaries as dna
import dna_generator as gen


def PrintFeatures(dnaSequence):
    encoder = gen.getNumberOfEncodedBases() - 1
    read = 0

    for 
    read += encoder
    toRead = len(list(dna.hair_textures.keys())[0])
    print("Hair Texture: " +
          dna.hair_textures[dnaSequence[read : read + toRead]])

    read += toRead
    toRead = len(list(dna.hair_types.keys())[0])
    print("Hair Type: " +
          dna.hair_types[dnaSequence[read : read + toRead]])

    read += toRead
    toRead = len(list(dna.hair_colours.keys())[0])
    print("Hair Colour: " + dna.hair_colours[dnaSequence[read : read + toRead]])

    read += toRead + encoder
    toRead = len(list(dna.eye_tones.keys())[0])
    print("Eyes Tone: " + dna.eye_tones[dnaSequence[read : read + toRead]])

    read += toRead
    toRead = len(list(dna.eye_primary_colours.keys())[0])
    print("Eyes Primary Colour: " +
          dna.eye_primary_colours[dnaSequence[read : read + toRead]])

    primary = toRead
    read += toRead
    toRead = len(list(dna.eye_secondary_colours.keys())[0])
    if dna.eye_primary_colours[dnaSequence[read - primary : read]] \
            in dna.eye_secondary_colours[dnaSequence[read : read + toRead]]:
        print("Eyes Secondary Colour: N/A")
    else:
        print("Eyes Secondary Colour: " +
              dna.eye_secondary_colours[dnaSequence[read : read + toRead]])

    read += toRead + encoder
    toRead = len(list(dna.skin_types.keys())[0])
    print("Skin Type: " + dna.skin_types[dnaSequence[read : read + toRead]])

    read += toRead
    toRead = len(list(dna.skin_tones.keys())[0])
    tone = dna.skin_tones[dnaSequence[read : read + toRead]]
    read += toRead
    toRead = len(list(dna.skin_colours.keys())[0])
    colour = dna.skin_colours[dnaSequence[read: read + toRead]]
    print("Skin Tone: " + tone + " " + colour)


def RandomMutation(motherDNA, fatherDNA):

    childDNA = ""

    for i in range(0,len(motherDNA)):
        motherGene = motherDNA[i]
        fatherGene = fatherDNA[i]

        if random.randint(0,1) == 0:
            childGene = motherGene
        else:
            childGene = fatherGene

        childDNA = childDNA + childGene

    return childDNA

def SignalSwitching(motherDNA, fatherDNA):

    childDNA = ""
    baseCount = 0

    for geneGroups in range(len(gen.allGenes)):

        geneLength = gen.getNumberOfEncodedBases() + \
                     gen.bases.index(motherDNA[baseCount]) + \
                     gen.bases.index(motherDNA[baseCount + 1])

        motherGene = ""
        fatherGene = ""
        for basePairs in range(baseCount,
                               geneLength + baseCount,
                               1):
            motherGene = motherGene + motherDNA[basePairs]
            fatherGene = fatherGene + fatherDNA[basePairs]

        if random.randint(0,2) == 0:
            childGene = motherGene
        else:
            childGene = fatherGene

        childDNA = childDNA + childGene

        baseCount += geneLength

    return childDNA

motherDNA = gen.BuildSequenceFromGenes()
fatherDNA = gen.BuildSequenceFromGenes()

childDNASignal = SignalSwitching(motherDNA, fatherDNA)
childDNAMutation = RandomMutation(motherDNA, fatherDNA)

print(motherDNA)
print(fatherDNA)
#print(childDNASignal)
#print(childDNAMutation)

print("\nMother:")
PrintFeatures(motherDNA)

print("\nFather:")
PrintFeatures(fatherDNA)

print("\nChild [Signal Switching]:")
PrintFeatures(childDNASignal)

print("\nChild [Random Mutation]:")
PrintFeatures(childDNAMutation)