import dna_generator as gen
import developerMain

def runTest(numberOfGenes):
    testResults = []
    for test in range(1000):
        thisTest = {"[SS] From Mother": 0,
                    "[SS] From Father": 0,
                    "[Mu] From Mother": 0,
                    "[Mu] From Father": 0}

        motherDNA = gen.BuildSequenceFromGenes(numberOfGenes)
        fatherDNA = gen.BuildSequenceFromGenes(numberOfGenes)

        childDNASignal, signalList = developerMain.SignalSwitching(motherDNA, fatherDNA, True)
        childDNAMutation, mutantList = developerMain.RandomMutation(motherDNA, fatherDNA, True)

        thisTest["[SS] From Mother"] = signalList[0]
        thisTest["[SS] From Father"] = signalList[1]
        thisTest["[Mu] From Mother"] = mutantList[0]
        thisTest["[Mu] From Father"] = mutantList[1]

        testResults.append(thisTest)

    for entry in testResults:
        print(entry)


#Either "all" or numeric value
runTest("all")