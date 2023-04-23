# Author: Ariel Amtequiera
# Purpose: Display a story to the screen.
#I added extra paragraphs to the story, with more words to be filled by the user

print('Please enter the following:\n')

adjective = input('An adjective:')
animal = input('An animal:')
verb = input('A verb:')
exclamation = input('An exclamation:')
second_verb = input('A second verb:')
third_verb = input('A third verb:')
second_adjective = input('A second adjective:')
third_adjective = input('A third adjective:')

print('\nYour story is:\n')

print(f'The other day, I was really in trouble. It all started when I saw a very')
print(f'{adjective.lower()} {animal.lower()} {verb.lower()} down the hallway. "{exclamation.capitalize()}!" I yelled. But all')
print(f'I could think to do was to {second_verb.lower()} over and over. Miraculously,')
print(f'that caused it to stop, but not before it tried to {third_verb.lower()}')
print(f'right in front of my family.')
print(f'When I thought that everything was over, the {animal.lower()} appeared again in front of us. We where such {second_adjective.lower()}')
print(f'Hopefully nothing happens, and all ends like a {third_adjective.lower()} story')