import os
import shutil

src_dir = "/home/yvnsu/Imágenes/Capturas de pantalla/"
dst_dir = "/home/yvnsu/gabo/imgs/"

files_to_copy = [
    "Captura desde 2026-05-07 01-20-36.png",
    "Captura desde 2026-05-07 01-18-34.png",
    "Captura desde 2026-05-07 01-18-07.png",
    "Captura desde 2026-05-07 01-15-35.png",
    "Captura desde 2026-05-07 01-14-54.png",
    "Captura desde 2026-05-07 01-14-34.png",
    "Captura desde 2026-05-07 01-14-14.png",
    "Captura desde 2026-05-07 01-01-48.png",
    "Captura desde 2026-05-07 01-01-28.png"
]

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

for i, filename in enumerate(files_to_copy, 1):
    src_path = os.path.join(src_dir, filename)
    # let's keep original names or use simple ones, let's copy to both to be safe
    dst_name_simple = f"win7_{i:02d}.png"
    dst_path_simple = os.path.join(dst_dir, dst_name_simple)
    dst_path_orig = os.path.join(dst_dir, filename)
    
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path_simple)
        shutil.copy2(src_path, dst_path_orig)
        print(f"Copied {filename} -> {dst_name_simple} and original name.")
    else:
        print(f"Source file not found: {src_path}")
