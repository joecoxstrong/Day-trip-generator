

import random

destination = ['Washington D.C.', 'Richmond, VA', 'Virginia Beach, VA', 'Raleigh, NC']
restaurant = ['The Reserve', 'Bell Greek', 'Riptides', 'Brocks BBQ']
mode_of_transportation = ['Car', 'Train', 'Bus', 'Hitch hike']
entertainment = ['a movie', 'an escape room', 'visit a museum', 'take a cave tour']


def generate_destination():
    random_destination = random.choice(destination)
    user_approval = input('We have selected ' +random_destination+ ' for your destination! Does this sound good? Enter y/n: ')
    while user_approval == 'n':
        print('Ok, let us select a new destination.')
        generate_destination()
    else:
        print("Excelent choice. Now let's select your mode of transportation.")
        return random_destination
        
    
           

# def generate_destination():
#     random_destination = random.choice(destination)
#     user_approval = input('We have selected ' +random_destination+ ' for your destination! Does this sound good? Enter y/n: ')
#     if user_approval == 'y':
#         return random_destination
#         print("Excelent choice. Now let's select your mode of transportation.")
        
#     else:
#         print('Ok, let us select a new destination.')
#         generate_destination()
                

def generate_restaurant():
    random_restaurant = random.choice(restaurant)
    # print(random_restaurant)
    user_approval = input('We have selected ' +random_restaurant+ ' for your dinner! Does this sound good? Enter y/n: ')
    if user_approval == 'y':
        return random_restaurant
        print("Excelent choice.")
        
    else:
        print('Ok, let us select a new restaurant.')
        generate_restaurant()

def generate_transportation():
    random_transportation = random.choice(mode_of_transportation)
    # print(random_transportation)
    user_approval = input('We have selected ' +random_transportation+ ' for your mode of transportation! Does this sound good? Enter y/n: ')
    if user_approval == 'y':
        return random_transportation
        print("Excelent choice. Let's select an activity now.")
        
    else:
        print('Ok, let us select a new mode of transportation.')
        generate_transportation()

def generate_entertainment():
    random_entertainment = random.choice(entertainment)
    # print(random_entertainment)           
    user_approval = input('We have selected ' +random_entertainment+ ' for your entertainment! Does this sound good? Enter y/n: ')
    if user_approval == 'y':
        return random_entertainment
        print("Excelent choice. Now let's choose a restaurant for dinner.")
        
    else:
        print('Ok, let us select a new activity.')
        generate_entertainment()
    
        
    


random_destination = generate_destination()

random_transportation = generate_transportation()

random_entertainment = generate_entertainment()

random_restaurant=generate_restaurant()

print(f'''Here are the details of your day trip:
        Destination:  {random_destination}
        Transportation:  {random_transportation}
        Activity:  {random_entertainment}
        Restaurant:  {random_restaurant}
        ''')


