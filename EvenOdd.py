if __name__ == '__main__':
    n = int(input().strip())
if n<1 and n>100:
    print("please enter a number between 1 and 100")
elif n % 2 != 0:
     print("Weird")
elif n % 2 == 0 and n in range(2,5):
    print("Not Weird")
elif n % 2 == 0 and n in range(6,20):
    print("Weird")
elif n % 2 ==0  and n > 20:
     print("Not Weird")
else:
    print("Not Weird")
