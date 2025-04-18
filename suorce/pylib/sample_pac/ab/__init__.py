'''
smaple_pac/ab/__init__.py
from sample_pac.ab import * 수행할 경우 자동 import될 모듈지정할 수 있음 (__all__)

smaple_pac/ab/a.py
smaple_pac/ab/b.py
'''
__all__ = ['a']
print('sample_pac 패키지 안의 ab 패키지 로드됩니다')