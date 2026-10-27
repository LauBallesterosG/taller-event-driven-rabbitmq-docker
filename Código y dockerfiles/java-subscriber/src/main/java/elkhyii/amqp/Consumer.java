package elkhyii.amqp;

import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.DeliverCallback;

import java.nio.charset.StandardCharsets;

public class Consumer {

    private static final String QUEUE_NAME = "cola_java";
    private static final String EXCH_NAME = "cambio";

    public static void main(String[] args) throws Exception {
        ConnectionFactory factory = new ConnectionFactory();

        factory.setHost("10.6.101.162");
        factory.setUsername("guest");
        factory.setPassword("guest");

        Connection connection = factory.newConnection();
        Channel channel = connection.createChannel();

        channel.exchangeDeclare(EXCH_NAME, "fanout", true);

        channel.queueDeclare(
                QUEUE_NAME,
                true,
                false,
                false,
                null
        );

        channel.queueBind(QUEUE_NAME, EXCH_NAME, "");

        DeliverCallback callback = (consumerTag, delivery) -> {
            String message = new String(
                    delivery.getBody(),
                    StandardCharsets.UTF_8
            );

            System.out.println("Recibido: " + message);
        };

        channel.basicConsume(
                QUEUE_NAME,
                true,
                callback,
                consumerTag -> {
                }
        );

        System.out.println("Esperando mensajes...");
    }
}