# Practica de la sesion 14

def name_change(current_name, modified_name):

    myFile = open('./PythonG2/scripts/yair_pkg/student_names.txt','r+')
    type(myFile)
    myFile_list = myFile.readlines()
    myFile.seek(0)
    mySearch = current_name + "\n"
    mySearch_index = myFile_list.index(mySearch)
    mySearch_index
    myFile_list[mySearch_index] = modified_name + "\n"
    myFile.writelines(myFile_list)
    myFile.close()


name_change("Vic","Vic ha sido modificado por Victor")


