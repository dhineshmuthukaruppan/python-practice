#set.add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
s = set()
for i in range(n):
    x = raw_input()
    s.add(x)

print(len(s))  