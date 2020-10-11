title = "Python Course"
print(title[0], title[1], title[2], title[-1], title[-2])

name = "jonathon swift"
print(name.title())
print(name.upper())
print(name.lower())
print(name.capitalize())

firstName = "Steve"
secondName = "Jobs"
print(firstName + " " + secondName)
print(firstName + "\n" + secondName)

anotherName = "    Mr. X    "
print("_" + anotherName + "_")
print("_" + anotherName.lstrip() + "_")
print("_" + anotherName.rstrip() + "_")
print("_" + anotherName.rstrip().lstrip() + "_")
print("_" + anotherName.strip() + "_")

sentence = "A quick brown fox jumps over the lazy dog"
print(sentence.find("fox"))
print(sentence.find("foxs"))
print(sentence.replace("fox", "cat"))

place1 = "Dhaka"
place2 = "Bogra"
place3 = "Comilla"
print(place1, place2, place3, sep="|")

anotherSentence = "{name}'s age is {age}"
print(anotherSentence.format(name="Rifat", age=27))

alterSentence = "%s's age is %d"
print(alterSentence % ("Rifat", 27))

singer = "Taylor Swift"
print(singer[:6])
print(singer[7:])