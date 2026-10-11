# la idea es poder calcular cuanto ganado se va a tener despues de x cantidad de años

# variables de interés
meses_para_parto = 9

cantidad_inicial_vacas = int(input("Ingrese la cantidad inicial de vacas: "))
print(f"Se ha ingresado una cantidad de {cantidad_inicial_vacas} vacas iniciales")
cantidad_total_años = int(
    input("Ingrese la cantidad total de años para hacer la proyección: ")
)
print(f"Se hará la proyección para un total de {cantidad_total_años} años")
# vamos a tomar como base 9 meses como un periodo porque 9 meses dura un parto y 18 meses dura una novilla en aumentarse
# aunque podemos tomar que dura 27 meses en tener un ternero o sea 3 periodos de 9 meses

duracion_periodos = 9
total_meses = cantidad_total_años * 12
total_periodos = int(total_meses / duracion_periodos)
cantidad_terneros = 0
cantidad_novillas = 0

# lo que es mas facil lo haremos primero calcular cuantas vacas pare una sola vaca a lo largo de los años pedidos
for i in range(total_periodos):
    cantidad_terneros = cantidad_terneros + 1
print(f"Una sola vaca puede parir {cantidad_terneros}")
