from collections import OrderedDict

if __name__ == "__main__":
    given_str = "Shellless mollusk lives in wallless house in wellness. Aaaarrghh!"
    print "".join(OrderedDict.fromkeys(given_str))