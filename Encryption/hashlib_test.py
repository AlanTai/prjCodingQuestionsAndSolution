# -*- coding: utf-8 -*-
import hashlib

if __name__ == "__main__":
    str_u = u'你好,連珍奶杯子也適用耶'
    str_gb = str_u.encode('gbk')
    str_u8 = str_u.encode('utf-8')

    print hashlib.md5(str_u8).hexdigest()