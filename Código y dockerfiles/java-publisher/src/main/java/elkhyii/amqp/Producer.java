package elkhyii.amqp;

import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.Channel;

import java.nio.charset.StandardCharsets;
import java.util.Scanner;

public class Producer {

    private static final String QUEUE_NAME = "cola_java";
    private static final String EXCH_NAME = "cambio";

    public static void main(String[] args) throws Exception {
        ConnectionFactory factory = new ConnectionFactory();

        factory.setHost("10.6.101.162");
        factory.setUsername("guest");
        factory.setPassword("guest");

        try (Connection connection = factory.newConnection(); Channel channel = connection.createChannel()) {

            channel.exchangeDeclare(EXCH_NAME, "fanout", true);

            String message = "JAVA4EVA";

                channel.basicPublish(
                        EXCH_NAME,
                        "",
                        null,
                        message.getBytes(StandardCharsets.UTF_8)
                );

                System.out.println("Enviado: " + message);

        }
    }
}