# Sistema Prestamo de libros
print("*****Sistema de Prestamo de Libros*****")

DISTANCIA_PERMITIDA_KM = 3
tiene_credencial = input("¿Tienes credencial de estudiante? (si/no): ").strip().lower() == "si"

distancia_biblioteca_km = int(input("¿Cuál es la distancia a la biblioteca en kilómetros? "))

es_elegible_prestamo = (tiene_credencial or distancia_biblioteca_km <= DISTANCIA_PERMITIDA_KM)

print(f"¿Eres elegible para el préstamo de libros? {es_elegible_prestamo}")