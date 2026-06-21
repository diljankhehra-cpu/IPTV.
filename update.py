import requests
import json

def update_list():
    # ਅਸਲੀ streams API URL
    url = "https://iptv-org.github.io/api/streams.json"
    try:
        response = requests.get(url)
        data = response.json()
        
        # ਫਾਈਲ ਵਿੱਚ ਲਿਖਣਾ ਸ਼ੁਰੂ ਕਰੋ
        with open("in.m3u", "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            
            count = 0
            for item in data:
                # ਇੱਥੇ ਦੇਖੋ ਕਿ ਕੀ 'country' ਫੀਲਡ 'in' ਹੈ
                if item.get("country") == "in":
                    f.write(f"#EXTINF:-1,{item.get('title', 'Channel')}\n")
                    f.write(f"{item.get('url')}\n")
                    count += 1
            
            print(f"Total channels found: {count}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_list()
