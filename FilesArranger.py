import os

# Default folder
file_path = '/home/meri/Downloads'


def folder_creator(folder, file_extensions_list, extensions_):
    """
     This function creates a file based on if a type of file is present in the folder.
    :param folder: The name of the folder to be created
    :param file_extensions_list: A list of the various file extensions present in the folder
    :param extensions_: The file extension
    :return:
    """
    if type(extensions_) == list:
        check_ = any([file in file_extensions_list for file in extensions_])
    else:
        check_ = extensions_ in file_extensions_list

    # Checking if the folder exists and the file type is present
    if os.path.exists(file_path+'/'+folder) is False and check_:
        # Creating the folder
        os.mkdir(file_path+'/'+folder)


# All file extensions
file_extensions_dict = {
    'photos': ['png', 'jpg', 'jpeg'],
    'docs': ['docx', 'doc', 'txt'],
    'pdf_documents': 'pdf',
    'archive': ['tar', 'zip'],
    'videos': ['3gp', 'mp4', 'mpeg'],
    'sheets': ['xlsx', 'csv', 'xls'],
    'jupyter_files': 'ipynb',
    'scripts': ['py', 'sh'],
    'music': 'mp3'
}

# Check if the path exists
if os.path.exists(file_path) is True:
    files = os.listdir(file_path)

    # Getting the various file extensions within the folder
    extension_list = set([file.split('.')[-1] for file in files if os.path.isfile(file_path + r'/' + file) is True])

    # Creating the folders specified in the file_extensions dictionary
    for folder_name, file_type in file_extensions_dict.items():
        folder_creator(folder_name, extension_list, file_type)

    # Creating the other files folder
    if os.path.exists(file_path+'/other_files') is False:
        # Creating the folder
        os.mkdir(file_path+'/other_files')

    # Checking all the file_extension_list
    for file in files:
        if os.path.isfile(file_path + r'/' + file) is True:
            ext = file.split('.')[-1].lower()  # Extracting the file extension

            # Moving the file
            for _folder, _files in file_extensions_dict.items():
                if ext in _files:
                    new_path = file_path + '/' + _folder + '/' + file
                    os.rename(file_path+'/'+file, new_path)
                    break
            else:
                # Moving the files into other files folder if
                new_path = file_path + '/other_files/' + file
                os.rename(file_path+'/'+file, new_path)

else:
    "Path does not exist"
