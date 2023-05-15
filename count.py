from collections import Counter

def count(s):
    return dict(Counter(s))

# def count(s):
#     export = {}
#     [
#         export.update({c: s.count(c)})
#         for c in s if c not in export.keys()
#     ]
#     return export    

if __name__ == '__main__':
    print(count("aabb"))