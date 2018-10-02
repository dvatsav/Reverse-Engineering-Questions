"""
import gdb

break_addr = 0x00000000004008e7
f=open("output.txt", 'w')
gdb.execute('break *{}'.format(break_addr))

vals = [0]*100
gdb.execute('run')
for r in range(100):
	
	val = gdb.parse_and_eval("${}".format('rdx'))
	print (val^1640)
	vals[r] = val^1640
	gdb.execute('c')
gdb.execute('quit')
print (vals)
"""
from socket import socket

ans = [1595, 1598, 1573, 1639, 1589, 1611, 1598, 1588, 1625, 1661, 1622, 1651, 1586, 1619, 1623, 1650, 1600, 1650, 1568, 1612, 1635, 1580, 1579, 1653, 1594, 1654, 1622, 1663, 1579, 1611, 1653, 1642, 1662, 1618, 1581, 1579, 1589, 1616, 1635, 1602, 1653, 1569, 1661, 1659, 1596, 1613, 1546, 1648, 1639, 1582, 1637, 1650, 1587, 1592, 1616, 1569, 1622, 1582, 1544, 1593, 1645, 1649, 1596, 1651, 1612, 1645, 1606, 1653, 1637, 1617, 1648, 1591, 1594, 1605, 1638, 1579, 1610, 1576, 1603, 1626, 1599, 1632, 1572, 1574, 1584, 1596, 1643, 1627, 1630, 1547, 1608, 1620, 1572, 1580, 1615, 1636, 1650, 1598, 1590, 1615]
s = socket()
s.connect(('reversing.chal.csaw.io', 10102))
c = 0
data = s.recv(1024)
print (data)

for i in range(100):
	data = s.recv(1024)
	print (data)
	print (c)
	s.send(str(ans[i]) + "\n")
	c += 1
	#data = s.recv(1024)
	#print (data)
s.send(str(1590) + "\n")
data = s.recv(1024)
print (data)
s.send(str(1615) + "\n")
data = s.recv(1024)
print (data)
data = s.recv(1024)
print (data)