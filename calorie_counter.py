"""This program was made for personal use but anybody can use it for making their diet plan for fat loss

Formula for total calories of higher body percentage is weight*20
Formula for total calories of low body percentage is weight*25

Macros
1gm carb = 4cal
1gm protein=4cal
1gm fat=9cal

Protein
Body weight * 1.5

Fats
Body weight * 0.7 (Higher body fat)
Body weight * 1 (Low body fat)

Carbs
(Total calories - (protein + fat))/4)
"""
body_weight=int(input("Enter your body weight: "))
print ("1:Higher body fat \n2:Lower body fat")
fat_percentage=int(input("Give Input: "))
calories=0
carb=0
fat=0
protein=0
def calorie_count():
    global calories
    calories=body_weight*20
    return calories
def fat_count():
    global fat
    if fat_percentage==1:
        fat=body_weight*0.7
        return fat
    else:
        fat=body_weight*1
        return fat
def protein_count():
    global protein
    protein=body_weight*1.5
    return protein
def carb_count():
    global carb
    carb=((calories-(fat+protein))/4)
    return carb
    
print(calorie_count())
print(fat_count())
print (protein_count())
print(carb_count())