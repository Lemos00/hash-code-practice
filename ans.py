from collections import Counter

ingredients = {}
people = {}

def main():
    global people, ingredients
    with open("a_an_example.in.txt") as f:
        lines = f.readlines()

    lineNumber = 1
    allLikes = []
    allDislikes = []
    for i in range(int(lines[0])):
        temp = {}
        likes = []
        dislikes = []

        line = lines[lineNumber].rstrip("\n").split(" ")
        for j in range(1, len(line)):
            likes.append(line[j])
        allLikes += likes
        temp["likes"] = likes
        lineNumber += 1
        line = lines[lineNumber].split(" ")
        for j in range(1, len(line)):

            dislikes.append(line[j])
        allDislikes += dislikes
        temp["dislikes"] = dislikes
        lineNumber += 1
        people[i] = temp

    releventIngredients = list(set(allLikes + allDislikes))
    ingredientCount = len(releventIngredients)
    setPlayerScore(ingredientCount)
    print("Player Score Created")
    arr = setIngredientScore(releventIngredients, allLikes, allDislikes)
    print("Ingredient Score created")
    #maybe loop through once to see all the liked ingredients in the for the current customers and remove ingredients that are not included
    if len(people)<100:
        arr =findBestPizza(arr)
    writeToFile(arr)
    print("Complete")

def writeToFile(arr):
    with open("output.txt", "w") as external_file:
        text = str(len(arr))
        for i in arr:
            text+= " " +i
      
        print(text, file=external_file)
    external_file.close()

def setPlayerScore(ingredientCount):
    for p in people:
        people[p]["score"] = ((ingredientCount - (len(people[p]["likes"]) + len(people[p]["dislikes"])))/ (ingredientCount - 1)) - 0.5


def setIngredientScore(releventIngredients, allLikes, allDislikes):
    trimmedIngredients = {}
    contradictionScore = 0
    for i in releventIngredients:
        l = Counter(allLikes)[i]
        d = Counter(allDislikes)[i]
        length = l + d
        contradictionScore = (l - d) / length + 1
        for p in people:
            if i in people[p]["likes"] or i in people[p]["dislikes"]:
                ingredientScore = (
                    people[p]["score"]
                    * (1 / len(releventIngredients))
                    * (contradictionScore)
                )
                if i in ingredients:
                    ingredients[i] += ingredientScore
                else:
                    ingredients[i] = ingredientScore

    values = ingredients.values()
    min_ = min(values)
    max_ = max(values)
    if len(people) > 100:
        normalizedIngredients = {
            key: ((val - min_) / (max_ - min_)) for (key, val) in ingredients.items()
        }
        trimmedIngredients = {
            key: val for key, val in normalizedIngredients.items() if val > 0
        }
    else:
        trimmedIngredients = ingredients
    sortedIngredients = sorted(
        trimmedIngredients.items(), key=lambda x: x[1], reverse=True
    )
    rankedIngredients = []
    for i in sortedIngredients:
        rankedIngredients.append(i[0])
    return rankedIngredients


def findBestPizza(sortedIngredients):

    bestPizza = []
    maxNumberOfCustomers = 0
    for i in range(len(sortedIngredients)):
        testIngredients = []

        for j in range(len(sortedIngredients) - i):
            testIngredients.append(sortedIngredients[j])
        testValue = testPizza(testIngredients)
        if testValue >= maxNumberOfCustomers:

            bestPizza = testIngredients
            maxNumberOfCustomers = testValue

    return bestPizza


def testPizza(testIngredients):
    numberOfCustomers = 0
    for p in people:
        likeCondition = sorted(testIngredients) == sorted(
            list(set.union(set(testIngredients), set(people[p]["likes"])))
        )
        dislikeCondition = not bool(
            set.intersection(set(testIngredients), set(people[p]["dislikes"]))
        )
        if likeCondition and dislikeCondition:
            numberOfCustomers += 1
    return numberOfCustomers


if __name__ == "__main__":
    main()
