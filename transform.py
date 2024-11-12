import csv
with open('items.csv', mode ='r') as file:    
       csvFile = csv.DictReader(file)
       for lines in csvFile:
            if lines["category"] == "WEAPON":
                  classification = lines["classification"]
                  classification = "MELEE" if classification == "Simple Melee Weapon" else classification
                  classification = "MELEE" if classification == "Martial Melee Weapons" else classification
                  classification = "RANGED" if classification == "Simple Ranged Weapons" else classification
                  classification = "RANGED" if classification == "Martial Ranged Weapons" else classification
                  rarity = lines['rarity']
                  rarity = "RARE" if rarity == "VERY_RARE" else rarity
                  rarity = "COMMON" if rarity == "MUNDANE" else rarity
                  item = \
f"""
{lines['name'].lower().replace(' ','_')} = Weapon(
    id              = "{lines['name'].lower().replace(' ','_')}",
    name            = "{lines['name']}",
    description     = "{lines['description']}",
    weapon_type     = WeaponType.{classification},
    rarity          = Rarity.{rarity}
    value           = {lines['cost']},
)"""
                  print(item)
