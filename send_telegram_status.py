import os
import glob
import datetime
import urllib.request
import urllib.parse

def send_telegram_status():
    posts_dir = "_posts"
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("Telegram token or chat ID missing.")
        return
        
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
    today_str = now.strftime("%Y-%m-%d")
    
    scheduled_list = []
    for filepath in glob.glob(os.path.join(posts_dir, "*.md")):
        if "gitkeep" in filepath:
            continue
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            continue
        
        title = ""
        p_date = ""
        p_time = ""
        
        parts = content.split("---")
        if len(parts) >= 3:
            yaml_lines = parts[1].split("\n")
            for line in yaml_lines:
                if line.startswith("title:"):
                    title = line.replace("title:", "").strip().strip('"').strip("'")
                if line.startswith("date:"):
                    date_val = line.replace("date:", "").strip()
                    date_parts = date_val.split()
                    if len(date_parts) >= 2:
                        p_date = date_parts[0]
                        p_time = ":".join(date_parts[1].split(":")[:2])
                        
        if p_date and p_date >= today_str:
            scheduled_list.append((p_date, p_time, title))
            
    scheduled_list.sort(key=lambda x: (x[0], x[1]))
    
    if not scheduled_list:
        message = "[Head Skinification Lab]\n오늘 이후로 예약된 포스트가 존재하지 않습니다."
    else:
        message = "[Head Skinification Lab]\n📅 블로그 예약 발행 현황 알림\n"
        current_date = ""
        for p_date, p_time, title in scheduled_list:
            if current_date != p_date:
                current_date = p_date
                message += f"\n■ {current_date}\n"
            message += f"- {p_time} : {title}\n"
            
    try:
        data = urllib.parse.urlencode({"chat_id": chat_id, "text": message}).encode("utf-8")
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        urllib.request.urlopen(req)
        print("Telegram notification sent successfully.")
    except Exception as e:
        print(f"Error sending Telegram message: {e}")

if __name__ == "__main__":
    send_telegram_status()
