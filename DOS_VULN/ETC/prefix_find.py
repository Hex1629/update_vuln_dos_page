def find_prefix(get):
    pre_import = open("ETC\\prefix.txt",'r')
    pre_command = pre_import.read()
    pre_import.close()
    get = ""
    return pre_command