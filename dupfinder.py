import os
import sys
import hashlib
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font


if len(sys.argv) != 2:
    print("Usage: \n\tdupfinder [directory]")


rootdir = sys.argv[1]
fileList = {}


for root, folders, files in os.walk(rootdir):
    #for folder in folders:
    #    print(os.path.join(root, folder))

    for file in files:
        filePath = os.path.join(root, file)
        f = open( filePath, 'rb' )
        content = f.read()
        digest = hashlib.md5(content).hexdigest()
        if digest in fileList: 
            fileList[digest].append(filePath)
        else:
            fileList[digest] = [filePath]
        f.close()

        # folderOut.close()

#for key in fileList:
#    if len(fileList[key]) > 1:
#        print(key)
#        print(fileList[key])


root = tk.Tk()
root.title('Dupfinder')
root.geometry('1200x900')

root.tk.call('tk', 'scaling', 2.0)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

tree = ttk.Treeview(root)
tree.heading('#0', text='Duplicates', anchor='w')

nid = 0
for key in fileList: 
    if len(fileList[key]) > 1:
        tree.insert('', tk.END, text=key, iid=nid, open=False, tags=('font'))
        kid = nid
        nid += 1
        for di in fileList[key]:
            tree.insert('', tk.END, text=di, iid=nid, open=False, tags=('font'))
            tree.move(nid, kid, nid-kid-1)
            nid += 1

tree.tag_configure('font', font=Font(family="Times New Roman", size=16))

# place the Treeview widget on the root window
tree.grid(row=0, column=0, sticky='nsew')

# run the app
root.mainloop()

