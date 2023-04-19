import math



def distanceFormula(p1, po1, p2, po2):

    distance = math.sqrt((po1 - p1)**2 + (po2 - p2)**2)
    print("The coordinates are: ", distance)


print("Select the distance between two points")

p = int(input("Where is the first x located?: "))
po1 = int(input("Whats the second x located: "))

p2 = int(input("Where is the first y located?: "))
po2 = int(input("Whats the second y located?: "))

distanceFormula(p1,po1,p2,po2)
