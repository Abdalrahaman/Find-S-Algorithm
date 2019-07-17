# sky = ("Sunny", "Rainy", "Cloudy")
# temp = ("Warm", "Cold")
# humdity = ("Normal", "High")
# wind = ("Strong", "Weak")
# water = ("Warm", "Cool")
# forecast = ("Same", "Change")
# enjoy = ("+", "-")

attributesName = (
    ("Sunny", "Rainy", "Cloudy"),
    ("Warm", "Cold"),
    ("Normal", "High"),
    ("Strong", "Weak"),
    ("Warm", "Cool"),
    ("Same", "Change"),
    ("+", "-")
)

outputHypo = []

# first hypotheses ho=< noValue, noValue,noValue, noValue, noValue, noValue >
hypotheses = [None, None, None, None, None, None]

# don't Care => ?
doNotCare = "?"

instances = [
    [attributesName[0][0], attributesName[1][0], attributesName[2][0], attributesName[3][0], attributesName[4][0],
     attributesName[5][0], attributesName[6][0]],

    [attributesName[0][0], attributesName[1][0], attributesName[2][1], attributesName[3][0], attributesName[4][0],
     attributesName[5][0], attributesName[6][0]],

    [attributesName[0][1], attributesName[1][1], attributesName[2][1], attributesName[3][0], attributesName[4][0],
     attributesName[5][1], attributesName[6][1]],

    [attributesName[0][0], attributesName[1][0], attributesName[2][1], attributesName[3][0], attributesName[4][1],
     attributesName[5][1], attributesName[6][0]],
]


def printAllInstances():
    for r in instances:
        for c in r:
            print(c, end=" ")
        print()


def printHypotheses(hypo, n):
    print("h"+str(n)+" =<", end=" ")
    for r in hypo:
        print(r, end=" ")
    print(">")


# print all instances
printAllInstances()

print("///////////// Hypotheses H ////////////////////")


def compute_FindS_Algorithm():
    for i in instances:

        if i[6] == "+":

            if not outputHypo:

                outputHypo.append(instances[0][:len(attributesName)-1])

            else:
                outputHypo.append(list(map(lambda x: x+"", outputHypo[len(outputHypo)-1])))
                for attribute in range(6):
                    if i[attribute] != outputHypo[len(outputHypo)-1][attribute]:
                        outputHypo[len(outputHypo)-1][attribute] = doNotCare
        else:
            outputHypo.append(list(map(lambda x: x+"", outputHypo[len(outputHypo)-1])))


# do operation
compute_FindS_Algorithm()

# print all hypotheses
for h in outputHypo:
    printHypotheses(h, outputHypo.index(h) + 1)
