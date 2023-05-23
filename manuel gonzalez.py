"""1. Cotización:
o Debe ofrecer los tratamientos disponibles.
o Debe calcular el total de la cotización, además debe consultar si tiene descuento y aplicarlo si corresponde.
o Desplegar el total de la cotización e indicar el valor de las cuotas mensuales
2. Renunciar:
o Debe permitir eliminar la cotización echa anteriormente, volver al menú y permitir realizar una nueva cotización.
3. Salir del programa sin considerar la cotización que se pueda haber ingresado."""

mi_lista=["a","b","c","d,","e","1","2","3","4","5"]
precio=0
menos=["a","b","c","e"]
while True:
    
    
    
    print("a.para cotizar")
    print("b.salir")
    
    cotiza=str(input("ingrese su opcion para cotizar")).lower()
    
    if cotiza in mi_lista:
        
        while True:    
            if cotiza=="a":
                print("1.Carillas Porcelana $250.000")    
                print("2. Implantes Dentales  $475.000")
                print("3.Ortodoncia Brackets$800.000")
                print("4.borrar cotizacion")
                print("5.salir")
                opc=str(input("ingrese su opcion"))
                
                
                if opc in mi_lista:
                    
                    
                    
                    if opc=="1":
                                        
                        precio+=250000
                    elif opc=="2":
                        precio+=475000

                    elif opc=="":
                                precio+=800000 
                    elif opc=="4":
                                #borra cotizacion 
                                precio=0
                                
                    elif  opc=="5":
                                print("a.Trabajador Auxiliar 15% descuento")
                                print("b.Trabajador Administrativo 10% descuento")
                                print("c.Trabajador Docente 5% descuento" )
                                print("d..salir")
                                menos=str(input("ingrese opcion")).lower()
                                if menos in mi_lista:
                                    if menos=="a":
                                        descuento=precio*0.15
                                        total=precio-descuento
                                                
                                    elif menos=="b":
                                        descuento=precio*0.10
                                        total=precio-descuento
                                        break
                                            
                                            
                                    elif descuento=="c":
                                        descuento=precio*0.05
                                        total=precio-descuento
                                            
                                            
                                            
                                    elif opc=="d":
                                                
                                        cuota=total/12
                                        print(f"su cuota mensual es de {cuota}")
                                        print(f"{total}")
                                        print(f"{descuento}")
            elif cotiza=="b":
                        print(" hasta pronto")
                        break 

            else:
                print("opcion invalida solo a o b")              