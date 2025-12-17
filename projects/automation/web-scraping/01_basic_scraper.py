"""
基础网络爬虫示例
使用 requests 和 BeautifulSoup 爬取网页数据
"""

import requests
from bs4 import BeautifulSoup
import json
import csv
import time
from pathlib import Path
from typing import List, Dict
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# ============================================================================
# 示例 1: 基础网页爬取
# ============================================================================

def basic_web_scraping():
    """基础网页爬取示例"""
    print("=" * 60)
    print("示例 1: 基础网页爬取")
    print("=" * 60)

    # 设置请求头，模拟浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # 发送 HTTP 请求
        url = "https://httpbin.org/html"
        logger.info(f"正在访问: {url}")
        response = requests.get(url, headers=headers, timeout=10)

        # 检查响应状态
        logger.info(f"响应状态码: {response.status_code}")
        logger.info(f"响应头 Content-Type: {response.headers.get('Content-Type')}")

        if response.status_code == 200:
            # 解析 HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # 提取标题
            title = soup.find('title')
            if title:
                print(f"网页标题: {title.text}")
            else:
                print("未找到标题")

            # 提取 h1 标签
            h1 = soup.find('h1')
            if h1:
                print(f"H1 标签内容: {h1.text}")

            # 提取段落
            paragraphs = soup.find_all('p')
            print(f"\n找到 {len(paragraphs)} 个段落:")
            for i, p in enumerate(paragraphs, 1):
                print(f"  段落 {i}: {p.text[:100]}...")

            # 保存 HTML
            output_dir = Path("output")
            output_dir.mkdir(exist_ok=True)

            with open(output_dir / "basic_page.html", "w", encoding="utf-8") as f:
                f.write(response.text)
            print(f"\n✓ HTML 已保存到: {output_dir / 'basic_page.html'}")

        else:
            logger.error(f"请求失败，状态码: {response.status_code}")

    except requests.exceptions.RequestException as e:
        logger.error(f"请求异常: {e}")


# ============================================================================
# 示例 2: 爬取新闻列表
# ============================================================================

def scrape_news_list():
    """爬取新闻列表示例"""
    print("\n" + "=" * 60)
    print("示例 2: 爬取新闻列表")
    print("=" * 60)

    # 使用示例新闻网站（JSONPlaceholder）
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        # 获取 JSON 数据
        logger.info(f"正在获取新闻数据: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # 解析 JSON
        news_list = response.json()
        logger.info(f"获取到 {len(news_list)} 条新闻")

        # 处理前 5 条新闻
        news_data = []
        for news in news_list[:5]:
            news_item = {
                "id": news["id"],
                "title": news["title"],
                "body": news["body"],
                "user_id": news["userId"]  # API 返回的是 userId
            }
            news_data.append(news_item)

        # 保存为 JSON
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)

        with open(output_dir / "news.json", "w", encoding="utf-8") as f:
            json.dump(news_data, f, ensure_ascii=False, indent=2)
        print(f"✓ 新闻数据已保存到: {output_dir / 'news.json'}")

        # 保存为 CSV
        csv_file = output_dir / "news.csv"
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
            if news_data:
                writer = csv.DictWriter(f, fieldnames=news_data[0].keys())
                writer.writeheader()
                writer.writerows(news_data)
        print(f"✓ 新闻数据已保存到: {csv_file}")

        # 显示新闻
        print("\n新闻列表:")
        for news in news_data:
            print(f"  ID: {news['id']}")
            print(f"  标题: {news['title']}")
            print(f"  内容: {news['body'][:100]}...")
            print()

    except requests.exceptions.RequestException as e:
        logger.error(f"请求异常: {e}")


# ============================================================================
# 示例 3: 使用 CSS 选择器
# ============================================================================

def css_selector_example():
    """CSS 选择器示例"""
    print("\n" + "=" * 60)
    print("示例 3: CSS 选择器使用")
    print("=" * 60)

    # 创建示例 HTML
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>产品列表</title>
    </head>
    <body>
        <div class="product">
            <h2 class="product-name">产品 A</h2>
            <p class="product-price">价格: ¥99</p>
            <p class="product-desc">这是产品 A 的描述</p>
        </div>
        <div class="product">
            <h2 class="product-name">产品 B</h2>
            <p class="product-price">价格: ¥199</p>
            <p class="product-desc">这是产品 B 的描述</p>
        </div>
        <div class="product">
            <h2 class="product-name">产品 C</h2>
            <p class="product-price">价格: ¥299</p>
            <p class="product-desc">这是产品 C 的描述</p>
        </div>
    </body>
    </html>
    """

    # 解析 HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 使用 CSS 选择器
    print("使用 CSS 选择器提取数据:\n")

    # 选择所有产品
    products = soup.select('.product')
    print(f"找到 {len(products)} 个产品\n")

    product_list = []
    for product in products:
        # 使用 CSS 选择器提取信息
        name = product.select_one('.product-name').text
        price = product.select_one('.product-price').text
        desc = product.select_one('.product-desc').text

        product_info = {
            "name": name,
            "price": price,
            "description": desc
        }
        product_list.append(product_info)

        print(f"产品名称: {name}")
        print(f"价格: {price}")
        print(f"描述: {desc}")
        print("-" * 40)

    # 保存数据
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    with open(output_dir / "products.json", "w", encoding="utf-8") as f:
        json.dump(product_list, f, ensure_ascii=False, indent=2)
    print(f"\n✓ 产品数据已保存到: {output_dir / 'products.json'}")


# ============================================================================
# 示例 4: 处理表格数据
# ============================================================================

def scrape_table_data():
    """爬取表格数据示例"""
    print("\n" + "=" * 60)
    print("示例 4: 爬取表格数据")
    print("=" * 60)

    # 创建示例表格 HTML
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>学生成绩表</title>
    </head>
    <body>
        <table id="students">
            <thead>
                <tr>
                    <th>姓名</th>
                    <th>年龄</th>
                    <th>数学成绩</th>
                    <th>英语成绩</th>
                    <th>语文成绩</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>张三</td>
                    <td>18</td>
                    <td>95</td>
                    <td>88</td>
                    <td>92</td>
                </tr>
                <tr>
                    <td>李四</td>
                    <td>19</td>
                    <td>87</td>
                    <td>90</td>
                    <td>85</td>
                </tr>
                <tr>
                    <td>王五</td>
                    <td>18</td>
                    <td>92</td>
                    <td>85</td>
                    <td>90</td>
                </tr>
            </tbody>
        </table>
    </body>
    </html>
    """

    # 解析 HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 找到表格
    table = soup.find('table')
    if not table:
        print("未找到表格")
        return

    # 提取表头
    headers = []
    header_row = table.find('thead')
    if header_row:
        for th in header_row.find_all('th'):
            headers.append(th.text.strip())

    print(f"表格列名: {headers}\n")

    # 提取数据行
    data_rows = []
    body = table.find('tbody')
    if body:
        for row in body.find_all('tr'):
            row_data = [td.text.strip() for td in row.find_all('td')]
            if row_data:
                data_rows.append(row_data)

    # 显示数据
    print("表格数据:")
    for row in data_rows:
        print(row)

    # 转换为字典列表
    students = []
    for row in data_rows:
        student = dict(zip(headers, row))
        students.append(student)

    # 计算平均分
    if students:
        print("\n学生平均成绩:")
        for student in students:
            math = int(student['数学成绩'])
            english = int(student['英语成绩'])
            chinese = int(student['语文成绩'])
            avg = (math + english + chinese) / 3
            print(f"{student['姓名']}: {avg:.1f}")

    # 保存数据
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    with open(output_dir / "students.json", "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)
    print(f"\n✓ 学生数据已保存到: {output_dir / 'students.json'}")


# ============================================================================
# 示例 5: 处理分页
# ============================================================================

def scrape_paginated_data():
    """处理分页数据示例"""
    print("\n" + "=" * 60)
    print("示例 5: 处理分页数据")
    print("=" * 60)

    # 使用分页 API 示例
    base_url = "https://jsonplaceholder.typicode.com/posts"
    all_posts = []
    page = 1

    try:
        while True:
            # 构建分页 URL
            url = f"{base_url}?_page={page}&_limit=10"
            logger.info(f"正在获取第 {page} 页数据")

            response = requests.get(url, timeout=10)
            response.raise_for_status()

            # 检查响应头中的总数量
            total_count = response.headers.get('X-Total-Count')
            if total_count:
                total_count = int(total_count)
                logger.info(f"总数据量: {total_count}")

            # 解析数据
            posts = response.json()
            if not posts:
                logger.info("没有更多数据，停止爬取")
                break

            all_posts.extend(posts)
            logger.info(f"当前页有 {len(posts)} 条数据，累计 {len(all_posts)} 条")

            # 只爬取前 3 页作为示例
            if page >= 3:
                logger.info("达到最大页数限制，停止爬取")
                break

            page += 1
            time.sleep(1)  # 避免请求过快

        logger.info(f"爬取完成，总共获取 {len(all_posts)} 条数据")

        # 保存数据
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)

        with open(output_dir / "all_posts.json", "w", encoding="utf-8") as f:
            json.dump(all_posts, f, ensure_ascii=False, indent=2)
        print(f"✓ 所有数据已保存到: {output_dir / 'all_posts.json'}")

        # 显示统计信息
        print(f"\n数据统计:")
        print(f"  总条数: {len(all_posts)}")
        print(f"  页数: {page - 1}")
        print(f"  平均每页: {len(all_posts) / (page - 1):.1f} 条")

    except requests.exceptions.RequestException as e:
        logger.error(f"请求异常: {e}")


if __name__ == "__main__":
    print("\n🕷️  网络爬虫基础示例\n")

    # 确保输出目录存在
    Path("output").mkdir(exist_ok=True)

    # 运行所有示例
    basic_web_scraping()
    scrape_news_list()
    css_selector_example()
    scrape_table_data()
    scrape_paginated_data()

    print("\n" + "=" * 60)
    print("✅ 所有爬虫示例完成！")
    print("=" * 60)
    print("\n💡 接下来可以尝试：")
    print("1. 运行 02_advanced_scraper.py 学习高级爬虫技巧")
    print("2. 查看 output/ 目录中的爬取结果")
    print("3. 修改代码爬取真实网站数据")
    print("=" * 60 + "\n")
