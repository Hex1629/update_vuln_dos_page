import os
print("""
.dP"Y8 888888 888888 88   88 88""Yb     8888b.   dP"Yb  .dP"Y8 
`Ybo." 88__     88   88   88 88__dP      8I  Yb dP   Yb `Ybo." 
o.`Y8b 88""     88   Y8   8P 88"""       8I  dY Yb   dP o.`Y8b 
8bodP' 888888   88   `YbodP' 88         8888Y"   YbodP  8bodP' 

SETUP CNC OR CONTROL PANEL . . .
1] PREFIX COMMAND SETUP
2] UPDATE CHECK (COMING SOON)
""")
print("example prefix command: . / - _ + = ! @ # $ % ^ & * > < ?")
prefix_get = input("prefix:")
pre_import = open("ETC\\prefix.txt",'w')
pre_import.write(str(prefix_get))
pre_import.close()

print("removeing setup.py")
os.remove(__file__)
