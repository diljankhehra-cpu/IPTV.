import requests
import os

def update_list():
    files = ["in", "in_distro", "in_doordarshan", "in_pishow", "in_samsung", "in_tango"]
    
    with open("in.m3u", "w", encoding="utf-8") as outfile:
        outfile.write("#EXTM3U\n")
        
        for file_name in files:
            url = f"https://iptv-org.github.io/iptv/languages/{file_name}.m3u"
            response = requests.get(url)
            if response.status_code == 200:
                lines = response.text.splitlines()
                for line in lines[1:]: # ਪਹਿਲੀ ਲਾਈਨ ਛੱਡ ਕੇ
                    if line.strip():
                        outfile.write(line + "\n")

    # ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਕਿ git ਨੂੰ ਲੱਗੇ ਕਿ ਕੁਝ ਬਦਲਿਆ ਹੈ
    os.system("echo ' ' >> in.m3u") 

if __name__ == "__main__":
    update_list()
