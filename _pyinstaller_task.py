import os
import subprocess
import shutil
import zipfile

str_project_name = 'main'

def bundle_project(str_project_name):

    str_parent_path = os.path.dirname(os.path.abspath(__file__))
    str_pyinstaller_path = os.path.join(str_parent_path,'_venv','Scripts', 'pyinstaller.exe')
    str_bundle_path =  os.path.join(str_parent_path, 'bundle')
    str_dist_path = os.path.join(str_bundle_path,'dist')
    str_build_path = os.path.join(str_bundle_path,'build')
    str_data_path = os.path.join(str_parent_path, 'tools') + ';tools'
    str_script_path = os.path.join(str_parent_path, str_project_name + '.py')

    # pyinstaller command as array
    pyinstaller_cmd = [
        f'{str_pyinstaller_path}',
        '--onedir',
        #'--noconsole',
        f'--distpath={str_dist_path}',
        f'--workpath={str_build_path}',
        f'--specpath={str_bundle_path}',
        f'--add-data={str_data_path}'
    ]

    pyinstaller_cmd.append(str_script_path)

    if(os.path.exists(str_bundle_path)):
        shutil.rmtree(str_bundle_path) # remove old bundle
    
    subprocess.run(pyinstaller_cmd, check=True)

    print(f'{str_project_name} was bundled successfully at {str_bundle_path}')

    str_dist_project_path = os.path.join(str_dist_path,str_project_name)
    str_dist_output_zip = os.path.join(str_dist_path,str_project_name+'.zip')
    compress(str_dist_project_path, str_dist_output_zip)


def compress(source_folder, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_folder):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), source_folder))
    print(f"Folder '{source_folder}' has been compressed to '{output_zip}'.")

if __name__ == "__main__":
    bundle_project(str_project_name)
