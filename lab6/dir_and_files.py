#1
import os


path = input("Input: ")


if not os.path.exists(path):
    print("Does not exist.")
else:
    
    items = os.listdir(path)
    
    directories = [item for item in items if os.path.isdir(os.path.join(path, item))]
    
    files = [item for item in items if os.path.isfile(os.path.join(path, item))]
    
    print("Directions:")
    print(directories)
    
    print("\nFiles:")
    print(files)
    
    print("\nAll elements:")
    print(items)


   
 #2
import os

path = r'C:\Windows\System32'
existence = os.path.exists(path)

if existence:
    ch=os.access(path, os.F_OK)
    print(f'Existence: {ch}')
    cho=os.access(path, os.R_OK)
    print(f'Readability: {cho}')
    chot=os.access(path, os.W_OK)
    print(f'Writeability: {chot}')
    choto=os.access(path, os.X_OK)
    print(f'Executeability: {ch}')
else:
    print("path doesnt exist")




#3
import os
path=r"C:\Users\sabin\OneDrive\Desktop\PP2\lab5"
dir=os.path.dirname(path)
file=os.path.basename(path)
if os.path.exists(path):
    print(f'directory-{dir}, file-{file}')
else:
    print('path doesnt exist')



#4
name=r"C:\Users\sabin\OneDrive\Desktop\PP2\lab6\row.txt"
file=open(name)
cnt=0
for line in file:
    cnt+=1
print(cnt)



#5
file_name="text.txt"
with open(file_name, "w") as file:
    file.write('[1, 2, 3, 4]')

arr=[1, 2, 4]
file_name="t.txt"
with open(file_name, "w") as file:
    for i in arr:
      file.write(str(i))




#6
for i in range(26):
    name=f'{chr(i+65)}.txt'
    with open(name, 'w') as file: 
        pass




#7
import os
name=r"C:\Users\sabin\OneDrive\Desktop\PP2\lab6\row.txt"
info=""
with open(name, 'r', encoding="UTF-8") as file:
    info=file.read()

n="new.txt"
with open(n, 'w', encoding="UTF-8") as file:
    file.write(info)



#8
import os
path = r"C:\Users\sabin\OneDrive\Desktop\PP2\1_booleans.py"

if os.path.exists(path) and os.access(path, os.F_OK):
    os.remove(path)  
    print("deleted")
else:
    print("path doesnt exist")
