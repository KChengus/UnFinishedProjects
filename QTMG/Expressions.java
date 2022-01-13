import java.util.Random;
public class Expressions {
    char[] operations = {'+', '-', '*', '/'};
    Random rand = new Random();
    int lowerLimit = 1;
    int upperLimit = 100;
    String exp = "1 + 1";

    public int generateNum() {
        rand.setSeed(rand.nextInt(100000));
        int num = rand.nextInt(upperLimit - lowerLimit) + lowerLimit;

        // easier calculations for numbers 100 or above
        if (num >= 100) {
            num = num / 10 * 10;
        }
        return num;
    }

    public void generateRandomExpression() {
        // generate random expression
        // start with a simple format
        // a operation b

        char op = operations[rand.nextInt(operations.length)];
        
        int a = generateNum();
        int b = generateNum();
        exp = a + " " + op + " " + b;
    }





}