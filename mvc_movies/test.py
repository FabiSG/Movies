# from model.model import Model

# m = Model()

# data = m.read_a_dir_mov(1)
# print(data)
# m.create_gen('Accion')
# m.create_gen('Accion')
# m.create_gen('Romance')


# fields = ('genero = %s',)
# vals =('Comedia',1)
# m.update_genero(fields,vals)
# data= m.read_all_generos()
# print('Generos')
# print(data)

# m.create_director('Pedro','Matadamas','Marin','Mexicano','1995-05-26','Ingeniero')
# m.create_director('Fabiola','Sierra','','Mexicano','1995-12-28','Ingeniero')

# m.delete_director(3)
# data = m.read_all_director()
# print('Directores')
# print(data)

# m.create_actor('Levi','Alvarez','Quijano','Mexicano','1995-10-22')
# m.create_actor('Alondra','Arredondo','Martinez','Mexicano','1996-05-08')
# data = m.read_all_actor()
# print('Actores')
# print(data)


# m.create_movie('Cloud Atlas','Español','Ingles','2017')
# m.create_movie('Batman','Ingles','Español','2010')
# m.create_movie('Avatar','Español',None,'2007')
# data = m.read_all_movies()
# print('pelicula')
# print(data)



# m.create_ac_mov(2,1)
# m.create_ac_mov(1,2)
# m.create_ac_mov(2,3)
# data = m.read_all_ac_mov()
# print(data)

# data = m.read_a_mov_ac(1)
# print(data)

# data = m.read_all_ac_mov()
# print(data)

# m.create_detalles_pelicula(1, 2 ,'Una historia de algo','120 min')
# data = m.read_detalles_pelicula(1)
# print(data)


from controller.controller import Controller

c = Controller()

c.start()