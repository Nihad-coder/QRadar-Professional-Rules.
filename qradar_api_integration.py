import requests
import json
import os

# Secrets-dəki adlarla eyni olmalıdır:
QRADAR_IP = os.environ.get('QRADAR_IPV4')
QRADAR_TOKEN = os.environ.get('QRADAR_TOKEN6')

headers = {
    'SEC': QRADAR_TOKEN, # Bura diqqət, yuxarıdakı dəyişən adı ilə eyni olmalıdır
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
