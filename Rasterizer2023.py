from gl import Renderer
import shaders

# El tama�o del FrameBuffer
width = 1024    
height = 683

# Se crea el renderizador
rend = Renderer(width, height)
# rend.glClearColor(0.5,0.5,0.5)
# rend.glClear()
rend.glBackgroundTexture("textures/lakedesert.bmp")
rend.glClearBackground()


# Le damos los shaders que se utilizar�s
#gourad, contour, outline, fadeshader, grayshader, snakeShader

# ------------------------ casa ---------------------------
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.toonShader 
rend.glLoadModel(filename = "models/OldHouse.obj",
                 textureName = "textures/Housebody.bmp",
                 translate = (8.5, 1,15),
                 rotate = (180, 90, 0),
                 scale = (1.3,1.3,1.3)) 
rend.glRender()
#------------------------ bote ---------------------------
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.gouradShader 
rend.glLoadModel(filename = "models/Boat.obj",
                 textureName = "textures/boat.bmp",
                 translate = (-5, 2,10),
                 rotate = (150, -120, 5),
                 scale = (0.7,0.7,0.7)) 
rend.glRender() 

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.OutlineShader 
rend.glLoadModel(filename = "models/Boat.obj",
                 textureName = "textures/boat.bmp",
                 translate = (-1.6, 3.4,10),
                 rotate = (150, -120, 5),
                 scale = (1,1,1)) 
rend.glRender() 

# ------------------------ torre ---------------------------
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.TextureFadeShader 
rend.glLoadModel(filename = "models/tower.obj",
                 textureName = "textures/tower.bmp",
                 translate = (-13, 1,28),
                 rotate = (180, 180, 0),
                 scale = (0.6,0.6,0.6)) 
rend.glRender() 

# ------------------------ árbol 1 ---------------------------
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.gouradShader 
rend.glLoadModel(filename = "models/DeadTree1.obj",
                 textureName = "textures/arbol-oscuro.bmp",
                 translate = (-26, 21,36),
                 rotate = (170, 180, 0),
                 scale = (3.5,3.5,3.5)) 
rend.glRender() 

# ------------------------ árbol 2 ---------------------------
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.grayShader 
rend.glLoadModel(filename = "models/DeadTree2.obj",
                 textureName = "textures/arbol-medio.bmp",
                 translate = (15, 2.8, 20),
                 rotate = (180, 180, 0),
                 scale = (0.5,0.5,0.5)) 
rend.glRender()



# ------------------------ árbol 3 ---------------------------
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.contourShader 
rend.glLoadModel(filename = "models/DeadTree3.obj",
                 textureName = "textures/arbol-gris.bmp",
                 translate = (-4, 0.6,30),
                 rotate = (180, 180, 0),
                 scale = (0.3,0.3,0.3)) 
rend.glRender()

# ------------------------ árbol 4 ---------------------------
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.contourShader 
rend.glLoadModel(filename = "models/DeadTree4.obj",
                 textureName = "textures/arbol-gris.bmp",
                 translate = (4, 0.8,30),
                 rotate = (180, 180, 0),
                 scale = (0.3,0.3,0.3)) 
rend.glRender()

rend.glFinish("photoshoot/pruebas.bmp")