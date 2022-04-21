# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
action_1 = 'take cows to cowshed'
action_2 = 'milk cows'
action_3 = 'fertilize pasture'
action_4 = 'mow grass'
action_5 = 'wait'
action_6 = 'take cows back to pasture'

def farm_action(weather,time,milk_status,location,season,slurrytank_status,grass_status):
    if time == 'night' and location != 'cowshed' or weather == 'rainy' and location != 'cowshed':
        return action_1
    elif milk_status == True and location == 'pasture':
        return (action_1 + '\n' + action_2 + '\n' + action_6)
    elif weather != 'sunny' or weather != 'windy' and slurrytank_status == True and location == 'cowshed':
        return (action_3)
    elif slurrytank_status == True and location == 'pasture' and weather != 'sunny' or weather != 'windy':
        return (action_1 + '\n' + action_3 + '\n' + action_6)
    elif grass_status == True and season == 'spring' and weather == 'sunny' and location == 'cowshed':
        return (action_4)
    elif grass_status == True and season == 'spring' and weather == 'sunny' and location == 'pasture':
        return (action_1 + '\n' + action_4 + '\n' + action_6)
    else:
        return (action_5)

print (farm_action('windy','night', True,'cowshed','winter', True, True))
