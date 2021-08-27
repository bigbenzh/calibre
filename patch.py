import re
import os
root_path = os.path.dirname(__file__)

# config_base.py
t = None
file_path = os.path.join(root_path,"src/calibre/utils/config_base.py")
with open(file_path) as f:
    t=f.read()
assert t 
i = t.index("if prefs['installation_uuid'] is None:")+3
t = t[:i]+ "True or "+t[i:]
with open(file_path,"w") as f:
    f.write(t)

def replace(text,pattern,s):
    for t in pattern.findall(text):
        text = text.replace(t,s)
    return text

# update.py and collection.py
pattern = re.compile("headers={[\s\S]+}\n")
file_path = os.path.join(root_path,"src/calibre/gui2/update.py")
with open(file_path) as f:
    t = f.read()
t = replace(t,pattern,"headers={}\n")
with open(file_path,"w") as f:
    f.write(t)

file_path = os.path.join(root_path,"src/calibre/web/feeds/recipes/collection.py")
with open(file_path) as f:
    t = f.read()
t = replace(t,pattern,"headers={}\n")
with open(file_path,"w") as f:
    f.write(t)
