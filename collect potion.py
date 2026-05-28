print("===================================")
print("Hello, welcome to the potion crafting menu")
print("===================================")

user=input("press any key to continue, or type quit to stop.\n")

herbs=0
mushrooms=0
crystals=0
healing_potions=0
Mana_potions=0
wolf_pelts=0
red_mushroom=0
instant_damage=0

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
        herbs+=3
        mushrooms+=4
        crystals+=2
        red_mushroom+=3
        wolf_pelts+=5
        print("You now have",herbs,"Herbs",mushrooms,"Mushrooms",crystals,"Crystals", wolf_pelts,"wolf pelts",red_mushroom, "red mushrooms")
    
    elif choice=="3":
        print("What potion would you like to craft?")
        print("1.Healing potion, the recipe is 2 herbs and 1 mushrooms")
        print("2.Mana potion, the recipe is 1 herb,1 Mushroom,1 Crystal")
        print("3.Instant damage potion, the reciep is 1 wolf pelt, 2 red mushrooms and 1 herb")
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

        elif potion =="3":
            if wolf_pelts >=1 and red_mushroom >=2 and herbs >=1:
                herbs-=1
                red_mushroom-=2
                wolf_pelts-=1
                instant_damage+=1
                print("You have successfully crafted a instant damage potion!!!","You currently have",instant_damage,"instant damage potions")
    
    elif choice=="4":
        print("Exiting")
        break

else:
    print("Exiting")