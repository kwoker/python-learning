"""
高级网络爬虫示例
使用 Scrapy、Selenium 和其他高级技术
"""

import time
import json
import csv
from pathlib import Path
from typing import List, Dict
import logging
import random

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# ============================================================================
# 示例 1: 使用 Scrapy 框架（伪代码示例）
# ============================================================================

def scrapy_example():
    """Scrapy 框架示例（伪代码）"""
    print("=" * 60)
    print("示例 1: Scrapy 框架使用")
    print("=" * 60)

    print("""
Scrapy 是一个强大的 Python 爬虫框架。以下是基本使用示例：

1. 安装 Scrapy:
   pip install scrapy

2. 创建 Scrapy 项目:
   scrapy startproject myproject

3. 创建爬虫:
   scrapy genspider example example.com

4. Scrapy 爬虫代码示例:

import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['http://example.com']

    def parse(self, response):
        # 提取标题
        title = response.css('title::text').get()

        # 提取所有链接
        links = response.css('a::attr(href)').getall()

        yield {
            'title': title,
            'links': links
        }

        # 跟随链接
        for link in links:
            yield response.follow(link, self.parse)

5. 运行爬虫:
   scrapy crawl example -o output.json
    """)

    # 模拟 Scrapy 输出
    sample_data = {
        "spider_name": "example",
        "items_scraped": 100,
        "status": "completed",
        "output_file": "output/scrapy_results.json"
    }

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    with open(output_dir / "scrapy_example.json", "w", encoding="utf-8") as f:
        json.dump(sample_data, f, ensure_ascii=False, indent=2)
    print(f"\n✓ Scrapy 示例配置已保存到: {output_dir / 'scrapy_example.json'}")


# ============================================================================
# 示例 2: 使用 Selenium 处理动态内容
# ============================================================================

def selenium_example():
    """Selenium 示例（伪代码）"""
    print("\n" + "=" * 60)
    print("示例 2: Selenium 处理动态内容")
    print("=" * 60)

    print("""
Selenium 用于处理 JavaScript 渲染的动态网页：

1. 安装 Selenium:
   pip install selenium

2. 下载浏览器驱动（ChromeDriver）

3. Selenium 代码示例:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 启动浏览器
driver = webdriver.Chrome()
driver.get('https://example.com')

# 等待元素加载
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'content'))
)

# 提取数据
title = driver.find_element(By.TAG_NAME, 'h1').text
paragraphs = driver.find_elements(By.TAG_NAME, 'p')

data = {
    'title': title,
    'content': [p.text for p in paragraphs]
}

# 关闭浏览器
driver.quit()
    """)

    # 模拟 Selenium 输出
    sample_data = {
        "browser": "Chrome",
        "page_title": "示例页面",
        "elements_found": 15,
        "dynamic_content": True,
        "wait_time": 5.2,
        "data": {
            "title": "动态加载的内容",
            "paragraphs": ["段落1", "段落2", "段落3"],
            "images": 5,
            "links": 10
        }
    }

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    with open(output_dir / "selenium_results.json", "w", encoding="utf-8") as f:
        json.dump(sample_data, f, ensure_ascii=False, indent=2)
    print(f"\n✓ Selenium 示例结果已保存到: {output_dir / 'selenium_results.json'}")


# ============================================================================
# 示例 3: 异步爬虫（aiohttp + asyncio）
# ============================================================================

def async_scraper_example():
    """异步爬虫示例"""
    print("\n" + "=" * 60)
    print("示例 3: 异步爬虫")
    print("=" * 60)

    import asyncio
    import aiohttp

    print("""
异步爬虫可以大幅提高爬取效率：

异步爬虫代码示例:

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
    """)

    # 模拟异步爬取结果
    print("\n模拟异步爬取过程...")

    async def simulate_scraping():
        """模拟异步爬取"""
        urls = [
            "https://api.example.com/data/1",
            "https://api.example.com/data/2",
            "https://api.example.com/data/3",
            "https://api.example.com/data/4",
            "https://api.example.com/data/5"
        ]

        results = []
        for url in urls:
            # 模拟网络请求
            await asyncio.sleep(random.uniform(0.1, 0.5))
            result = {
                "url": url,
                "status": "success",
                "data": f"数据来自 {url.split('/')[-1]}",
                "timestamp": time.time()
            }
            results.append(result)
            logger.info(f"完成爬取: {url}")

        return results

    # 运行模拟
    start_time = time.time()
    try:
        # 检查是否在事件循环中
        loop = asyncio.get_event_loop()
        if loop.is_running():
            # 如果已有循环，运行在新线程中
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(asyncio.run, simulate_scraping())
                results = future.result()
        else:
            results = loop.run_until_complete(simulate_scraping())
    except RuntimeError:
        # 如果没有循环，创建新的
        results = asyncio.run(simulate_scraping())

    elapsed_time = time.time() - start_time

    # 保存结果
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    with open(output_dir / "async_results.json", "w", encoding="utf-8") as f:
        json.dump({
            "total_urls": len(results),
            "elapsed_time": elapsed_time,
            "avg_time_per_url": elapsed_time / len(results),
            "results": results
        }, f, ensure_ascii=False, indent=2)

    print(f"\n✓ 异步爬取结果已保存到: {output_dir / 'async_results.json'}")
    print(f"爬取 {len(results)} 个 URL 用时: {elapsed_time:.2f} 秒")


# ============================================================================
# 示例 4: 数据清洗和处理
# ============================================================================

def data_cleaning_example():
    """数据清洗示例"""
    print("\n" + "=" * 60)
    print("示例 4: 数据清洗和处理")
    print("=" * 60)

    # 模拟爬取的原始数据（包含噪音）
    raw_data = [
        {"title": "  苹果 iPhone 15 Pro  ", "price": "¥8,999", "rating": "4.8/5"},
        {"title": "华为 Mate 60 Pro", "price": "¥6999", "rating": " 4.6 / 5 "},
        {"title": "小米14 Ultra", "price": "￥5999", "rating": "4.7/5"},
        {"title": "三星 Galaxy S24", "price": "¥7999", "rating": "4.5 /5"},
        {"title": "   OPPO Find X7   ", "price": "￥4999", "rating": "4.4/5"}
    ]

    print("原始数据:")
    for item in raw_data:
        print(f"  {item}")

    # 数据清洗
    cleaned_data = []
    for item in raw_data:
        cleaned_item = {
            # 清理标题（去除空格）
            "title": item["title"].strip(),
            # 清理价格（统一格式，去除符号）
            "price_numeric": int(item["price"].replace("¥", "").replace("￥", "").replace(",", "")),
            # 清理评分（提取数字，处理 "4.6 / 5" 和 "4.8/5" 格式）
            "rating_numeric": float(item["rating"].split('/')[0].strip())
        }
        cleaned_data.append(cleaned_item)

    print("\n清洗后的数据:")
    for item in cleaned_data:
        print(f"  {item}")

    # 数据处理和分析
    print("\n数据分析:")
    avg_price = sum(item["price_numeric"] for item in cleaned_data) / len(cleaned_data)
    avg_rating = sum(item["rating_numeric"] for item in cleaned_data) / len(cleaned_data)

    print(f"  平均价格: ¥{avg_price:.2f}")
    print(f"  平均评分: {avg_rating:.2f}")

    # 排序
    sorted_by_price = sorted(cleaned_data, key=lambda x: x["price_numeric"])
    print(f"\n价格排序（从低到高）:")
    for item in sorted_by_price:
        print(f"  {item['title']}: ¥{item['price_numeric']}")

    # 保存清洗后的数据
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    with open(output_dir / "cleaned_data.json", "w", encoding="utf-8") as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=2)

    # 保存为 CSV
    csv_file = output_dir / "cleaned_data.csv"
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        if cleaned_data:
            writer = csv.DictWriter(f, fieldnames=cleaned_data[0].keys())
            writer.writeheader()
            writer.writerows(cleaned_data)

    print(f"\n✓ 清洗后数据已保存:")
    print(f"  JSON: {output_dir / 'cleaned_data.json'}")
    print(f"  CSV: {csv_file}")


# ============================================================================
# 示例 5: 反反爬策略
# ============================================================================

def anti_anti_crawler_example():
    """反反爬策略示例"""
    print("\n" + "=" * 60)
    print("示例 5: 反反爬策略")
    print("=" * 60)

    print("""
常见的反反爬策略：

1. User-Agent 轮换:
   - 使用不同的浏览器标识

2. 请求头伪装:
   - 添加 Accept、Accept-Language 等

3. 代理 IP:
   - 使用代理池轮换 IP

4. 请求频率控制:
   - 添加随机延迟
   - 避免请求过快

5. 会话保持:
   - 使用 cookies 和 sessions

6. 验证码处理:
   - OCR 识别
   - 打码平台

7. 分布式爬取:
   - 使用多台机器
   - 负载均衡
    """)

    # 模拟实现：随机延迟
    def random_delay(min_sec=1, max_sec=3):
        """随机延迟"""
        delay = random.uniform(min_sec, max_sec)
        logger.info(f"等待 {delay:.2f} 秒...")
        time.sleep(delay)

    # 模拟爬取
    print("\n模拟爬取过程（带反反爬策略）:")

    urls = [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3"
    ]

    results = []
    for i, url in enumerate(urls, 1):
        logger.info(f"正在爬取 {i}/{len(urls)}: {url}")

        # 随机 User-Agent
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
        ]
        user_agent = random.choice(user_agents)

        # 模拟请求
        random_delay(0.5, 1.5)

        result = {
            "url": url,
            "status": "success",
            "user_agent": user_agent,
            "timestamp": time.time(),
            "data_length": random.randint(100, 1000)
        }
        results.append(result)
        logger.info(f"爬取完成，获取 {result['data_length']} 字节数据")

    # 保存结果
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    with open(output_dir / "anti_crawler_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n✓ 反反爬爬取结果已保存到: {output_dir / 'anti_crawler_results.json'}")


if __name__ == "__main__":
    print("\n🕷️  高级网络爬虫示例\n")

    # 确保输出目录存在
    Path("output").mkdir(exist_ok=True)

    # 运行所有示例
    scrapy_example()
    selenium_example()
    async_scraper_example()
    data_cleaning_example()
    anti_anti_crawler_example()

    print("\n" + "=" * 60)
    print("✅ 所有高级爬虫示例完成！")
    print("=" * 60)
    print("\n💡 接下来可以尝试：")
    print("1. 安装 scrapy: pip install scrapy")
    print("2. 安装 selenium: pip install selenium")
    print("3. 安装 aiohttp: pip install aiohttp")
    print("4. 查看 output/ 目录中的爬取结果")
    print("5. 编写自己的爬虫项目")
    print("=" * 60 + "\n")
