# criticas a pickle:
# https://www.benfrederickson.com/dont-pickle-your-data/

# - [ ] see also: https://www.geeksforgeeks.org/serializing-json-data-in-python/

from Algo import Algo
import json

if __name__ == "__main__":

    a = Algo(11)
    b = Algo(a)
    c = Algo(b)

    # w @ json file ...
    # try ... https://pynative.com/make-python-class-json-serializable/

    with open("salida.json", "w") as write:
        json.dump(a, write)
        json.dump(b, write)        
        json.dump(c, write)         


