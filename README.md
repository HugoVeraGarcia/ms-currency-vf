# ms currency exchange


 ## Objetivo
Esta es una api, para simular el intercambio de monedas:


## Notas

### Monedas:
 * USD
 * EUR
 * JPY
 * GBP
 * CHF
 * AUD
 * CAD
 * NZD

### Tecnologías del proyecto:

- [Python3]
- [Django3]
- [Django rest framework]
- [Postgresql]
- [Docker]

Pasos para levantar proyecto:

1. Crear entorno virtual
```
python -m venv .venv
```

2. Activar entorno virtual
```
windows:   .venv\Scripts.\activate
```

3. Instalar librerías
```
pip install -r requirements.txt
```

4. Iniciar la aplicación
```
python manage.py runserver
```

5. Ejecutar la población de la BD con la api:
```
http://127.0.0.1:8000/api/v1/setup/
```




