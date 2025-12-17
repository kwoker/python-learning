# 网络爬虫完整指南

> 🕷️ 从基础到高级的系统化网络爬虫学习项目

## 🎯 项目简介

这是一个全面的网络爬虫学习项目，涵盖从基础的 requests + BeautifulSoup 到高级的 Scrapy、Selenium 和异步爬虫技术。包含实际案例、最佳实践和反反爬策略。

## 📚 学习内容

### 核心模块

1. **基础爬虫** (`01_basic_scraper.py`)
   - HTTP 请求和响应处理
   - BeautifulSoup 解析 HTML
   - CSS 选择器使用
   - 表格数据提取
   - 分页处理
   - 数据保存（JSON、CSV）

2. **高级爬虫** (`02_advanced_scraper.py`)
   - Scrapy 框架使用
   - Selenium 处理动态内容
   - 异步爬虫（aiohttp + asyncio）
   - 数据清洗和处理
   - 反反爬策略
   - 代理和请求伪装

## 🚀 快速开始

### 安装依赖

```bash
# 基础依赖
pip install requests beautifulsoup4 lxml

# 高级依赖（可选）
pip install scrapy selenium aiohttp asyncio
pip install aiofiles  # 异步文件操作

# Selenium 额外安装
# 1. 下载 ChromeDriver
# 2. 或使用 webdriver-manager 自动管理
pip install webdriver-manager
```

### 运行示例

```bash
# 1. 学习基础爬虫
python 01_basic_scraper.py

# 2. 学习高级爬虫
python 02_advanced_scraper.py
```

## 📖 学习路径

### 第一步：基础概念
1. 理解 HTTP 协议
2. 学习 HTML 解析
3. 掌握 CSS 选择器
4. 学会数据提取

### 第二步：实际应用
1. 处理静态网页
2. 提取表格数据
3. 处理分页
4. 数据存储

### 第三步：高级技术
1. Scrapy 框架
2. JavaScript 处理
3. 异步爬取
4. 反反爬策略

## 📊 示例输出

运行后会生成：
- `output/basic_page.html` - 原始 HTML
- `output/news.json` - 新闻数据
- `output/products.json` - 产品信息
- `output/students.json` - 学生数据
- `output/all_posts.json` - 分页数据
- `output/cleaned_data.json` - 清洗后数据
- `output/*.json` - 各种爬取结果

## 💻 核心代码示例

### 基础爬虫

```python
import requests
from bs4 import BeautifulSoup

# 发送请求
url = "https://example.com"
response = requests.get(url)

# 解析 HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 提取数据
title = soup.find('title').text
links = soup.find_all('a')
data = [{"link": link.get('href')} for link in links]
```

### CSS 选择器

```python
# 选择所有产品
products = soup.select('.product')

for product in products:
    name = product.select_one('.product-name').text
    price = product.select_one('.product-price').text
    print(f"{name}: {price}")
```

### 异步爬虫

```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ['url1', 'url2', 'url3']
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

asyncio.run(main())
```

### Scrapy 框架

```python
import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['http://example.com']

    def parse(self, response):
        for item in response.css('.item'):
            yield {
                'title': item.css('h2::text').get(),
                'price': item.css('.price::text').get()
            }
```

### Selenium 处理动态内容

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://example.com')

# 等待元素加载
element = driver.find_element(By.CLASS_NAME, 'content')

# 提取数据
title = driver.title
paragraphs = driver.find_elements(By.TAG_NAME, 'p')

driver.quit()
```

## 🔍 数据提取技巧

### CSS 选择器速查表

| 选择器 | 示例 | 说明 |
|--------|------|------|
| 标签选择器 | `h1` | 所有 h1 标签 |
| 类选择器 | `.product` | class="product" 的元素 |
| ID 选择器 | `#header` | id="header" 的元素 |
| 后代选择器 | `.content p` | .content 内的所有 p 标签 |
| 子选择器 | `.menu > li` | .menu 的直接子元素 li |
| 属性选择器 | `a[href]` | 带有 href 属性的 a 标签 |
| 伪类 | `a:hover` | 鼠标悬停的 a 标签 |

### BeautifulSoup 方法

```python
# 查找单个元素
soup.find('div')  # 第一个 div
soup.find(id='content')  # id 为 content 的元素

# 查找所有元素
soup.find_all('p')  # 所有 p 标签

# 获取文本
element.get_text()  # 获取所有文本
element.text  # 简化版本

# 获取属性
element.get('href')  # 获取 href 属性
element['src']  # 获取 src 属性
```

## 🛡️ 反反爬策略

### 1. 请求头伪装

```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}
```

### 2. 随机延迟

```python
import random
import time

def random_delay(min_sec=1, max_sec=3):
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)
```

### 3. 代理轮换

```python
proxies = [
    'http://proxy1:port',
    'http://proxy2:port',
    'http://proxy3:port'
]

proxy = random.choice(proxies)
response = requests.get(url, proxies={'http': proxy, 'https': proxy})
```

### 4. 会话保持

```python
session = requests.Session()
session.headers.update({'User-Agent': '...'})
response = session.get(url)
```

## 📊 数据处理

### 数据清洗

```python
import re

def clean_price(price_str):
    # 提取数字
    numbers = re.findall(r'\d+', price_str)
    return int(''.join(numbers))

def clean_text(text):
    # 去除空白和换行
    return ' '.join(text.split())
```

### 数据存储

```python
import json
import csv
import pandas as pd

# JSON 存储
with open('data.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# CSV 存储
with open('data.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

# Pandas DataFrame
df = pd.DataFrame(data)
df.to_excel('data.xlsx', index=False)
```

## 🔧 高级技巧

### 1. 处理验证码

```python
# OCR 识别（简单验证码）
import pytesseract
from PIL import Image

def solve_captcha(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text.strip()
```

### 2. 模拟登录

```python
# 登录
login_data = {
    'username': 'user',
    'password': 'pass'
}
session.post('https://example.com/login', data=login_data)

# 访问需要登录的页面
response = session.get('https://example.com/profile')
```

### 3. 处理 Cookies

```python
# 设置 Cookies
cookies = {'session_id': 'abc123'}
response = requests.get(url, cookies=cookies)

# 获取 Cookies
jar = response.cookies
```

### 4. 文件下载

```python
def download_file(url, filename):
    response = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
```

## 🐛 常见问题

### Q1: 编码问题
```python
# 指定编码
response.encoding = 'utf-8'
content = response.text

# 或使用二进制模式
content = response.content.decode('utf-8')
```

### Q2: SSL 证书错误
```python
# 忽略 SSL 验证（仅开发环境）
response = requests.get(url, verify=False)
```

### Q3: 超时处理
```python
# 设置超时
response = requests.get(url, timeout=10)
```

### Q4: 限流处理
```python
# 添加重试机制
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(total=3, backoff_factor=1)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
```

## 📚 学习资源

### 官方文档
- [Requests 文档](https://docs.python-requests.org/)
- [BeautifulSoup 文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Scrapy 文档](https://docs.scrapy.org/)
- [Selenium 文档](https://selenium-python.readthedocs.io/)

### 推荐工具
- **Chrome DevTools**: 分析网页结构
- **XPath Helper**: XPath 测试工具
- **Postman**: API 测试
- **Scrapy Shell**: 交互式调试

### 实践网站
- **httpbin.org**: 测试 HTTP 请求
- **jsonplaceholder.typicode.com**: 假数据 API
- **quotes.toscrape.com**: 练习爬取
- **books.toscrape.com**: 书籍信息爬取

## ⚠️ 爬虫伦理

### 遵守 robots.txt
```python
import urllib.robotparser

def can_fetch(url, user_agent='*'):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(f"{urllib.parse.urljoin(url, '/robots.txt')}")
    rp.read()
    return rp.can_fetch(user_agent, url)
```

### 最佳实践
1. 遵守网站 robots.txt
2. 控制请求频率，避免给服务器造成压力
3. 不要爬取敏感或私人信息
4. 尊重版权，注明数据来源
5. 不要破坏网站正常运行
6. 遵守相关法律法规

## 🏆 实战项目建议

### 项目 1: 新闻聚合器
- 爬取多个新闻网站
- 去重和分类
- 生成每日新闻摘要

### 项目 2: 商品价格监控
- 爬取电商平台价格
- 价格变动提醒
- 价格趋势分析

### 项目 3: 招聘数据分析
- 爬取招聘网站职位
- 技能需求分析
- 薪资趋势统计

### 项目 4: 舆情监控系统
- 爬取社交媒体内容
- 情感分析
- 热点话题追踪

## 🤝 贡献

欢迎贡献更多示例和最佳实践！

## 📄 许可证

MIT License

## 👨‍💻 作者

Claude - Anthropic

---

**开始你的爬虫之旅！** 🚀

记住：技术无罪，请合理使用，遵守法律和道德规范！
