a, b = map(int, input().split()) # a = 시, b = 분
c = int(input())

a += c // 60
b += c % 60

if b >= 60:
    a += 1
    b -= 60
    
if a >= 24:
    a -= 24
    
print(a, b)