import json
list_info = []
final_dict = {"list": list_info}
with open('../xh747364.github.io/a.json','w') as f: # 'a'表示append,即在原来文件内容后继续写数据（不清楚原有数据）
    json.dump(final_dict, f)
   
print(final_dict)

