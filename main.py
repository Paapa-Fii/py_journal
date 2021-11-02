
#MY FIRST MAD LIB GAME
adjective1 = input("Enter an adjective and click enter: ")
adjective2 = input("Enter another adjective and click enter: ")
bird = input("Enter name of type of bird and click enter: ")
room = input("Enter a type of room in a house and click enter: ")
verb1 = input("Enter a verb (past tense) and click enter: ")
verb2 = input("Enter a another verb and click enter: ")
rel_name = input("Enter a relative's name and click enter: ")
noun1 = input("Enter a noun and click enter: ")
liquid = input("Enter a liquid you know and click enter: ")
verb3 = input("Enter a verb which ends in -ing you know and click enter: ")
body = input("Enter body part in the plural form and click enter: ")
noun2 = input("Enter a noun(plural) you know and click enter: ")
verb4 = input("Enter another verb ending in -ing and click enter: ")
noun3 = input("Enter another noun you know and click enter: ")


story = "It was a " + adjective1 + ", cold November day. I\n" \
        "woke up to the " + adjective2 + " smell of " + bird + "\n" \
        "roasting in the " + room + " downstairs.\n" \
        "I " + verb1 + " down the stairs to see if I could\n" \
        "help " + verb2 + " the dinner. My mom said,\n" \
        "See if " + rel_name + " needs a fresh " + noun1 + ". So I \n " \
        "carried a tray of glasses of " + liquid + " into\n" \
        "the " + verb3 + " room. When I got there, I \n " \
        "couldn't believe my " + body + "! There were\n" \
        "" + noun2 + " " + verb4 + " on the " + noun3 + "!"

print(story)

