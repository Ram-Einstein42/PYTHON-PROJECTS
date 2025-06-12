story = "{} went to {} to {} with a {} dragon."
# Ask the user for inputs
name = input("Enter a name: ")
place = input("Enter a place: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")

# Format the story with the user's inputs
story = story.format(name, place, verb, adjective)
# Print the completed story
print("\nHere is your story:")
print(story)