n=int(input("輸入一個數字:"))
if n%3==0 and n%5==0:
  print("FB")

elif n%5==0:
    print("B")
elif n%3==0:
    print("F")
else:
  for i in range(1,n+1):
        print(i)
