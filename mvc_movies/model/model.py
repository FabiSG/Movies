from mysql import connector

class Model:
    """
    *****************************************
    * a data model with MySQL for a store DB*
    *****************************************
    """
    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d={}
        with open(self.config_db_file ) as f_r:
            for line in f_r: 
                (key, val) = line.strip().split(':')
                d[key] = val
        return d
        
    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

    """
    *****************
    * Genero metodos*
    *****************
    """
    def create_gen(self,genero):
        try:
            sql = 'INSERT INTO genero (`genero`) VALUES (%s)'
            vals = (genero,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_genero(self,genero):
        try:
            sql = 'SELECT * FROM genero WHERE id_genero = %s'
            vals = (genero,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err


    def read_all_generos(self):
        try:
            sql = 'SELECT * FROM genero'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def update_genero(self,fields,vals):
        try:
            sql = 'UPDATE genero SET '+','.join(fields)+'WHERE id_genero = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_genero(self, id_genero):
        try:
            sql = 'DELETE FROM genero WHERE id_genero = %s'
            vals = (id_genero,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *********************
    * Directores metodos*
    *********************
    """
    def create_director(self,d_nombre,d_apellidoPat,d_apellidoMat,d_nacionalidad,d_fnacimiento,d_educacion):
        try:
            sql = 'INSERT INTO directores (`d_nombre`,`d_apellidoPat`,`d_apellidoMat`,`d_nacionalidad`,`d_fnacimiento`,`d_educacion`) VALUES (%s,%s,%s,%s,%s,%s)'
            vals = (d_nombre,d_apellidoPat,d_apellidoMat,d_nacionalidad,d_fnacimiento,d_educacion)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_director(self,id_director):
        try:
            sql = 'SELECT * FROM directores WHERE id_director = %s'
            vals = (id_director,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_a_director_nacionalidad(self,d_nacionalidad):
        try:
            sql = 'SELECT * FROM directores WHERE d_nacionalidad = %s'
            vals = (d_nacionalidad,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err


    def read_all_director(self):
        try:
            sql = 'SELECT * FROM directores'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def update_director(self,fields,vals):
        try:
            sql = 'UPDATE directores SET '+','.join(fields)+'WHERE id_director = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_director(self, id_genero):
        try:
            sql = 'DELETE FROM directores WHERE id_director = %s'
            vals = (id_genero,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *********************
    * actores metodos*
    *********************
    """
    def create_actor(self,a_nombre,a_apellidoPat,a_apellidoMat,a_nacionalidad,a_fnacimiento):
        try:
            sql = 'INSERT INTO actores (`a_nombre`,`a_apellidoPat`,`a_apellidoMat`,`a_nacionalidad`,`a_fnacimiento`) VALUES (%s,%s,%s,%s,%s)'
            vals = (a_nombre,a_apellidoPat,a_apellidoMat,a_nacionalidad,a_fnacimiento)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_actor(self,id_director):
        try:
            sql = 'SELECT * FROM actores WHERE id_actor = %s'
            vals = (id_director,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_a_actor_nacionalidad(self,d_nacionalidad):
        try:
            sql = 'SELECT * FROM actores WHERE a_nacionalidad = %s'
            vals = (d_nacionalidad,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err


    def read_all_actor(self):
        try:
            sql = 'SELECT * FROM actores'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def update_actor(self,fields,vals):
        try:
            sql = 'UPDATE actores SET '+','.join(fields)+'WHERE id_actor = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_actor(self, id_actor):
        try:
            sql = 'DELETE FROM actores WHERE id_actor = %s'
            vals = (id_actor,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    """
    *********************
    * peliculas metodos*
    *********************
    """
    def create_movie(self,p_titulo,p_idioma,p_subtitulos,p_año):
        try:
            sql = 'INSERT INTO peliculas (`p_titulo`,`p_idioma`,`p_subtitulos`,`p_año`) VALUES (%s,%s,%s,%s)'
            vals = (p_titulo,p_idioma,p_subtitulos,p_año)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_movie(self,id_pelicula):
        try:
            sql = 'SELECT * FROM peliculas WHERE id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_a_movies_year(self,p_año):
        try:
            sql = 'SELECT * FROM peliculas WHERE p_año = %s'
            vals = (p_año,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err


    def read_all_movies(self):
        try:
            sql = 'SELECT * FROM peliculas'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def update_movie(self,fields,vals):
        try:
            sql = 'UPDATE peliculas SET '+','.join(fields)+'WHERE id_pelicula = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_movie(self, id_actor):
        try:
            sql = 'DELETE FROM peliculas WHERE id_pelicula = %s'
            vals = (id_actor,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ***********************
    * actor_movies metodos*
    ***********************
    """
    def create_ac_mov(self,ap_id_actor,ap_id_pelicula):
        try:
            sql = 'INSERT INTO actorpeliculas (`ap_id_actor`,`ap_id_pelicula`) VALUES (%s,%s)'
            vals = (ap_id_actor,ap_id_pelicula)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err


    def read_a_ac_mov(self, ap_id_actor):
        try:
            sql = 'SELECT peliculas.id_pelicula ,peliculas.p_titulo, peliculas.p_idioma, peliculas.p_subtitulos, peliculas.p_año from actorpeliculas join peliculas on peliculas.id_pelicula = actorpeliculas.ap_id_pelicula where ap_id_actor = %s'
            vals = (ap_id_actor,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_a_mov_ac(self, ap_id_pelicula):
        try:
            sql = 'SELECT actores.id_actor,actores.a_nombre, actores.a_apellidoPat, actores.a_apellidoMat , actores.a_nacionalidad, actores.a_fnacimiento from actorpeliculas join actores on actores.id_actor = actorpeliculas.ap_id_actor where ap_id_pelicula = %s'
            vals = (ap_id_pelicula,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_all_ac_mov(self):
        try:
            sql = 'select peliculas.p_titulo, actores.a_nombre from peliculas join actorpeliculas on  actorpeliculas.ap_id_pelicula = peliculas.id_pelicula join actores on actores.id_actor = actorpeliculas.ap_id_actor'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def update_ac_mov(self,fields,vals):
        try:
            sql = 'UPDATE actorpeliculas SET '+','.join(fields)+'WHERE ap_id_actor = %s AND ap_id_pelicula  = %s '
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_ac_mov(self, ap_id_actor,ap_id_pelicula):
        try:
            sql = 'DELETE FROM actorpeliculas WHERE ap_id_actor = %s AND ap_id_pelicula  = %s '
            vals = (ap_id_actor,ap_id_pelicula,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ***
    * Detalles
    **
    """

    def create_detalles_pelicula(self, dp_id_pelicula, dp_id_director, descripcion,dp_duracion):
        try:
            sql = 'INSERT INTO detalles_peliculas(`dp_id_pelicula`, `dp_id_director`, `descripcion`,`dp_duracion`) VALUES ( %s, %s, %s, %s)'
            vals = ( dp_id_pelicula, dp_id_director, descripcion,dp_duracion)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return err

    def read_detalles_pelicula(self, dp_id_pelicula):
        try: 
            sql ='SELECT detalles_peliculas.dp_id_pelicula, peliculas.p_titulo, directores.d_nombre , detalles_peliculas.descripcion, detalles_peliculas.dp_duracion FROM peliculas JOIN detalles_peliculas ON peliculas.id_pelicula =  detalles_peliculas.dp_id_pelicula JOIN directores ON detalles_peliculas.dp_id_director = directores.id_director WHERE dp_id_pelicula = %s'
            vals=(dp_id_pelicula, )
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err


    def read_all_detalles_pelicula(self):
        try: 
            sql ='SELECT detalles_peliculas.dp_id_pelicula, peliculas.p_titulo, directores.d_nombre , detalles_peliculas.descripcion, detalles_peliculas.dp_duracion FROM peliculas JOIN detalles_peliculas ON peliculas.id_pelicula =  detalles_peliculas.dp_id_pelicula JOIN directores ON detalles_peliculas.dp_id_director = directores.id_director'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    
    def update_detalles_pelicula(self, fields, vals):
        try:
            sql = 'UPDATE detalles_peliculas SET '+','.join(fields)+'WHERE id_dp = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delate_detalles_prlicula(self, dp_id_pelicula):
        try:
            sql = 'DELETE FROM detalles_peliculas WHERE dp_id_pelicula = %s '
            vals = (dp_id_pelicula, )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    def read_a_dir_mov(self, id_director):
        try:
            sql = 'SELECT peliculas.id_pelicula ,peliculas.p_titulo, peliculas.p_idioma, peliculas.p_subtitulos, peliculas.p_año from detalles_peliculas join peliculas on peliculas.id_pelicula = detalles_peliculas.dp_id_pelicula where dp_id_director = %s'
            vals = (id_director,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err