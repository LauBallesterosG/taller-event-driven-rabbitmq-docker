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

        conn, err := amqp.Dial(rabbitURL)
        if err != nil {
                log.Fatalf("Error al conectar con RabbitMQ: %v", err)
        }
        defer conn.Close()

        ch, err := conn.Channel()
        if err != nil {
                log.Fatalf("Error al crear el canal: %v", err)
        }

        // Publicar mediante el exchange
        var mensaje string
        mensaje = "Mensaje enviado desde productor go"

        err = ch.Publish(
                "delta",
                "",
                false,
                false,
                amqp.Publishing{
                        ContentType:  "text/plain",
                        Body:         []byte(mensaje),
                        DeliveryMode: amqp.Persistent,
                },
        )
        if err != nil {
                log.Fatalf("Error al enviar el mensaje: %v", err)
        }
        fmt.Printf("Mensaje enviado: %s\n", mensaje)
}