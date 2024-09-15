import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':

  abstenciones_totales_2022 = 0
  votos_totales_2022 = 0

  abstenciones_totales_2019 = 0
  votos_totales_2019 = 0

  abstenciones_totales_2015 = 0
  votos_totales_2015 = 0

  abstenciones_totales_2011 = 0
  votos_totales_2011 = 0

  abstenciones_totales_2007 = 0
  votos_totales_2007 = 0

  abstenciones_totales_2003 = 0
  votos_totales_2003 = 0

  # 2022

  with open('datos/Elecciones2022.csv', encoding='ISO-8859-1') as file:
    
    data = file.readlines()
    lines = []
    

    for line in data:
      lines.append(line.split(';'))

    # Solo me importa el 8º (censo), el 11º (total votantes)

    
    lines.pop(0)

    i = 0
    while i < len(lines):
      lines[i][7] = lines[i][7].replace('.', '')
      lines[i][10] = lines[i][10].replace('.', '')
      abstenciones = int(lines[i][7]) - int(lines[i][10])
      abstenciones_totales_2022 += abstenciones
      votos_totales_2022 += int(lines[i][10])
      i += 1
      
      while(lines[i][0] == lines[i-1][0]): 
        i += 1
        if(i == len(lines)): break

  # 2019

  with open('datos/Elecciones2019.csv', encoding='ISO-8859-1') as file:
    
    data = file.readlines()
    lines : list[list[str]] = []
    line : str = ''
    

    for line in data:
      lines.append(line.split(';'))
      

    # Solo me importa el 8º (censo), el 11º (total votantes)

    
    lines.pop(0)

    i = 0
    while i < len(lines):
      lines[i][7] = lines[i][7].replace('.', '')
      lines[i][10] = lines[i][10].replace('.', '')
      abstenciones = int(lines[i][7]) - int(lines[i][10])
      abstenciones_totales_2019 += abstenciones
      votos_totales_2019 += int(lines[i][10])
      i += 1
      
      while(lines[i][0] == lines[i-1][0]): 
        i += 1
        if(i == len(lines)): break

  # 2015

  with open('datos/Elecciones2015.csv', encoding='ISO-8859-1') as file:
    
    data = file.readlines()
    lines = []
    

    for line in data:
      lines.append(line.split(';'))

    # Solo me importa el 8º (censo), el 11º (total votantes)

    
    lines.pop(0)

    i = 0
    while i < len(lines):
      lines[i][7] = lines[i][7].replace('.', '')
      lines[i][10] = lines[i][10].replace('.', '')
      abstenciones = int(lines[i][7]) - int(lines[i][10])
      abstenciones_totales_2015 += abstenciones
      votos_totales_2015 += int(lines[i][10])
      i += 1
      
      while(lines[i][0] == lines[i-1][0]): 
        i += 1
        if(i == len(lines)): break

   # 2011

  with open('datos/Elecciones2011.csv', encoding='ISO-8859-1') as file:
    
    data = file.readlines()
    lines = []
    

    for line in data:
      lines.append(line.split(';'))

    # Solo me importa el 8º (censo), el 11º (total votantes)

    
    lines.pop(0)

    i = 0
    while i < len(lines):
      lines[i][7] = lines[i][7].replace('.', '')
      lines[i][10] = lines[i][10].replace('.', '')
      abstenciones = int(lines[i][7]) - int(lines[i][10])
      abstenciones_totales_2011 += abstenciones
      votos_totales_2011 += int(lines[i][10])
      i += 1
      
      while(lines[i][0] == lines[i-1][0]): 
        i += 1
        if(i == len(lines)): break

  # 2007

  with open('datos/Elecciones2007.csv', encoding='ISO-8859-1') as file:
    
    data = file.readlines()
    lines = []
    

    for line in data:
      lines.append(line.split(';'))

    # Solo me importa el 8º (censo), el 11º (total votantes)

    
    lines.pop(0)

    i = 0
    while i < len(lines):
      lines[i][7] = lines[i][7].replace('.', '')
      lines[i][10] = lines[i][10].replace('.', '')
      abstenciones = int(lines[i][7]) - int(lines[i][10])
      abstenciones_totales_2007 += abstenciones
      votos_totales_2007 += int(lines[i][10])
      i += 1
      
      while(lines[i][0] == lines[i-1][0]): 
        i += 1
        if(i == len(lines)): break

  # 2003

  with open('datos/Elecciones2003.csv', encoding='ISO-8859-1') as file:
    
    data = file.readlines()
    lines = []
    

    for line in data:
      lines.append(line.split(';'))

    # Solo me importa el 8º (censo), el 11º (total votantes)

    
    lines.pop(0)

    i = 0
    while i < len(lines):
      lines[i][7] = lines[i][7].replace('.', '')
      lines[i][10] = lines[i][10].replace('.', '')
      abstenciones = int(lines[i][7]) - int(lines[i][10])
      abstenciones_totales_2003 += abstenciones
      votos_totales_2003 += int(lines[i][10])
      i += 1
      
      while(lines[i][0] == lines[i-1][0]): 
        i += 1
        if(i == len(lines)): break

  n_grupos = 6
  
  abst = (abstenciones_totales_2003, abstenciones_totales_2007, abstenciones_totales_2011, abstenciones_totales_2015, abstenciones_totales_2019, abstenciones_totales_2022)
  votos = (votos_totales_2003, votos_totales_2007, votos_totales_2011, votos_totales_2015, votos_totales_2019, votos_totales_2022)

  fig, ax = plt.subplots()

  index = np.arange(n_grupos)

  bar_width = 0.30
  opacity = 0.5
  error_config = {'ecolor': '0.3'}

  rects1 = plt.bar(index, abst, bar_width,
                   alpha=opacity,
                   color='b',
                   error_kw=error_config,
                   label='Abstenciones')
  
  rects2 = plt.bar(index + bar_width, votos, bar_width,
                   alpha=opacity,
                   color='r',
                   error_kw=error_config,
                   label='Votos totales')
  
  plt.xlabel('Años en los que se hicieron votaciones en Castilla y León')
  plt.ylabel('Personas mayores de 18 años')
  plt.title('Comparación del absentismo frente a la votación a lo largo de los años')
  plt.xticks(index + bar_width / 2, ['2003', '2007', '2011', '2015', '2019', '2022'])
  plt.legend()
  ax.grid(True)

  plt.tight_layout()
  plt.show()

  

    
    
      





    

    

 
 

