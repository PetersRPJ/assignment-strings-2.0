# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
from mimetypes import guess_all_extensions
from unicodedata import name

first_scorer = 'Ruud Gullit'
second_scorer = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = first_scorer + " " + str(goal_0)+ "," + " " + second_scorer + " " + str(goal_1) 
print (scorers)
# Bij onderstaande code krijg ik tips terug, ik zie alleen geen verschil met hoe de output zou moeten zijn t.o.v. mijn input. 
report = f'{first_scorer} scored in the {goal_0}nd minute {second_scorer} scored in the {goal_1}th minute'
player = 'Jan Wouters'
a = player.find(" ")
first_name = player[:a]
last_name = player[a+1 :]
print (first_name)
print (last_name)
name_short = f"{first_name[:1]}. {last_name}"
chant = (first_name + "! ") * len(first_name)
chant = chant.rstrip()
x = len(chant)
print (x)
good_chant = (chant[:-1] != ' ')
print (good_chant)