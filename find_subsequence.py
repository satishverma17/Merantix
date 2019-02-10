#importing necessary libraries
import sys

#initialize max_limit as a global variable
max_limit = 0  

#function for processing absolute differences
def sumAbsolute(data_arr): 
  
    sum = 0
    n = len(data_arr)
    for i in range(n - 1, -1, -1): 
        sum += i*data_arr[i] - (n-1-i) * data_arr[i] 
    return abs(sum)

#function for colculating non-empty subsequence with the highest _sum_
def processarray(logfile,num):

    max_so_far = num[0]
    cur_max = num[0]

    #sys.argv[2] is passed to limit maximum length of subsequence 
    if len(sys.argv) >= 3:
        max_limit = sys.argv[2]
    else :
        max_limit = len(num);

    #looping for each element of the arrat num
    for i in range(1,int(max_limit)):
        cur_max = max(num[i], cur_max + num[i])
        max_so_far = max(max_so_far,cur_max)
	    
    print("maximun sum is " + str(max_so_far))
    

def main(argv):
    logfile = sys.argv[1]
    max_limit = 0
    #Opening the logfile passed as parameter sys.arg[1] and fetching the values to an array
    with open(logfile, 'r') as f:
        nums = f.read().split()
        num = []
    for i in nums : num.append(int (i))
    #checking for third parameter for selecting type of processing algorithm    
    if sys.argv[3] == "differences":
        print("Absolute value is " + str(sumAbsolute(num)))
    elif sys.argv[3] == "values":
        processarray(logfile,num)


if __name__ == "__main__":
   main(sys.argv[1:])
