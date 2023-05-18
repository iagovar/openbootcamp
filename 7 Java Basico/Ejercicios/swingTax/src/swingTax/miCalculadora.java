package swingTax;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class miCalculadora {
    private JPanel mainTaxPanel;
    private JTextPane pricePane;
    private JTextPane totalPane;
    private JTextPane taxPane;
    private JButton buttonCalculate;

    public miCalculadora() {
        // El event handler en Swing se mete en el constructor, el codigo
        // boilerplate se escribe automáticamente desde el menú "create event" del
        // gestor gráfico.
        buttonCalculate.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                // Tomamos los textos y los convertimos a double
                String textoPrecio = pricePane.getText();
                double numeroPrecio = Double.parseDouble(textoPrecio);

                String textoVAT = taxPane.getText();
                double numeroVAT = Double.parseDouble(textoVAT);

                // Calculamos el resultado y lo metemos en el campo de resultado
                double resultado = numeroPrecio * (1 + (numeroVAT / 100));
                totalPane.setText(String.valueOf(resultado));
            }
        });
    }

    public static void main(String args[]) {
        JFrame frame = new JFrame("SwingTax");
        frame.setSize(400, 400);

        miCalculadora calculadora = new miCalculadora();
        frame.setContentPane(calculadora.mainTaxPanel);
        frame.setVisible(true);

    }
}
