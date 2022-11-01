heroes= {"flash":
                   {"speed": "fastest", 
                    "intelligence": "lowest", 
                    "strength": "lowest"}, 
         "batman":
                   {"speed": "slowest", 
                    "intelligence": "highest", 
                    "strength": "money"}, 
         "superman":
                   {"speed": "fast", 
                    "intelligence": "average", 
                     "strength": "strongest"}}
print(f"Flash is {heroes['flash']['speed']}!")
print("Superman is " + heroes['superman']['strength'] + "!")
print(f"Batman has the ultimate super power: {heroes['batman']['strength']}")                   
