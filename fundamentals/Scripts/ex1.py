# Find the probability
import random

def probability(x , n):
    return round(x/n , 2)

blueBall  = random.randint(0,2)
redBall  = random.randint(2,10)
yellowBall = random.randint(2,10)
totalBalls = blueBall + redBall + yellowBall
print("-"*30)
print("The total number of balls in the bucket are : " , totalBalls)
print("A monkey has affection towards  colored things so he steals 2 balls from the basket ! ")
print("The catch is the blue ball in the whole basket can be zero or one or two")




