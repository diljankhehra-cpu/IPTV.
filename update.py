import requests

def update_list():
    base_url = "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/"
    files = ["in", "in_distro", "in_doordarshan", "in_pishow", "in_samsung", "in_tango"]
    
    with open("in.m3u", "w", encoding="utf-8") as outfile:
        # 1. ਪਹਿਲਾਂ ਤੁਹਾਡੀ ਮੈਨੁਅਲ ਲਿਸਟ ਲਿਖੋ
        outfile.write('#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/in.xml.gz"\n')
        
        try:
            with open("channels.txt", "r", encoding="utf-8") as manual_file:
                outfile.write(manual_file.read() + "\n")
        except FileNotFoundError:
            print("channels.txt ਨਹੀਂ ਮਿਲੀ, ਸਿਰਫ ਆਟੋ-ਲਿਸਟ ਅਪਡੇਟ ਹੋ ਰਹੀ ਹੈ।")

        # 2. ਹੁਣ ਆਟੋਮੈਟਿਕ ਲਿਸਟਾਂ ਲਿਖੋ
        for file_name in files:
            url = f"{base_url}{file_name}.m3u"
            response = requests.get(url)
            
            if response.status_code == 200:
                lines = response.text.splitlines()
                # ਪਹਿਲੀ ਲਾਈਨ (#EXTM3U) ਛੱਡ ਕੇ ਬਾਕੀ ਸਾਰਾ ਡੇਟਾ ਲਿਖੋ
                for line in lines[1:]:
                    if line.strip():
                        outfile.write(line + "\n")
            else:
                print(f"Failed to fetch {file_name}")

if __name__ == "__main__":
    update_list()
