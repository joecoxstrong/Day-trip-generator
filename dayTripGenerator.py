from tkinter import Y


def main():


    import random

    destination = ['Washington D.C.', 'Richmond, VA', 'Virginia Beach, VA', 'Raleigh, NC']
    restaurant = ['The Reserve', 'Bell Greek', 'Riptides', 'Brocks BBQ']
    mode_of_transportation = ['Car', 'Train', 'Bus', 'Hitch hiking']
    entertainment = ['watching a movie', 'doing an escape room', 'visiting a museum', 'takting a cave tour']


            

    def generate_destination():
        random_destination = random.choice(destination)
        user_approval = input('We have selected ' +random_destination+ ' for your destination! Does this sound good? Enter y/n: ')
        if user_approval == 'y':
            print("Excelent choice. Now let's select your mode of transportation.")
            return random_destination
        elif user_approval == 'n':
            print('Ok, let us select a new destination.')
        else:
            print('Please select an appropriate response')    
        return generate_destination()
                    

    def generate_restaurant():
        random_restaurant = random.choice(restaurant)
        user_approval = input('We have selected ' +random_restaurant+ ' for your dinner! Does this sound good? Enter y/n: ')
        if user_approval == 'y':
            print("Excelent choice.")
            return random_restaurant
        elif user_approval == 'n':
            print('Ok, let us select a new restaurant.')
        else:
            print('Please select an appropriate response')    
        return generate_restaurant()

    def generate_transportation():
        random_transportation = random.choice(mode_of_transportation)
        user_approval = input('We have selected ' +random_transportation+ ' for your mode of transportation! Does this sound good? Enter y/n: ')
        if user_approval == 'y':
            print("Excelent choice. Let's select an activity now.")
            return random_transportation
        elif user_approval == 'n':
            print('Ok, let us select a new mode of transportation.')
        else:
            print('Please select an appropriate response')    
        return generate_transportation()

    def generate_entertainment():
        random_entertainment = random.choice(entertainment)           
        user_approval = input('We have selected ' +random_entertainment+ ' for your entertainment! Does this sound good? Enter y/n: ')
        if user_approval == 'y':
            print("Excelent choice. Now let's choose a restaurant for dinner.")
            return random_entertainment    
        elif user_approval == 'n':
            print('Ok, let us select a new activity.')
        else:
            print('Please select an appropriate response')    
        return generate_entertainment()
        
            
        


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


    
    def trip_confirmed():
        confirm_trip = input('Would you like to keep, cancel, or start over? ')
        if confirm_trip == 'keep':
            print(f'Excellent! Time to prepare for your trip. You will be arriving in {random_destination} via {random_transportation}, where you will spend the day {random_entertainment}. You will end your day having an amazing dinner at {random_restaurant}.')
        elif confirm_trip == 'cancel': 
            print("No problem. This trip has been cancelled.")
        elif confirm_trip == 'start over':
            print("Ok. Let's start over.")
            main()    
        else:
            print('Please enter "keep", "cancel", or "start over"')
          
              
        
               
        
        
        

    trip_confirmed()

main()
