fibonacci=[]
x=0 
a=1 
b=1
fibonacci.insert(0,0)
fibonacci.append(a)
fibonacci.append(b)
print("Serie fibonacci")
for x in range(21):
    
    total = a + b
    b=a
    a= total
    fibonacci.append(total)
print(fibonacci)
