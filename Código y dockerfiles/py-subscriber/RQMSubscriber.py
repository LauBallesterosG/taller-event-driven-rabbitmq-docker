import pika as pk

#Menú inicial
print("*******************************")
print("* Consumer AMQP para rabbitMQ *")
print("*  2230083 - UIS - IngSoft 3  *")
print("*******************************")

# Se pide la dirección del host a conectar
hostDir = '10.6.101.162'

# Se generan los parámetros de conexión para el host con la dirección que le pases
connPar = pk.ConnectionParameters(host= hostDir,
                              port= 5672,
                              credentials= pk.PlainCredentials('guest', 'guest'))

# Crea un objeto de tipo 'connection' con los parámetros dados
print('intentando conectarse a ' + hostDir + ' como guest:guest...')
connection = pk.BlockingConnection(connPar)

# Se crea un nuevo canal de conexión
channel = connection.channel()


######################################
######################################
####                              ####
####  INICIO DEL LOOP FUNCIONAL   ####
####                              ####
######################################
######################################

############
# Exchange #
############
# Se le pide un nombre de exchange
exchangeName = 'cambio'

# Se declara un exchange de tipo fanout
channel.exchange_declare(exchange=exchangeName,
                     exchange_type='fanout',
                     durable=True)

########
# Cola #
########
# Se le pide un nombre de cola
queueName = 'colaPython'+exchangeName

# Se declara una cola en el canal
channel.queue_declare(queue=queueName,
                  durable=True)

# Se ata el exchange a la cola con un bind
channel.queue_bind(exchange=exchangeName,
               queue=queueName)

# Se define la función de callback
def callbackSazo(ch, method, properties, body):
        print('')
        print('Recibido de '+ exchangeName +':')
        print(body)

#Se define de dónde se va a escuchar y cómo
print('')
channel.basic_consume(queue=queueName,
                  auto_ack=True,
                  on_message_callback=callbackSazo)

# Finalmente, se empieza a escuchar
print('')
print('Esperando mensajes...')
channel.start_consuming()