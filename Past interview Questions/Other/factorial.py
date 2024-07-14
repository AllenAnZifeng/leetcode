def factorial(num):
    if num==0:
        return 1
    else:
        product = num*factorial(num-1)
        return product

print (factorial(4))