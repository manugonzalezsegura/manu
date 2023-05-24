import random


lista=["1","2","3","4","5","6","7"]

lazar=["grifindor","hufelpuff","sliceryn","ravenclaw"]
while True:
    sliceryn=0 
    hafelpuff=0
    grifindor=0
    ravenclaw=0
    azar=0
    print("bienvenido al sombrero seleccionador de howarts")

    while True:
        
        print("cual es tu animal favorito?")
        print("1.serpiente")
        print("2.tejon")
        print("3.leon")
        print("4.aguila")  
        print("5.ninguno")            
            
        opc=str(input("ingrese su opcion "))
        if opc in lista:
            
            while True:
                
                if opc=="1":
                    sliceryn +=1
                    break
                elif opc =="2":
                    hafelpuff +=1
                    break
                elif opc =="3":
                    grifindor
                    break   
                elif opc=="4":
                    ravenclaw +=1
                    break
                elif opc=="5":
                    azar+=1
                    break
                else:
                    print("opcion invalida")  
                          
                    
            while True:
                print("con cual de estas cualidades te sientes mas identificado")
                print("1.astucia")
                print("2.perseverancia")
                print("3.valentia")
                print("4.sabiduria")  
                print("5.ninguno")            
                opc=str(input("ingrese su opcion "))
                if opc=="1":
                    sliceryn +=1
                    break
                elif opc =="2":
                    hafelpuff +=1
                    break
                elif opc =="3":
                    grifindor
                    break   
                elif opc=="4":
                    ravenclaw +=1
                    break
                elif opc=="5":
                    azar+=1
                    break
                else:
                    print("opcion invalida")
            while True:
                print("elige una de estas destrezas")
                print("1.rapidez")
                print("2.inteligencia")
                print("3.valentia")
                print("4.sabiduria")  
                print("5.ninguno")            
                opc=str(input("ingrese su opcion "))
                if opc=="1":
                    sliceryn +=1
                    break
                elif opc =="2":
                    hafelpuff +=1
                    break
                elif opc =="3":
                    grifindor
                    break   
                elif opc=="4":
                    ravenclaw +=1
                    break
                elif opc=="5":
                    azar+=1
                    break
                else:
                    print("opcion invalida")
                            
            while True:
                print("cual seria tu asignatura favorita")
                print("1.artes oscuras")
                print("2.pociones")
                print("3.vuelo")
                print("4.animales miticos")  
                print("5.ninguno")            
                opc=str(input("ingrese su opcion "))
                if opc=="1":
                    sliceryn +=1
                    break
                elif opc =="2":
                    hafelpuff +=1
                    break
                elif opc =="3":
                    grifindor
                    break   
                elif opc=="4":
                    ravenclaw +=1
                    break
                elif opc=="5":
                    azar+=1
                    break
                else:
                    print("opcion invalida")     
        
        if sliceryn > hafelpuff and sliceryn> grifindor and sliceryn> ravenclaw  and sliceryn > azar:
            print("tu escuela es slicerin") 
            break             
        elif hafelpuff> sliceryn and hafelpuff> grifindor and hafelpuff> ravenclaw  and hafelpuff > azar: 
            print("hafelpuff")
            break             
        elif grifindor> hafelpuff and grifindor> sliceryn and grifindor> ravenclaw  and grifindor > azar:
            print("grifindor")  
            break
        elif azar > sliceryn and azar>hafelpuff and azar>ravenclaw and azar > grifindor :
            print(random.choice(lazar))
            break
            


