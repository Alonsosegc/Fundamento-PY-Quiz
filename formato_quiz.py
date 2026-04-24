
#Quizz

quiz = {
"1) ¿Cuál es la capital de Chile?" : "Santiago",
"2) ¿Cuál es la capital de Colombia?" : "Bogota",
"3) ¿Cuál es la capital de Argentina?" : "Buenos aires"
}
contador_correctas = 0
estudiante = input("Ingrese su nombre: ")

for pregunta in quiz:
    print(pregunta)
    respuestas = input("Ingrese su respuesta: ").strip().capitalize()
    if respuestas == quiz[pregunta]:
        contador_correctas = contador_correctas + 1

if contador_correctas == 3:
    rendimiento = "Excelente"
elif contador_correctas == 2:
    rendimiento = "Óptimo"
else:
    rendimiento = "Insuficiente"

print(estudiante+ " obtuvo: "+ str(contador_correctas)+" respuesta/s correcta/s.")
print("Su rendimiento fue: "+ rendimiento)


