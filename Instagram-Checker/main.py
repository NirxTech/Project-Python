import json
import os

# Fungsi untuk memuat file JSON dengan aman
def load_json_file(filename):
    if not os.path.exists(filename):
        print(f"❌ File '{filename}' tidak ditemukan.")
        return None
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"❌ File '{filename}' tidak valid atau rusak.")
        return None

# Muat data dari file JSON
followers_data = load_json_file('followers_1.json')
following_data = load_json_file('following.json')

if followers_data is None or following_data is None:
    print("Program dihentikan karena file JSON tidak valid.")
    exit()

# Ambil username followers
followers_usernames = {
    item['string_list_data'][0]['value'] for item in followers_data
    if 'string_list_data' in item and item['string_list_data']
}

# Ambil username yang di-follow
following_usernames = {
    item['string_list_data'][0]['value'] for item in following_data.get('relationships_following', [])
    if 'string_list_data' in item and item['string_list_data']
}

# Cari siapa yang kamu follow tapi tidak follback
not_following_back = following_usernames - followers_usernames

# Cetak hasilnya
print("Yang kamu follow tapi tidak follback:")
if not not_following_back:
    print("Semua orang yang kamu follow sudah follback")
else:
    for username in sorted(not_following_back):
        print("-", username)
