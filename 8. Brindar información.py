""" Programa que brinda información de artes
Autor: Estefani Ortega
Fecha: 24 octubre 2026
Descripción: Escribe un programa que permite al usuario ingresar el nombre 
de un artista, película, serie u otro tema de 
y muestra información relacionada."""

arte= int(input("Ingresa el número del tema que quieras conocer: 1. Titanic, 2. Shakira, 3.Incepction, 4. Dr. House, 5. Gotham: "))

match arte:
        case 1:
            print("Titanic es una película protagonizada por Leonardo Di Caprio y Kate Winslet, dirigida por James Cameron, relata la historia de amor entre dos personajes dentro de la tragedia del hundimiento del Titanic. Se estrenó en 1997 y es una de las películas más taquilleras y ganadoras del Oscar") 
        case 2:
            print("Shakira es una artista colombiana mundialmente reconocida, tiene 12 discos, de origen libanés ha construido su carrera con base en la cultura pop, pero también ha participado en las copas mundiales de futbol soccer. Es la máxima representante de la música latina.")
        case 3:
            print("Inception es una película dirigida por Christopher Nolan, que relata la historia de un ladrón que roba secretos corporativos a través de la tecnología de entrar en el subconsciente. Se estrenó en 2010 y ganó 4 Oscares")
        case 4:
            print("Dr. House es una serie estadounidense que relata la vida de un médico que, junto con su equipo de trabajo, diagnostican enfermedades que nadie más puede solucionar. Interpretado por Hugh Laurie se estrenó en 2004 y finalizó en 2012.")
        case 5:
            print("Gotham es una serie estadounidense creada por Bruno Heller y basada en los primeros pasos de varios personajes de las publicaciones DC Comics, especialmente James Gordon y Bruce Wayne, creados por Bob Kane y Bill Finger e interpretados por Ben McKenzie y David Mazouz, estrenada en 2014 finalizó transmisiones en 2019")
        case _:
            print("Opción no es válida.")


