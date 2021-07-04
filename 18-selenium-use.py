import select

from selenium import webdriver
import time

driver = webdriver.Firefox()

# 请求一个网址
# driver.get('https://www.baidu.com')

# 关闭当前页面
# driver.close()
# 关闭整个浏览器
# driver.quit()

# 根据id来查找元素
# inputTag = driver.find_element_by_id('kw')

# 根据类名查找元素，find_elements_by_class_name()查找所有这个类名，返回列表
# inputTag = driver.find_element_by_class_name('s_ipt')

# 根据name值查找元素
# inputTag = driver.find_element_by_name('wd')

# 根据Tag名称查找元素，这里返回只返回第一个input标签
# inputTag = driver.find_element_by_tag_name('input')

# 根据xpath语法查找元素
# inputTag = driver.find_element_by_xpath('//input[@id="kw"]')

# 根据CSS选择器查找元素
# inputTag = driver.find_element_by_css_selector("#form #kw")

# 操作输入框，填充数据
# inputTag.send_keys("Python")

# driver.get("https://www.zhihu.com/signin?next=%2Fhot")
# username = driver.find_element_by_name('username')
# password = driver.find_element_by_name('password')
# login = driver.find_element_by_class_name("SignFlow-submitButton")
# # 输入数据
# username.send_keys("18788748257")
# password.send_keys("byackzh89HKC")
# # 点击按钮
# login.click()

# # 页面内嵌套另一个页面，我们直接访问源页面
# driver.get("https://xui.ptlogin2.qq.com/cgi-bin/xlogin?target=self&appid=522005705&daid=4&s_url=https://mail.qq.com/cgi-bin/readtemplate?check=false%26t=loginpage_new_jump%26vt=passport%26vm=wpt%26ft=loginpage%26target=&style=25&low_login=1&proxy_url=https://mail.qq.com/proxy.html&need_qr=0&hide_border=1&border_radius=0&self_regurl=http://zc.qq.com/chs/index.html?type=1&app_id=11005?t=regist&pt_feedback_link=http://support.qq.com/discuss/350_1.shtml&css=https://res.mail.qq.com/zh_CN/htmledition/style/ptlogin_input_for_xmail51328e.css")
# # 选中checkbox元素
# checkboxTag = driver.find_element_by_id("q_low_login_enable")
# checkboxTag.click()

# from selenium.webdriver.support.ui import Select
# driver.get("https://www.w3school.com.cn/tiy/t.asp?f=eg_html_select")
# select1 = Select(driver.find_element_by_tag_name("select"))
# select1.select_by_index(3)
# select1.select_by_visible_text("")
