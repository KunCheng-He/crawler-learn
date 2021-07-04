import json


# books = [
#     {
#         'name': "水浒传",
#         'prices': 56
#     },
#     {
#         'name': "三国演义",
#         'prices': 79
#     }
# ]
# # dumps将Python对象转化为json字符串
# result = json.dumps(books, ensure_ascii=False)
# print(result)
# # dump直接将Python对象转化为json字符串写入文件中
# with open('books.json', 'w', encoding='utf-8') as f:
#     json.dump(books, f, ensure_ascii=False)

json_str = '[{"name": "水浒传", "prices": 56}, {"name": "三国演义", "prices": 79}]'

# loads将json字符串转化为Python对象
result = json.loads(json_str)
print(result, type(result))
# load将文件中的json字符串转化为Python对象
with open('books.json', 'r', encoding='utf-8') as f:
    res = json.load(f)
    print(res, type(res))
