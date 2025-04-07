import random

respuestas = [
    "¡Sí, definitivamente!",
    "No cuentes con ello.",
    "Pregunta de nuevo más tarde.",
    "Sin duda.",
    "Mi respuesta es no.",
    "Parece probable.",
    "No puedo decirlo ahora.",
    "¡Claro que sí!"
]

print("Bienvenido a la Bola Mágica 🎱")
input("Hazme una pregunta: ")
print("Pensando..")
print("Respuesta:", random.choice(respuestas))