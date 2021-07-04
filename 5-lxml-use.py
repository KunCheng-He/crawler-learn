from lxml import etree

# text = """
# <div>
#     <ul>
#         <li class="item-0"><a href="index.html"></a></li>
#         <li class="item-1"><a href="index.html"></a></li>
#         <li class="item-2"><a href="index.html"></a>
#     </ul>
# </div>
# """
#
# # 将字符串解析为HTML文档
# html = etree.HTML(text)
# print(html)
#
# # 将字符串系列化html
# result = etree.tostring(html).decode('utf-8')
# print(result)

# 从文件中读取html，如果不能因为html文件的规范问题不能直接读取，那我们需要加入第一行，指定编码方式
# parse = etree.HTMLParser(encoding='utf-8')
# html = etree.parse('Xpath-test.html', parser=parse)
# print(etree.tostring(html).decode('utf-8'))


# lxml使用xpath
text = """
<!-- hello.thml -->
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-0"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>"""

html = etree.HTML(text)

# 获取所有li标签
# result = html.xpath('//li')
# for i in result:
#     print(etree.tostring(i))

# 获取所有li标签下所有class属性值
# result = html.xpath('//li/@class')
# print(result)

# 获取li标签下href为www.baidu.com的a标签，找不到会返回空列表
# result = html.xpath('//li/a[@href="www.baidu.com"]')
# print(result)

# 获取li下所有span标签
# result = html.xpath('//li//span')
# for i in result:
#     print(etree.tostring(i))

# 获取li下所有a标签里的class
# result = html.xpath('//li/a//@class')
# print(result)

# 获取最后一个li的a标签的href值
# result = html.xpath('//li[last()]/a/@href')
# print(result)

# 获取倒数第二个li元素的内容
result0 = html.xpath('//li[last()-1]/a')
print(result0[0].text)

result1 = html.xpath('//li[last()-1]/a/text()')
print(result1)