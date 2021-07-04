import time
import threading

#
# def coding():
#     for i in range(3):
#         print(i, "写代码...")
#         time.sleep(1)
#
#
# def drawing():
#     for i in range(3):
#         print(i, "画画...")
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     # 指定target参数来指定线程运行时执行的函数
#     th1 = threading.Thread(target=coding)
#     th2 = threading.Thread(target=drawing)
#
#     th1.start()
#     th2.start()


# class coding(threading.Thread):
#     # 重写run()方法，线程开始执行，从这个方法开始
#     def run(self) -> None:
#         # threading.current_thread()获取当前线程对象
#         thd = threading.current_thread()
#         print("当前线程的名字：", thd.name)
#         for i in range(3):
#             print("写代码...")
#             time.sleep(1)
#
#
# if __name__ == '__main__':
#     # 获取整个程序的所有线程
#     thd1 = threading.enumerate()
#     print(thd1)
#     th1 = coding()
#     th1.start()
#     thd2 = threading.enumerate()
#     print(thd2)

# value = 0
# # 创建一个锁
# lock = threading.Lock()
#
#
# def add_value():
#     # 在函数中使用全局变量是，用global关键字进行说明
#     global value
#     # 上锁
#     lock.acquire()
#     for i in range(1000000):
#         value += 1
#     # 释放锁
#     lock.release()
#     print(value)
#
#
# if __name__ == '__main__':
#     # 创建两个线程来执行
#     for j in range(2):
#         th = threading.Thread(target=add_value)
#         th.start()

# condition = threading.Condition()
#
# condition.notify_all()
