import os
'''
need do step 2
1.change path
2.change dirpath position
'''
clearBeforePath='E:/Seafile/1'
clearAfterPath='E:/Seafile/1_align'

def clearBefore():
    with open('log.txt', 'a') as a_writer:
        file_count=0
        for dirpath, dirnames, filenames in os.walk(clearBeforePath):
            for file in filenames:
                file_count=file_count+1
                print(f"{file_count} \n")
                '''
                Update dirpath, Sample: dirpath[10:] ,cut root dir. 
                '''
                a_writer.write(f'{dirpath[0:]}\{file}\n')
    return
def clearAfter():
    with open('log2.txt', 'a') as a_writer:
        file_count=0
        for dirpath, dirnames, filenames in os.walk(clearAfterPath):
            for file in filenames:
                file_count=file_count+1
                print(f"{file_count} \n")
                '''
                Update dirpath, Sample: dirpath[10:] ,cut root dir. 
                '''
                a_writer.write(f'{dirpath[0:]}\{file}\n')

if __name__ == "__main__":
    clearBefore()
    clearAfter()
    fa=open("log.txt",'r')
    fb=open("log2.txt",'r')
    fc=open("log3.txt",'a')
    str1=[]
    str2=[]
    str_dump=[]
    for line in fa.readlines():
        str1.append(line.replace("\n",''))
    for line in fb.readlines():
        str2.append(line.replace("\n",''))

    for i in str1:
        if i in str2:
            str_dump.append(i)
    str_all=set(str1) #+str2
 
    for i in str_dump:
        if i in str_all:
            str_all.remove(i)

    for i in list(str_all):
        fc.write(i+'\n')