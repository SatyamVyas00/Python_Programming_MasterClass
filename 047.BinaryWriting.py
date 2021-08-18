# with open("FileIO\BinaryWritesample",'bw') as Bin_file:
#     Bin_file.write(bytes(range(17)))
#
# with open("FileIO\BinaryWritesample",'br') as Binfile:
#     for b in Binfile:
#         print(b)

a = 65534   # FF FE
b = 65535   # FF FF
c = 65536   # 00 01 00 00
x = 2998302 # 00 2D C0 1E

with open("FileIO\BinaryWritesample",'bw') as Bin_file:
    Bin_file.write(a.to_bytes(2,'big'))
    Bin_file.write(b.to_bytes(2,'big'))
    Bin_file.write(c.to_bytes(4,'big'))
    Bin_file.write(x.to_bytes(4,'big'))
    Bin_file.write(x.to_bytes(4,'little'))

with open("FileIO\BinaryWritesample",'br') as Bin_file:
    e = int.from_bytes(Bin_file.read(2),'big')
    print(e)
    f = int.from_bytes(Bin_file.read(2),'big')
    print(f)
    g = int.from_bytes(Bin_file.read(4),'big')
    print(g)
    h = int.from_bytes(Bin_file.read(4),'big')
    print(h)
    # i = int.from_bytes(Bin_file.read(4),'big')
    # print(i)
    i = int.from_bytes(Bin_file.read(4),'little')
    print(i)