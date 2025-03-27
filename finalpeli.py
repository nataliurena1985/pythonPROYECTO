class Video:
    def __init__(self, nombre, visualizaciones, actores):
        self.nombre = nombre
        self.visualizaciones = visualizaciones
        self.actores = actores

class Serie(Video):
    def __init__(self, nombre, visualizaciones, actores, temporadas):
        super().__init__(nombre, visualizaciones, actores)
        self.temporadas = temporadas

class Pelicula(Video):
    def __init__(self, nombre, visualizaciones, actores, duracion):
        super().__init__(nombre, visualizaciones, actores)
        self.duracion = duracion

# Instanciar las listas
series = [
    Serie("Peaky Blinders", 1234567, ["Cillian Murphy", "Paul Anderson", "Helen McCrory"], 5),
    Serie("The Umbrella Academy", 2434908, ["Tom Hopper", "Emmy Raver-Lampman", "Ellen Page", "David Castañeda"], 2)
]

peliculas = [
    Pelicula("Inception", 4760183, ["Leonardo DiCaprio", "Ellen Page", "Joseph Gordon-Levitt"], 148),
    Pelicula("Batman Begins", 17319533, ["Christian Bale", "Cillian Murphy", "Michael Caine"], 140),
    Pelicula("Inmortales", 35, ["Mirtha Legrand", "Leonardo DiCaprio", "Elizabeth Segunda"], 30)
]



# Funciones
def video_con_mayor_visualizaciones(videos):
    mayor = videos[0]  # primer video es el de mayor visualización
    for video in videos:  # Recorre todos los videos, incluye el primero
        if video.visualizaciones > mayor.visualizaciones:
            mayor = video
    return mayor.nombre

def promedio_de_duracion_peliculas(peliculas):
    
    duracion_total = 0
    
    # Recorre la lista de películas y suma la duración de cada una
    for pelicula in peliculas:
        duracion_total += pelicula.duracion
    
    # Calcula el promedio dividiendo la duración total entre la cantidad de películas
    cantidad_peliculas = len(peliculas)
    promedio_duracion = duracion_total / cantidad_peliculas
    
    return promedio_duracion

def actores_de_series_y_peliculas(series, peliculas):
    # Crear listas vacías para almacenar los actores
    actores_en_series = []
    actores_en_peliculas = []
    
    # Recorre las series y agrega los actores a la lista de actores de series
    for serie in series:
        for actor in serie.actores:
            if actor not in actores_en_series:  # Evitar duplicados
                actores_en_series.append(actor)
    
    # Recorre las películas y agregamos los actores a la lista de actores de películas
    for pelicula in peliculas:
        for actor in pelicula.actores:
            if actor not in actores_en_peliculas:  # Evitar duplicados
                actores_en_peliculas.append(actor)
    
    # Encontrar los actores que están en ambas listas
    actores_comunes = []
    for actor in actores_en_series:
        if actor in actores_en_peliculas:
            actores_comunes.append(actor)
    
    # Devolver los de actores comunes
    act_comu=', '.join(actores_comunes) 
    return act_comu

def series_de_mas_de_tres_temporadas(series):
    # Inicializa una lista para almacenar los nombres de las series 
    series_con_mas_de_tres_temporadas = []
    
    # Recorremos cada serie en la lista de series 
    for serie in series:
        # Verificamos si la serie tiene más de tres temporadas
        if serie.temporadas > 3:
            # Si cumple agregamos el nombre de la serie a la lista
            series_con_mas_de_tres_temporadas.append(serie.nombre)
    
    # Devolvemos la lista de nombres de series que tienen más de tres temporadas

    series_con_mas_de_tres_tem=', '.join(series_con_mas_de_tres_temporadas)
    return series_con_mas_de_tres_tem

def mostrar_menu():
    while True:
        print("\nMenú:\n 1. Video con mayor visualización \n 2. Promedio de duración de películas \n 3. Actores que trabajan en series y películas \n 4. Series con más de 3 temporadas \n 5. Salir \n")
        
        opcion = input("Elija una opción: ")
        
        if opcion == '1':
            print("El video con mayor visualización es:", video_con_mayor_visualizaciones(series + peliculas))
        elif opcion == '2':
            print("El promedio de duración de las películas es:", promedio_de_duracion_peliculas(peliculas), "minutos")
        elif opcion == '3':
            print("Actores que trabajan en series y películas:", actores_de_series_y_peliculas(series, peliculas))
        elif opcion == '4':
            print("Series con más de 3 temporadas:", series_de_mas_de_tres_temporadas(series))
        elif opcion == '5':
            break
        else:
            print("Opción inválida, intente de nuevo!!")

# Ejecutar menú
mostrar_menu()