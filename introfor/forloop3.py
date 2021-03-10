#!/usr/bin/env python3
# create the list called farms
#farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
#         {"agriculture": ["garlic"]}]
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# unnecessarily repeated code
# inflexible code
# what if more farms are added?
# what if farms are taken away?
# what if name or agriculture doesn't have a value?
def farm(firefly):
    # let firefly equal the farm dictionary being passed into this function
    print(f"Resources in {firefly.get('name','UNNAMED FARM')}:")
    for animals in firefly.get('agriculture'):
        print(animals)
    print()
for x in farms:
    # don't I want to "talk" to each of those dictionaries?
    # don't I want to get the "name" and "agriculture" from both those dictionaries?
    farm(x)
