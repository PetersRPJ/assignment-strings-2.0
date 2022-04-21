# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
#1. gesproken taal
from operator import le


most_lan_switz = "German"
most_lan_spain = "Castilian Spanish"
print (most_lan_spain == most_lan_switz)

#2. religie
religion_spain = 'Roman Catholic'
religion_switz = 'Roman Catholic'
print (religion_spain == religion_switz)

#3. name length
length_capital_spain = '6'
length_capital_switz = '4'
print (length_capital_spain != length_capital_switz)

#4. GDP
switz_gdp = 590
spain_gdp = 1714
print (switz_gdp > spain_gdp)

#5. population growth
growth_spain = 0.13
growth_switz = 0.65
print (growth_spain and growth_switz < 1)

#6. population count
population_count_spain=47260584
population_count_switzerland=8453550
population_count_over=10000000
print(population_count_spain > population_count_over or population_count_switzerland > population_count_over)

if ((population_count_spain>population_count_over) and (population_count_switzerland <population_count_over)) or((population_count_spain<population_count_over) and (population_count_switzerland>population_count_over)): 
    Exactly_one_of_the_two_has_population_count_of_over_10_milion = True
else: Exactly_one_of_the_two_has_population_count_of_over_10_milion = False
print(Exactly_one_of_the_two_has_population_count_of_over_10_milion)
