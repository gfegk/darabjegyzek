import os
import shutil

# A főkönyvtár, ahol az almappák vannak
base_dir = os.getcwd()  # vagy írd be: pl. "C:/projektek/weboldalak"

# A célkönyvtár, ahová a .html fájlok kerülnek
target_dir = os.path.join(base_dir, "osszes_html")
os.makedirs(target_dir, exist_ok=True)

# Bejárja az almappákat
for folder_name in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder_name)
    
    if os.path.isdir(folder_path) and folder_path != target_dir:
        for file_name in os.listdir(folder_path):
            if file_name.lower().endswith(".html"):
                source_path = os.path.join(folder_path, file_name)
                base_name = os.path.splitext(file_name)[0]
                extension = os.path.splitext(file_name)[1]

                # Eredeti fájl másolása
                target_path = os.path.join(target_dir, file_name)
                if not os.path.exists(target_path):
                    shutil.copy2(source_path, target_path)
                    print(f"Másolva: {file_name}")

                # Kisbetűs nevű másolat készítése
                lower_file_name = base_name.lower() + extension
                lower_target_path = os.path.join(target_dir, lower_file_name)
                if not os.path.exists(lower_target_path):
                    shutil.copy2(source_path, lower_target_path)
                    print(f"Kisbetűs másolat: {lower_file_name}")
