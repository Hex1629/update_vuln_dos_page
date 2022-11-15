import os
print("""
SETUP CNC OR CONTROL PANEL . . .
1] PREFIX COMMAND SETUP
2] UPDATE CHECK (COMING SOON)
""")
prefix_get = input("prefix:")
pre_import = open("ETC\\\\prefix.txt",'w')
pre_import.write(str(prefix_get))
pre_import.close()

print("removeing setup.py")
os.remove(__file__)
