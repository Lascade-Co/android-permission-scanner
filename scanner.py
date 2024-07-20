import os
import xml.etree.ElementTree as ET

def scan_permissions(project_dir):
    """Scan all XML files for permissions in the Android project."""
    namespace = '{http://schemas.android.com/apk/res/android}'
    permissions = set()
    
    for subdir, dirs, files in os.walk(project_dir):
        for file in files:
            if file.endswith('.xml'):
                file_path = os.path.join(subdir, file)
                try:
                    tree = ET.parse(file_path)
                    root = tree.getroot()
                    for elem in root.iter():
                        if 'permission' in elem.tag or elem.get(f'{namespace}permission'):
                            permissions.add(elem.get(f'{namespace}name'))
                except ET.ParseError:
                    continue  # Skip files that are not proper XML (e.g., binary XML files)

    return permissions

def main():
    project_directory = os.path.dirname(os.path.realpath(__file__))  # Automatically set to script location
    permissions = scan_permissions(project_directory)
    if permissions:
        print("Permissions found in the project:")
        for perm in permissions:
            print(perm)
    else:
        print("No permissions found in the project.")

if __name__ == '__main__':
    main()