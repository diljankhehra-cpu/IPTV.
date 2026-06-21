import requests

def update_list():
    # ਉਹ ਸਾਰੀਆਂ ਫਾਈਲਾਂ ਜੋ ਤੈਨੂੰ ਚਾਹੀਦੀਆਂ ਹਨ
    files = ["in", "in_distro", "in_doordarshan", "in_pishow", "in_samsung", "in_tango"]
    
    with open("in.m3u", "w", encoding="utf-8") as outfile:
        outfile.write("#EXTM3U\n")
        
        for file_name in files:
            url = f"https://iptv-org.github.io/iptv/languages/{file_name}.m3u"
            response = requests.get(url)
            if response.status_code == 200:
                # ਫਾਈਲ ਵਿੱਚੋਂ ਪਹਿਲੀ ਲਾਈਨ (#EXTM3U) ਹਟਾ ਕੇ ਬਾਕੀ ਡੇਟਾ ਜੋੜੋ
                lines = response.text.splitlines()
                for line in lines[1:]: # ਪਹਿਲੀ ਲਾਈਨ ਛੱਡ ਕੇ
                    if line.strip():
                        outfile.write(line + "\n")

update_list()
