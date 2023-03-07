# A program to find how many ways a husband and wife can wear different colour clothes

husband = "VIBGYOR"
wife = "VIBGYOR" 
count = 0
for i in range(7):
    for j in range(7):
        print(i,j,husband[i],wife[j])
        count +=1
print("The total number of ways the couple can wear clothes is ", count)
