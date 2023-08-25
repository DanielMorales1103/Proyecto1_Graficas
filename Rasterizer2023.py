from gl import Renderer
import shaders

# El tama�o del FrameBuffer
width = 560
height = 540

# Se crea el renderizador
rend = Renderer(width, height)

# Le damos los shaders que se utilizar�s
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.gouradShader 
# rend.fragmentShader = shaders.contourShader 
# rend.fragmentShader = shaders.OutlineShader
# rend.fragmentShader = shaders.DiagonalLinesShader
rend.glLoadModel(filename = "models/Boat.obj",
                 textureName = "textures/boat.bmp",
                 translate = (0, 0,10),
                 rotate = (90, 101, 70),
                 scale = (1,1,1)) 


rend.glRender()

# Se crea el FrameBuffer con la escena renderizada
# rend.glFinish("photoshoot/gouradShader.bmp")
# rend.glFinish("photoshoot/contourShader.bmp")
# rend.glFinish("photoshoot/OutlineShader.bmp")
# rend.glFinish("photoshoot/TextureFadeShader.bmp")
# rend.glFinish("photoshoot/pixelShader.bmp")

rend.glFinish("photoshoot/pruebas.bmp")