# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    ## create r, which is our request object
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/ditto')

    ## pokefact is our iterable -- that just means it will take on the values found within
    ## r.json()["all"], one after the next-- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
    ## print the value associated with text"
    #for pokename in r.json():
   #     print(pokename.get("name"))  # the .get() method returns NONE if key not found
    print(r.json())
    #print(r.headers)
    #print(r.text)
main()
