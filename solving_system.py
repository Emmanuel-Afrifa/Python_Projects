# In this code snippet, I solved a system of equations using the naive Gaussian elimination method


import numpy as np

def syssolver(seq,ans):
    # Reducing the first column
    tmp = seq[0]/seq[0][0]
    ans[1] = ans[1] - (ans[0]/seq[0][0]*seq[1][0])
    ans[2] = ans[2] - (ans[0]/seq[0][0]*seq[2][0])
    seq[1] = seq[1] - ( tmp*-3)
    seq[2] = seq[2] - (tmp*5)
    

    # Reducing the second column
    tmp = seq[1]/seq[1][1]
    ans[2] = ans[2] - ((ans[1]/seq[1][1])*seq[2][1])
    seq[2] = seq[2] - (tmp*seq[2][1])

    # Backwards substitution
    x3 = ans[2]/seq[2][2]
    x2 = (ans[1] - (seq[1][2]*x3))/seq[1][1]
    x1 = (ans[0] - (seq[0][2]*x3) - (seq[0][1]*x2))/seq[0][0]

    result = np.array([x1,x2,x3])
    return seq, result.T

if __name__ == "__main__":
    A = np.array([[20, 15, 10], [-3,-2.249,7], [5, 1 ,3]])
    b = np.array([45,1.751,9])

    new_matrix, answers = syssolver(A,b)
    print(f"The reduced matrix is given by \n{new_matrix}\n\nThe solution is given by \n{answers}")

