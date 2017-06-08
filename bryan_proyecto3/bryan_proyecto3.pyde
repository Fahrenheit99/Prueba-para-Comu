#saludos a la Clase
import json

m = []
lado = 9
pausa = False
guardar = False
cargar = False

def setup():
    global m, lado
    fullScreen()
    background(0)#______________________Color de fondo
    m = generarm(height/lado, width/lado)
    dibujarm(m)
        
        
def draw():
    global m, pausa, lado, cargar, guardar
    #fill(0,0,0,100)
    #rect(0,0, width, height)
    #noFill()
    background(0)
    dibujarm(m)
    #m = siguientem(m)
    if not pausa:
        m = siguientem(m)
    if guardar:
        archivo = open("guardar.txt", "w")
        json.dump(m, archivo)
        archivo.close()
        guardar = False
    if cargar:
        archivo = open("guardar.txt", "r")
        m = json.load(archivo)
        archivo.close()
        dibujarm(m)
        cargar = False
    if mousePressed:
        f = mouseY/lado
        c = mouseX/lado
        if f >= len(m):
            f %= len(m)
        if c >= len(m[0]):
            c %= len(m[0]) 
        m[f][c] = 1
    

    
    
def generarm(fil, col):
    return [[int(random(3)) for _ in range(col)] for _ in range(fil)]


def dibujarm(m):
    global lado
    for fil in range(len(m)):
        for col in range(len(m[0])):
            if m[fil][col] == 1:
                fill(0,40 , 255)
                rect(col * lado, fil * lado, lado, lado)
                #ellipse(col*lado, fil*lado, lado, lado)
                noFill()
            elif m[fil][col] == 2:
                fill(152,159, 193)
                rect(col * lado, fil * lado, lado, lado)
                #ellipse(col*lado, fil*lado, lado, lado)
                noFill()
        

def vecinosv(m, fil, col):
    total = 0
    topefil = len(m)
    topecol = len(m[0])
    for _ in range(fil-1, fil+2):
        for j in range(col-1, col+2):
            if _ >= topefil:
                _ %= topefil
            if j >= topecol:
                j %= topecol                     
            if _ != fil or j != col:
                if m[_][j] == 1:
                    total += m[_][j]
                    #print(_, j)
                    #total += m[_ % len(m)][j% len(m[0])]
                else:
                    pass
            else:
                pass
    #print(total)
    return total
                        
                    
def siguientem(m):
    nueva = [[0 for _ in range(len(m[0]))] for _ in range(len(m))]
    for fil in range(len(m)):
        for col in range(len(m[0])):
            v = vecinosv(m, fil, col)
            if m[fil][col] == 0 and v == 2:
                nueva[fil][col] = 1
            elif m[fil][col] == 1:
                nueva[fil][col] = 2
            elif m[fil][col] == 2:
                nueva[fil][col] = 0
    return nueva
            
                
    
def keyPressed():
    global pausa, guardar, cargar
    if key == " ":
        pausa = not pausa
    if key == "g" or key == "G":
        guardar = True
    if key == "c" or key == "C":
        cargar = True
        
    
    
    
    
    
    
    
    
    
    
    
    
                
                
    
