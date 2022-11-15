import requests
def find_update(ver):
    data = open('ETC\\update\\ver_of_dos.txt',"r")
    data_update = data.read()
    data.close()
    for x2 in data_update:
        if x2 == ver:
            return False
        else:
            return True

def get_update(etc):
    data = open('ETC\\update\\ver_of_dos.txt',"r")
    data_update = data.read()
    data.close()
    etc = ""
    return data_update

def download_file(url, local_file_path):

    response = requests.get(url=url)
    if response.status_code == 200:
        with open(local_file_path, 'w') as local_file:
            local_file.write(str(response.text))
