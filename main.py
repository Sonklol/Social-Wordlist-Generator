# SOCIAL WORDLIST GENERATOR
# Consiste en generar una lista de palabras con ingeniería social para ataques de fuerza bruta
import os
from art import *

num_finales = 99 # Para crear listas más cortas/largas puedes reducir/aumentar el número
num_cero_mas_finales2 = 9 # 01-09 - aumentar para más combinaciones

linux = 'clear'
windows = 'cls'

def marca_agua():
    os.system ([linux, windows][os.name == 'nt'])
    tprint('SOCIAL')
    tprint('WORDLIST')
    tprint('GENERATOR')
    print('Creada por Sonk    ----    github.com/sonklol\n')
marca_agua()

print('[+] Inserta la información de la víctima para hacer un diccionario')
print('[+] Si no conoce toda la información, simplemente presiona enter.')

# Persona
print('\n\n-- Persona --')
nick = input('Nickname: ')
nombre_victima = input('Nombre: ')
priape_victima = input('Primer Apellido: ')
segape_victima = input('Segundo Apellido: ')
ano_victima = input('Fecha de Nacimiento (DDMMYYYY): ')

if nombre_victima == '' or ano_victima == '' or nick == '':
    os.system ([linux, windows][os.name == 'nt'])
    print('ERROR - El nombre, año o nickname de la víctima no pueden estar vacios.')
    quit()

pueblo_ciudad = input('Pueblo/Ciudad: ')

# Padres
print('\n-- Madre --')
nombre_madre = input('Nombre: ')
ano_madre = input('Año de Nacimiento (1920-20XX): ')
print('\n-- Padre --')
nombre_padre = input('Nombre: ')
ano_padre = input('Año de Nacimiento (1920-20XX): ')

# Mascota
print('\n-- Mascota --')
nombre_mascota = input('Nombre: ')
ano_mascota = input('Año de Nacimiento (1920-20XX): ')

# Palabras clave
print('\n-- Palabras Clave --')
input_palabras_clave = str(input('Palabras clave (rio,alonso,fuente,montaña): '))
if input_palabras_clave != '':
    palabras_clave = input_palabras_clave.split(",")

if ano_madre != '' and ano_padre != '' and ano_mascota != '':
    anos = [ano_victima[-4::], ano_madre, ano_padre, ano_mascota]
elif ano_madre == '' and ano_padre != '' and ano_mascota != '':
    anos = [ano_victima[-4::], ano_padre, ano_mascota]
elif ano_madre != '' and ano_padre == '' and ano_mascota != '':
    anos = [ano_victima[-4::], ano_madre, ano_mascota]
elif ano_madre != '' and ano_padre != '' and ano_mascota == '':
    anos = [ano_victima[-4::], ano_madre, ano_padre]
elif ano_madre == '' and ano_padre == '' and ano_mascota != '':
    anos = [ano_victima[-4::], ano_mascota]
elif ano_madre != '' and ano_padre == '' and ano_mascota == '':
    anos = [ano_victima[-4::], ano_madre]
elif ano_madre == '' and ano_padre != '' and ano_mascota == '':
    anos = [ano_victima[-4::], ano_padre]
else:
    anos = [ano_victima[-4::]]

min_ano = int(min(anos))
max_ano = int(max(anos))

cnombre_victima = nombre_victima.capitalize()
cnombre_madre = nombre_madre.capitalize()
cnombre_padre = nombre_padre.capitalize()
lnombre_victima = nombre_victima.lower()
lnombre_madre = nombre_madre.lower()
lnombre_padre = nombre_padre.lower()
cnombre_mascota = nombre_mascota.capitalize()
lpriape_victima = priape_victima.lower()
cpriape_victima = priape_victima.capitalize()
lsegape_victima = segape_victima.lower()
csegape_victima = segape_victima.capitalize()
lnombre_mascota = nombre_mascota.lower()

open('wordlist-'+str(nick)+'.txt', 'x')
f = open('wordlist-'+str(nick)+'.txt', 'a')

# Algoritmos
f.write('Madrid'+cnombre_victima+'\n')
f.write('Betis'+cnombre_victima+'\n')
f.write('Barcelona'+cnombre_victima+'\n')
f.write('Barsa'+cnombre_victima+'\n')
f.write('Atleti'+cnombre_victima+'\n')
f.write('Madrid'+lnombre_victima+'\n')
f.write('Betis'+lnombre_victima+'\n')
f.write('Barcelona'+lnombre_victima+'\n')
f.write('Barsa'+lnombre_victima+'\n')
f.write('Atleti'+lnombre_victima+'\n')
f.write(cnombre_victima+'Madrid'+'\n')
f.write(cnombre_victima+'Betis'+'\n')
f.write(cnombre_victima+'Barcelona'+'\n')
f.write(cnombre_victima+'Barsa'+'\n')
f.write(cnombre_victima+'Atleti'+'\n')
f.write(cnombre_victima+'madrid'+'\n')
f.write(cnombre_victima+'betis'+'\n')
f.write(cnombre_victima+'barcelona'+'\n')
f.write(cnombre_victima+'barsa'+'\n')
f.write(cnombre_victima+'atleti'+'\n')
if pueblo_ciudad != '':
    f.write(cnombre_victima+pueblo_ciudad.capitalize()+'\n')
    f.write(cnombre_victima+pueblo_ciudad.lower()+'\n')
    f.write(cnombre_victima+pueblo_ciudad.capitalize()+'\n')
    f.write(cnombre_victima+pueblo_ciudad.capitalize()[:3]+'\n')
    f.write(cnombre_victima+pueblo_ciudad.capitalize()[:4]+'\n')
    f.write(pueblo_ciudad.lower()+'\n')
    f.write(pueblo_ciudad.capitalize()+'\n')
if segape_victima != '' and priape_victima != '':
    f.write(cnombre_victima+lpriape_victima[:1]+lsegape_victima[:1]+'\n')
if priape_victima != '':
    f.write(cnombre_victima+lpriape_victima[:1]+'\n')
if nombre_padre != '':
    f.write(cnombre_victima+cnombre_padre+'\n')
    f.write(cnombre_victima+lnombre_padre+'\n')
if nombre_madre != '':
    f.write(cnombre_victima+cnombre_madre+'\n')
    f.write(cnombre_victima+lnombre_madre+'\n')
if nombre_mascota != '':
    f.write(cnombre_victima+cnombre_mascota+'-'+'\n')
    f.write(cnombre_victima+lnombre_mascota+'-'+'\n')
    f.write(cnombre_victima+cnombre_mascota+'_'+'\n')
    f.write(cnombre_victima+lnombre_mascota+'_'+'\n')
    f.write(cnombre_victima+cnombre_mascota+'!'+'\n')
    f.write(cnombre_victima+lnombre_mascota+'!'+'\n')
    f.write(cnombre_victima+cnombre_mascota+'\n')
    f.write(cnombre_victima+lnombre_mascota+'\n')

while min_ano <= max_ano:
    # Nick
    f.write(nick+str(min_ano)+'\n')
    f.write(nick+str(min_ano)+'_'+'\n')
    f.write(nick+'_'+str(min_ano)+'\n')
    f.write(nick+str(min_ano)+'$'+'\n')
    f.write(nick+'-'+str(min_ano)+'\n')
    f.write(str(min_ano)+nick+'\n')
    f.write(str(min_ano)+'-'+nick+'\n')
    f.write(str(min_ano)+'_'+nick+'\n')
    f.write(str(min_ano)+'$'+nick+'\n')

    # Persona
    f.write(lnombre_victima+str(min_ano)+'\n')
    f.write(cnombre_victima+str(min_ano)+'\n')

    f.write(cnombre_victima+'$'+str(min_ano)+'\n')
    f.write(cnombre_victima+'_'+str(min_ano)+'\n')
    f.write(cnombre_victima+'-'+str(min_ano)+'\n')
    f.write(cnombre_victima+'!'+str(min_ano)+'\n')
    f.write(cnombre_victima+'!!'+str(min_ano)+'\n')
    f.write(cnombre_victima+'$$'+str(min_ano)+'\n')
    f.write(cnombre_victima+'&'+str(min_ano)+'\n')
    f.write(cnombre_victima+'%'+str(min_ano)+'\n')
    f.write(cnombre_victima+'#'+str(min_ano)+'\n')
    f.write(cnombre_victima+'@'+str(min_ano)+'\n')
    f.write(cnombre_victima+','+str(min_ano)+'\n')
    f.write(cnombre_victima+'.'+str(min_ano)+'\n')
    f.write(cnombre_victima+'/'+str(min_ano)+'\n')
    f.write(cnombre_victima+')'+str(min_ano)+'\n')
    f.write(cnombre_victima+'('+str(min_ano)+'\n')
    f.write(cnombre_victima+'='+str(min_ano)+'\n')
    f.write(cnombre_victima+'?'+str(min_ano)+'\n')
    f.write(cnombre_victima+'ñ'+str(min_ano)+'\n')
    f.write(cnombre_victima+'^'+str(min_ano)+'\n')
    f.write(cnombre_victima+':'+str(min_ano)+'\n')
    f.write(cnombre_victima+';'+str(min_ano)+'\n')

    f.write(cnombre_victima+str(min_ano)+'$'+'\n')
    f.write(cnombre_victima+str(min_ano)+'_'+'\n')
    f.write(cnombre_victima+str(min_ano)+'-'+'\n')
    f.write(cnombre_victima+str(min_ano)+'!'+'\n')
    f.write(cnombre_victima+str(min_ano)+'!!'+'\n')
    f.write(cnombre_victima+str(min_ano)+'$$'+'\n')
    f.write(cnombre_victima+str(min_ano)+'&'+'\n')
    f.write(cnombre_victima+str(min_ano)+'%'+'\n')
    f.write(cnombre_victima+str(min_ano)+'#'+'\n')
    f.write(cnombre_victima+str(min_ano)+'@'+'\n')
    f.write(cnombre_victima+str(min_ano)+','+'\n')
    f.write(cnombre_victima+str(min_ano)+'.'+'\n')
    f.write(cnombre_victima+str(min_ano)+'/'+'\n')
    f.write(cnombre_victima+str(min_ano)+')'+'\n')
    f.write(cnombre_victima+str(min_ano)+'('+'\n')
    f.write(cnombre_victima+str(min_ano)+'='+'\n')
    f.write(cnombre_victima+str(min_ano)+'?'+'\n')
    f.write(cnombre_victima+str(min_ano)+'ñ'+'\n')
    f.write(cnombre_victima+str(min_ano)+'^'+'\n')
    f.write(cnombre_victima+str(min_ano)+':'+'\n')
    f.write(cnombre_victima+str(min_ano)+';'+'\n')

    f.write(str(min_ano)+cnombre_victima+'\n')
    f.write(str(min_ano)+'-'+cnombre_victima+'\n')
    f.write(str(min_ano)+'_'+cnombre_victima+'\n')
    f.write(str(min_ano)+'$'+cnombre_victima+'\n')

    f.write(cnombre_victima[:3]+str(min_ano)+'\n')
    f.write(cnombre_victima[:3]+str(min_ano)+'_'+'\n')
    f.write(cnombre_victima[:3]+'_'+str(min_ano)+'\n')
    f.write(cnombre_victima[:3]+str(min_ano)+'$'+'\n')
    f.write(cnombre_victima[:3]+'-'+str(min_ano)+'\n')
    f.write(str(min_ano)+cnombre_victima[:3]+'\n')
    f.write(str(min_ano)+'-'+cnombre_victima[:3]+'\n')
    f.write(str(min_ano)+'_'+cnombre_victima[:3]+'\n')
    f.write(str(min_ano)+'$'+cnombre_victima[:3]+'\n')

    # Apellidos Persona
    if priape_victima != '' and segape_victima != '':
        f.write(cnombre_victima+cpriape_victima[:1]+csegape_victima[:1]+str(min_ano)+'\n')
        f.write(cnombre_victima+lpriape_victima[:1]+lsegape_victima[:1]+str(min_ano)+'\n')
        f.write(lnombre_victima+cpriape_victima[:1]+csegape_victima[:1]+str(min_ano)+'\n')
        f.write(cnombre_victima+cpriape_victima[:3]+csegape_victima[:3]+str(min_ano)+'\n')
        f.write(cnombre_victima+lpriape_victima[:3]+lsegape_victima[:3]+str(min_ano)+'\n')
        f.write(lnombre_victima+cpriape_victima[:3]+csegape_victima[:3]+str(min_ano)+'\n')
        
        f.write(cnombre_victima+str(min_ano)+cpriape_victima[:1]+csegape_victima[:1]+'\n')
        f.write(cnombre_victima+str(min_ano)+lpriape_victima[:1]+lsegape_victima[:1]+'\n')
        f.write(lnombre_victima+str(min_ano)+cpriape_victima[:1]+csegape_victima[:1]+'\n')
        f.write(cnombre_victima+str(min_ano)+cpriape_victima[:3]+csegape_victima[:3]+'\n')
        f.write(cnombre_victima+str(min_ano)+lpriape_victima[:3]+lsegape_victima[:3]+'\n')
        f.write(lnombre_victima+str(min_ano)+cpriape_victima[:3]+csegape_victima[:3]+'\n')

        f.write(cpriape_victima+csegape_victima+str(min_ano)+'\n')
        f.write(cpriape_victima+lsegape_victima+str(min_ano)+'\n')
        f.write(lpriape_victima[:3]+csegape_victima[:3]+str(min_ano)+'\n')
    elif priape_victima != '':
        f.write(cnombre_victima+cpriape_victima[:1]+str(min_ano)+'\n')
        f.write(cnombre_victima+lpriape_victima[:1]+str(min_ano)+'\n')
        f.write(lnombre_victima+cpriape_victima[:1]+str(min_ano)+'\n')
        f.write(cnombre_victima+cpriape_victima[:3]+str(min_ano)+'\n')
        f.write(cnombre_victima+lpriape_victima[:3]+str(min_ano)+'\n')
        f.write(lnombre_victima+cpriape_victima[:3]+str(min_ano)+'\n')
        
        f.write(cnombre_victima+str(min_ano)+cpriape_victima[:1]+'\n')
        f.write(cnombre_victima+str(min_ano)+lpriape_victima[:1]+'\n')
        f.write(lnombre_victima+str(min_ano)+cpriape_victima[:1]+'\n')
        f.write(cnombre_victima+str(min_ano)+cpriape_victima[:3]+'\n')
        f.write(cnombre_victima+str(min_ano)+lpriape_victima[:3]+'\n')
        f.write(lnombre_victima+str(min_ano)+cpriape_victima[:3]+'\n')

        f.write(cpriape_victima+str(min_ano)+'\n')
        f.write(lpriape_victima[:3]+str(min_ano)+'\n')

    # Madre
    if nombre_madre != '':
        f.write(lnombre_madre+str(min_ano)+'\n')
        f.write(cnombre_madre+str(min_ano)+'\n')
        f.write(cnombre_madre+str(min_ano)+'_'+'\n')
        f.write(cnombre_madre+'_'+str(min_ano)+'\n')
        f.write(cnombre_madre+str(min_ano)+'$'+'\n')
        f.write(cnombre_madre+'-'+str(min_ano)+'\n')

        f.write(str(min_ano)+cnombre_madre+'\n')
        f.write(str(min_ano)+'-'+cnombre_madre+'\n')
        f.write(str(min_ano)+'_'+cnombre_madre+'\n')
        f.write(str(min_ano)+'$'+cnombre_madre+'\n')

        f.write(cnombre_madre[:3]+str(min_ano)+'\n')
        f.write(cnombre_madre[:3]+str(min_ano)+'_'+'\n')
        f.write(cnombre_madre[:3]+'_'+str(min_ano)+'\n')
        f.write(cnombre_madre[:3]+str(min_ano)+'$'+'\n')
        f.write(cnombre_madre[:3]+'-'+str(min_ano)+'\n')
        f.write(str(min_ano)+cnombre_madre[:3]+'\n')
        f.write(str(min_ano)+'-'+cnombre_madre[:3]+'\n')
        f.write(str(min_ano)+'_'+cnombre_madre[:3]+'\n')
        f.write(str(min_ano)+'$'+cnombre_madre[:3]+'\n')

    # Padre
    if nombre_padre != '':
        f.write(lnombre_padre+str(min_ano)+'\n')
        f.write(cnombre_padre+str(min_ano)+'\n')
        f.write(cnombre_padre+str(min_ano)+'_'+'\n')
        f.write(cnombre_padre+'_'+str(min_ano)+'\n')
        f.write(cnombre_padre+str(min_ano)+'$'+'\n')
        f.write(cnombre_padre+'-'+str(min_ano)+'\n')

        f.write(str(min_ano)+cnombre_padre+'\n')
        f.write(str(min_ano)+'-'+cnombre_padre+'\n')
        f.write(str(min_ano)+'_'+cnombre_padre+'\n')
        f.write(str(min_ano)+'$'+cnombre_padre+'\n')

        f.write(cnombre_padre[:3]+str(min_ano)+'\n')
        f.write(cnombre_padre[:3]+str(min_ano)+'_'+'\n')
        f.write(cnombre_padre[:3]+'_'+str(min_ano)+'\n')
        f.write(cnombre_padre[:3]+str(min_ano)+'$'+'\n')
        f.write(cnombre_padre[:3]+'-'+str(min_ano)+'\n')
        f.write(str(min_ano)+cnombre_padre[:3]+'\n')
        f.write(str(min_ano)+'-'+cnombre_padre[:3]+'\n')
        f.write(str(min_ano)+'_'+cnombre_padre[:3]+'\n')
        f.write(str(min_ano)+'$'+cnombre_padre[:3]+'\n')

    # Mascota
    if nombre_mascota != '':
        f.write(lnombre_mascota+str(min_ano)+'\n')
        f.write(cnombre_mascota+str(min_ano)+'\n')
        f.write(cnombre_mascota+str(min_ano)+'_'+'\n')
        f.write(cnombre_mascota+'_'+str(min_ano)+'\n')
        f.write(cnombre_mascota+str(min_ano)+'$'+'\n')
        f.write(cnombre_mascota+'-'+str(min_ano)+'\n')

        f.write(str(min_ano)+cnombre_mascota+'\n')
        f.write(str(min_ano)+'-'+cnombre_mascota+'\n')
        f.write(str(min_ano)+'_'+cnombre_mascota+'\n')
        f.write(str(min_ano)+'$'+cnombre_mascota+'\n')

        f.write(cnombre_mascota[:3]+str(min_ano)+'\n')
        f.write(cnombre_mascota[:3]+str(min_ano)+'_'+'\n')
        f.write(cnombre_mascota[:3]+'_'+str(min_ano)+'\n')
        f.write(cnombre_mascota[:3]+str(min_ano)+'$'+'\n')
        f.write(cnombre_mascota[:3]+'-'+str(min_ano)+'\n')
        f.write(str(min_ano)+cnombre_mascota[:3]+'\n')
        f.write(str(min_ano)+'-'+cnombre_mascota[:3]+'\n')
        f.write(str(min_ano)+'_'+cnombre_mascota[:3]+'\n')
        f.write(str(min_ano)+'$'+cnombre_mascota[:3]+'\n')

        f.write(cnombre_victima+lnombre_mascota+str(min_ano)+'\n')
        f.write(cnombre_victima+cnombre_mascota+str(min_ano)+'\n')
        f.write(cnombre_victima+cnombre_mascota+str(min_ano)+'_'+'\n')
        f.write(cnombre_victima+cnombre_mascota+'_'+str(min_ano)+'\n')
        f.write(cnombre_victima+cnombre_mascota+str(min_ano)+'$'+'\n')
        f.write(cnombre_victima+cnombre_mascota+'-'+str(min_ano)+'\n')
        f.write(cnombre_victima+lnombre_mascota+str(min_ano)+'_'+'\n')
        f.write(cnombre_victima+lnombre_mascota+'_'+str(min_ano)+'\n')
        f.write(cnombre_victima+lnombre_mascota+str(min_ano)+'$'+'\n')
        f.write(cnombre_victima+lnombre_mascota+'-'+str(min_ano)+'\n')
    
    min_ano += 1

contador = 0
while contador <= num_finales:
    f.write(lnombre_victima+str(contador)+'\n')
    f.write(cnombre_victima+str(contador)+'\n')
    f.write(cnombre_victima+str(contador)+'_'+'\n')
    f.write(cnombre_victima+str(contador)+'-'+'\n')
    if priape_victima != '':
        f.write(lpriape_victima+str(contador)+'\n')
        f.write(cpriape_victima+str(contador)+'\n')
        f.write(cpriape_victima+str(contador)+'-'+'\n')
    if segape_victima != '':
        f.write(lsegape_victima+str(contador)+'\n')
        f.write(csegape_victima+str(contador)+'\n')
        f.write(csegape_victima+str(contador)+'-'+'\n')
    if pueblo_ciudad != '':
        f.write(pueblo_ciudad.capitalize()+str(contador)+'\n')
        f.write(pueblo_ciudad.lower()+str(contador)+'\n')
    if nombre_mascota != '':
        f.write(cnombre_victima+lnombre_mascota+str(contador)+'\n')
        f.write(cnombre_victima+cnombre_mascota+str(contador)+'\n')
        f.write(cnombre_victima+cnombre_mascota+str(contador)+'_'+'\n')
        f.write(cnombre_victima+cnombre_mascota+str(contador)+'-'+'\n')
        f.write(cnombre_victima+cnombre_mascota+'_'+str(contador)+'\n')
        f.write(cnombre_victima+cnombre_mascota+str(contador)+'$'+'\n')
        f.write(cnombre_victima+cnombre_mascota+'-'+str(contador)+'\n')
        f.write(cnombre_victima+lnombre_mascota+str(contador)+'_'+'\n')
        f.write(cnombre_victima+lnombre_mascota+str(contador)+'-'+'\n')
        f.write(cnombre_victima+lnombre_mascota+'_'+str(contador)+'\n')
        f.write(cnombre_victima+lnombre_mascota+str(contador)+'$'+'\n')
        f.write(cnombre_victima+lnombre_mascota+'-'+str(contador)+'\n')
    if input_palabras_clave != '':
        for i in palabras_clave:
            f.write(lnombre_victima+str(contador)+'\n')
            f.write(cnombre_victima+str(contador)+'\n')
            f.write(i.lower()+str(contador)+'\n')
            f.write(i.capitalize()+str(contador)+'\n')

    f.write(cnombre_victima+'madrid'+str(contador)+'\n')
    f.write(cnombre_victima+'betis'+str(contador)+'\n')
    f.write(cnombre_victima+'barcelona'+str(contador)+'\n')
    f.write(cnombre_victima+'barsa'+str(contador)+'\n')
    f.write(cnombre_victima+'atleti'+str(contador)+'\n')
    f.write(cnombre_victima+'Madrid'+str(contador)+'\n')
    f.write(cnombre_victima+'Betis'+str(contador)+'\n')
    f.write(cnombre_victima+'Barcelona'+str(contador)+'\n')
    f.write(cnombre_victima+'Barsa'+str(contador)+'\n')
    f.write(cnombre_victima+'Atleti'+str(contador)+'\n')

    contador += 1

contador = 0
while contador <= num_cero_mas_finales2:
    f.write(lnombre_victima+'0'+str(contador)+'\n')
    f.write(cnombre_victima+'0'+str(contador)+'\n')
    if priape_victima != '':
        f.write(cpriape_victima+'0'+str(contador)+'\n')
        f.write(lpriape_victima+'0'+str(contador)+'\n')
    if segape_victima != '':
        f.write(csegape_victima+'0'+str(contador)+'\n')
        f.write(lsegape_victima+'0'+str(contador)+'\n')
    if pueblo_ciudad != '':
        f.write(pueblo_ciudad.capitalize()+'0'+str(contador)+'\n')
        f.write(pueblo_ciudad.lower()+'0'+str(contador)+'\n')
    if nombre_mascota != '':
        f.write(cnombre_victima+lnombre_mascota+'0'+str(contador)+'\n')
        f.write(cnombre_victima+cnombre_mascota+'0'+str(contador)+'\n')
        f.write(cnombre_victima+cnombre_mascota+'0'+str(contador)+'_'+'\n')
        f.write(cnombre_victima+cnombre_mascota+'_'+'0'+str(contador)+'\n')
        f.write(cnombre_victima+cnombre_mascota+'0'+str(contador)+'$'+'\n')
        f.write(cnombre_victima+cnombre_mascota+'-'+'0'+str(contador)+'\n')
        f.write(cnombre_victima+lnombre_mascota+'0'+str(contador)+'_'+'\n')
        f.write(cnombre_victima+lnombre_mascota+'_'+'0'+str(contador)+'\n')
        f.write(cnombre_victima+lnombre_mascota+'0'+str(contador)+'$'+'\n')
        f.write(cnombre_victima+lnombre_mascota+'-'+'0'+str(contador)+'\n')
    f.write('Madrid'+'0'+str(contador)+'\n')
    f.write('Betis'+'0'+str(contador)+'\n')
    f.write('Barcelona'+'0'+str(contador)+'\n')
    f.write('Barsa'+'0'+str(contador)+'\n')
    f.write('Atleti'+'0'+str(contador)+'\n')
    f.write(cnombre_victima+'Madrid'+'0'+str(contador)+'\n')
    f.write(cnombre_victima+'Betis'+'0'+str(contador)+'\n')
    f.write(cnombre_victima+'Barcelona'+'0'+str(contador)+'\n')
    f.write(cnombre_victima+'Barsa'+'0'+str(contador)+'\n')
    f.write(cnombre_victima+'Atleti'+'0'+str(contador)+'\n')
    f.write(cnombre_victima+'madrid'+'0'+str(contador)+'\n')
    f.write(cnombre_victima+'betis'+'0'+str(contador)+'\n')
    f.write(cnombre_victima+'barcelona'+'0'+str(contador)+'\n')
    f.write(cnombre_victima+'barsa'+'0'+str(contador)+'\n')
    f.write(cnombre_victima+'atleti'+'0'+str(contador)+'\n')
    if input_palabras_clave != '':
        for i in palabras_clave:
            f.write(lnombre_victima+'0'+str(contador)+'\n')
            f.write(cnombre_victima+'0'+str(contador)+'\n')
            f.write(i.lower()+'0'+str(contador)+'\n')
            f.write(i.capitalize()+'0'+str(contador)+'\n')

    contador += 1

if input_palabras_clave != '':
    for i in palabras_clave:
        f.write(i.lower()+'\n')
        f.write(i.capitalize()+'\n')
        f.write(cnombre_victima+i.capitalize()+'\n')
        f.write(cnombre_victima+i.lower()+'\n')

        f.write(i.capitalize()+'-'+'\n')
        f.write(i.capitalize()+'!'+'\n')
        f.write(i.capitalize()+'&'+'\n')
        f.write(i.capitalize()+'!!'+'\n')
        f.write(i.capitalize()+'$'+'\n')
        f.write(i.capitalize()+'$$'+'\n')
        f.write(i.capitalize()+'_'+'\n')
        f.write(i.capitalize()+'@'+'\n')
        f.write(i.capitalize()+'ñ'+'\n')
        f.write(i.lower()+'-'+'\n')
        f.write(i.lower()+'!'+'\n')
        f.write(i.lower()+'&'+'\n')
        f.write(i.lower()+'!!'+'\n')
        f.write(i.lower()+'$'+'\n')
        f.write(i.lower()+'$$'+'\n')
        f.write(i.lower()+'_'+'\n')
        f.write(i.lower()+'@'+'\n')
        f.write(i.lower()+'ñ'+'\n')

f.close()
marca_agua()
print('La wordlist se ha creado exitosamente. La podrás encontrar en: wordlist-'+str(nick)+'.txt')