import bao1
import os

print("_" * 30)
file = open("README.txt",encoding="utf-8")
text=file.read()
print(text)
# for texts in file:
#     print(texts,end="")
file.close()

file1=open("README.txt",encoding="UTF-8")
while True:
    text=file1.readline()
    print(text,end="")
    if not text:
        break
file1.close()

# file_read=open("README.txt",encoding="UTF-8")
# file_write=open("README【附件】.txt","w",encoding="UTF-8")
# text=file_read.read()
# file_write.write(text)
# file_read.close()
# file_write.close()

file_read=open("README.txt",encoding="UTF-8")
file_write=open("README【附件】.txt","w",encoding="UTF-8")
while True:
    text=file_read.readline()
    if not text:
        break
    file_write.write(text)
file_write.close()
file_read.close()

os.rename("README.txt","READ.txt")
os.remove("READ.txt")
