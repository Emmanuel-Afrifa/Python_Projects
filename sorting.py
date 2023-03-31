import numpy as np

def sorter(seq,descending=False):
    """This function sorts a given sequence in ascending order by default.
    An optional argument (descending) can be set to True, which gives the descending order     
    """
    n = len(seq)
    if descending:
        for i in range(n):
            for j in range(n-i-1):
                if seq[j] < seq[j+1]:
                    seq[j], seq[j+1] = seq[j+1],seq[j] 
    else:
        for i in range(n):
            for j in range(n-i-1):
                if seq[j] > seq[j+1]:
                    seq[j], seq[j+1] = seq[j+1],seq[j]
                    # Another way of implement the line above is given below
                    # tmp = seq[j]
                    # seq[j] = seq[j+1]
                    # seq[j+1] = tmp
    return seq

if __name__ == "__main__":
    a = np.array([34, 89, 23, 76, 7, 13, -3, 300, -47, 8, 5])
    print(sorter(a))