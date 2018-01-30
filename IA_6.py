def merge(X, p, q, r):
    left = []
    right = []
    # A = [None]*(r+1)
    n1 = int(q - p + 1)
    n2 = int(r - q)
    for i in range(n1):
        left.append(X[p+i])
    for i in range(n2):
        right.append(X[q+i+1])
    left.append(float('inf'))
    right.append(float('inf'))
    print(left)
    print(right)
    i = j = 0
    for k in range(p,r+1):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
    print(A)
    return A

def mergeSort(A, p, r):
    if p < r:
        q = int((p+r)/2)
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        print(merge(A,p,q,r))
    return


#print(merge([2,4,5,7,1,2,3,6],0,3,7))
#[1,2,2,3,4,5,6,7]
#print(merge([5,2],0,0,1))
global A
A = [5,2,7,4,3,1,6,2]
mergeSort(A,0,7)
