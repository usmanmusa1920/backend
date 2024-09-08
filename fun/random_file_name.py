import os
import secrets


def pic_or_doc_name(file_name):
    """Random file name generator"""
    
	# split file name & it extension in form of tuple ('index', '.py')
    _, _ext = os.path.splitext(file_name)
    
	# random hexa-decimal value of 16 characters long
    random_hex = secrets.token_hex(8)
    
	# append random name to the file
    _fn_ = random_hex + _ext
    
    new_name = _ + "_" + _fn_
    return new_name

file_name_1 = pic_or_doc_name("my_python_file.py")
file_name_2 = pic_or_doc_name("my_ipynb_file.py")
file_name_3 = pic_or_doc_name("my_shell_file.py")

print("\t", ">>> ", file_name_1, "\n")
print("\t", ">>> ", file_name_2, "\n")
print("\t", ">>> ", file_name_3, "\n")
