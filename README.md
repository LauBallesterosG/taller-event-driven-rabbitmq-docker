# Taller: Arquitectura Event-Driven Multilenguaje con RabbitMQ y Docker

## Integrantes

- **Integrante 1:** Nikolas Pedrozo Mieles
- **Integrante 2:** Laura Natalia Ballesteros Gualdrón 
- **Integrante 3:** Juan Gabriel Garcia Jimenez

## Descripción del proyecto

Este proyecto consiste en la implementación de una arquitectura orientada a eventos (*Event-Driven*) utilizando RabbitMQ como intermediario de mensajería y Docker para la ejecución de los servicios en contenedores.

El sistema permite la comunicación asíncrona entre productores y consumidores mediante un broker RabbitMQ. El taller busca comprender el funcionamiento de este tipo de arquitectura y analizar las diferencias entre una infraestructura centralizada y una distribuida.

## Objetivos

- Comprender y aplicar la arquitectura Event-Driven en un entorno distribuido.
- Implementar un sistema de mensajería utilizando RabbitMQ y AMQP.
- Desplegar servicios distribuidos mediante contenedores Docker.
- Analizar las ventajas y limitaciones de las arquitecturas centralizadas y distribuidas.

## Escenarios de distribución

### 1. Escenario centralizado

Los productores, consumidores y el broker RabbitMQ se ejecutan en un único nodo.

### 2. Escenario distribuido en dos nodos

- **Nodo 1:** productores y consumidores.
- **Nodo 2:** broker RabbitMQ.

Cada nodo cuenta con su propio archivo docker-compose.yml.

### 3. Escenario distribuido en tres nodos

- **Nodo 1:** un conjunto de productores y consumidores.
- **Nodo 2:** otro conjunto de productores y consumidores.
- **Nodo 3:** broker RabbitMQ.

Cada nodo cuenta con su propio archivo docker-compose.yml.

## Tecnologías utilizadas

- **RabbitMQ:** gestión de la mensajería entre productores y consumidores.
- **Docker:** ejecución de los servicios en contenedores.
- **Docker Compose:** configuración y despliegue de los servicios.
- **Lenguajes de programación:** Python, Java y Go

## Entregables de código

- Código fuente de los productores y consumidores.
- Archivos Dockerfile`de los servicios.
- Archivos docker-compose.yml correspondientes a los tres escenarios.
