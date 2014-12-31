
if __name__ == "__main__":
    lst = [(1,2,3),(2,3,4),(3,4,5)]
    for i, j in enumerate(lst):
        print "{0} ; {1}".format(i, j)
        
    print getattr((1,2,3), 2)