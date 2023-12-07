import sys

def floyds_algorithm(a):
    for k in range (0,4):
        for i in range(0,4):
            for j in range(0,4):
                a[i][j] = min(a[i][j], a[i][k]+a[k][j])
                
    for i in range(0,4):
        print("\n")
        for j in range(0,4):
            print(a[i][j], end="\t")

a = [ 
        [ 0, 3 , sys.maxsize, 7 ],
        [ 8, 0 , 2 , sys.maxsize],
        [ 5, sys.maxsize, 0, 1 ],
        [ 2, sys.maxsize, sys.maxsize, 0] 
    ]

floyds_algorithm(a)