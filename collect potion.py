print("===================================")
print("Hello, welcome to the potion crafting menu")
print("===================================")

user=input("press any key to continue, or type quit to stop.\n")

herbs=0
mushrooms=0
crystals=0
healing_potions=0
Mana_potions=0

while user!="quit":
    print("what u like to do?")
    print("1.Track ingredients and Crafted Potions")
    print("2.Gather resources")
    print("3.Craft potion")
    print("4.Exit the game")
    choice=input("Type what you want to do here\n")
    
    if choice=="1":
        print("Your currently have",herbs,"Herbs",mushrooms,"Mushrooms",crystals,"Crystals",healing_potions,"Healing potions",Mana_potions,"Mana potions.")
    
    elif choice=="2":
        herbs+=1
        mushrooms+=1
        crystals+=1
        print("You now have",herbs,"Herbs",mushrooms,"Mushrooms",crystals,"Crystals")
    
    elif choice=="3":
        print("What potion would you like to craft?")
        print("1.Healing potion, the recipe is 2 herbs and 1 mushrooms")
        print("2.Mana potion, the recipe is 1 herb,1 Mushroom,1 Crystal")
        potion=input("")
        
        if potion=="1":
            if herbs >=2 and mushrooms >=1:
                herbs-=2
                mushrooms-=1
                healing_potions +=1
                print("You have successfully crafted a Healing potion!!!","You currently have",healing_potions,"Healing potion")
            
            elif herbs <2 and mushrooms <1:
                print("You do not have enough resources!")
        
        elif potion =="2":
            if herbs >=1 and mushrooms >=1 and crystals >=1:
                herbs-=1
                mushrooms-=1
                crystals-=1
                Mana_potions+=1
                print("You have successfully crafted a Mana potion!!!","You currently have",Mana_potions,"Mana potions")
    
    elif choice=="4":
        print("Exiting")
        break

else:
    print("Exiting")