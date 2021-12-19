* Iniciar pipenv
* Migrar django para generar la db
* Los archivos de configuracion de django se encuentran en la carpeta core.
* La aplicación al iniciar cuenta con dos opciones principales, q fueron separadas en dos aplicaciones. departamentos y empleados.
* Cada app tiene sus respectivas templates, models, views y urls.
* A su vez una vez ingresado a departamentos se pueden tanto listar como crear nuevos departamentos, y en empleados se puede listar y crear, jefes o empleados.
* Hay otra aplicacion que es la pagina de inicio que redirige a departamento o empleados.
* Entrar a cualquiera de ellas y primero crear algunos itemos, tanto en departamentos como empleados.
* Luego entrar a listar para ver el listado completo de los items ingresados, o para buscar algun item en particular.
* Los estilos estan guardados en la carpeta static en la aplicacion 'inicio'



*clonar
*pipenv shell
*createsuperuser