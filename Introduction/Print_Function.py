#Without using any string methods, try to print the following:
#Input n=5
#Output 12345

from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(1,n+1):
        print(i,end="")
    

