#dict
key-value的集合  
key不可以为可变类型（例如list），而字符串和整数则可以  
dict通过哈希算法（Hash）得到key的位置，索引不会因为key的多少而影响速度，但会占用大量的内存；    
d_port_passwod = {8989:'pass1',8990:'pass2'}

#set
key的集合，但不存储value    
set需要list作为输入    
s = set([1,2,3])
