
import json

with open("Jikan.json", "r", encoding="utf-8") as f:
    data = json.load(f)

anime_list = data["data"]   # a list of 25 anime (each one is a dictionary)

# ------------------------------------------------------------
# Q1. Filtering and counting
# Print the title and score of every anime with a score
# greater than 9.0. Then print how many there were.
# ------------------------------------------------------------
def scorecount():
    for i in anime_list:
        try:
            if i["score"] > 9:
                print(i["title"]) 
        except KeyError:
            continue           


# ------------------------------------------------------------
# Q2. Accumulator
# Calculate and print the average score of all the anime
# in the list. Round the answer to 2 decimal places.
# ------------------------------------------------------------
def averagescore():
    a=0
    b=0
    for i in anime_list:
        a += i["score"]
        b += 1
    g = a / b
    print(f"{g:,.2f}")





# ------------------------------------------------------------
# Q3. Finding the maximum
# Print the title and episode count of the anime that has the
# most episodes.
# Hint: look closely at the "episodes" values. Does every
# anime have a number?
# ------------------------------------------------------------
def maxepisodes():
    list=[]
    for i in anime_list:
        if type(i["episodes"]) == int or type(i["episodes"]) == float:
           list.append(i["episodes"])
    g=max(list)
    print(g)



# ------------------------------------------------------------
# Q4. Nested lists
# Each anime has a "genres" list. Each item in that list is a
# dictionary with a "name" key (for example, "Comedy").
# Print the title of every anime that has the genre "Comedy".
# ------------------------------------------------------------
def findgenre():
    for i in anime_list:
        for f in i["genres"]:
            if f["name"] == "Comedy":
                print(i["title"])
findgenre()



