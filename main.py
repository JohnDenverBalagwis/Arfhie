print("\n[1]. Create a program that will input two variables and will determine the two statement is True and False using logical And.\n")
a = bool(False)
b = bool(False)
c = a and b
print(a, "and", b, "=", c)

d = bool(False)
e = bool(True)
f = d and e
print(d, "and", e, "=", f)

g = bool(True)
h = bool(False)
i = g and h
print(g, "and", h, "=", i)

j = bool(True)
k = bool(True)
l = j and k
print(j, "and", k, "=", l)

print("\n==========================")
print("\n[2]. Create a program that will input four variables and will determine the four statement is True or False using logical OR. Display the four possible output.\n")
m = bool(True)
n = bool(True)
o = bool(True)
p = bool(True)
q = m or n or o or p
print(m, "or", n, "or", o, "or", p, "=", q)

mm = bool(True)
nn = bool(False)
oo = bool(False)
pp = bool(False)
qq = mm or nn or oo or pp
print(mm, "or", nn, "or", oo, "or", pp, "=", qq)

r = bool(False)
s = bool(False)
t = bool(False)
u = bool(False)
v = r or s or t or u
print(r, "or", s, "or", t, "or", u, "=", v)

rr = bool(False)
ss = bool(True)
tt = bool(False)
uu = bool(True)
vv = rr or ss or tt or uu
print(rr, "or", ss, "or", tt, "or", uu, "=", vv)


print("\n==========================")
print("[3]. Create a program that will execute the conditional statement which either True or False with the ff. given: x = 5; y = 10 \n")
x = 5
y = 10
if x < y:
    print(f"True {x} is less than {y}\n")
else:
    print("False")
