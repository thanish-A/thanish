n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)

2ques;
n=int(input())
for i in range (1,n+1):
 print(i,end=" ")

n=int(input())
for i in range (2,n+1,2):
 print(i,end=" ")

n=int(input())
total=0
for i in range(1,n+1):
 total+=1
print(total)

n=int(input())
for i in range(1,11):
 print(n,"*",i,n*i)

n=int(input())
fact=1
for i in range(1,n+1):
  fact*=i
print(fact)

n=int(input())
count=0
while n!=0:
  count +=1
  n//=10
print(count)


n=int(input())
t=0
while n!=0:
  t=n%10
  print(t,end="")
  n//=10



n = int(input())
sum = 0
while n > 0:
    sum += n % 10
    n //= 10
print(sum)

n=int(input())
for i in range(1,n+1):
 print(i*i,end=" ")

n=int(input())
for i in range(1,n+1):
  if n%i==0:
    print(i,end=" ")

a=int(input())
b=int(input())
for i in range(a,b+1):
  if i%2!=0:
    print(i,end=" ")

n = int(input())
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
if count == 2:
    print("Prime")
else:
    print("Not Prime")

base = int(input())
exponent = int(input())
result = 1
for i in range(exponent):
    result = result * base
print(result)

n = int(input())
if n > 35:
    print("pass")
else:
    print("fail")

n=int(input())
if n%2==0:
  print("even")
else:
  print("odd")

