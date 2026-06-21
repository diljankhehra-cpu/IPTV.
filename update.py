import requests

def update_list():
    # streams ਫੋਲਡਰ ਵਿੱਚ ਸਾਰੀਆਂ ਫਾਈਲਾਂ ਦੇ ਨਾਮ
    files = ["in", "in_distro", "in_doordarshan", "in_pishow", "in_samsung", "in_tango"]
    
    with open("in.m3u", "w", encoding="utf-8") as outfile:
        outfile.write("#EXTM3U\n")
        
        for file_name in files:
            # ਸਹੀ path: https://iptv-org.github.io/iptv/streams/in.m3u
            url = f"https://iptv-org.github.io/iptv/streams/{file_name}.m3u"
            response = requests.get(url)
            
            if response.status_code == 200:
                lines = response.text.splitlines()
                # ਪਹਿਲੀ ਲਾਈਨ (#EXTM3U) ਛੱਡ ਕੇ ਬਾਕੀ ਡੇਟਾ ਲਿਖੋ
                for line in lines[1:]:
                    if line.strip():
                        outfile.write(line + "\n")
            else:
                print(f"Error fetching {file_name}: {response.status_code}")

if __name__ == "__main__":
    update_list()
