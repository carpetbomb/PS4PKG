import os
import requests
import sys

def getGoogleSheet(spreadsheet_id, outDir, outFile):
  
  url = f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv'
  response = requests.get(url)
  if response.status_code == 200:
    filepath = os.path.join(outDir, outFile)
    with open(filepath, 'wb') as f:
      f.write(response.content)
      print('list downloaded to: {}'.format(filepath))    
  else:
    print(f'error downloading Google Sheet: {response.status_code}')
    sys.exit(1)


##############################################

outDir = 'bin/cache/'
os.makedirs(outDir, exist_ok = True)

getGoogleSheet('1i00BIlxnXicwuMzY3LT_Yn7Ah-DcYuHHtouyAw9bEKI', outDir, "list.csv")

dir = 'bin/cache/list.json'
if not os.path.isfile(dir):
  with open(dir, "w") as write_file:
    write_file.write("")

getGoogleSheet('14Qkz8ouWGeWHQw74S1hdOo29j9oIVCl7HgRXA8TPazo', outDir, "list_cid.csv")

sys.exit(0); ## success