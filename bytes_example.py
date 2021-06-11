tag = 13
amount = 1 * 10 ** 8       # 1 0000 0000

data = tag.to_bytes(1, byteorder='little') + amount.to_bytes(8, byteorder='little')
 
assert int.from_bytes(data[:1], byteorder='little', signed=False) == tag, 'check tag'
assert int.from_bytes(data[1:], byteorder='little', signed=False) == amount, 'check amount'