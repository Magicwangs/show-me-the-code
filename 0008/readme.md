## HTML_Extractor

**基于行块分布函数的通用网页正文抽取算法**

算法主要原理

1.正文区密度：在去除HTML中所有tag之后，正文区字符密度更高，较少出现多行空白；

2.行块长度：非正文区域的内容一般单独标签（行块）中较短。

算法基本可以应对大部分（中文）网页正文的提取，针对有些网站正文图片多于文字的情况，可以采用保留<img> 标签中图片链接的方法，增加正文密度。目前少量测试发现的问题有：1）文章分页或动态加载的网页；2）评论长度过长喧宾夺主的网页。

- [参考教程](http://web.jobbole.com/83498/)

## HTTP库：requests

- [参考教程](http://liam0205.me/2016/02/27/The-requests-library-in-Python/)
- [官方文档](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html)

## python转义字符

| 转义字符  |          描述         |
|---------- |:---------------------:|
|\\(在行尾) | 续行符                |
|\\\\       | 反斜杠符号            |
|\\'        | 单引号                |
|\\"        | 双引号                |
|\\a        | 响铃                  |
|\\b        | 退格(Backspace)       |
|\\e        | 转义                  |
|\\000      | 空                    |
|\\n        | 换行                  |
|\\v        | 纵向制表符            |
|\\t        | 横向制表符            |
|\\r        | 回车                  |
|\\f        | 换页                  |

## lambda()

lambda()是Python里的匿名函数，其语法如下：

lambda [arg1[, arg2, ... argN]]: expression

下面是个1+2=3的例子
```
>>> fun = lambda x,y:x+y
>>> fun(1,2)
3
>>> (lambda x,y:x+y)(1,2)
```
## map()

map(function, sequence) ：对sequence中的item依次执行function(item)，见执行结果组成一个List返回：
```
>>> def cube(x): return x*x*x
>>> map(cube, range(1, 11))
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
>>> def cube(x) : return x + x
>>> map(cube , "abcde")
['aa', 'bb', 'cc', 'dd', 'ee']
```

另外map也支持多个sequence，这就要求function也支持相应数量的参数输入：
```
>>> def add(x, y): return x+y
>>> map(add, range(8), range(8))
[0, 2, 4, 6, 8, 10, 12, 14]
```
## 正则匹配中的\1

相当于（.*?）,表示任意内容，用自身的一种匹配结果代替

```
>>> regex = re.compile(r".*?var:(.*?);")
>>> regex.sub(r"\1test", "fksf var:asfkj;")
'asfkjtest'
```