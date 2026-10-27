package main

import (
        "fmt"
        "log"
        "os"

        amqp "github.com/rabbitmq/amqp091-go"
)

func main() {
        rabbitURL := os.Getenv("RABBITMQ_URL")

        if rabbitURL == "" {
                rabbitURL = "amqp://guest:guest@10.6.101.162:5672/"
        }

        // Conectar con RabbitMQ.
        conn, err := amqp.Dial(rabbitURL)
        if err != nil {
                log.Fatalf("Error al conectar con RabbitMQ: %v", err)
        }
        defer conn.Close()

        // Crear un canal de comunicación.
        ch, err := conn.Channel()
        if err != nil {
                log.Fatalf("Error al crear el canal: %v", err)
        }
        defer ch.Close()

        // Declarar el exchange de tipo direct.
        err = ch.ExchangeDeclare(
                "delta",
                "fanout",
                true,
                false,
                false,
                false,
                nil,
        )
        if err != nil {
                log.Fatalf("Error al declarar el exchange: %v", err)
        }

        // Declarar la cola de eventos.
        queue, err := ch.QueueDeclare(
                "cola_go",
                true,
                false,
                false,
                false,
                nil,
        )
        if err != nil {
                log.Fatalf("Error al declarar la cola: %v", err)
        }

        // Asociar la cola con el exchange.
        err = ch.QueueBind(
                queue.Name,
                "",
                "delta",
                false,
                nil,
        )
        if err != nil {
                log.Fatalf("Error al asociar la cola al exchange: %v", err)
        }

        // Registrar el consumidor para recibir mensajes.
        mensajes, err := ch.Consume(
                queue.Name,
                "",
                false,
                false,
                false,
                false,
                nil,
        )
        if err != nil {
                log.Fatalf("Error al registrar el consumidor: %v", err)
        }

        fmt.Println("Consumidor Go esperando mensajes...")

        for mensaje := range mensajes {
                fmt.Printf("Evento recibido: %s\n", string(mensaje.Body))

                if err := mensaje.Ack(false); err != nil {
                        log.Printf("Error al connfirmar el mensaje: %v", err)
                }
        }
}