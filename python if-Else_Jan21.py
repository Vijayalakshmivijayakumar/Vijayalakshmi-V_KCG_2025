#Task
#Given an integer, , perform the following conditional actions:
#If  is odd, print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird

#Input Format
#A single line containing a positive integer

#Output Format
#Print Weird if the number is weird. Otherwise, print Not Weird.

#Sample Input 0
#3
#Sample Output 0
#Weird
#Sample Input 1
#24
#Sample Output 1
#Not Weird

if __name__ == '__main__':
    n = int(input().strip())
if(n%2==0):
        if(2<=n<=5):
            print("Not Weird")
        elif(6<=n<=20) or (n>20):
            print("Not Weird")
else:
     print("Weird")

    
    
    
