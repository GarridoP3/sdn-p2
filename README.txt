Este script retorna un listado de las organizaciones a las que el usuario (API Key) tiene privilegios.
Hace una verificación de errores con la funciión raise_for_status()
Imprime en pantalla las organizaciones

La variable KEY define la API Key de mi organización

La respuesta está definida de la forma 'cliente.scope.operación'. Donde el 'cliente' es el dashboard de meraki, en este caso se el 'scope' son las organizaciones y finalmente la 'operación' utilizada es GetOrganizations

Referencias: 	https://pypi.org/project/meraki/
				https://developer.cisco.com/meraki/api-v1/get-organizations/