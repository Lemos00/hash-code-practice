

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

    playerNumber=1
    likes = []
    dislikes=[]
    for i in range(int(lines[0])):

        line = lines[playerNumber].split(" ")
        for j in range(1,len(line)):
            #adding the likes and removing the \n on the final value
            likes.append(line[j] if j==line[-1] else line[j].rstrip("\n"))

        playerNumber+=1
        line =lines[playerNumber].split(" ")
        for j in range(1,len(line)):
            #adding the dislikes and removing the \n on the final valueF
            dislikes.append(line[j] if j==line[-1] else line[j].rstrip("\n"))

        playerNumber+=1
    print(Counter(likes),Counter(dislikes))
    releventIngredients= list(set(likes+dislikes))
    print(releventIngredients)


if __name__ == "__main__":
    main()