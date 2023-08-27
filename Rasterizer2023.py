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

# rend.fragmentShader = shaders.contourShader 
# rend.fragmentShader = shaders.OutlineShader
# rend.fragmentShader = shaders.DiagonalLinesShader

# ------------------------ casa ---------------------------
# rend.vertexShader = shaders.vertexShader
# rend.fragmentShader = shaders.gouradShader 
# rend.glLoadModel(filename = "models/OldHouse.obj",
#                  textureName = "textures/Housebody.bmp",
#                  translate = (8.5, 1,15),
#                  rotate = (180, 90, 0),
#                  scale = (1,1,1)) 
# rend.glRender()

# ------------------------ bote ---------------------------
# rend.vertexShader = shaders.vertexShader
# rend.fragmentShader = shaders.gouradShader 
# rend.glLoadModel(filename = "models/Boat.obj",
#                  textureName = "textures/boat.bmp",
#                  translate = (-5.6, 3.4,10),
#                  rotate = (150, -120, 5),
#                  scale = (1,1,1)) 
# rend.glRender() 

# ------------------------ torre ---------------------------
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.gouradShader 
rend.glLoadModel(filename = "models/tower.obj",
                 textureName = "textures/tower.bmp",
                 translate = (-5.6, 3.4,10),
                 rotate = (150, -120, 5),
                 scale = (1,1,1)) 
rend.glRender() 


# rend.glLoadModel(filename = "models/DeadTree1.obj",
#                  textureName = "textures/arbol-gris.bmp",
#                  translate = (0, 0,30),
#                  rotate = (180, 180, 0),
#                  scale = (1,1,1)) 

# rend.glLoadModel(filename = "models/DeadTree2.obj",
#                  textureName = "textures/arbol-medio.bmp",
#                  translate = (0, 0,30),
#                  rotate = (180, 180, 0),
#                  scale = (1,1,1)) 

# rend.glLoadModel(filename = "models/DeadTree3.obj",
#                  textureName = "textures/arbol-oscuro.bmp",
#                  translate = (0, 0,30),
#                  rotate = (180, 180, 0),
#                  scale = (1,1,1)) 

# rend.glLoadModel(filename = "models/DeadTree4.obj",
#                  textureName = "textures/arbol-gris.bmp",
#                  translate = (0, 0,30),
#                  rotate = (180, 180, 0),
#                  scale = (1,1,1)) 


# Se crea el FrameBuffer con la escena renderizada
# rend.glFinish("photoshoot/gouradShader.bmp")
# rend.glFinish("photoshoot/contourShader.bmp")
# rend.glFinish("photoshoot/OutlineShader.bmp")
# rend.glFinish("photoshoot/TextureFadeShader.bmp")
# rend.glFinish("photoshoot/pixelShader.bmp")

rend.glFinish("photoshoot/pruebas.bmp")