#Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

def mult_sum(n1,n2):
    multiplication = n1*n2

    if multiplication <= 1000:
        return multiplication
    
    else:
        return n1+n2
    
result = mult_sum(10,20)
print("The result is: ",result)

result = mult_sum(30,40)
print("The result is: ",result)