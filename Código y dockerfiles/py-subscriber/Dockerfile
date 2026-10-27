# From <Nombre imagen>
# Toma una imagen pre-existente como base.
# En este caso, se requiere python.
FROM python:3.15-bookworm

# ADD <Nombre archivo> <Nombre directorio>
# Copia un archivo del directorio especificado al contenedor.
# En este caso, el programa en sí
ADD RMQSubscriber.py .

# RUN pip install <nombre paquete a instalar>
# Le dice a python que instale la(s) dependencia(s) necesaria(s)
# En este caso, se requiere python.
RUN pip install pika

ENV PYTHONUNBUFFERED=1

# ["python", "./<nombrearchivo>"]
# Le dice a la línea de comandos que corra el archivo
CMD ["python", "./RMQSubscriber.py"]