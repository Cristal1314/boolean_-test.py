# # while loop = execute some code WHILE some condition remains true

# name = input("Enter your name:")
# # iteration (noun version) = loop over something (verb form)
# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name")
# # infinite loops are bad
# print(f"Hello {name}")

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative:")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another you like(q to quit): ")
# print("Bye!")

# num = int(input("Enter a # between 1 -10:" ))

# while num < 1 or nuym > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a # between 1 -10"))

# print(f"Your Number is {num}")

#-------------------------------------------------------------------------------------------------------------------------------------------
#for loops = execfute a block of code a fixed number of times.
#          You can ioterate over a range, string, sequance, ect.
# iterate : loops, when there is more then one thing
#-------------------------------------------------------------------
# credit_card = "1234-5678-9012-3456"

# for x in credit_card:   # every time that x prints out it will be every number in credit_card until if finish displaying the numbers                     
#     print(x)              
#------------------------------------------------------------------------------------
# for x in reversed(range(1, 11, 2)):
#     print(x)

# for x in range(1,13):
#     if x == 13:
#         continue
#     else:
#         print(x)

# for x in range( 13, 21):
#     if x == 13:
#         continue
#     else:
#         print(x)


# for x in range(1,21):
#     if x == 13:
#         break
#     else: 
#         print(x)

#--------------------------------------------------------------------------------------------------------------------------------------------

#Create a list of famous horror movie characters 

horror_characters = ["Freddy Kruger", "Jason Voorhees", "Michael Myers", "Pennywise", "Chucky"]
#Iterate through the list and print each character

# for character in horror_characters:
#     print(character)

# if character == "Jason Voorhees":
#     continue
# print(character)

# if character == "Michael Myers":
# #     character == "Dracula"
# # print(character)

# # if character == "Chucky":
# #     character == "jeepers creepers"

# # print(character)
# print(horror_characters)
#----------------------------------------------------------------------------------------------------------------------------
#create a list of famous horror movies or you
movies = ["Halloween", "Terrifer", "Jeepers Creepers", "Conjureing", "Jane Doe"]
#favorite horror movies
favevotie_movie = "incantation"
# iterate through the list and of a certain movie is found
for x in movies:
    print(x)
#is your least favorite movie, break out of the loop
    if x == "Jane Doe":
        break
    print(x)
# print out the rest of the movies
for x in movies:
    print(x)
# next replace one opf the movies with a movie that you like
    if x == "Conjureing":
        x == "incatation"
    print(x)






