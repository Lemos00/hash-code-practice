

# player score for each
# keep track of amount of ppl that like/dislike each ingredient



# item1 += (player score created by likes and dislikes)*1/(total number of items)
# player score --> sum of all scores for liked ingredients

# loop through --> get all ppl and all ingredients
#   score ingredients
#   score ppl
# 4 cheese tomato pineapple pepper
ingredients = {}
people = {}
# 2 mushrooms tomatoes
def main():
  global people, ingredients
  with open('a_an_example.in.txt') as f:
      lines = f.readlines()

  playerNumber=1
  
  for i in range(int(lines[0])):
      line = lines[playerNumber].split(" ")
      for j in range(1,len(line)):
          print(line[j],end="")

      playerNumber+=1
      line =lines[playerNumber].split(" ")
      for j in range(1,len(line)):
          print(line[j],end="")
      playerNumber+=1
    
    
if __name__ == "__main__":
    main()