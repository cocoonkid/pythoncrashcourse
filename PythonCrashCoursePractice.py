#
# names = ["Eric schmmIdt","Franz xoPpen","Andy warHol","Whizzey mcKinsey"]
#
# for each in names:
#     print(f"Hi {each}, how are you today? ")
#
# print("\n")
#
# for each in names:
#     print(f"Hi {each.lower()}, how are you today? ")
#
# print("\n")
#
# for each in names:
#     print(f"Hi {each.upper()}, how are you today? ")
#
# print("\n")
#
#
# for each in names:
#     print(f"Hi {each.title()}, how are you today? ")
#
#
# print("Famous Quote")
# print("\n")
# print("Freddy said today:'Coding essentially is an infinite loop of:\nwtf\nah yea\nAdd sprinkles of 'that should be easy' and 'why did i agree on this'")
#
# print("\n")
#
# famous_person="Freddy"
# quote="'Coding essentially is an infinite loop of:\nwtf\nah yea\nAdd sprinkles of 'that should be easy' and 'why did i agree on this''"
#
# print(f"{famous_person} said today:{quote}")
# print("\n")
#
#
# name = "\t        Andy Warhol\n   "
# print(name)
#
#
# print(name.lstrip().rstrip().strip())
#
#
#
# my_list = ["Martin","Benjamin","Frank","Jason","Michael","Andreas"]
# for i in my_list:
# 	print (f"{i}")
#
# for i in my_list:
# 	print (f"Hello {i} how are you today?")
#
# list=["Honday FZ","Ferrari Spyder","Volkswagen","Tesla","Yamaha Xmax"]
#
# print(f"I'd really like to drive a {list[0]} in Bali")
# print(f"I'd really like to crash a {list[1]} in Bali")
# print(f"I'd really like to own a {list[2]} in Bali")
# print(f"One of my friends owns a  {list[3]} in Bangkok")
# print(f"Still my favorite is a {list[4]}. {list[4]} are just awesome for cruising with the family.")
#
# guest_list = ["Ayn Rand","Robert Oppenheimer","Adolf Hitler","Albert Einstein","Albert Hoffman"]
#
# for i in guest_list:
# 	print (f"Hello, {i} you're invited to dinner today at my place. Looking forward to some great discussions.!")
#
# print (f"Hello, {guest_list[2]} unfortunately can't make it.He's stuck in a Opium Den with Mao.! We could invite Joseph Stalin instead? He's not into drugs that much!")
#
# guest_list[2] ="Joseph Stalin"
# print (f"The Guest List currently consists of {guest_list}")
#
# for i in guest_list:
# 	print (f"Hello, {i} you're invited to dinner today at my place. Looking forward to some great discussions.!")
#
# # How to get rid of the brackets in the print output?
# print (f"Hello, {guest_list[:]} We've reserved an even bigger Table so we're inviting Janet Jackson, Michael Jackson and Muhammad Ali as well! YAY!")
#
# guest_list.insert(0,"Janet Jackson")
# guest_list.insert(3,"Michael Jackson")
# guest_list.append("Muhammad Ali")
#
# print (f"The Guest List currently consists of {guest_list}")
# guest_list_length = len(guest_list)
#
# print (f"Currently there are {guest_list_length} guests invited.")
#
# guest_list_sorted = sorted(guest_list)
# print(guest_list_sorted)
#
# travel_list = ["Rome","Italy","Denver","Chirac","Montpelier"]
#
#
# print (travel_list)
#
# print(sorted(travel_list))
#
# travel_list.reverse()
#
# print(travel_list)
#
# travel_list.reverse()
# print(travel_list)
#
# travel_list.sort()
# print(travel_list)
#
# travel_list.sort(reverse=True)
# print(travel_list)


#
# menu = ("Spagehtti Carbonara", "Spagehtti Bolognese", "Spagehtti","Gnocci","Pizza")
#
# for meal in menu:
#     print(meal)
#
# menu = ("Spagehtti Carbonara", "Spagehtti Bolognese", "Gelato","Gnocci","Cheese",)
#
# for meal in menu:
#     print(meal)


# person = {"first_name": "Frederik",
#            "last_name": "Hossak",
#            "age": 21,
#            "city":"Munich"}
#
# print(person["first_name"])


# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician.title() + ", that was a great trick!")
#     print("I can't wait to see your next trick, " + magician.title() + ".\n")


# pizzas = ["Margherita","Funghi","Calzone"]
# # for pizza in pizzas:
# #     print(f"I like Pizza {pizza}")
# # print("I love Pizza so much")


# animals = ["Kangarooh","Shark","Bat"]
# for animal in animals:
#     print(f"A |{animal} would make a great pet.")
# print(f"These animals are very dangerous though.")

# cubes = [value**3 for value in range(1,11)]
# print(cubes)
# print(f"THe first three items in the list are {(cubes[3:])} ")


# pizzas = ["Margherita","Funghi","Calzone"]
# friends_pizza = pizzas[:]
# friends_pizza.append("Maccaroni")
#
#
# delimiter = ' '
# friends_pizza_output = delimiter.join(friends_pizza)
#
#
# for pizza in friends_pizza:
#     print(f"My Friends pizzas are {friends_pizza_output} and mine are {pizzas}")

# foods = ("bread","apples","bananas","brezels","pork")
# for food in foods:
#     print(food)
#
# foods = ("swine","pork","bananas","brezels","pork")
# for food in foods:
#     print(food)

#
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')

#
# alien_color = "black"
#
# if alien_color == "green":
#     print("You earned 5 points")
# elif alien_color == "yellow":
#     print("You earned 10 points")
# elif alien_color == "red":
#         print("You earned 15 points")
#
# else:
#     print("You failed to stop the Invasion.")


# users = ["admin", "fiverr","hardcore","letsdoit","ganjaking"]
# #users = []
#
# if users:
#     for user in users:
#         if user == "admin":
#             print("Good Evening Master!")
#         else:
#             print(f"Hello {user}, how are you today?")
# else:
#     print("We don't have any users yet.")

# current_users = ["hellobear","byebear","makessense","total87","viola","macadamia""haagendazs","newuser"]
# new_users = ["newusers","Hellobear","patrick","robert","enjoy","halleluja","byebyemercer","fucktard78"]
#
# for user in new_users:
#     if user.lower() in current_users:
#         print("Already in use.Please chose another!")
#     else:
#         print("This username is available.")


# numbers = [1,2,3,4,5,6,7,8,10]
# for number in numbers:
#     if number == 1:
#         print(f"{number}st")
#     elif number == 2:
#             print(f"{number}nd")
#     elif number == 3:
#             print(f"{number}rd")
#     else:
#             print(f"{number}th")

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])
#
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

#
# alien_0 = {'color': 'green'}
# print("The alien is " + alien_0['color'] + ".")
#
# alien_0['color'] = 'yellow'
# print("The alien is now " + alien_0['color'] + ".")
#
#
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
# print("Original x-position: " + str(alien_0['x_position']))
#
# # Move the alien to the right.
# # Determine how far to move the alien based on its current speed.
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#      # This must be a fast alien.
#     x_increment = 3
# # The new position is the old position plus the increment.
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print("New x-position: " + str(alien_0['x_position']))
#
#
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)
#
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
#
# print(favorite_languages)
#
# favorite_languages_new = dict(name="edward", surname="Thoreau")
#
#
# print(f"Sarah\'s favorite language is {favorite_languages['sarah'].title()}.")
#
#
# person_i_know = dict(first_name='Jean', last_name='Baptiste', age=19, city="Paris")
#
#
# print(person_i_know)
# print(f"{person_i_know['first_name']} {person_i_know['last_name']} is {person_i_know['age']} and lives in {person_i_know['city']}.")

#
# favorite_numbers = {
#     "Helen": 1,
#     "Jean": 2,
#     "Richard": 5,
#     "Markus": 12,
#     "Hannah": 19,
#              }
#
# for key in favorite_numbers:
#     print(key)
#     print(favorite_numbers[key])



# glossary = {
#     "lists" : "These are lists ordered by indices.",
#     "tuples": "These are the same as lists but immutable.",
#     "dictionary": "These are key,value pairs accessible by there keys.",
#     "objects": "Everything is a object in Python.",
#     "Assignment Operator" : "This operator (=) assigns a value to a variable name.",
#     }
#
# for term in glossary:
#     print(term + ":" + "\n")
#     print("\t" + glossary[term] + "\n")
#
#
#
# favorite_numbers = {
#     "Helen": 1,
#     "Jean": 2,
#     "Richard": 5,
#     "Markus": 12,
#     "Hannah": 19,
#              }
#
# for key,value in favorite_numbers.items():
#     print(key)
#     print(value)

#
#
# glossary = {
#     "lists" : "These are lists ordered by indices.",
#     "tuples": "These are the same as lists but immutable.",
#     "dictionary": "These are key,value pairs accessible by there keys.",
#     "objects": "Everything is a object in Python.",
#     "Assignment Operator" : "This operator (=) assigns a value to a variable name.",
#     }
#
# for term in glossary:
#     print(term + ":" + "\n")
#     print("\t" + glossary[term] + "\n")
#
#
# for term,explanation in glossary.items():
#     print(term + ":" + "\n" + "\t" + explanation + "\n")



# rivers = {"nile": "egypt",
#           "donau": "Munich",
#             "Ruhr": "Berlin",
#           }
# for river,city in rivers.items():
#     print(f"The {river} runs through {city}")
#
# for river in rivers.keys():
#     print(river)
# for city in rivers.values():
#     print(city)

#
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
#
#
# list = ["edward", "nicole", "phil", "Daniel"]
#
# for name in list:
#     if name in favorite_languages.keys():
#         print(f"Thank you {name} for taking the poll")
#     if name not in favorite_languages.keys():
#         print(f"Please take the poll {name}")

# person1 = dict(first_name='Jean', last_name='Baptiste', age=19, city="Paris")
# person2 = dict(first_name='Luc', last_name='Piccard', age=21, city="Munich")
# person3 = dict(first_name='Harold', last_name='Kuma', age=33, city="Antwerp")
#
# people = [person1, person2, person3]
#
# for person in people:
#     name = person['first_name'].title() + " " + person['last_name'].title()
#     age = str(person['age'])
#     city = person['city'].title()
#
#     print(name + ", from " + city + ", is " + age + " years old.")

# toppings_list = []
#
# while True:
#     toppings = input("Please enter your favorite toppings. When done please enter 'quit'. ")
#     if toppings != "quit":
#         toppings_list.append(toppings)
#         print(f"We'll add {toppings} to our list")
#     if toppings == "quit":
#         print(toppings_list)
#         break
#

# while True:
#     age = (input("Please tell me your age: \n"))
#     if str(age) == "quit":
#         break
#     if int(age) < 3:
#         print("Your ticket is free!")
#     elif int(age) < 12:
#         print("Your ticket costs 10$.")
#     else:
#         print("Your ticket costs 15$.")
#


# sandwich_orders = ["BigMac","Pastrami", "Club","Pastrami", "Salami", "House", "Veggie", "Pastrami"]
# finished_sandwiches = []
#
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     if current_sandwich != "Pastrami":
#         print(f"I made you a {current_sandwich} sandwich!")
#         finished_sandwiches.append(current_sandwich)
#     while "Pastrami" in sandwich_orders:
#         sandwich_orders.remove(current_sandwich)
#         print("The deli has run out of Pastrami Sandwiches!")
#
#
# print(finished_sandwiches)

# poll = {}
#
# print("This is a poll about your most favorite destination. Enter 'quit' to exit! \n")
#

# while True:
#     username = input("What's your name? \n")
#     if username == "quit":
#         break
#     else:
#         destination = input("If you could visit one place in the world, where would you go?\n ")
#     if destination == "quit":
#         break
#     else:
#         poll[username] = destination
#         print("\n-----NEXT PERSON TO POLL-----\n")
#
# if len(poll) > 0:
#     for username,response in poll.items():
#         print(f"{username} responded with {response}")


# def display_message():
#     print("Hello I'm learning about functions today.")
#
# display_message()

#
# def favorite_book(title):
#     print(f"My favorite books is " + title.title() + "!")
#
#
# favorite_book("alice in Wonderland")
#
#
# def make_shirt(size="Large", text="I Love Python"):
#     #text = "I play keyboard in a band called Internet."
#     print("The t-shirt will be size " + str(size) + " and show " + (f"'{text}'"))
#
# make_shirt(size="medium")
#
# make_shirt()
#
# make_shirt(size="Xtralarge",text="Fuck Off!")


#
# def city_country(city,country):
#     text = city + "," + country
#     return text
#
# print(city_country("Santiago","Chile"))
# print(city_country("Munich","Germany"))
# print(city_country("Berlin","Germany"))




# album1 = make_album("Heart","Michael Jackson")
# album2 = make_album("Sexualite","Pit Baccardi")
# album3 = make_album("Warum","Hansi Hinterseer")
# album4 = make_album("Hello","Pigface",15)
#
# print(album1)
# print(album2)
# print(album3)
# print(album4)
#
# while True:
#     print("We'll ask for some informations.To stop enter 'q'")
#     album_title = input("Please enter the albums name! \n")
#     if album_title == 'q':
#         break
#     artist_name = input("Please enter the artists name \n")
#     if artist_name == 'q':
#         break
#     tracks = input("Please enter the number of tracks (optional) \n")
#     if tracks == 'q':
#         break
#     print(make_album(album_title,artist_name,tracks))


#
# def make_album(album_title,artist_name, tracks=""):
#     music_albums = {'album_title' : album_title, 'artist_name' : artist_name}
#     if tracks:
#         music_albums['tracks'] = tracks
#     return music_albums
#
# while True:
#     print("We'll ask for some information.To stop enter 'q'")
#     album_title = input("Please enter the albums name! \n")
#     if album_title == 'q':
#         break
#     artist_name = input("Please enter the artists name \n")
#     if artist_name == 'q':
#         break
#     print(make_album(album_title,artist_name))


#
# magician = ["leerla","Gandalf","Asshole","Wizard","Lancelot","Whatever"]
#
# def show_magician(names):
#     for name in names:
#         print(name)
#
# show_magician(magician)
#
# magician_copy = magician[:]
# new_magician = []
#
# def make_great(names):
#     for name in names:
#         great_name = name + " the Great"
#         print(great_name)
#         new_magician.append(great_name)
#
#
# make_great(magician_copy)
#
# print(new_magician)
#
# def make_sandwich(*toppings):
#     sandwich_topping = []
#     for topping in toppings:
#         sandwich_topping.append(topping)
#     print(f"We're making a sandwich with {','.join(sandwich_topping)}.")
#
#
# make_sandwich("Chesse", "Ham","Eggs","Paprika")
# make_sandwich("Chesse", "Ham")
# make_sandwich("Chesse", "Ham","Eggs")
#
#
# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
#
# user_profile = build_profile('Frederik', 'Hossak',
#                              location='Bali',
#                              field='Hacker')
# print(user_profile)

#
# def build_car(manufacturer, model_name, **properties):
#     car_properties = {}
#     car_properties['manufacturer'] = manufacturer
#     car_properties['model_name'] = model_name
#     for key, value in properties.items():
#         car_properties[key] = value
#     return car_properties
#
# car = build_car('subaru', 'outback', color='blue', tow_package=True)
#
# print(car)


#
# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(self.restaurant_name + " " + self.cuisine_type)
#
#     def open_restaurant(self):
#         print("The " + self.restaurant_name + " is open!")
#
#     def set_number_served(self, served):
#         restaurant.number_served = served
#
#     def increment_number_served(self, increment):
#         self.number_served += increment
#
#
# restaurant = Restaurant("Le Chic", "French")
#
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
#
# print(restaurant.number_served)
# restaurant.number_served = 17
# print(restaurant.number_served)
#
# restaurant.set_number_served(23)
#
# print(restaurant.number_served)
#
# restaurant.increment_number_served(99)
# print(restaurant.number_served)
#






# class User():
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print(self.first_name + " " + self.last_name)
#
#     def greet_user(self):
#         print("Hello " + self.first_name.title() + " " + self.last_name.title())
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
#
# user = User("Frederik","Hossak")
#
# user.describe_user()
# user.greet_user()
#
# user.increment_login_attempts()
# print(user.login_attempts)
#
# user.increment_login_attempts()
# print(user.login_attempts)
#
#
# user.reset_login_attempts()
# print(user.login_attempts)




# class Car():
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odomoeter_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# class ElectricCar(Car):
#     def __init__(self, make , model ,year):
#         super().__init__(make,model,year)
#         self.battery = Battery()
#
#
# class Battery():
#     def __init__(self, battery_size = 70):
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         print("This car has " + str(self.battery_size) + "-kWh battery.")
#
#     def get_range(self):
#         """Print a statement about the range this battery provides."""
#
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size == 85:
#             range = 270
#         message = "This car can go approximately " + str(range)
#         message += " miles on a full charge."
#         print(message)
#
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
#
# my_tesla.battery.describe_battery()
#
# my_tesla.battery.get_range()


# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(self.restaurant_name + " " + self.cuisine_type)
#
#     def open_restaurant(self):
#         print("The " + self.restaurant_name + " is open!")
#
#     def set_number_served(self, served):
#         restaurant.number_served = served
#
#     def increment_number_served(self, increment):
#         self.number_served += increment
#
# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type='ice_cream'):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = ["Strawberry","Vanilla","Chocolate","Amarena"]
#
#
#
#     def list_flavors(self):
#         print("\nWe have the following flavors available:")
#         for flavor in self.flavors:
#             print("- " + flavor.title())
#
#
# organic_icecream = IceCreamStand('Organic Icecream')
#
# organic_icecream.list_flavors()
#
# organic_icecream.describe_restaurant()
#
# organic_icecream.open_restaurant()



#
#
# class User():
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print(self.first_name + " " + self.last_name)
#
#     def greet_user(self):
#         print("Hello " + self.first_name.title() + " " + self.last_name.title())
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
# class Admin(User):
#     def __init__(self, first_name, last_name):
#         super().__init__(first_name, last_name)
#         self.privileges = Privileges()
#
#
# class Privileges():
#     def __init__(self):
#         self.privileges = ["can add post", "can delete user", "can edit user"]
#
#
#     def show_privileges(self):
#         print("The admin " + admin.first_name.title() + " " + admin.last_name.title() + " has the following privileges:\n")
#         for privilege in self.privileges:
#             print("- " + privilege.title())
#
#
# admin = Admin("Frederik","Hossak")
#
# admin.describe_user()
# admin.greet_user()
#
#
# admin.privileges.show_privileges()





class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odomoeter_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


# class ElectricCar(Car):
#     def __init__(self, make , model ,year):
#         super().__init__(make,model,year)
#         self.battery = Battery()
#
#
# class Battery():
#     def __init__(self, battery_size = 70):
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         print("This car has " + str(self.battery_size) + "-kWh battery.")
#
#     def get_range(self):
#         """Print a statement about the range this battery provides."""
#
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size == 85:
#             range = 270
#         message = "This car can go approximately " + str(range)
#         message += " miles on a full charge."
#         print(message)
#
#     def upgrade_battery(self):
#         if self.battery_size != 85:
#             self.battery_size = 85
#             print("Battery has been upgraded to " + str(self.battery_size) + ".")
#         else:
#             print("This cars battery has already been upgraded.")
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
#
# my_tesla.battery.describe_battery()
#
# my_tesla.battery.get_range()
#
# my_tesla.battery.upgrade_battery()
#
#
# my_tesla.battery.upgrade_battery()
#
#
# my_tesla.battery.get_range()



