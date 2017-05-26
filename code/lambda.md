# 匿名函数（lambda）

        l = list(map(lambda x:x*x,range(1,20,3)))
        lambda关键字表示匿名函数，冒号之前的x表示参数，冒号后面是表达式。匿名函数只能返回表达式，没有return