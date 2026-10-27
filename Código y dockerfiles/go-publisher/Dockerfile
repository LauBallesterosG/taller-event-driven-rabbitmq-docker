#Se toma la imagen de golang como base
FROM golang:1.27.3-alpine AS builder

#Se establece el directorio de trabajo
WORKDIR /app

#Se copian modulos y dependencias al directorio
COPY go.mod go.sum ./
RUN go mod download

#Se copia el código fuente
COPY ./main.go .

#Se construye usando go
RUN  go build -o pub-go ./
# CGO_ENABLED=0 GOOS=linux (?)

#Ahora se toma alpine
FROM alpine:3.21

#Se establece el directorio de trabajo
WORKDIR /app

#Se copia únicamente el ejecutable para ser más ligero
COPY --from=builder /app/pub-go .

#Y se corre
CMD ["./pub-go"]