#coding=utf8

import pickle
import StringIO

class Person():
    '''
    自定义
    '''

    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def display(self):
        print 'name: ', self.name, ' address: ', self.address


jj = Person('JGood', '中国,杭州')
jj.display()

file = StringIO.StringIO()

#序列化
pickle.dump(jj, file, 0)

#序列化的结果
#print file.getvalue()


#反序列化时, 必须能找到相应的定义, 否则反序列化将失败
#del Person

file.seek(0)

jj1 = pickle.load(file)
jj1.display()

file.close()
