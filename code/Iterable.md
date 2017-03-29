# 迭代器
## Iterable

    `for` 循环可以作用于：
   - 数据集合    
    `list`,`tuple`,`dict`,`set`,`str`
   - generator    
    包括生成器和带yield的generator function
    
    这些可以直接作用于for循环的对象叫做可迭代对象：`Iterable`
    可以用`isinstance()`判断一个对象是否是`Iterable`对象
    
    from collections import Iterable
    
    def fun_Iterable(a):
         print(a,'is Iterable ?',isinstance(a,Iterable))
         return
    
    fun_Iterable(123)
    fun_Iterable((1,2,3,4))
    fun_Iterable('abc')
    [参考代码](/code/Iteration.py)

## Iterator

    生成器不但可以作用于`for`循环，还可以被`next()`函数不断调用并返回下一个值直到抛出错误
    可以被`next()`函数调用并返回下一个对象的迭代器称为：`Iterator`
    
    可以使用`isinstance()`判断一个对象是否为`Iterator`对象
    
    [参考代码](/code/Iteration.py)