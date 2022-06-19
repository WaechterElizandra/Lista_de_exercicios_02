n=int(input("Qual tabuada deseja?: "))

for tabuada in range(10):
    print("{} x {:2} = {}".format (n, tabuada+1, n*(tabuada+1)) )
