primeNum = ""
for num in range(2, 250):
    if all(num%i !=0 for i in range(2, num)):
         primeNum = primeNum + "" + str(num)


with open('result.txt', 'w') as f:
        f.write(primeNum)
        f.close()