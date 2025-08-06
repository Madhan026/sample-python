import os
import shutil

# Define the directory to organize
source_folder = "I:\old back i\PDF" 

# Define file type categories
file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css', '.java'],
    'Others': []  # For uncategorized files
}

# Create a reverse lookup for extensions
extension_map = {}
for category, extensions in file_categories.items():
    for ext in extensions:
        extension_map[ext.lower()] = category

# Organize files
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    
    if os.path.isfile(file_path):
        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        category = extension_map.get(ext, 'Others')
        
        target_folder = os.path.join(source_folder, category)
        os.makedirs(target_folder, exist_ok=True)  # Create if not exists
        
        target_path = os.path.join(target_folder, filename)
        shutil.move(file_path, target_path)
        print(f"Moved: {filename} ➝ {category}/")

print("\n✅ File organization complete!")
