# We are going to create a mad libs starter project
# We are going to create a story with the help of inputs from a user

# Create a function that uses the input from someone and make sure that the "word_type" they use is going to be a string(str)

def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input


# I created the story first, but these are the defined words to be inputed

Adjective1 = get_input("Adjective")
Place = get_input("Place")
Adjective2 = get_input("Adjective")
Creature = get_input("Creature")
Verb_Present_Tense = get_input("Verb Present Tense")
Adjective3 = get_input("Adjective")
Adjective4 = get_input("Adjective")
Sound = get_input("Sound")
Name_of_Friend = get_input("Name")
Object1 = get_input("Object")
Adjective5 = get_input("Adjective")
Adverb = get_input("Adverb")
Adjective6 = get_input("Adjective")
Emotion = get_input("Emotion")
Adjective7 = get_input("Adjective")
Object2 = get_input("Object")
Noun1 = get_input("Noun")
Adjective8 = get_input("Adjective")
Adjective9 = get_input("Adjective")
Noun2 = get_input("Noun")
Creepy_Phrase = get_input("Creepy Phrase")
Verb_Past_Tense = get_input("Verb Past Tense")
Noun3 = get_input("Noun")
Adjective10 = get_input("Adjective")
Adjective11 = get_input("Adjective")


# I am going to create mad lib structures first so I would know what inputs to add to the story
# Create the story using f strings

story = f"""
Last night, my friends and I decided to explore the old, abondoned {Adjective1} {Place} at the edge of town.

Rumor has it the place is haunted by a {Adjective2} {Creature} that {Verb_Present_Tense} anyone who dates enter.

As we stepped inside, the air turned {Adjective3}, and we heard a {Adjective4} {Sound} echo through the halls.

"Did you hear that?" whispered {Name_of_Friend}, clutching their {Object1} tightly.

Suddenly, a {Adjective5} shadow darted past us, and we all screamed {Adverb}!

"It's just the wind," I said, trying to sound {Adjective6}, but deep down, I felt {Emotion}.

As we moved deeper into the {Place}, we found a {Adjective7} {Object2} covered in {Noun1}.

"This must belong to the {Adjective8} {Creature}!" said {Name_of_Friend}.

Just then, the lights flickered, and a {Adjective9} {Noun2} appeared in front of us.

It whispered, "{Creepy_Phrase}," and we all {Verb_Past_Tense} as fast as we could.

Later, we found out that the {Place} was built on a {Noun3}, and the {Adjective10} {Creature} was protecting a {Adjective11} {Object2} hidden within its walls.

Would you be brave enough to explore it yourself?
"""

# Print the story with the inputed words
print(story)