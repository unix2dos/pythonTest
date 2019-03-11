import logging

logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

# 直接把这个文件命名为 logging.py
# 一定不要和系统名同名
