def modificar_archivo(alumno_original, nuevo_alumno):
    f = open("data/alumnos.txt", "r")
    # print(f.read())
    # f.seek(0)
    # print(f.read())
    # print(f.read())
    # f.seek(0)
    lista_alumnos = f.readlines()
    f.close()
    f = open("data/alumnos.txt", "w")
    lista_alumnos
    # [alumno if not alumno_original in alumno else nuevo_alumno for alumno in lista_alumnos]
    lista_alumnos = [alumno if not alumno_original in alumno else alumno.replace(alumno_original, nuevo_alumno) for alumno in lista_alumnos]
    f.seek(0)
    f.writelines(lista_alumnos)
    f.close()

alumno_original = "Osmar"
nuevo_alumno = "Carlos"
modificar_archivo(alumno_original,nuevo_alumno )

f = open("data/alumnos.txt", "r+")
texto = f.read()
texto = texto.replace(alumno_original, nuevo_alumno)
f.seek(0)
f.write(texto)
f.close()