# In this code, a given array contains a list of commands.
# There are two categories of commeands, there are; 'goto' and 'create'
# The goto command creates a new bucket (container) where as the create command creates files inside these buckets
# Each bucket contains the number of unique create commands that immediately follows it.
# The aim of this code is to identify the bucket with the maximum number of commands 

# Creating two lists
# One saves the name of the goto command
# The other saves the things created in that space


def solution(arr):
    kk = []
    vv = []
    ind = []
    for kkk in arr:
        if kkk.startswith("g"):
            ind.append(arr.index(kkk))
    print(ind)

    i = 0
    for k in arr:
        skt = []
        if k.startswith("g"):
            sm = k.split(" ")
            kk.append(sm[1]) 
            if i < len(ind):
                if (len(ind)-i != 1):
                    a = ind[i]+1
                    b = ind[i+1]
                    i += 1
                elif ((len(ind) - i) == 1):
                    a = ind[-1]+1
                    b = len(arr)
            for l in arr[a:b]:
                sub = l.split()
                if (sub[1] not in skt):
                    skt.append(sub[1])
                #print(skt)
            vv.append(skt)
    print(vv)
        
    # Creating a dictionary that links the two lists created
    mydict = {}
    for key, value in zip(kk,vv):
        mydict[key] = value
    print(mydict)

    # Calculating the maximum number of values
    max = 0
    for k,v in mydict.items():
        if (max >= len(v)):
            pass
        else:
            max = len(v)

   # Printing the bucket with the maximum number of commands
    for k,v in mydict.items():
        if (len(v) == max):
            #print(f"\n{k} has {v} commands and it's bucket with maximum number of commands\n")
            return k, max

        
if __name__ == "__main__":
    arr = ['goto bucketA',
        'create fileA',
        'create fileB',
        'create fileC',
        'create fileD',
        'goto bucketB',
        'create fileA',
        'create fileB',
        'create fileC',
        'create fileD',
        'create fileE',
        'create fileF',
        'goto bucketC',
        'create fileA',
        'create fileB',
        'create fileC']
    buc_name, m = solution(arr)
    print(f"\n{buc_name} has {m} commands and it's bucket with maximum number of commands\n")

