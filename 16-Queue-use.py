import queue

# 新建一个队列，队列的最大容量为4
q = queue.Queue(4)

# qsize()反回队列的大小
print(q.qsize())

# empty()判断队列是否为空
print(q.empty())

# put()将一个数据放到队列中
# 如果队列满了发生阻塞，直到队列中的数据被取走，再加入数据
# 设置block=False关闭阻塞，队列满时再加抛出异常
for i in range(4):
    q.put(i)
try:
    q.put('已经满了再加', block=False)
except queue.Full:
    print("队列满了，已接收异常")

# full()判断队列是否满
print(q.full())

# get()从队列头取出一个数据
# 如果队列已空，发生阻塞，直到队列中有数据后再取出数据
# 设置block=False可以关闭阻塞，队列已空时再取抛出异常
for i in range(5):
    try:
        value = q.get(block=False)
    except queue.Empty:
        print("队列已空")
        break
    print(value)
