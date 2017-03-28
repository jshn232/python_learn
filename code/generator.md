# generator（生成器）
    有时不必创建完整的list，通过一边循环一边计算的机制，叫做generator
    只需把列表生成式的[]变成()就是generator
    
    l = (x*x for x in range(10))
    
    一个函数中包含yield，则这个函数已经不是一个普通的函数，而是generator
    
    