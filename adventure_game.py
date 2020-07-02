import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def intro(items, monsters):
    print_pause("You find yourself standing on a sandy beach,")
    print_pause("the sun is blazing and waves crash against the rocky shore.")
    print_pause("A villager said there was a " + monsters + " near here")
    print_pause("that has been terrorizing the fishing village for weeks.")
    print_pause("To your right is a sea cave,")
    print_pause("the tide is low so you may be able to search inside.")
    print_pause("To your left is a beached shipwreck,")
    print_pause("you can smell the soggy, rotting wood.")


def choice_place(items, monsters):
    print_pause("Enter 1 to search the shipwreck.")
    print_pause("Enter 2 to wade through the flooded cave.")
    choice = input("(Please enter 1 or 2.)\n")
    if choice == '1':
        ship_wreck(items, monsters)
    elif choice == '2':
        sea_cave(items, monsters)
    else:
        choice_place(items, monsters)


def ship_wreck(items, monsters):
    if "sword" in items:
        print_pause("You have been here before, the shipwreck is empty.")
        print_pause("You turn around and head back to the sandy beach.")
        choice_place(items, monsters)
    else:
        print_pause("You carefully enter an opening in the shipwreck,")
        print_pause("there is debris everywhere.")
        print_pause("A crab scurries across your boot.")
        print_pause("You notice something shine at the other end of the ship.")
        print_pause("You have found a pirate's sword!")
        print_pause("The hilt is encrusted with sea shells and pearls.")
        items.append("sword")
        print_pause("You take the sword and head back out to the beach.")
        choice_place(items, monsters)


def sea_cave(items, monsters):
    print_pause("You step down into the sea cave,")
    print_pause("salt water fills your boots and crashes at your knees.")
    print_pause("The cave smells like rotting fish.")
    print_pause("Deep within the cave something begins to stir.")
    print_pause("A " + monsters + " creeps out from the darkness.")
    if "sword" in items:
        print_pause("You hold tight to your sword")
        print_pause("and charge through the water at the " + monsters + ".")
        print_pause("Swinging your sword, you wound the beast badly.")
        print_pause("The " + monsters + " shrieks, plunges into the water")
        print_pause("and swims away into the open ocean.")
        print_pause("HUZZAH! You have saved the small fishing village!")
        play_again()
    else:
        print_pause("You're trembling, you have no weapon to defend yourself.")
        print_pause("You may not make it out alive.")
        escape_cave(items, monsters)


def escape_cave(items, monsters):
    print_pause("Enter 1 to defend yourself against the " + monsters + ".")
    print_pause("Enter 2 to escape the sea cave.")
    choice = input("(Please enter 1 or 2.)\n")
    if choice == '1':
        print_pause("You raise your fists in an attempt to defend yourself.")
        print_pause("The beast lunges at you,")
        print_pause("you leap out of the way into the water.")
        print_pause("Submerged in the salty sea water,")
        print_pause("you feel the " + monsters + " grasp your body")
        print_pause("and drag you out to sea. You've lost your life.")
        play_again()
    elif choice == '2':
        print_pause("The beast lunges at you")
        print_pause("but you escape through the cave's opening.")
        choice_place(items, monsters)
    else:
        escape_cave(items, monsters)


def play_again():
    response = input("Play again? Y/N\n").lower()
    if 'y' in response:
        play()
    elif 'n' in response:
        print_pause("Thank you for playing!")
    else:
        play_again()


def play():
    monsters = random.choice(["Sea Dragon", "Siren", "Giant Serpent"])
    items = []
    intro(items, monsters)
    choice_place(items, monsters)


play()
