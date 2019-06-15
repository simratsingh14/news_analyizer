array = ['hello', 'is' , 'this','car'] 
ask = [0]*len(array)


# print(array[2])

 
with open('sample.txt', 'r') as f:
    for line in f:
        words = line.split()
        for i in range(len(array)):
        	if array[i] in line:
        		ask[i] += 1

print("Number of words:")
print(ask)