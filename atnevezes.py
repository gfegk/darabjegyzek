import os

# Az aktuális könyvtár elérése
current_dir = os.getcwd()

# Végigmegy az aktuális könyvtárban található almappákon
for folder_name in os.listdir(current_dir):
    folder_path = os.path.join(current_dir, folder_name)
    
    # Csak könyvtárakat vizsgálunk
    if os.path.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".html"):
                old_path = os.path.join(folder_path, file_name)
                new_file_name = folder_name + ".html"
                new_path = os.path.join(folder_path, new_file_name)
                
                # Ha már létezik ilyen nevű fájl, ne írjuk felül
                if not os.path.exists(new_path):
                    os.rename(old_path, new_path)
                    print(f"{old_path} → {new_path}")
                else:
                    print(f"Figyelem: {new_path} már létezik, nem történt átnevezés.")
