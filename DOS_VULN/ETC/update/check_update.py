import requests
def find_update(ver):
    data = open('ETC\\\\update\\\\ver_of_dos.txt',"r")
    data_update = data.read()
    data.close()
    for x2 in data_update:
        if x2 != ver:
            return True
        else:
            return False

def get_update(etc):
    data = open('ETC\\\\update\\\\ver_of_dos.txt',"r")
    data_update = data.read()
    data.close()
    etc = ""
    return data_update

def download_file(url, local_file_path):

    response = requests.get(url=url)
    if response.status_code == 200:
        with open(local_file_path, 'wb') as local_file:
            for chunk in response.iter_content(chunk_size=128):
                local_file.write(chunk)
