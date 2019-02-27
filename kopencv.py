import numpy as np
import cv2

def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x

def pollution(s):
    img = cv2.imread(s)

    Z = img.reshape((-1,3))

    Z = np.float32(Z)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 4
    ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    #print("\n--------------------------\n")
    #print(res2)

    arr = [1, 2, 3, 4]
    j=0;
    for i in res2:
        s = int(i[0][0])+int(i[0][1])+int(i[0][2]);
        f = True;
        for k in range (0,j):
                if (arr[k]==s):
                    f = False;
                    break;
        if(f):
            arr[j]=s;
            j = j+1
        #print(s)

    arr = selection_sort(arr)
    print(arr)
    if(arr[0]<100):
        print("Oil Spill detected.")
    else:
        print("No Oil Spill detected.")
    cv2.imshow('res2',res2)
    print("\n--- --- --- --- --- --- --- ---\n")
    cv2.waitKey(0)
    #cv2.destroyAllWindows()

for m in range(1,37):
    z='H:/Satellite complete/Satellite/pic'+str(m)+'.jpg';
    print(z)
    pollution(z)
