# QRadar SIEM Professional Rules & API Integration

Bu layihə SOC mühitində kibertəhlükəsizlik insidentlərini aşkar etmək üçün hazırlanmış 10 kritik qaydanı (rules) və QRadar API vasitəsilə bu qaydaların idarə olunmasını əhatə edir.

## 🛠 Texnologiyalar
* **SIEM:** IBM QRadar
* **Dil:** AQL (Ariel Query Language), Python
* **İnteqrasiya:** QRadar REST API

## 📝 Qaydaların Siyahısı
1. **Brute Force Detection:** Eyni IP-dən ardıcıl uğursuz girişlər.
2. **Suspicious PowerShell:** Təhlükəli parametrlərlə işə düşən skriptlər.
*(Digərlərini bura əlavə edəcəyik)*
## 🚀 Necə İstifadə Etməli?
1. QRadar API Tokeninizi `qradar_api_integration.py` faylına daxil edin.
2. Skripti işə salın: `python qradar_api_integration.py`
3. Qaydalar avtomatik olaraq QRadar **Offense > Rules** panelində görünəcək.
