# Python 基础语法笔记

## 1. 变量和数据类型

### 基本数据类型
- **整数 (int)**: `42`, `-10`, `0`
- **浮点数 (float)**: `3.14`, `-2.5`, `1.0`
- **字符串 (str)**: `'hello'`, `"world"`, `"""多行"""`
- **布尔值 (bool)**: `True`, `False`

### 集合数据类型
- **列表 (list)**: `[1, 2, 3]`, `['a', 'b', 'c']`
- **元组 (tuple)**: `(1, 2, 3)`, `('x', 'y', 'z')`
- **字典 (dict)**: `{'key': 'value'}`, `{'name': 'John', 'age': 25}`
- **集合 (set)**: `{1, 2, 3}`, `{'a', 'b', 'c'}`

### 类型转换
```python
int('42')      # 字符串转整数
float('3.14')  # 字符串转浮点数
str(42)        # 整数转字符串
list((1, 2, 3)) # 元组转列表
```

## 2. 运算符

### 算术运算符
- `+` 加法: `5 + 3` → `8`
- `-` 减法: `5 - 3` → `2`
- `*` 乘法: `5 * 3` → `15`
- `/` 除法: `5 / 3` → `1.666...`
- `//` 整除: `5 // 3` → `1`
- `%` 取模: `5 % 3` → `2`
- `**` 幂: `5 ** 3` → `125`

### 比较运算符
- `==` 等于
- `!=` 不等于
- `>` 大于
- `<` 小于
- `>=` 大于等于
- `<=` 小于等于

### 逻辑运算符
- `and` 逻辑与
- `or` 逻辑或
- `not` 逻辑非

## 3. 控制流

### if 语句
```python
if condition:
    # 执行代码
elif another_condition:
    # 执行其他代码
else:
    # 执行默认代码
```

### for 循环
```python
# 遍历范围
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# 遍历列表
for item in [1, 2, 3]:
    print(item)

# 带索引遍历
for index, value in enumerate([1, 2, 3]):
    print(index, value)
```

### while 循环
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### 循环控制
- `break`: 跳出循环
- `continue`: 跳过当前迭代，进入下一次迭代

## 4. 函数

### 定义函数
```python
def function_name(parameter1, parameter2):
    """函数文档字符串"""
    # 函数体
    return result
```

### 默认参数
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
```

### 可变参数
```python
def sum_all(*args):
    return sum(args)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

### 匿名函数（lambda）
```python
square = lambda x: x ** 2
add = lambda x, y: x + y
```

## 5. 列表推导式

```python
# 创建平方数列表
squares = [x ** 2 for x in range(10)]

# 筛选偶数
evens = [x for x in range(10) if x % 2 == 0]

# 创建字典
square_dict = {x: x ** 2 for x in range(5)}

# 创建集合
vowels = {char for char in "hello world" if char in "aeiou"}
```

## 6. 字符串操作

### 基本操作
```python
text = "Hello, World!"

# 长度
len(text)  # 13

# 切片
text[0:5]      # "Hello"
text[7:]       # "World!"
text[::-1]     # 反转字符串

# 大小写
text.upper()   # "HELLO, WORLD!"
text.lower()   # "hello, world!"
text.title()   # "Hello, World!"

# 查找
text.find("World")  # 7
text.count("l")     # 3

# 替换
text.replace("World", "Python")  # "Hello, Python!"

# 分割和连接
text.split(",")     # ["Hello", " World!"]
" ".join(["Hello", "World"])  # "Hello World"
```

### 格式化
```python
name = "Alice"
age = 25

# f-string（推荐）
message = f"Hello, {name}! You are {age} years old."

# format 方法
message = "Hello, {}! You are {} years old.".format(name, age)

# % 格式化
message = "Hello, %s! You are %d years old." % (name, age)
```

## 7. 异常处理

```python
try:
    # 尝试执行的代码
    result = 10 / 0
except ZeroDivisionError:
    # 处理特定异常
    print("除数不能为零")
except Exception as e:
    # 处理其他异常
    print(f"发生错误: {e}")
else:
    # 没有异常时执行
    print("操作成功")
finally:
    # 无论是否异常都执行
    print("清理代码")
```

## 8. 文件操作

### 读取文件
```python
# 读取整个文件
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 逐行读取
with open("file.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

### 写入文件
```python
# 写入文本
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!")

# 追加文本
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("\n追加一行")
```

## 9. 常用内置函数

- `len()`: 获取长度
- `range()`: 生成数字序列
- `sum()`: 求和
- `max()`: 最大值
- `min()`: 最小值
- `sorted()`: 排序
- `enumerate()`: 枚举
- `zip()`: 合并
- `map()`: 映射
- `filter()`: 过滤
- `any()`: 是否有真值
- `all()`: 是否全为真值

## 10. 编码建议

1. **变量命名**: 使用有意义的名称，`user_name` 而不是 `x`
2. **函数命名**: 使用动词，`calculate_sum()` 而不是 `sum()`
3. **常量命名**: 全大写，`MAX_SIZE = 100`
4. **类命名**: 首字母大写，`class User:`
5. **空行使用**: 函数之间空两行，逻辑块之间空一行
6. **注释**: 解释为什么这么做，而不是做什么
7. **类型提示**: 使用类型注解提高代码可读性
