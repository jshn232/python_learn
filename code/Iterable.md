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
    
    [参考代码](/Iteration.py)

## Iterator

    生成器不但可以作用于`for`循环，还可以被`next()`函数不断调用并返回下一个值直到抛出错误
    可以被`next()`函数调用并返回下一个对象的迭代器称为：`Iterator`
    
    可以使用`isinstance()`判断一个对象是否为`Iterator`对象
    
    from collections import Iterator

    def fun_Iterator(a):
        print(a,'is Iterator ?',isinstance(a,Iterator))
        return

    fun_Iterator(123)
    fun_Iterator([x*x for x in range(10)])
    fun_Iterator((y+y for y in range(10)))
    
    生成器都是`Iterator`，但`list`,`dict`,`str`虽然是`Iterable`,却不是`Iterator`
    把`Iterable`变成`Iterator`，可以使用`Iter()`函数
    
    `Iterator`的计算是惰性的，只有不断调用next()才能计算出下一个数据，而且无法提前知道序列的长度
    `Iterator`甚至可以表示一个无限大的数据流，例如全体自然数。而使用`list`是无法表达全体自然数的
    
    `python`的`for`循环本质上就是通过不断的next()函数实现的，例如
    for n in [1,2,3,4,5]
        pass
    等价于
    i = iter([1,2,3,4,5])
    
    while True:
        try:
            next(i)
        except StopIteration:
        break
        
    [参考代码](/Iteration.py)
