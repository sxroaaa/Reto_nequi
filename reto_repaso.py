
import random
celular='3212501850'
clave= '2244'
intentos=4
saldoinicial=4500
salir=False
dinero_colchon=0
valor_donacion=0
eleccion=0

for i in range(1, 5):
    acceso1= input("ingrese su numero celular, porfavor:")
    accesoclave= input('Escribe tu clave de 4 digitos, no dudadomos que seas tu pero es mejor confirmar;):')
    intentos=intentos-1
    if celular == acceso1 and clave == accesoclave:
        while salir == False:   
            print(f"Su saldo disponible es de {saldoinicial}")
            print(" 1.Saca\n 2.Envia\n 3.Recarga\n 4.Colchon\n 5.Donaciones\n 6.Salir")
            servicio=(int(input('¡ELIGE UNO DE NUESTROS SERVICIOS:)!')))
            
            
            
            if servicio==1:
                
                print(' 1.cajero\n 2.punto fisico')
                opsacar=(int(input('Elige una opcion para sacar:')))
                
                if opsacar==1:
                    if saldoinicial<2000:
                        print('Lo sentimos, no te alcanza;(')
                    else:
                        valor_retiro=(int(input('¿cuanto desea retirar?:')))
                        saldoinicial= saldoinicial-valor_retiro
                        print(random.randint(1000, 9999))
                        print("escribe este numero en el cajero para sacar la plata:")
                        
                if opsacar==2:
                    if saldoinicial<2000:
                        print('Lo sentimos, no te alcanza')
                    else:
                        valor_retiro=(int(input('¿cuanto desea retirar?:')))
                        saldoinicial= saldoinicial-valor_retiro
                        print(random.randint(1000, 9999))
                        print("escribe este numero en el cajero para sacar la plata:")
            if servicio==2:
                print('Envia plata')
                cel=input('escriba el celular al que desea enviar el dinero:')
                valor=(int(input("¿cuanto?:")))
                
                if valor>saldoinicial:
                    print("No te alcanza")
                if valor<=saldoinicial:
                    saldoinicial=saldoinicial-valor
            if servicio==3:
                valor_recarga=(int(input("ingrese el valor a recargar:")))
                confirmacion=input("¿desea realizar la recarga?, Escriba si de lo contrario escriba no:")
                
                if confirmacion.lower()=="si" :
                    saldoinicial=saldoinicial+valor_recarga
                if confirmacion.lower()=="no" :
                    print('transaccion cancelada')
                    
            if servicio==4:
                print('Guarda tu plata debajo del colchon, para un ahorro mas seguro!:)')
                print(f"tu colchon {dinero_colchon} ")
                dinero_colchon=(int(input("¿Cuanto vas a meter?")))
                if saldoinicial<dinero_colchon:
                    print("lo sentimos, no te alcanza:(")
                else:
                    rectificar=input("¿seguro que quiere mandar este dinero al colchon?, escribe si o no:")
                    if rectificar.lower()=="si":
                        saldoinicial=saldoinicial-dinero_colchon
                    else:
                        print("cancelando proceso")
            if servicio==5:
                print("Donaciones")
                print(" 1.Antioquia presente\n 2. Fundacion ANDI\n 3.ABACO\n 4.Colombia se nota\n 5.Fundacion United Way\n 6.clinica Cardio\n 7.Aldeas Infantiles")
                eleccion=(int(input("elige el numero de la empresa a la que deseas ayudar con una donacion:)")))
                if eleccion==1 or eleccion==2 or eleccion==3 or eleccion==4 or eleccion==5 or eleccion==6 or eleccion==7:
                    valor_donacion=(int(input("¿Cuanto quieres donar?")))
                    pregunta=input("escriba 'Si' para continuar con el proceso de lo contrario escriba 'no':")
                    if pregunta.lower()=="si":
                        saldoinicial=saldoinicial-valor_donacion
                    else:
                        print("cancelando proceso")
                    
            if servicio == 6:
                print("Saliendo...")
                salir=True
                
        
    if  celular != acceso1 and clave != accesoclave:       
            print(f"¡Upps! Parece que tus datos de acceso no son correctos, Tienes {intentos} intentos más")
            
                
            if intentos==0:
                print("lo lamento, ha agotado todos sus intentos;(")
                   
                
  