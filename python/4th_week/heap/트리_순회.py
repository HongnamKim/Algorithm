import sys

input = sys.stdin.readline

N = int(input())
LEFT = [-1] * 26
RIGHT = [-1] * 26

for _ in range(N):
    p, l, r = input().split()
    pi = ord(p) - 65
    LEFT[pi] = -1 if l == "." else (ord(l) - 65)
    RIGHT[pi] = -1 if r == "." else (ord(r) - 65)

print(ord("A") - 65)
print(LEFT)
print(RIGHT)


def preorder(u, out):
    if u == -1:
        return
    out.append(chr(u + 65))
    preorder(LEFT[u], out)
    preorder(RIGHT[u], out)


def inorder(u, out):
    if u == -1:
        return
    inorder(LEFT[u], out)
    out.append(chr(u + 65))
    inorder(RIGHT[u], out)


def postorder(u, out):
    if u == -1:
        return
    postorder(LEFT[u], out)
    postorder(RIGHT[u], out)
    out.append(chr(u + 65))


root = 0

res = []
preorder(root, res)
print("".join(res))
res = []
inorder(root, res)
print("".join(res))
res = []
postorder(root, res)
print("".join(res))
