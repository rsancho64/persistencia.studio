from Algo import Algo
import pickle

if __name__ == "__main__":

    a = Algo(11)
    b = Algo(a)
    c = Algo(b)

    print(a)
    print(b)
    print(c)

    with open('cosillas.pkl', 'wb') as outp:
        pickle.dump(a, outp, pickle.HIGHEST_PROTOCOL)
        pickle.dump(b, outp, pickle.HIGHEST_PROTOCOL)
        pickle.dump(c, outp, pickle.HIGHEST_PROTOCOL)

    del a
    del b
    del c
    with open('cosillas.pkl', 'rb') as inp:
        a = pickle.load(inp)
        b = pickle.load(inp)
        c = pickle.load(inp)
        # d = pickle.load(inp) # EOFError: Ran out of input

    print(a)
    print(b)
    print(c)
