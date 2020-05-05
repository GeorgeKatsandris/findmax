import sympy as sym
import matplotlib.pyplot as plt
import itertools as itt

def getPerms(list1,list2):
    all_combinations = []
    list1_permutations = itt.permutations(list1, len(list2))
    for each_permutation in list1_permutations:
        zipped = zip(each_permutation, list2)
        all_combinations.append(list(zipped))
    return flattenList(all_combinations)

def flattenList(l):
    flat_list = []
    for sublist in l:
        for item in sublist:
            flat_list.append(item)
    return flat_list
    
def getCriticalPoints(f):
    dfx = sym.diff(f,x)
    dfy = sym.diff(f,y)
    
    dfx_solutions = sym.solve(dfx,x)
    dfy_solutions = sym.solve(dfy,y)
    return getPerms(dfx_solutions,dfy_solutions)
#functionsfile = open("functions.txt","r+")
#lines = functionfile.readlines()
#for i,line in enumerate(lines,start=1):
#    print(str(i) + ") " + line,end='')
#print("\n")

x = sym.Symbol('x')
y = sym.Symbol('y')
f = x**4 - 4*x**2 + y**2

plotf = sym.plotting.plot3d(f,(x,-1,1),(y,-1,1),show=False)

points = getCriticalPoints(f)

print(points)

#sym.plotting.plot3d(points,(x,-1,1),(y,-1,1),show=False)

