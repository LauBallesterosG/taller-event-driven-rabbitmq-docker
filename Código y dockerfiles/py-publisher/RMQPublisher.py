import pika as pk

#Menú inicial
print("********************************")
print("* Publisher AMQP para rabbitMQ *")
print("*  2230083 - UIS - IngSoft 3   *")
print("********************************")

####################
# Conexión inicial #
####################

# Se pide la dirección del host a conectar
hostDir = '10.6.101.162'

# Usuario por defecto para mi broker, toca cambiar después
uName = 'guest'
pWord = 'guest'
logInfo = pk.PlainCredentials(uName, pWord)

# Se formatean los parámetros de conexión
connPar = pk.ConnectionParameters(
                                  host= hostDir,
                                  port= 5672,
                                  credentials= logInfo
                                  )

# Se crea una conexión y se asigna al objeto connection
print('')
print('Intentando conectarse a' + hostDir + ' como ' + uName + ':' + pWord + '...')
connection = pk.BlockingConnection(connPar)

# Se crea un nuevo canal de conexión
channel = connection.channel()

###################
###################
####           ####
####  Tareas   ####
####           ####
###################
###################

# 4 consumidores se van suscribir a 2 exchanges: eventos_exchange y cambio
# Se desea que:
# Py1 mande a todos,
# Py2 mande a ninguno,
# Java mande a cambio,
# Go mande a delta


#Este va a mandar a una cola, que va a variar dependiendo de la versión de la imagen
exName = 'cambio'

# Se declara un exchange de tipo fanout
channel.exchange_declare(exchange=exName,
                     exchange_type='fanout',
                     durable=True)

print('')
channel.basic_publish(exchange=exName,
                      routing_key='',
                      body='mensaje enviado desde productor python ('+exName+')')
print('Mensaje enviado con éxito a ' + exName)


#################################################################################
#Ahora para delta
#################################################################################
exName='delta'

# Se declara un exchange de tipo fanout
channel.exchange_declare(exchange=exName,
                     exchange_type='fanout',
                     durable=True)

print('')
channel.basic_publish(exchange=exName,
                      routing_key='',
                      body='mensaje enviado desde productor python ('+exName+')')
print('Mensaje enviado con éxito a ' + exName)