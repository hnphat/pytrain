def fibo(n):
    if n == 0: return 0
    elif n == 1: return 1
    elif n > 1: return fibo(n-1) + fibo(n-2)
    else: return "n <= 1"

def pow(x,y):
    try:
        result = 1
        if x < 0 or y < 0: return 0
        for i in range(0,y):
            result = result * x
        return result
    except:
        return 0

def powToFile(url,x,y):
    
    file = open(url,"w",encoding="utf-8")
    file.write("Tính pow \n")
    file.write("X = " + str(x) + "\n")
    file.write("Y = " + str(y) + "\n")
    file.write("Result = " + str(pow(x,y)))
    file.close()

set1 = {1,2,3,4,5,"ABC",2.5,(1,2),True} # Không sử dụng list trong set

list1 = [1,2,3,4,5,(1,2),{"a":1},True]
tuple1 = (1,2,3,4,5, (1,2), [1,2], {"A":1},True)

dict1 = dict({"A": "Apple", "A": "Apple", "C": [1,2,3], "D": (1,2,3,4), "E": {1,2,3,4,5}, "F": 2.5, "G": dict({"A":1}), "H": True})


