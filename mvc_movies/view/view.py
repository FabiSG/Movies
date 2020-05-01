class View:
    """
    **************************
    * A view for a movies DB *
    **************************
    """
    def start(self):
        print('==============')
        print('= Bienvenido =')
        print('==============')

    def end(self):
        print('================================')
        print('=        Hasta la vista!       =')
        print('================================')

    def main_menu(self):
        print('================================')
        print('=        Menu Principal        =')
        print('================================')
        print('1. Películas')
        print('2. Actores')
        print('3. Directores')
        print('4. Generos')
        print('5. Salir')

    def option(self,last):
        print('Selecciona un opcion (1-'+last+'): ', end = '')

    def not_valid_option(self):
        print('Opcion no valida!\nIntenta de nuevo')
    
    def ask(self, output):
        print(output, end = '' )
    
    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))
    
    def error(self, err):
        print(' Error! '.center(len(err)+4,'-'))
        print('-'+err+'-')
        print('-'*(len(err)+4))
    

    """
    *********************
    * A view for movies *
    *********************
    """
    def movies_menu(self):
        print('************************')
        print('* -- Submenu Movies -- *')
        print('************************')
        print('1. Agregar Pelicula')
        print('2. Mostrar Pelicula')
        print('3. Mostrar todas las Peliculas')
        print('4. Mostrar Peliculas por año')
        print('5. Mostrar Descripciones')
        print('6  Ver detalles de pelicula')
        print('7  Agregar detalles')
        print('8  Editar detalles')
        print('9. Actualizar Pelicula')
        print('10. Borrar Detalles')
        print('11. Borrar Pelicula')
        print('12. Regresar')
    
    def show_a_movie(self, record):
        if record[3] == None:
            print(f'{record[0]:<3}|{record[1]:<30}|{record[2]:<20}|'+'                    '+f'|{record[4]:<5}')
        else:
            print(f'{record[0]:<3}|{record[1]:<30}|{record[2]:<20}|{record[3]:<20}|{record[4]:<5}')
    
    def show_movie_header(self, header):
        print(header.center(92,'*'))
        print('ID'.ljust(3)+'|'+'Pelicula'.ljust(30)+'|'+'Idioma'.ljust(20)+'|'+'Subtitulo'.ljust(20)+'|'+'Año'.ljust(5))
        print('-'*92)

    def show_movie_midder(self):
        print('-'*92)
    
    def show_movie_footer(self):
        print('-'*92)

    def show_a_detail(self, record):
        print(f'{record[0]:<3}|{record[1]:<20}|{record[2]:<20}|{record[3]:<100}|{record[4]:<8}')
    
    def show_detail_header(self, header):
        print(header.center(92,'*'))
        print('ID'.ljust(3)+'|'+'Pelicula'.ljust(20)+'|'+'Director'.ljust(20)+'|'+'Descripcion'.ljust(100)+'|'+'Duracion'.ljust(8))
        print('-'*156)

    def show_detail_midder(self):
        print('-'*156)
    
    def show_detail_footer(self):
        print('-'*156)


    """
    *********************
    * A view for Actors *
    *********************
    """
    def actors_menu(self):
        print('************************')
        print('* -- Submenu Actors -- *')
        print('************************')
        print('1. Agregar Actor')
        print('2. Mostrar Actor')
        print('3. Mostrar todas los Actores')
        print('4. Mostrar Peliculas de actor')
        print('5  Ver Actor por nacionalidad')
        print('6  Editar Actor')
        print('7  Agregar pelicula del actor')
        print('8  Eliminar pelicula del actor ')
        print('9  Eliminar actor ')
        print('10 Regresar')
 
    
    def show_a_actor(self, record):
        print(f'{record[0]:<3}|{record[1]:<30}|{record[2]:<15} {record[3]:<15}|{record[4]:<20}|{record[5]}')
    
    def show_actor_header(self, header):
        print(header.center(105,'*'))
        print('ID'.ljust(3)+'|'+'Nombre'.ljust(30)+'|'+'Apellido'.ljust(31)+'|'+'Nacionalidad'.ljust(20)+'|'+'Año de nacimeinto'.ljust(5))
        print('-'*105)

    def show_actor_midder(self):
        print('-'*105)
    
    def show_actor_footer(self):
        print('-'*105)

    """
    ************************
    * A view for Directors *
    ************************
    """
    def directors_menu(self):
        print('***************************')
        print('* -- Submenu Directors -- *')
        print('***************************')
        print('1. Agregar Director')
        print('2. Mostrar Director')
        print('3. Mostrar todas los Directores')
        print('4  Motrar Director por nacionalidad')
        print('5  Mostras peliculas del director ')
        print('6  Actualizar Director ')
        print('7  Eliminar Director ')
        print('8  Regresar')
 
    
    def show_a_director(self, record):
        if record[3] == None:
            print(f'{record[0]:<3}|{record[1]:<30}|{record[2]:<30}|{record[4]:<20}|{record[5]}'+'      'f'|{record[6]:<20}')
        else:      
            print(f'{record[0]:<3}|{record[1]:<30}|{record[2]:<15} {record[3]:<15}|{record[4]:<20}|{record[5]}'+'      'f'|{record[6]:<20}')
    
    def show_director_header(self, header):
        print(header.center(105,'*'))
        print('ID'.ljust(3)+'|'+'Nombre'.ljust(30)+'|'+'Apellido'.ljust(31)+'|'+'Nacionalidad'.ljust(20)+'|'+'nacimiento'.ljust(16)+'|'+'Estudios'.ljust(20))
        print('-'*105)

    def show_director_midder(self):
        print('-'*105)
    
    def show_director_footer(self):
        print('-'*105)
