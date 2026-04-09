from requests_html import HTMLSession
import asyncio

async def get_full_reviews_requests_html():
    """使用requests-html获取完整评论"""
    session = HTMLSession()
    
    try:
        url = "https://movie.douban.com/subject/1292052/reviews"
        r = session.get(url)
        
        # 执行JavaScript渲染页面
        await r.html.arender(sleep=2, timeout=20)
        
        # 点击所有展开按钮
        unfold_buttons = r.html.find('a.unfold')
        for button in unfold_buttons[:3]:  # 前3个
            # 模拟点击
            await button.click()
            await asyncio.sleep(1)  # 等待加载
        
        # 重新获取页面内容
        await r.html.arender(sleep=1)
        
        # 提取完整内容
        reviews = r.html.find('.review-item')
        for review in reviews[:3]:
            title = review.find('h2 a', first=True).text
            content = review.find('.review-content', first=True)
            if content:
                print(f"标题: {title}")
                print(f"内容: {content.text[:300]}...")
                print("-" * 50)
                
    finally:
        session.close()

# 运行
# asyncio.run(get_full_reviews_requests_html())