#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

class hashfind:

def __init__(self):
self.W = [0,0,0,0,0]
self.W[0]=("0")
self.W[1]= (bin(0x1023456789abcdef)[2:].zfill(64))
self.W[2]= (bin(0xfedcba9876543210)[2:].zfill(64))
self.W[3]= (bin(0x98765abc43210def)[2:].zfill(64))
self.W[4]= (bin(0xecb1234567890fda)[2:].zfill(64))

self.B = []
self.T = [0, 2147483659, 2147483693, 2147483713, 2147483743, 2147483777,
2147483783, 2147483813, 2147483857, 2147483867,
2147483869, 2147483887, 2147483893, 2147483929, 2147483951, 2147483993,
2147483999, 2147484007, 2147484037,
2147484041, 2147484043, 2147484061, 2147484083, 2147484109, 2147484161,
2147484167, 2147484197, 2147484203,
2147484221, 2147484223, 2147484233, 2147484239, 2147484259, 2147484271,
2147484277, 2147484331, 2147484337,
2147484349, 2147484377, 2147484433, 2147484439, 2147484461, 2147484491,
2147484499, 2147484517, 2147484527,
2147484541, 2147484553, 2147484569, 2147484601, 2147484611, 2147484613,
2147484617, 2147484641, 2147484679,
2147484697, 2147484721, 2147484733, 2147484751, 2147484791, 2147484821,
2147484851, 2147484869, 2147484877,
2147484919]

def add(self, x1, x2):
y1 = self.findy(x1)
y1 = math.sqrt(abs(y1))
y2 = self.findy(x2)
y2 = math.sqrt(abs(y2))
l = int((y1 - y2) / (x1 - x2))
x3 = int(l * l - 486662 - x1 - x2)
return x3

def double(self, x):
x2 = ((x * x - 1) * (x * x - 1)) / (4 * (x * x * x + 486662 * x * x + x))
return x2

def pmul(self, a, x):
a = bin(a)[2:]
Q0 = 0
Q1 = x
for i in a[::-1]:
if i == '1':
Q0 = self.add(Q0, Q1)
Q1 = self.double(Q1)
return (abs(Q0))

def findy(self, a):
x = a
y = x * x * x + 486662 * x * x + x
return y

def F1(self, x, y, z):

b = self.add(x, y)
c = self.add(~b, z)
a = b | c
a = a ^ x
return a

def F2(self, x, y, z):
b = self.add(x, z)
c = self.add(b, ~z)
b = b ^ x
c = c ^ y
a = b | c
return a

def F3(self, x, y, z):
U = self.add(self.add(x, y), self.add(x, z))
t=U^z^y
return t

def F4(self, x, y, z):
a = self.double(y)
b = self.add(x, a)
c = self.double(b)
h = self.add(a, z)
l = self.add(h, c)
l=l^h^(~int(c))
return l

rol = lambda self, val, r_bits, max_bits: ((val & (2**max_bits-1)) >> r_bits%max_bits) | 
(val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

def op1(self, Pa, Pb, Pc, Pd, k, s, i):

self.W[Pa] = bin(self.rol(self.pmul(self.T[i], (int(self.W[Pb], 2) + (int(self.W[Pa], 2)
^ self.F1(int(self.W[Pb], 2), int(self.W[Pc], 2), int(self.W[Pd], 2)) ^ int(self.B[k], 2)))), s,
64) + self.T[i])[2:]
if(len(self.W[Pa])>64):
self.W[Pa] = self.W[Pa][::-1]
self.W[Pa] = self.W[Pa][:63]
self.W[Pa] = self.W[Pa][::-1]
self.W[Pa] = self.W[Pa].zfill(64)

def op2(self, Pa, Pb, Pc, Pd, k, s, i):

self.W[Pa] = bin(self.rol(self.pmul(self.T[i], (int(self.W[Pb], 2) + (int(self.W[Pa], 2)
^ self.F2(int(self.W[Pb], 2), int(self.W[Pc], 2), int(self.W[Pd], 2)) ^ int(self.B[k], 2)))), s,
64) + self.T[i])[2:]
if (len(self.W[Pa]) > 64):
self.W[Pa] = self.W[Pa][::-1]
self.W[Pa] = self.W[Pa][:63]
self.W[Pa] = (self.W[Pa][::-1])
self.W[Pa] = self.W[Pa].zfill(64)

def op3(self, Pa, Pb, Pc, Pd, k, s, i):

self.W[Pa] = bin(self.rol(self.pmul(self.T[i], (int(self.W[Pb], 2) + (int(self.W[Pa], 2)
^ self.F3(int(self.W[Pb], 2), int(self.W[Pc], 2), int(self.W[Pd], 2)) ^ int(self.B[k], 2)))), s,
64) + self.T[i])[2:]
if (len(self.W[Pa]) > 64):
self.W[Pa] = self.W[Pa][::-1]

self.W[Pa] = self.W[Pa][:63]
self.W[Pa] = self.W[Pa][::-1]
self.W[Pa] = self.W[Pa].zfill(64)

def op4(self, Pa, Pb, Pc, Pd, k, s, i):

self.W[Pa] = bin(self.rol(self.pmul(self.T[i], (int(self.W[Pb], 2) + (int(self.W[Pa], 2)
^ self.F4(int(self.W[Pb], 2), int(self.W[Pc], 2), int(self.W[Pd], 2)) ^ int(self.B[k], 2)))), s,
64) + self.T[i])[2:]
if (len(self.W[Pa]) > 64):
self.W[Pa] = self.W[Pa][::-1]
self.W[Pa] = self.W[Pa][:63]
self.W[Pa] = self.W[Pa][::-1]
self.W[Pa] = self.W[Pa].zfill(64)

def findhash(self,inputmsg):

self.blocks = []

self.string = str(inputmsg)
self.bin_string = ''.join(format(ord(x), 'b') for x in self.string)

self.l1 = int(len(self.bin_string))
self.bin_string = self.bin_string + '1'
self.length = len(self.bin_string)
self.n = 1
self.a = 0
self.b = 64
self.i = 0
self.temp = self.length

# checking the multipilicty of string length with 1024

while self.temp > 1024:
self.n += 1
self.temp -= 1024

# appending 0s at the end leaving last 128
while self.length%1024!= 896:
self.bin_string = self.bin_string + '0'
self.length += 1

#append zeroes before length bits and add to binary string

self.length_rep = bin(self.l1)[2:].zfill(128)
self.bin_string = self.bin_string + self.length_rep

#total blocks of 64 bits add to the block array

self.total_blocks = int(len(self.bin_string) / 64)

for i in range(0, self.total_blocks):
self.blocks.append(self.bin_string[self.a:self.b])
self.a = self.b
self.b += 64

#clear the temp block 'B' if it already exists

for i in range(0, self.total_blocks, 16):

#copy message blocks to temp block 'B'
for j in range(0, 16):

self.B.append(self.blocks[i + j])

#perform 64 operations on the temporary block to generate the hash of block
for t1 in range(1):
A1 = self.W[1]
B1 = self.W[2]
C1 = self.W[3]
D1 = self.W[4]

self.op1(1, 2, 3, 4, 0, 7, 1)
self.op1(4, 1, 2, 3, 1, 12, 2)
self.op1(3, 4, 1, 2, 2, 17, 3)
self.op1(2, 3, 4, 1, 3, 22, 4)
self.op1(1, 2, 3, 4, 4, 7, 5)
self.op1(4, 1, 2, 3, 5, 12, 6)
self.op1(3, 4, 1, 2, 6, 17, 7)
self.op1(2, 3, 4, 1, 7, 22, 8)
self.op1(1, 2, 3, 4, 8, 7, 9)
self.op1(4, 1, 2, 3, 9, 12, 10)
self.op1(3, 4, 1, 2, 10, 17, 11)
self.op1(2, 3, 4, 1, 11, 22, 12)
self.op1(1, 2, 3, 4, 12, 7, 13)
self.op1(4, 1, 2, 3, 13, 12, 14)
self.op1(3, 4, 1, 2, 14, 17, 15)
self.op1(2, 3, 4, 1, 15, 22, 16)
self.op2(1, 2, 3, 4, 1, 5, 17)
self.op2(4, 1, 2, 3, 6, 13, 18)
self.op2(3, 4, 1, 2, 11, 20, 19)
self.op2(2, 3, 4, 1, 0, 26, 20)
self.op2(1, 2, 3, 4, 5, 5, 21)
self.op2(4, 1, 2, 3, 10, 13, 22)

self.op2(3, 4, 1, 2, 15, 20, 23)
self.op2(2, 3, 4, 1, 4, 26, 24)
self.op2(1, 2, 3, 4, 9, 5, 25)
self.op2(4, 1, 2, 3, 14, 13, 26)
self.op2(3, 4, 1, 2, 3, 20, 27)
self.op2(2, 3, 4, 1, 8, 26, 28)
self.op2(1, 2, 3, 4, 13, 5, 29)
self.op2(4, 1, 2, 3, 2, 13, 30)
self.op2(3, 4, 1, 2, 7, 20, 31)
self.op2(2, 3, 4, 1, 12, 26, 32)
self.op3(1, 2, 3, 4, 5, 4, 33)
self.op3(4, 1, 2, 3, 8, 13, 34)
self.op3(3, 4, 1, 2, 11, 20, 35)
self.op3(2, 3, 4, 1, 14, 29, 36)
self.op3(1, 2, 3, 4, 1, 4, 37)
self.op3(4, 1, 2, 3, 4, 13, 38)
self.op3(3, 4, 1, 2, 7, 20, 39)
self.op3(2, 3, 4, 1, 10, 29, 40)
self.op3(1, 2, 3, 4, 13, 4, 41)
self.op3(4, 1, 2, 3, 0, 13, 42)
self.op3(3, 4, 1, 2, 3, 20, 43)
self.op3(2, 3, 4, 1, 6, 29, 44)
self.op3(1, 2, 3, 4, 9, 4, 45)
self.op3(4, 1, 2, 3, 12, 13, 46)
self.op3(3, 4, 1, 2, 15, 20, 47)
self.op3(2, 3, 4, 1, 2, 29, 48)
self.op4(1, 2, 3, 4, 0, 6, 49)
self.op4(4, 1, 2, 3, 7, 9, 50)
self.op4(3, 4, 1, 2, 14, 15, 51)
self.op4(2, 3, 4, 1, 5, 24, 52)
self.op4(1, 2, 3, 4, 12, 6, 53)

self.op4(4, 1, 2, 3, 3, 9, 54)
self.op4(3, 4, 1, 2, 10, 15, 55)
self.op4(2, 3, 4, 1, 1, 24, 56)
self.op4(1, 2, 3, 4, 8, 6, 57)
self.op4(4, 1, 2, 3, 15, 9, 58)
self.op4(3, 4, 1, 2, 6, 15, 59)
self.op4(2, 3, 4, 1, 13, 24, 60)
self.op4(1, 2, 3, 4, 4, 6, 61)
self.op4(4, 1, 2, 3, 11, 9, 62)
self.op4(3, 4, 1, 2, 2, 15, 63)
self.op4(2, 3, 4, 1, 9, 24, 64)

#add to existing block that serves as iv for nex round(if required) else considered
as digest of block
#also length of block is regulated at 64 bits

self.W[1] = bin(int(self.W[1],2) + int(A1,2))[2:]
if len(self.W[1]) > 64:
self.W[1] = self.W[1][::-1]
self.W[1] = self.W[1][:63]
self.W[1] = self.W[1][::-1]

self.W[2] = bin(int(self.W[2],2) + int(B1,2))[2:]
if len(self.W[2]) > 64:
self.W[2] = self.W[2][::-1]
self.W[2] = self.W[2][:63]
self.W[2] = self.W[2][::-1]

self.W[3] = bin(int(self.W[3],2) + int(C1,2))[2:]
if len(self.W[3]) > 64:
self.W[3] = self.W[3][::-1]

self.W[3] = self.W[3][:63]
self.W[3] = self.W[3][::-1]

self.W[4] = bin(int(self.W[4],2) + int(D1,2))[2:]
if len(self.W[4]) > 64:
self.W[4] = self.W[4][::-1]
self.W[4] = self.W[4][:63]
self.W[4] = self.W[4][::-1]
print(i)
#final hex is concatenation of all the IVs
hex1 = self.W[1].zfill(64) + self.W[2].zfill(64) + self.W[3].zfill(64) +
self.W[4].zfill(64)
hex1 = hex(int(hex1, 2))[2:].zfill(64)
return hex1

if __name__=="__main__":
ob=hashfind()
a11=input()
print(ob.findhash(a11))

