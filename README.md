# Software de Inventario
El proyecto "Software Inventory" es una aplicación web que está comprendido en la recoleccion de datos de inventario. 
# Integrantes
##### 1)YAMIL YONDER LLAMPI HANCCO
##### 2)ANGELA SOLANGE SUCSO CHOQUE
##### 3)ERICK JESUS TORRES QUISPE
##### 4)EVELYN LIZBETH CUSI HANCCO
##### 5)FREDDY LEONEL HUMPIRI VALDIVIA
# Instalación

##### - Clonar o descargar el proyecto del repositorio

`git clone https://github.com/YLlampi/software-inventory.git`

##### - Crear un entorno virtual para posteriormente instalar las librerias del proyecto

- `python3 -m venv venv` (Windows)
-  `virtualenv venv -ppython3` (Linux)

##### - Instalar el complemento de [weasyprint](https://weasyprint.org/ "weasyprint")

- Si estas usando Windows debe descargar el complemento de [GTK3 installer](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases "GTK3 installer"). En algunas ocaciones se debe colocar en las variables de entorno como primera para que funcione y se debe reiniciar el computador.
- Si estas usando Linux debes instalar las [librerias](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#linux "librerias") correspondientes a la distribución que tenga instalado en su computador.

##### - Activar el entorno virtual de nuestro proyecto

- `cd venv\Scripts\activate.bat` (Windows)
- `source venv/bin/active` (Linux)

##### - Instalar todas las librerias del proyecto

- `pip install -r requirements.txt`

##### - Crear la base de datos con las migraciones y el superuser para iniciar sesión.

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`

# Pipeline de CI/CD
## a) Construcción Automática:

Para este proyecto, se utilizará un pipeline de Jenkins que se encargará de la construcción automática.

![image](https://github.com/YLlampi/software-inventory/blob/main/img/jk.jpeg)

![image](https://github.com/YLlampi/software-inventory/blob/main/img/jk-2.jpeg)

## b) Análisis Estático:
### Requisitos
##### - Sonarqube Server
##### - sonar-project.properties




Al inicializar SonarQube nos arroja scripts de configuración y de permisos.

![image](https://github.com/YLlampi/software-inventory/blob/main/img/Sonar-permisos.jpeg)

Una vez ejecutado.
![image](https://github.com/YLlampi/software-inventory/blob/main/img/Sonar-ejecucion.jpeg)

Obtendremos el reporte.
![image](https://github.com/YLlampi/software-inventory/blob/main/img/Sonar-reporte.jpeg)
![image](https://github.com/YLlampi/software-inventory/blob/main/img/Sonar-success.jpeg)

## c) Pruebas Unitarias:
En las pruebas unitarias se verifica partes del código para verificar su correcto funcionamiento.

![image](https://github.com/YLlampi/software-inventory/blob/main/img/Unit-test.jpeg)




## d) Pruebas de Seguridad:
### Requisitos

##### - OWASP ZAP
##### - URL: https://localhost:8000/

Usamos OWASP ZAP para realizar el ataque
![image](https://github.com/YLlampi/software-inventory/blob/main/img/OWASP%20ZAP-1.jpeg)

Una vez terminado el ataque
![image](https://github.com/YLlampi/software-inventory/blob/main/img/OWASP%20ZAP-2.jpeg)

Generamos el reporte

![image](https://github.com/YLlampi/software-inventory/blob/main/img/OWASP%20ZAP-4.jpeg)

Y como resultado del reporte obtenemos.
![image](https://github.com/YLlampi/software-inventory/blob/main/img/OZ_1.jpeg)
![image](https://github.com/YLlampi/software-inventory/blob/main/img/OZ_2.jpeg)
![image](https://github.com/YLlampi/software-inventory/blob/main/img/OZ_3.jpeg)



## f)Gestión de Issues: 

Para la gestión de issues se uso la herramienta Trello.

![image](https://github.com/YLlampi/software-inventory/blob/main/img/Trello.png)

[URL Trello]([https://weasyprint.org/ "weasyprint"](https://trello.com/b/IpZx5E1E/proyecto-final-isii))
