## Flask
Flask 是一个 Python 实现的 Web 开发微框架
- [文档](http://docs.jinkan.org/docs/flask/)
- [Jinja2 模板文档](http://docs.jinkan.org/docs/jinja2/templates.html)

## Jinja2
`{% ... %}`：[控制结构](http://docs.jinkan.org/docs/jinja2/templates.html#id18)   
`{{ ... }}`：接受传递过来的变量   
`{# ... #}`：多行注释    
`#  ... ## `：行语句，效果同控制结构    
行语句需要开启：`app.jinja_env.line_statement_prefix = '#'`

## 留言簿参考
- [Jaccorot](https://github.com/Show-Me-the-Code/python/blob/master/Jaccorot/0023/guestbook.py)
- [Flask](http://wiki.jikexueyuan.com/project/flask-guide/the-course.html)

## 虚拟环境
虚拟环境是一个将不同项目所需求的依赖分别放在独立的地方的一个工具，它给这些工程创建虚拟的Python环境。它解决了“项目X依赖于版本1.x，而项目Y需要项目4.x”的两难问题，而且使你的全局site-packages目录保持干净和可管理。   
比如，你可以工作在一个需求Django 1.3的工程，同时维护一个需求Django 1.0的工程。   

在cmd窗口：   
安装`virtualenv`和`virtualenvwrapper`：   
```
pip install virtualenv
pip install virtualenvwrapper
```
基本使用：   
虚拟环境保存在`C:\Users\MagicWang\Envs`中   
创建一个虚拟环境venv
```
mkvirtualenv venv
```
**工作** 在虚拟环境venv上：
```
workon venv
```
**停止工作**
```
deactivate
```
**删除**
```
rmvirtualenv venv
```
- [更多](http://pythonguidecn.readthedocs.io/zh/latest/dev/virtualenvs.html#virtualenv)   
