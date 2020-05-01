from model.model import Model
from view.view import View
from datetime import date
from datetime import datetime

 
class Controller:
    """
    *******************************
    * A controller for a store DB *
    *******************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    def start(self):
        self.view.start()
        self.main_menu()

    """
    ***********************
    * General controllers *
    ***********************
    """   
    def main_menu(self):
        o = '0'
        while o != '5':
            self.view.main_menu()
            self.view.option('5')
            o = input()
            if o == '1':
                self.movies_menu()
            elif o == '2':
                self.actors_menu()
            elif o == '3':
                self.director_menu()
            # elif o == '4':
            #     self.orders_menu()
            elif o == '5':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def update_lists(self, fs , vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields, vals

    """
    **********************
    * General for movies *
    **********************
    """
    def movies_menu(self):
        o = '0'
        while o != '10':
            self.view.movies_menu()
            self.view.option('10')
            o = input()
            if o == '1':
                self.create_a_movie()
            elif o == '2':
                self.read_a_movie()
            elif o == '3':
                self.read_all_movies()
            elif o == '4':
                self.read_movie_year()
            elif o == '5':
                self.read_all_details()
            elif o == '6':
                self.read_details()
            elif o == '7':
                self.add_details()
            elif o == '8':
                self.edit_details()
            elif o == '9':
                self.update_pelicula()
            elif o == '10':
                self.delete_detail()
            elif o == '11':
                self.delete_movie()
            elif o == '12':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_movie(self):
        self.view.ask('Titulo: ')
        Titulo = input()
        self.view.ask('Idioma: ')
        Idioma = input()
        self.view.ask('Subtitulo: ')
        Subtitulo = input()
        self.view.ask('año: ')
        Año = input()
        return [Titulo,Idioma,Subtitulo,Año]

    def ask_detail(self):
        self.view.ask('id Titutlo: ')
        id_pelicula= input()
        self.view.ask('Id Director: ')
        id_director = input()
        self.view.ask('Descripcion: ')
        descripcion = input()
        self.view.ask('Duracion: ')
        duracion = input()
        return [id_pelicula,id_director, descripcion,duracion]
    
    def create_a_movie(self):
        Titulo,Idioma,Subtitulo,Año = self.ask_movie()
        out = self.model.create_movie(Titulo,Idioma,Subtitulo,Año)
        if out == True:
            self.view.ok(Titulo, 'agrego')
        else:
            self.view.error('No se pudo agregar la pelicula')
        return

    def read_a_movie(self):
        self.view.ask('ID de pelicula: ')
        i_movie = input()
        movie = self.model.read_a_movie(i_movie)
        if type(movie) == tuple:
            self.view.show_movie_header('Datos de la pelicula  '+i_movie+' ')
            self.view.show_a_movie(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if movie == None:
                self.view.error('La pelicula no existe')
            else:
                self.view.error(' Hay un problema al leer la pelicula ')
        return
    
    def read_all_movies(self):
        movies = self.model.read_all_movies()
        if type(movies) ==  list:
            self.view.show_movie_header(' Todos las peliculas ')
            for movie in movies:
                self.view.show_a_movie(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('Hay un problema todas las peliculas ')

    def read_movie_year(self):
        self.view.ask('año de la pelicula: ')
        year = input()
        movies = self.model.read_a_movies_year(year)
        if type(movies) == list:
            self.view.show_movie_header('Peliculas del año  '+year+' ')
            for movie in movies:
                self.view.show_a_movie(movie)
            self.view.show_movie_footer()
        else:
            if movies == []:
                self.view.error('No hay pelicula del año '+year)
            else:
                self.view.error(' Hay un problema al leer las peliculas del año '+year)
        return

    def add_details(self):
        dp_id_pelicula, dp_id_director, descripcion,dp_duracion = self.ask_detail()
        out = self.model.create_detalles_pelicula(dp_id_pelicula, dp_id_director, descripcion,dp_duracion)
        if out == True:
            self.view.ok(dp_id_pelicula, 'agrego')
        else:
            if out == 1062:
                print('ya existe una descripcion')
            else:
                self.view.error('No se pudo agregar la pelicula')
        return

    def read_details(self):
        self.view.ask('ID de pelicula: ')
        i_movie = input()
        details = self.model.read_detalles_pelicula(i_movie)
        if type(details) == list:
            if details == []:
                print('*********************************************')
                print('* La pelicula no cuenta con una descripcion *')
                print('*********************************************')
                return
            self.view.show_detail_header('Description de la pelicula  '+details[0][1]+' ')
            for detail in details:
                self.view.show_a_detail(detail)
            self.view.show_detail_midder()
            self.view.show_detail_footer()
        actors = self.model.read_a_mov_ac(i_movie)
        #print(actors)
        if type(actors) ==  list:
            self.view.show_actor_header(' Actores de la pelicula ')
            for actor in actors:
                self.view.show_a_actor(actor)
            self.view.show_actor_midder()
            self.view.show_actor_footer()
        else:
            self.view.error('Hay un problema todas los actores ')


    def read_all_details(self):
        movies = self.model.read_all_detalles_pelicula()
        if type(movies) ==  list:
            self.view.show_detail_header(' Todos las descripciones ')
            for movie in movies:
                self.view.show_a_detail(movie)
            self.view.show_detail_midder()
            self.view.show_detail_footer()
        else:
            self.view.error('Hay un problema al leer todas las decripciones ')       

    def edit_details(self):
        self.view.ask(' ID de descripcion de pelicula: ')
        i_desc = input()
        details = self.model.read_detalles_pelicula(i_desc)
        if type(details) == list:
            self.view.show_detail_header('Description de la pelicula  '+details[0][1]+' ')
            for detail in details:
                self.view.show_a_detail(detail)
            self.view.show_detail_midder()
            self.view.show_detail_footer()
        else:
            if details == None:
                self.view.error('No existe la descricion')
            else:
                self.view.error('Problema al leer la descripcion')
            return

        self.view.msg('Ingresa los valores a modificar ( vacio para dejarlo igual ):')
        whole_vals = self.ask_detail()
        fields, vals = self.update_lists(['dp_id_pelicula', 'dp_id_director', 'descripcion','dp_duracion'],whole_vals)
        vals.append(i_desc)
        vals = tuple(vals)
        out = self.model.update_detalles_pelicula(fields,vals)
        if out == True:
            self.view.ok(i_desc, 'atualizo')
        else:
            self.view.error('No se pudo actualizar')
        return        

    def delete_detail(self):
        self.view.ask('ID de detalle a borrar: ')
        dp_id_pelicula = input()
        count = self.model.delate_detalles_prlicula(dp_id_pelicula)
        if count != 0:
            self.view.ok(dp_id_pelicula, 'Borro')
        else:
            if count == 0:
                self.view.error('La pelicula no exite')
            else:
                self.view.error('Prblema al borrar la pelicula')
        return



    def update_pelicula(self):
        self.view.ask(' ID de pelicula a modificar: ')
        id_pelicula = input()
        movie = self.model.read_a_movie(id_pelicula)
        if type(movie) == tuple:
            self.view.show_movie_header('Datos de la pelicula  '+id_pelicula+' ')
            self.view.show_a_movie(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if movie == None:
                self.view.error('La pelicula no existe')
            else:
                self.view.error('Problema al leer la pelicula')
            return
        self.view.msg('Ingresa los valores a modificar ( vacio para dejarlo igual ):')
        whole_vals = self.ask_movie()
        fields, vals = self.update_lists(['p_titulo','p_idioma','p_subtitulos','p_año'],whole_vals)
        vals.append(id_pelicula)
        vals = tuple(vals)
        out = self.model.update_movie(fields,vals)
        if out == True:
            self.view.ok(id_pelicula, 'atualizo')
        else:
            self.view.error('No se pudo actualizar')
        return

    def delete_movie(self):
        self.view.ask('ID de pelicula a borrar: ')
        id_pelicula = input()
        count = self.model.delete_movie(id_pelicula)
        if count != 0:
            self.view.ok(id_pelicula, 'Borro')
        else:
            if count == 0:
                self.view.error('La pelicula no exite')
            else:
                self.view.error('Prblema al borrar la pelicula')
        return


    """
    **********************
    * General for actors *
    **********************
    """
    def actors_menu(self):
        o = '0'
        while o != '8':
            self.view.actors_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.create_a_actor()
            elif o == '2':
                self.read_a_actor()
            elif o == '3':
                self.read_all_actor()
            elif o == '4':
                self.read_movie_actor()
            elif o == '5':
                self.read_a_actor_nacionality()                
            elif o == '6':
                self.update_actor()
            elif o == '7':
                self.add_movie()
            elif o == '8':
                self.del_movie()
            elif o == '9':
                self.delete_actor()
            elif o == '10':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_actor(self):
        self.view.ask('Nombre: ')
        Nombre = input()
        self.view.ask('Apellido Paterno: ')
        ApellidoPat = input()
        self.view.ask('Apellido Materno: ')
        ApellidoMat = input()
        self.view.ask('Nacionalidad: ')
        Nacionalidad = input()
        self.view.ask('Fecha de nacimiento: ')
        Año = input()        
        return [Nombre,ApellidoPat,ApellidoMat,Nacionalidad,Año]
    
    def create_a_actor(self):
        Nombre,ApellidoPat,ApellidoMat,Nacionalidad,Año = self.ask_actor()
        out = self.model.create_actor(Nombre,ApellidoPat,ApellidoMat,Nacionalidad,Año)
        if out == True:
            self.view.ok(Nombre+' '+ApellidoPat, ' se agrego')
        else:
            self.view.error('No se pudo agregar el actor')
        return

    def read_a_actor(self):
        self.view.ask('ID de Actor: ')
        i_actor = input()
        actor = self.model.read_a_actor(i_actor)
        if type(actor) == tuple:
            self.view.show_movie_header('Datos del actor  '+i_actor+' ')
            self.view.show_a_actor(actor)
            self.view.show_actor_midder()
            self.view.show_actor_footer()
        else:
            if actor == None:
                self.view.error('El actor no existe')
            else:
                self.view.error(' Hay un problema al leer el actor ')
        return

    def read_a_actor_nacionality(self):
        self.view.ask('Nacionalidad: ')
        nacionality = input()
        actors = self.model.read_a_actor_nacionalidad(nacionality)
        if type(actors) == list:
            self.view.show_actor_header('Peliculas del año  '+nacionality+' ')
            for actor in actors:
                self.view.show_a_actor(actor)
            self.view.show_actor_footer()
        else:
            if actors == []:
                self.view.error('No hay actores de la nacionalidad '+nacionality)
            else:
                self.view.error(' Hay un problema al leer las nacionalidades '+nacionality)
        return
    
    def read_all_actor(self):
        actors = self.model.read_all_actor()
        if type(actors) ==  list:
            self.view.show_actor_header(' Todos los actores ')
            for actor in actors:
                self.view.show_a_actor(actor)
            self.view.show_actor_midder()
            self.view.show_actor_footer()
        else:
            self.view.error('Hay un problema todas los actores ')

    def read_movie_actor(self):
        self.view.ask('ID del actor: ')
        i_actor = input()
        movies = self.model.read_a_ac_mov(i_actor)
        if type(movies) == list:
            self.view.show_movie_header('Peliculas del actor ')
            for movie in movies:
                self.view.show_a_movie(movie)
            self.view.show_movie_footer()
        else:
            if movies == []:
                self.view.error('No hay pelicula del actor')
            else:
                self.view.error(' Hay un problema al leer las peliculas del actor')
        return
    
    def update_actor(self):
        self.view.ask(' ID de ator a modificar: ')
        id_actor = input()
        actor = self.model.read_a_actor(id_actor)
        if type(actor) == tuple:
            self.view.show_movie_header('Datos del actor  '+actor[1]+' ')
            self.view.show_a_actor(actor)
            self.view.show_actor_midder()
            self.view.show_actor_footer()
        else:
            if actor == None:
                self.view.error('El actor no existe')
            else:
                self.view.error('Problema al leer el actor')
            return
        self.view.msg('Ingresa los valores a modificar ( vacio para dejarlo igual ):')
        whole_vals = self.ask_actor()
        fields, vals = self.update_lists(['a_nombre','a_apellidoPat','a_apellidoMat','a_nacionalidad','a_fnacimiento'],whole_vals)
        vals.append(id_actor)
        vals = tuple(vals)
        out = self.model.update_actor(fields,vals)
        if out == True:
            self.view.ok(id_actor, 'atualizo')
        else:
            self.view.error('No se pudo actualizar')
        return

    def add_movie(self):
        movies = self.model.read_all_movies()
        if type(movies) ==  list:
            self.view.show_movie_header(' Todos las peliculas ')
            for movie in movies:
                self.view.show_a_movie(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('Hay un problema todas las peliculas ')
        self.view.ask('ID de actor: ')
        id_actor= input()
        self.view.ask('ID de pelicula: ')
        id_movie = input()
        out = self.model.create_ac_mov(id_actor,id_movie)
        if out == True:
            self.view.ok(id_movie , 'Se agrego la pelicula al actor')
        else:
            self.view.error('No se pudo agregar')
        return        

    def del_movie(self):
        self.view.ask('ID de actor a borrar: ')
        id_actor = input()
        self.view.ask('ID de pelicula a borrar: ')
        id_movie = input()
        count = self.model.delete_ac_mov(id_actor,id_movie)
        if count != 0:
            self.view.ok(id_actor, 'Borro')
        else:
            if count == 0:
                self.view.error('El actor no exite')
            else:
                self.view.error('Prblema al borrar la pelicula del actor')
        return

    def delete_actor(self):
        self.view.ask('ID de actor a borrar: ')
        id_actor = input()
        count = self.model.delete_actor(id_actor)
        if count != 0:
            self.view.ok(id_actor, 'Borro')
        else:
            if count == 0:
                self.view.error('El actor no exite')
            else:
                self.view.error('Prblema al borrar el actor')
        return
    """
    ************************
    * General for director *
    ************************
    """
    def director_menu(self):
        o = '0'
        while o != '8':
            self.view.directors_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.create_a_director()
            elif o == '2':
                self.read_a_director()
            elif o == '3':
                self.read_all_directors()
            elif o == '4':
                self.read_a_director_nacionality()                
            elif o == '5':
                self.read_director_movies()
            elif o == '6':
                self.edit_director()
            elif o == '7':
                self.del_director()
            elif o == '8':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_director(self):
        self.view.ask('Nombre: ')
        Nombre = input()
        self.view.ask('Apellido Paterno: ')
        ApellidoPat = input()
        self.view.ask('Apellido Materno: ')
        ApellidoMat = input()
        self.view.ask('Nacionalidad: ')
        Nacionalidad = input()      
        self.view.ask('Fecha de nacimiento: ')
        año = input()       
        self.view.ask('Estudios: ')
        Estudios = input() 
        return [Nombre,ApellidoPat,ApellidoMat,Nacionalidad,año,Estudios]
    
    def create_a_director(self):
        Nombre,ApellidoPat,ApellidoMat,Nacionalidad,año,Estudios = self.ask_director()
        out = self.model.create_director(Nombre,ApellidoPat,ApellidoMat,Nacionalidad,año,Estudios)
        if out == True:
            self.view.ok(Nombre+' '+ApellidoPat, ' se agrego')
        else:
            self.view.error('No se pudo agregar el actor')
        return

    def read_a_director(self):
        self.view.ask('ID de Director: ')
        i_director = input()
        director = self.model.read_a_director(i_director)
        if type(director) == tuple:
            self.view.show_director_header('Datos del director  '+i_director+' ')
            self.view.show_a_director(director)
            self.view.show_director_midder()
            self.view.show_director_footer()
        else:
            if director == None:
                self.view.error('El director no existe')
            else:
                self.view.error(' Hay un problema al leer el director ')
        return

    def read_a_director_nacionality(self):
        self.view.ask('Nacionalidad: ')
        nacionality = input()
        directors = self.model.read_a_director_nacionalidad(nacionality)
        if type(directors) == list:
            self.view.show_director_header('Directores de la nacionalidad: '+nacionality+' ')
            for actor in directors:
                self.view.show_a_actor(actor)
            self.view.show_actor_footer()
        else:
            if directors == []:
                self.view.error('No hay directores de la nacionalidad '+nacionality)
            else:
                self.view.error(' Hay un problema al leer las nacionalidades '+nacionality)
        return
    
    def read_all_directors(self):
        directors = self.model.read_all_director()
        if type(directors) ==  list:
            self.view.show_director_header(' Todos los directores ')
            for director in directors:
                self.view.show_a_director(director)
            self.view.show_director_midder()
            self.view.show_director_footer()
        else:
            self.view.error('Hay un problema todas los actores ')

    def read_director_movies(self):
        self.view.ask('ID del director: ')
        id_director = input()
        movies = self.model.read_a_dir_mov(id_director)
        if movies == []:
            print('*************************')
            print('* No existe el director *')
            print('*************************')
            return
        else:
            if type(movies) == list:
                self.view.show_movie_header('Peliculas del director ')
                for movie in movies:
                    self.view.show_a_movie(movie)
                self.view.show_movie_footer()
            else:
                if movies == []:
                    self.view.error('No hay pelicula del director')
                else:
                    self.view.error(' Hay un problema al leer las peliculas del director')
            return
    
    def edit_director(self):
        self.view.ask(' ID de director a modificar: ')
        id_director = input()
        director = self.model.read_a_director(id_director)
        if type(director) == tuple:
            self.view.show_director_header('Datos del director  '+id_director+' ')
            self.view.show_a_director(director)
            self.view.show_director_midder()
            self.view.show_director_footer()
        else:
            if director == None:
                self.view.error('El director no existe')
            else:
                self.view.error(' Hay un problema al leer el director ')
            return
        self.view.msg('Ingresa los valores a modificar ( vacio para dejarlo igual ):')
        whole_vals = self.ask_director()
        fields, vals = self.update_lists(['d_nombre','d_apellidoPat','d_apellidoMat','d_nacionalidad','d_fnacimiento','d_educacion'],whole_vals)
        vals.append(id_director)
        vals = tuple(vals)
        out = self.model.update_director(fields,vals)
        if out == True:
            self.view.ok(id_director, 'atualizo')
        else:
            self.view.error('No se pudo actualizar')
        return


    def del_director(self):
        self.view.ask('ID de director a borrar: ')
        id_director = input()
        count = self.model.delete_director(id_director)
        if count != 0:
            self.view.ok(id_director, 'Borro')
        else:
            if count == 0:
                self.view.error('El director no exite')
            else:
                self.view.error('Prblema al borrar el director')
        return
