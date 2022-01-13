import java.util.InputMismatchException;

public class Calc {
    Expressions expressions = new Expressions();

    public int getAnswer() {
        String[] splitExp = expressions.exp.split(" ");
        String op = splitExp[1];
        op = "k";
        switch (op) {
        case ("+"):
            return Integer.parseInt(splitExp[0]) + Integer.parseInt(splitExp[2]);
        case ("-"):
            return Integer.parseInt(splitExp[0]) - Integer.parseInt(splitExp[2]);
        case ("*"):
            return Integer.parseInt(splitExp[0]) * Integer.parseInt(splitExp[2]);

        default:
            if (!op.equals("/") ) {
                throw new InputMismatchException();
            }
            return Integer.parseInt(splitExp[0]) / Integer.parseInt(splitExp[2]);
        }

    }


    // public static void main(String[] args) {
    //     Calc calc = new Calc();
    //     for (int i = 0; i < 10; i++) {
    //         calc.expressions.generateRandomExpression();
    //         System.out.println(calc.expressions.exp + " " + calc.getAnswer());
    //     }
    // }
}