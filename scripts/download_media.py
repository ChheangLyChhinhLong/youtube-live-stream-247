import os
import requests
import gspread

# Connect to Google Sheets API
gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key(os.getenv('SPREADSHEET_ID'))

# Fetch Playlist
playlist_sheet = sh.worksheet('Playlist')
records = playlist_sheet.get_all_records()

os.makedirs('assets', exist_ok=True)

with open('assets/playlist.concat', 'w') as concat_file:
    for row in records:
        if str(row.get('Enabled')).upper() == 'TRUE':
            file_id = row['Google Drive File ID']
            file_name = f"assets/{file_id}.mp3"
            
            # Direct Google Drive Download URL
            download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
            
            if not os.path.exists(file_name):
                print(f"Downloading {row['Track Name']}...")
                res = requests.get(download_url)
                with open(file_name, 'wb') as f:
                    f.write(res.content)
            
            concat_file.write(f"file '{file_id}.mp3'\n")
