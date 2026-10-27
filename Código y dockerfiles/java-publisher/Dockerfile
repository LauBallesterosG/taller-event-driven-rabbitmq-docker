FROM maven:3.9-eclipse-temurin-21

WORKDIR /app

# Copiar la configuración de Maven
COPY pom.xml .

# Descargar las dependencias
RUN mvn dependency:go-offline

# Copiar el código fuente
COPY src ./src

# Compilar el proyecto
RUN mvn package

# Ejecutar la aplicación
CMD ["mvn", "exec:java", "-Dexec.mainClass=elkhyii.amqp.Producer"]