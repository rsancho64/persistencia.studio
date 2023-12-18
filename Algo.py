class Algo:

    def __init__(self, undato):
        self.data = undato

    def __str__(self):
        return (f"Algo-obj: {self.data}")


import json
from json import JSONEncoder


# subclass JSONEncoder
class AlgoEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

if __name__ == "__main__":

    a = Algo("hola")
    b = Algo(a)    
    c = Algo(b)

    print(a.__dict__)
    print(b.__dict__)    
    print(c.__dict__)        

    print(AlgoEncoder().encode(a))
    print(AlgoEncoder().encode(b))    
    print(AlgoEncoder().encode(c))    
    print()

    # json es en realidad un formato de texto
    print(json.dumps(a, indent=4, cls=AlgoEncoder))
    print(json.dumps(b, indent=4, cls=AlgoEncoder))    
    print(json.dumps(c, indent=4, cls=AlgoEncoder))    

    # TODO : los formatos anteriores, guardalos en un fichero
    # TODO : los formatos anteriores, cargarlos desde un fichero    

    # Let's load it using the load method to check if we can decode it or not.
    aJSON = json.loads(AemployeeJSONData)
    print(employeeJSON)





