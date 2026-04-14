import requests
import json
import os

# QRadar Bağlantı Məlumatları
# QRadar Bağlantı Məlumatları
QRADAR_IP = "YOUR_QRADAR_IP"  # 16.16.141.142
API_TOKEN = "YOUR_API_TOKEN"  # f55c9495-c441-4a73-b69b-1dd6044ccabe

headers = {
    'SEC': API_TOKEN,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

def upload_rules():
    # Cari qovluqdakı bütün .json fayllarını tapır
    files = [f for f in os.listdir('.') if f.endswith('.json')]
    
    for file_name in files:
        with open(file_name, 'r') as f:
            rule_data = json.load(f)
            
            # QRadar API Endpoint (Analytics Rules)
            url = f"https://{QRADAR_IP}/api/analytics/rules"
            
            # Qeyd: Real mühitdə verify=True olmalıdır (SSL sertifikat varsa)
            response = requests.post(url, headers=headers, data=json.dumps(rule_data), verify=False)
            
            if response.status_code == 201:
                print(f"[+] Uğurlu: {rule_data['name']} QRadar-a əlavə edildi.")
            else:
                print(f"[-] Xəta: {rule_data['name']} yüklənə bilmədi. Status: {response.status_code}")

if __name__ == "__main__":
    upload_rules()
