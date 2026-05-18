my_favorite_pets = ["turtle", "dog", "cat", "fish"]

# print("These are my favorite pets: ")
# for pet in my_favorite_pets:
#     if pet == "cat":
#         print(" this is your most favorite pet")
#     print(pet)

for index in range(0, len(my_favorite_pets)):
    #pet = my_favorite_pets[index]
    #print(index, pet)

    if my_favorite_pets[index] == "dog":
        my_favorite_pets[index] = "cat2"
        #print(index, my_favorite_pets[1])
    print(my_favorite_pets[index])

print(my_favorite_pets)

print("With enumerate()")
for index, pets in enumerate(my_favorite_pets):
    print(f"Pet {index}: {pets}")

print(index(my_favorite_pets))