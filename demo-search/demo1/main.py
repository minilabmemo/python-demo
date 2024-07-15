from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def crawl_search(keyword):
    try:
        url = f'https://tpml.ebook.hyread.com.tw/searchList.jsp?search_field=FullText&search_input={keyword}'

        # 设置Chrome选项
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # 无头模式，不显示浏览器窗口
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        # 启动Chrome浏览器
        service = Service('/path/to/chromedriver')  # 指定chromedriver的路径
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # 打开页面
        driver.get(url)

        # 等待页面加载完成
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'center')))

        # 等待一段时间以确保JavaScript加载完成
        time.sleep(5)

        # 获取页面内容
        page_source = driver.page_source

        # 使用BeautifulSoup解析页面内容
        soup = BeautifulSoup(page_source, 'html.parser')

        # 找到包含JavaScript生成内容的部分
        script_content = soup.find('script', text=lambda text: 'var aaa = \'/mservice/\'' in text)

        # 如果找到了相应的内容
        if script_content:
            search_result = script_content.text.strip()
            html_content = soup.prettify()  # 获取整个页面的HTML内容
            return {
                'id': 'test',
                'data': search_result,
                'html': html_content,
                'search': keyword
            }

        # 如果未找到目标内容
        return {
            'id': 'test',
            'data': '未找到目标内容',
            'search': keyword
        }

    except Exception as e:
        print('Error fetching data:', e)
        return {
            'id': 'test',
            'data': None,
            'search': keyword
        }

    finally:
        driver.quit()  # 关闭浏览器

# 测试
if __name__ == "__main__":
    keyword = 'test'  # 替换为你想要搜索的关键词
    result = crawl_search(keyword)
    print(result)
