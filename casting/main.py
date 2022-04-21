# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
#part 1
leek_price = 2
print ('Leek is '+ str(leek_price) +' euro per kilo.')

#of

#part 2

leek_order = 'leek 4'
number = leek_order.find('4')
leek_order_number = leek_order[4:6]
sum_total = leek_price * int(leek_order_number)
print (sum_total)

#part 3
broccoli_price = 2.34 #euros p/k
broccoli_order = 1.6 #kg
price_order = round(1.6 * 2.34, 2)

print ('1.6kg broccoli costs' + " " + str(price_order) +'e')
