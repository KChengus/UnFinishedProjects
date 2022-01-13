public class Calc {
    Expressions expressions = new Expressions();

    public int getAnswer() {
        String[] splitExp = expressions.exp.split(" ");
        String op = splitExp[1];

        switch (op) {
        case ("+"):
            return Integer.parseInt(splitExp[0]) + Integer.parseInt(splitExp[2]);
        case ("-"):
            return Integer.parseInt(splitExp[0]) - Integer.parseInt(splitExp[2]);
        case ("*"):
            return Integer.parseInt(splitExp[0]) * Integer.parseInt(splitExp[2]);
        case ("/"):
            
            return Integer.parseInt(splitExp[0]) / Integer.parseInt(splitExp[2]);
        default:
            // TODO find better error handling
            return Integer.MAX_VALUE;
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