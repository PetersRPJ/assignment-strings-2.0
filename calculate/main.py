# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line
from lib2to3.pgen2.token import PERCENT


broccoli = 2
leek = 2
potato = 3
brussel_sprout = 7
sum_one_each = broccoli+leek+potato+brussel_sprout
avg_price = sum_one_each / 4
num_potatoes = potato * 7
num_broccolis = broccoli * 5
num_leeks = leek * 2
num_brussel_sprouts = brussel_sprout * 10
sum_total = num_broccolis+num_brussel_sprouts+num_leeks+num_potatoes
discount_percentage = 30
discounted_sum_total = sum_total - (sum_total / 100 * discount_percentage)
print (discounted_sum_total)