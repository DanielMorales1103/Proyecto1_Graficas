import numpy as np
import libreria as lb
import random

def vertexShader(vertex, **kwargs):  
    # El Vertex Shader se lleva a cabo por cada v�rtice

    modelMatrix = kwargs["modelMatrix"]
    viewMatrix= kwargs["viewMatrix"]
    projectionMatrix= kwargs["projectionMatrix"]
    vpMatrix= kwargs["vpMatrix"]

    vt = [vertex[0],
          vertex[1],
          vertex[2],
          1]

    vt1= lb.multi4x4matrix(vpMatrix, projectionMatrix)
    vt2= lb.multi4x4matrix(vt1, viewMatrix)
    vt3= lb.multi4x4matrix(vt2, modelMatrix)
    vt = lb.multimatrixvec(vt3, vt)

    """ vt = vt.tolist()[0] """

    vt = [vt[0]/vt[3],
          vt[1]/vt[3],
          vt[2]/vt[3]]

    return vt
 
def gouradShader(**kwargs):
    texture= kwargs["texture"]
    tA, tB, tC= kwargs["texCoords"]
    nA, nB, nC= kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w= kwargs["bCoords"]
    modelMatrix= kwargs["modelMatrix"]


    b= 1.0
    g= 1.0
    r= 1.0

    if texture != None:
        tU= u * tA[0] + v * tB[0] + w * tC[0]
        tV= u * tA[1] + v * tB[1] + w * tC[1]
        
        textureColor = texture.getColor(tU, tV)    
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    normal= [u * nA[0] + v * nB[0] + w * nC[0],
             u * nA[1] + v * nB[1] + w * nC[1],
             u * nA[2] + v * nB[2] + w * nC[2],
             0]
    
    normal = lb.multimatrixvec(modelMatrix, normal)
    normal = [normal[0], normal[1], normal[2]]

    dLight =(-dLight[0], -dLight[1], -dLight[2])
    intensity= lb.dot_product(normal, dLight)
    
    b *= intensity
    g *= intensity
    r *= intensity

    b = min(b, 1.0)
    g = min(g, 1.0)
    r = min(r, 1.0)

    if intensity > 0:
        return r, g, b

    else:
        return [0,0,0]
    
def pixelShader(**kwargs):
    numero_aleatorio = random.randint(1, 100)
    if (numero_aleatorio <= 40):
        texture= kwargs["texture"]
        tA, tB, tC= kwargs["texCoords"]
        nA, nB, nC= kwargs["normals"]
        dLight = kwargs["dLight"]
        u, v, w= kwargs["bCoords"]
        modelMatrix= kwargs["modelMatrix"]


        b= 1.0
        g= 1.0
        r= 1.0

        if texture != None:
            tU= u * tA[0] + v * tB[0] + w * tC[0]
            tV= u * tA[1] + v * tB[1] + w * tC[1]
            
            textureColor = texture.getColor(tU, tV)    
            b *= textureColor[2]
            g *= textureColor[1]
            r *= textureColor[0]

        normal= [u * nA[0] + v * nB[0] + w * nC[0],
             u * nA[1] + v * nB[1] + w * nC[1],
             u * nA[2] + v * nB[2] + w * nC[2],
             0]
    
        normal = lb.multimatrixvec(modelMatrix, normal)
        normal = [normal[0], normal[1], normal[2]]

        dLight =(-dLight[0], -dLight[1], -dLight[2])
        intensity= lb.dot_product(normal, dLight)
        
        b *= intensity
        g *= intensity
        r *= intensity

        if intensity > 0:
            return r, g, b

        else:
            return [0,0,0]
    else:
        return [0.5,0.5,0.5]

def contourShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]

    delta_normal_A = lb.vector_subtraction(nA, nB)
    delta_normal_B = lb.vector_subtraction(nB, nC)
    delta_normal_C = lb.vector_subtraction(nC, nA)

    intensity_diffuse = lb.dot_product(nA, [-component for component in dLight])
   
    delta_intensity_A = lb.dot_product(delta_normal_A, dLight)
    delta_intensity_B = lb.dot_product(delta_normal_B, dLight)
    delta_intensity_C = lb.dot_product(delta_normal_C, dLight)

    delta_intensity_magnitude = max(abs(delta_intensity_A),
                                    abs(delta_intensity_B),
                                    abs(delta_intensity_C))

    threshold = 0.5 * delta_intensity_magnitude

    if abs(intensity_diffuse) > threshold:
        color = [0, 0, 0]
    else:
        if texture != None:
            tU = u * tA[0] + v * tB[0] + w * tC[0]
            tV = u * tA[1] + v * tB[1] + w * tC[1]
            textureColor = texture.getColor(tU, tV)
            color = textureColor
        else:
            color = [1, 1, 1] 

    return color

def OutlineShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    u, v, w = kwargs["bCoords"]

    angle_A = lb.angle_between_vectors(nA, nB)
    angle_B = lb.angle_between_vectors(nB, nC)
    angle_C = lb.angle_between_vectors(nC, nA)

    threshold_angle = 0.8 
    if angle_A > threshold_angle or angle_B > threshold_angle or angle_C > threshold_angle:
        color = [0.04, 0.03, 0.37]  
    else:
        if texture != None:
            tU = u * tA[0] + v * tB[0] + w * tC[0]
            tV = u * tA[1] + v * tB[1] + w * tC[1]
            textureColor = texture.getColor(tU, tV)
            color = textureColor
        else:
            color = [0, 0, 0.1]  

    return color

def TextureFadeShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    u, v, w = kwargs["bCoords"]

    # Calcular la posición vertical del píxel con respecto al centro del objeto
    center_y = (tA[1] + tB[1] + tC[1]) / 3.0
    vertical_distance = abs(center_y - v)

    # Calcular el factor de mezcla utilizando la distancia vertical
    mix_factor = 1.0 - vertical_distance

    # Obtener el color de la textura original
    texture_color = texture.getColor(tA[0], tA[1])

    # Mezclar la textura con el color negro utilizando el factor de mezcla
    mixed_color = [c * mix_factor for c in texture_color]

    return mixed_color

def DiagonalLinesShader(**kwargs):
    u, v, w = kwargs["bCoords"]

    color1 = [1.0, 0.0, 0.0] 
    color2 = [0.0, 0.0, 1.0]  

   
    stripe_width = 0.5  
    stripe_frequency = 4.0  
    position_in_stripe = (u + v) * stripe_frequency

    if position_in_stripe % stripe_width < stripe_width / 2:
        color = color1
    else:
        color = color2

    return color

def toonShader(**kwargs):
    texture= kwargs["texture"]
    tA, tB, tC= kwargs["texCoords"]
    nA, nB, nC= kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w= kwargs["bCoords"]

    b= 1.0
    g= 1.0
    r= 1.0

    if texture != None:
        tU= u * tA[0] + v * tB[0] + w * tC[0]
        tV= u * tA[1] + v * tB[1] + w * tC[1]
        
        textureColor = texture.getColor(tU, tV)    
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    normal= [u * nA[0] + v * nB[0] + w * nC[0],
            u * nA[1] + v * nB[1] + w * nC[1],
            u * nA[2] + v * nB[2] + w * nC[2]]
    
    dLight= (-dLight[0], -dLight[1], -dLight[2])
    intensity= lb.dot_product(normal, dLight)

    if intensity <= 0.25:
        intensity= 0.2

    elif intensity <=0.5:
        intensity= 0.45

    elif intensity <=0.75:
        intensity=0.7

    elif intensity<=1.0:
        intensity= 0.95
    
    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b

    else:
        return [0,0,0]
    
def grayShader(**kwargs):
    texture= kwargs["texture"]
    tA, tB, tC= kwargs["texCoords"]
    nA, nB, nC= kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w= kwargs["bCoords"]

    b= 1.0
    g= 1.0
    r= 1.0

    if texture != None:
        tU= u * tA[0] + v * tB[0] + w * tC[0]
        tV= u * tA[1] + v * tB[1] + w * tC[1]
        
        textureColor = texture.getColor(tU, tV)    
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    normal= [u * nA[0] + v * nB[0] + w * nC[0],
             u * nA[1] + v * nB[1] + w * nC[1],
             u * nA[2] + v * nB[2] + w * nC[2]]
    
    dLight= (-dLight[0], -dLight[1], -dLight[2])
    intensity= lb.dot_product(normal, dLight)
    
    b *= intensity
    g *= intensity
    r *= intensity

    red= (0.8,0.8,0.8)

    b *= red[2]
    g *= red[1]
    r *= red[0]

    if intensity > 0:
        return r, g, b

    else:
        return [0,0,0]


def snakeShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]
    modelMatrix = kwargs["modelMatrix"]

    b = 1.0
    g = 1.0
    r = 1.0

    # Define las coordenadas del punto actual
    x, y = u, v

    # Define el umbral para la detección de líneas diagonales
    threshold = 0.3

    # Verifica si el punto está en una línea diagonal
    if abs(x - y) < threshold:
        return 0, 0, 0  # Devuelve color transparente

    if texture is not None:
        tU = u * tA[0] + v * tB[0] + w * tC[0]
        tV = u * tA[1] + v * tB[1] + w * tC[1]

        textureColor = texture.getColor(tU, tV)
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    normal = [u * nA[0] + v * nB[0] + w * nC[0],
              u * nA[1] + v * nB[1] + w * nC[1],
              u * nA[2] + v * nB[2] + w * nC[2],
              0]

    normal = lb.multimatrixvec(modelMatrix, normal)
    normal = [normal[0], normal[1], normal[2]]

    dLightNeg = (-dLight[0], -dLight[1], -dLight[2])
    intensity = lb.dot_product(normal, dLightNeg)

    gradient_intensity = (u + v) / 2

    b *= intensity * gradient_intensity
    g *= intensity * gradient_intensity
    r *= intensity * gradient_intensity

    b = min(b, 1.0)
    g = min(g, 1.0)
    r = min(r, 1.0)

    if intensity > 0:
        return r, g, b
    else:
        return [0, 0, 0]