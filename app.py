import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
def pokemoniterate():
    for i in range(len(data)):
        print(data[i]["name"]["english"])
# Add a language choice feature and print the pokemons name based on the user input
def findpokemonwithlangauge():
    ajsfa = input("What language ")

    f = input("What pokemon ")

    for i in range(len(data)):
        if data[i]["name"]["english"] == f:
            print(data[i]["name"][ajsfa])
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
def typepokemonlist():
    typepokemon = input("Give me a type ")
    pokelist = []
    for i in range(len(data)):
        f = data[i]["type"]
        for g in f:
            if g == typepokemon:
                pokelist.append(data[i]["name"]["english"])
    print(pokelist)

typepokemonlist()
        
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!

