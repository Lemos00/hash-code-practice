

# player score for each
# keep track of amount of ppl that like/dislike each ingredient



# item1 += (player score created by likes and dislikes)*1/(total number of items)
# player score --> sum of all scores for liked ingredients

# loop through --> get all ppl and all ingredients
#   score ingredients
#   score ppl
# 4 cheese tomato pineapple pepper

#issues: - ranking system doesnt really work
#        - too slow, wont run the d and e files
from collections import Counter
ingredients = {}
people = {}
# 2 mushrooms tomatoes
def main():
    global people, ingredients
    with open('test-cases/a_an_example.in.txt') as f:
        lines = f.readlines()

    lineNumber=1
    allLikes = []
    allDislikes=[]
    for i in range(int(lines[0])):
        temp = {}
        likes=[]
        dislikes=[]
        line = lines[lineNumber].split(" ")
       
        for j in range(1,len(line)):
            #adding the likes and removing the \n on the final value
            likes.append(line[j] if j==line[-1] else line[j].rstrip("\n"))
        allLikes+=likes
        temp["likes"]=likes 
        lineNumber+=1
        line =lines[lineNumber].split(" ")
        for j in range(1,len(line)):
            #adding the dislikes and removing the \n on the final value
            dislikes.append(line[j] if j==line[-1] else line[j].rstrip("\n"))
        allDislikes+=dislikes
        temp["dislikes"]=dislikes
        lineNumber+=1
        people[i]=temp

    #print(Counter(allLikes),Counter(allDislikes))
    releventIngredients= list(set(allLikes+allDislikes))
    #print(releventIngredients)
    ingredientCount = len(releventIngredients)
    setPlayerScore(ingredientCount)
    #print(people)
    arr =setIngredientScore(releventIngredients,allLikes,allDislikes)
    findBestPizza(arr)
def setPlayerScore(ingredientCount):
    for p in people:

        people[p]["score"]=((ingredientCount-(len(people[p]["likes"])+len(people[p]["dislikes"])))/(ingredientCount-1))-0.5
def setIngredientScore(releventIngredients,allLikes,allDislikes):
    contradictionScore=0
    for i in releventIngredients:
        l = Counter(allLikes)[i]
        d = Counter(allDislikes)[i]
        length = l+d
        contradictionScore=(l-d)/length+1
        for p in people:
            if i in people[p]["likes"]:
                ingredientScore = people[p]["score"]*(1/len(releventIngredients))*contradictionScore
                if i in ingredients:
                    ingredients[i]+=ingredientScore
                else:
                    ingredients[i]=ingredientScore

            if i in people[p]["dislikes"]:
                ingredientScore = (people[p]["score"])*(1/len(releventIngredients))*contradictionScore
                if i in ingredients:
                    ingredients[i]+=ingredientScore
                else:
                    ingredients[i]=ingredientScore
      

    sortedIngredients = sorted(ingredients.items(), key=lambda x: x[1],reverse=True)
    rankedIngredients =[]
    for i in sortedIngredients:
        rankedIngredients.append(i[0])
    return rankedIngredients

def findBestPizza(sortedIngredients):
    bestPizza = []
    maxNumberOfCustomers=0
    for i in range(len(sortedIngredients)):
        testIngredients = []
        for j in range(len(sortedIngredients)-i):
            testIngredients.append(sortedIngredients[j])
            testValue = testPizza(testIngredients)
        if testValue >=maxNumberOfCustomers:
            bestPizza = testIngredients
            maxNumberOfCustomers= testValue 
    print(bestPizza)

def testPizza(testIngredients):
    numberOfCustomers=0
    for p in people:
    
        likeCondition = (sorted(testIngredients)==sorted(list(set.union(set(testIngredients),set(people[p]["likes"])))))
        dislikeCondition =(not bool(set.intersection(set(testIngredients),set(people[p]["dislikes"]))))
        if likeCondition and dislikeCondition:
            numberOfCustomers+=1
    return numberOfCustomers
if __name__ == "__main__":
    main()

