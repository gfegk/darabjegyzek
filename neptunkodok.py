neptun_kodok=[
'PWEUDK',
'DFD5MP',
'GZN62D',
'M9OAUR',
'AX6WI4',
'DZY2PB',
'O2NPYS',
'N7X6K0',
'HDUC79',
'VGNO39',
'CVDALP',
'PAMXRB',
'IJCJQG',
'SGXJUH',
'D4VDCM',
'SQRNLK',
'MZGFIY',
'MQ1MF0',
'YQN6FK',
'HGWXYW',
'U3BHVM',
'JH7PER',
'CRLVC9',
'EJ1MA8',
'HPWWCY',
'NUHBUU',
'UCDL53',
'GULI9Z',
'Q4W14G',
'H1KU7O',
'IEV77G',
'B1IDKL'
]

import os

# Az aktuális mappa elérési útvonala
current_directory = os.getcwd()

for neptun_kod in neptun_kodok:
    new_folder_path = os.path.join(current_directory, neptun_kod)

    # Mappa létrehozása
    if not os.path.exists(new_folder_path):
        os.mkdir(new_folder_path)
        print(f"Mappa '{neptun_kod}' létrehozva!")
    else:
        print(f"A mappa '{neptun_kod}' már létezik.")
