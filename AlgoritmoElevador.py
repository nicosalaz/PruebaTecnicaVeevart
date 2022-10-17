import time

piso_inicial = 4 #piso en el que inicia
recorrido = [5,29,13,10] # los pisos iniciales digitados
pisos_ingresados = {5:2,29:10,13:1,10:1} # pisos donde subio y el piso que selecciono
sentido = "Subiendo" #sentido en el que se desplaza el asensor

#funcion que valida si el piso es permitido y diferente al piso en el que se encuentra
def seleccionarPiso(piso,parada):
	min = 1 # piso minimo
	maximo = 29 # maximo
	if isinstance(piso,int) and piso!= parada: # validacion si es entero y diferente al actual
		if min <= piso <= maximo:#validacion del rango del numero
			return True
	#mensaje de error
	print("Recuerde que el piso debe estar en el rango de 0 a 29 y diferente al actual")
	#retorno falso
	return False

def validar_seleccion():# determinar si el usuario quiere o no elegir o otro piso
	estado = False #estado para control de iteraciones
	opcion = 0 #variable que almacena la respuesta
	while not estado:#Ciclo para preguntar hasta que el usuario ingrese una opcion valida
		opcion = input("Desea elegir un nuevo piso [s/n]:",)#input
		#validación para determinar si digito correctamente
		if opcion.strip().lower() == "s" or opcion.strip().lower() == "n":
			estado = True
		else:
			#mensaje de error
			print("Recuerde que solo se acepta s para 'Sí' y n para 'No'")
	#validacion que determina que si elegirá un piso
	if opcion.strip().lower() == "s":
		return True
	# validacion que determina que no elegirá un piso
	elif opcion.strip().lower() == "n":
		return False

#funcion principal donde esta toda la logica
def principal(piso_inicial,recorrido,pisos_ingresados,sentido):
	#print("Elevador en piso ",piso_inicial)# imprime el inicio
	contador = piso_inicial #variable que me controlara el recorrido del elevador
	parada = 0#variable que me indicara el piso actual del elevador
	estado = False#esatdo que me controla si el elevador para o no
	estado_final = True#estado que me controla toda la iteracion
	estado_validacion = False#estado que me valida si el nuevo piso es valido
	nuevo_piso = 0#variable que almacena el nuevo piso que va digitando el usuario
	#flujo principal
	while estado_final:
		#flujo de recorrido hasta el siguiente piso de array
		while estado == False:
			print("Elevador en piso ",contador)# piso por el que pasa el elevador
			if contador in recorrido: #validación para saber si el elevador debe parar
				print("Elevador se detuvo")
				eleccion = validar_seleccion()#variable que me valida si va a seleccionar un nuevo piso
				if eleccion: #control del nuevo piso
					while not estado_validacion: #ciclo hasta que reciba un piso valido
						try:
							nuevo_piso = int(input("Digite el piso al que se dirige:",))#input del piso
							estado_validacion = seleccionarPiso(nuevo_piso,contador)#validacion del piso ingresado
						except Exception as e:
							estado_validacion = False
							print("Recuerde que el piso debe estar en el rango de 0 a 29 y diferente al actual")
							print(e.args)
				else:
					nuevo_piso = 0 #valor de 0 en caso de no quere seleccionar un nuevo piso
				parada = contador
				estado = True #se detiene el ciclo de recorrido
			else:#en caso de que no se deba parar en el piso actual
				if sentido == "Subiendo":#validación de si el elevador va de subida
					contador+=1 #se suma un piso
				elif sentido == "Bajando":#validación de si el elevador va de bajada
					contador -= 1 #se resta un piso
		maximo = max(recorrido)#se encuentra piso maximo del array
		minimo = min(recorrido)# se encuentra el piso minimo del array
		if parada in recorrido: # validar si la parada esta dentro del array de recorrido
			recorrido.remove(parada)# se elimina ese piso
			if nuevo_piso not in recorrido and nuevo_piso != 0: #si hay un nuevo piso valido selecionado
				recorrido.append(int(nuevo_piso))#se agrega al recorrido
			estado_validacion = False #se actualiza la opcion para seleccionar un piso
			contador = parada # se actualiza el piso en el que se inicia el siguiente recorrido
		if len(recorrido) > 0: #se valida si aun hay pisos por recorrer
			if sentido == "Subiendo": # si va subiendo
				if parada == maximo: # se encuentra con el piso más alto del recorrido actual
					sentido = "Bajando" # comienza su decenso
			elif sentido == "Bajando":# si el elvador esta bajando
				if parada == minimo: # se encuentra en el piso minimo del recorrido actual
					sentido = "Subiendo" # comienza su ascenso
			estado = False # se actualiza la variable para un nuevo recorrido
			print("Elevador",sentido) # se muestra el sentido en el que va el elevador
		else:#en caso de que no hayan mas pisos por recorrer
			print("Hasta pronto")
			estado_final = False # se finaliza el programa
		
	
principal(piso_inicial,recorrido,pisos_ingresados,sentido)#llamado a la función principal
	
