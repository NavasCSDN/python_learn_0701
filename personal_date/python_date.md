# PYTHON复习

# 一.	linux操作

1. scp操作

   1. 远程复制 ：把本地的文件复制到远程主机上

   2. 命令格式

      ```linux
      scp 文件名 用户名@IP地址:绝对路径
      scp pycharm.tar.gz tarena@172.40.78.200:/home/tarena/ 
      ```

2. ```linux
   init+
   
   0:关机
   1：单用户形式，只root进行维护
   2：多用户，不能使用net file system
   3：完全多用户
   5：图形化
   6：重启
   ```

3. 打开rar压缩包的步骤

   1. 在终端安装rar
      sudo apt-get install rar
   2. 到你所放压缩包的路径下进行解压rar压缩包
      rar x file.rar

# 二.	python基础

1. number.isdigit(): 判断一个字符串是否可以转换为整整型数字

2. ```python
   import string
   定义变量
   all_chars = string.punctuation + string.whitespace
   import getpass
   getpass.getpass('请输入密码:')###pycharm不可以用，客户端可以用
   ```

3. 创建俩数字对象，id地址不同
   创建俩字符串对象，id地址相同

4. 生成秘钥：ssh-keygen

5. Python 字典(Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组。

   ```python
   #!/usr/bin/python
   
   coding=utf-8
   
   dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
   
   print ()"字典值 : %s" %  dict.items())
   
   遍历字典列表
   
   for key,values in  dict.items():
       print key,values
   
   以上实例输出结果为：
   字典值 : [('Google', 'www.google.com'), ('taobao', 'www.taobao.com'), ('Runoob', 'www.runoob.com')]
   Google www.google.com
   taobao www.taobao.com
   Runoob www.runoob.com
   ```

6. break--退出while循环，但while循环后面还有其他语句的话，还是会执行，
   continue--退出当次while，会接着从while循环的开始部分重新执行下来，
   return--退出函数，while循环后面还有其他语句的话，直接跳过不会执行

7. eval()方法:将字符串str当成有效的表达式来求值并返回计算结果

8. 递归方法：def f(n) if n==0 return else * return f(n-1)

9. 迭代

   ```shell
   迭代器　＝　可迭代对象.iter()
   变量　＝　迭代器.next()
   In [10]: a= [1,3]
   In [11]: item = a.iter()
   In [12]: item.next()
   Out[12]: 1
   In [13]: item.next()
   Out[13]: 3
   In [14]: item.next()
   StopIteration: 
   
   博客园地址：https://www.cnblogs.com/wqzn/archive/2019/06/02.html
   ```

   

10. yield用法：https://blog.csdn.net/mieleizhi0522/article/details/82142856

11. 推导式

    **列表推导式[]     字典推导式 {键:值　for ...}   集合 { for ... }**
    如果要用()，则生成的是一个生成器对象，需要用for语句提出；
    for item in result:
        print(item)

12. 列表可以存储实例化对象

    通过类名调用实例方法，传递进去的是对象

    一个对象也可以作为一个参数进行传递

13. 闭包

    闭包：函数作为返回值

14. 装饰器

    ~~装饰器：装饰器是将一个函数镶嵌在另一个函数中进行重复使用的目的，增加函数的使用方式，但是不用写过多冗余的代码。
    @print_func_name放在函数定义前是否等于
    say_hello = print_func_name(say_hello)~~

15. 类：一对一，最好做到外部一个需求改变内部一个类；尽量避免一对多

16. 注释：

    

17. 类变量定义

    (例如定义一个类变量，用于统计所有实例对象的某个属性，对类变量的操作，需要类方法)
    @classmethon
    类方法
    在类中建立的类变量和类方法，需要类名.方法/变量名调用（无论类内部外部）
    调用类方法时，会自动传递类名进入方法（类似于对象实例化传参数self实例化对象，类方法传递cls类对象）

18. 静态方法

    @staticmethod 静态方法只是名义上归属类管理，但是不能使用类变量和实例变量，是类的工具包
    放在函数前（该函数不传入self或者cls），所以不能访问类属性和实例属性

19. 私有变量

    以双下划线开头的类变量或方法属于私有变量，使用私有变量可以防止外界随意更改类内变量。如果想访问更改两个方法：1. 对象名._类名.私有变量名 2. 通过在类内定义返回函数，将私有成员变量return回

20. 限制当前类对象的变量

    ```python
    # 限制当前类,创建的对象,只能具有的实例变量.(实例只能有括号内的属性)
    __slots__ = ("__name")
    #子类默认不继承slots，如果子类也添加了slots属性，则子类自身的加父类的属性。
    ```

21. @property拦截读取操作@属性名.setter拦截写入操作；这两个一起使用，如果只有property没有setter，实例属性则为只读属性。如果只有setter没有property则只写属性。

22. 在模块的一开始定义 all 变量，import该模块后，只能找到 all中存在的变量或者函数，其他的不能调用

23. isinstance/issubclass判段对象/子类 是否兼容一个类型

24. 模块

    ```python
    #获取模块文档注释
    import module01
    print(module01.doc)
    #获取模块文件路径
    print(module01.file)
    #获取模块名称
    print(module01.name) #模块名  main
    
    if name == "__main__":
        pass# 如果程序从当前模块运行,则执行下列的测试代码；如果当前模块被主模块导入,则下列测试代码不再执行
    ```

25. python引用上级包

    如果python需要引用上级目录的包：
    import sys
    通过sys.path.append("绝对路径")的方式，将python的环境变量切换到上一级
    之后就可以正常引用了

26. 魔法方法

    在python中方法名如果是__xx__()的，那么就有特殊的功能，因此叫做“魔法”方法：<https://www.cnblogs.com/seablog/p/7173107.html>

    例如: 当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据

27. pycharm的使用

    单击行号添加断点，F7分句执行
    Pycharm调试程序时，有时需要直接从第一个断点跳转至第二个断点，如果还是用单步调试的话就非常麻烦了，当然解决方法也很简单，点击“Dubug”，当程序停在第一个断点的时候，点击菜单栏的Run-> Resume Program即可跳转至第二个断点。
    Step Over：在单步执行时，在函数内遇到子函数时不会进入子函数内单步执行，而是将子函数整个执行完再停止，也就是把子函数整个作为一步。有一点，经过我们简单的调试，在不存在子函数的情况下是和Step Into效果一样的（简而言之，越过子函数，但子函数会执行）。
    Step Into：单步执行，遇到子函数就进入并且继续单步执行（简而言之，进入子函数）。
    Step Into My Code：进入自己编写的函数，不进入系统函数，很少用到。
    Force Step Into：强制进入，在调试的时候能进入任何方法。
    Step Out：当单步执行到子函数内时，用Step Out就可以执行完子函数余下部分，并返回到上一层函数。
    Run to Cursor：一直执行，到光标处停止，用在循环内部时，点击一次就执行一个循环。

28. 

# 三.	python数据结构+I/O+正则

# 四.	数据库

# 五.	pythonweb

1. git使用

   ```shell
   echo "# python_learn_0701" >> README.md
   git init
   git add README.md
   git commit -m "first commit"
   git remote add origin git@github.com:NavasCSDN/python_learn_0701.git
   git push -u origin master
   ```

   

# 六.	框架

# 七．其他软件的使用

1. git的使用

   在未进行任何add 和commit时，是没有master分支的，因为commit必须指向一个分支，commit后自动创建master分支．	

# 八．	软件安装

1. typora的安装步骤

   ```shell
   1.	sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE这是一个可选的操作，但是建议还是添加上这一步。
   2.	sudo add-apt-repository 'deb http://typora.io linux/'添加typora的远程仓库
   3.	sudo apt-get update更新
   4.	sudo apt-get install typora 安装
   如果出现typora无法打开的情况，执行 sudo apt install gconf2
   ```

2. chrome的安装步骤

   ```shell
   #将下载源加入到系统的源列表;如果返回“地址解析错误”等信息，可以百度搜索其他提供 Chrome 下载的源，用其地址替换掉命令中的地址。
   sudo wget https://repo.fdzh.org/chrome/google-chrome.list -P /etc/apt/sources.list.d/
   #导入谷歌软件的公钥，用于下面步骤中对下载软件进行验证。如果顺利的话，命令将返回“OK”
   wget -q -O - https://dl.google.com/linux/linux_signing_key.pub  | sudo apt-key add -
   #用于对当前系统的可用更新列表进行更新。
   sudo apt-get update
   #如果提示错误，就根据提示使用以下语句对依赖包进行更新
   sudo apt-get -f install
   #执行对谷歌 Chrome 浏览器（稳定版）的安装
   sudo apt-get install google-chrome-stable
   #在终端中执行以下命令启动浏览器，然后右键锁定到启动器即可
   google-chrome-stable
   
   ```

   
