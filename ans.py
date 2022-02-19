

# player score for each
# keep track of amount of ppl that like/dislike each ingredient



# item1 += (player score created by likes and dislikes)*1/(total number of items)
# player score --> sum of all scores for liked ingredients

# loop through --> get all ppl and all ingredients
#   score ingredients
#   score ppl
# 4 cheese tomato pineapple pepper
from collections import Counter
ingredients = {}
people = {}
# 2 mushrooms tomatoes
def main():
    global people, ingredients
    with open('hash-code-practice/test-cases/a_an_example.in.txt') as f:
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
    setIngredientScore(releventIngredients)
def setPlayerScore(ingredientCount):
    for p in people:
        #((number of ingredients/#of liked ingredients)-number of disliked ingredients)/number of ingrendients
        #people[p]["score"]=((ingredientCount/len(people[p]["likes"]))-len(people[p]["dislikes"]))/ingredientCount
        #people[p]["score"]=round(((len(people[p]["likes"])+len(people[p]["dislikes"]))/(ingredientCount-1)-0.5),3)
        people[p]["score"]=((ingredientCount-(len(people[p]["likes"])+len(people[p]["dislikes"])))/(ingredientCount-1))-0.5
def setIngredientScore(releventIngredients):
    for i in releventIngredients:
        for p in people:
            if i in people[p]["likes"] or i in people[p]["dislikes"]:
                ingredientScore = people[p]["score"]*(1/len(releventIngredients))
                if i in ingredients:
                    ingredients[i]+=ingredientScore
                else:
                    ingredients[i]=ingredientScore
    sorted_ingredients = sorted(ingredients.items(), key=lambda x: x[1],reverse=True)
    rankedIngredients =[]
    for i in sorted_ingredients:
        rankedIngredients.append(i[0])
    print(rankedIngredients)      
        
if __name__ == "__main__":
    main()
#ingridented +=(player score)*(1/ingCount)