## 传递变量给SQL语句时需要注意
```py
# Never do this -- insecure!
symbol = 'RHAT'
c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

# Do this instead
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print c.fetchone()

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
```

## list去重方法：(按原list排序)
```py
a=['a','ss','d','d','r','a']
news_ids=list(set(a))
news_ids.sort(key=a.index)
# or 建议采用后者，后者可以处理任何可迭代对象。
sorted(news_ids,key=a.index)

```