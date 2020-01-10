
#Given an array of integers, calculate the fractions of its elements tahta are positive, negative and are zeros. Print the decimal value of each fraction on a new line. 
#Test cases are scaled to 6 decimal answers.
#For example given the arr arr = [1, 1, 0, -1, -1] there are 5 elements, two positive, two netgiave and one zero. Their rations would be
# 2/5 = 0.4000000 2/5 = 0.400000 and 1/5 = 0.200000.

def positive(n):
    if n > 0 : 
        return (n)

def negative(n):
    if n < 0 :
        return (n)

def zero(n):
    if n == 0 :
        return (1)

numbers = [-4, 3, -9, 0, 4, 1]

posList = list(filter(positive, numbers))
negList = list(filter(negative, numbers))
zeroList = list(filter(zero, numbers))

print('%.6f'%(len(posList)/len(numbers)))
print('%.6f'%(len(negList)/len(numbers)))
print('%.6f'%(len(zeroList)/len(numbers)))
