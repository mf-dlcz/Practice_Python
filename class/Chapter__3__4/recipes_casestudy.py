recipes = {
    "Pasta": {
        "ingredients": ["spaghetti", "tomato sauce", "garlic", "olive oil"],
        "instructions": ["Boil pasta", "Heat sauce", "Mix together"],
        "prep_time": 15,
        "cook_time": 20
    },
    "Pancakes": {
        "ingredients": ["flour", "milk", "eggs", "butter"],
        "instructions": ["Mix batter", "Heat pan", "Cook pancakes"],
        "prep_time": 10,
        "cook_time": 15
    }
}

#1. What does recipes["Pasta"]["ingredients"][2] print?

#2. What does recipes["Pancakes"]["prep_time"] print?

#3. What is the length of recipes["Pasta"]["instructions"]?

#4. Write code to add "salt" to the ingredients list for Pasta.

#5. Write code to update the cook_time for Pancakes to 20 minutes.

#6. Write code to add a new instruction "Serve hot" to both recipes.

#7. Write code to print all recipe names (keys) in the recipes dictionary.

#8. Write code to check if "sugar" is in the Pancakes ingredients list

#9. would this code work to add Parmesan to the list of ingredients?
recipes["Pasta"]["ingredients"] = "parmesan"

#10. What happens when you run each of the individual code statements:
print(recipes["Pasta"]["ingredients"][10])

print(recipes["Cookie"])


