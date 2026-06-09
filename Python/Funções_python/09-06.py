

def soma(x,y):
    result = x+y
    return result
while True:
    try:
        a = int (input("N1:"))
        b = int (input("N2:"))
        break
    except:
        print("Apenas números!")
res = soma (a,b)
print("Soma:",res)        

