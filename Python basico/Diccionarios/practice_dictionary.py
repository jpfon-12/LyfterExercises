
europe_capitals = {
    "spain": "madrid",
    "france": "paris",
    "germany": "berlin",
    "norway": "oslo",
    "portugal": "lisbon" ,
}

#print(europe_capitals.get("spain"))

europe_capitals["italy"] = "rome"
europe_capitals.pop("germany")



for key, value in europe_capitals.items():
    print(f"{key}: {value}")
    

for value in europe_capitals.values():
    print( value)