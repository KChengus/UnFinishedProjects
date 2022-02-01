import java.util.Scanner;
public class TicTacToe {
    int[][] board = {
        {0, 0, 0},
        {0, 0, 0},
        {0, 0, 0}
    };
    
    public boolean checkWon(boolean isP1Turn, int coords) {

        int symbol = playerSymbol(isP1Turn);
        int y = coords % 10;
        int x = coords / 10;
        // horizontal
        boolean hasWon = true;

        for (int col : board[y]) {
            if (col != symbol) {
                hasWon = false;
                break;
            }
        }
        if (hasWon) {
            return true;
        } else {
            hasWon = true;    
        }
        
        // vertical
        for (int i = 0; i < board.length; i++) {
            if (board[i][x] != symbol) {
                hasWon = false;
                break;
            }
        }

        if (hasWon) {
            return true;
        } else {
            hasWon = true;    
        }
        // 00 02 20 22 11

        if (coords == 00 || coords == 22 || coords == 11) {
            // check diagonal from top left to botton right
            for (int i = 0; i < board.length; i++) {
                if (board[i][i] != symbol) {
                    hasWon = false;
                    break;
                }
            }
        } 
        
        if (hasWon) {
            return true;
        } else {
            hasWon = true;    
        }
        if (coords == 02 || coords == 20 || coords == 11) {
            for (int i = 0; i < board.length; i++) {
                if (board[board.length - 1 - i][i] != symbol) {
                    hasWon = false;
                    break;
                }
            }
        }
        return hasWon;
    }

    public int playerSymbol(boolean isP1Turn) {
        return isP1Turn ? 1 : -1;
    }   

    public void place(int coords, boolean isP1Turn) {
        int y = coords % 10;
        int x = coords / 10;
        if (board[y][x] != 0) {
            return;
        }
        // able to place
        board[y][x] = playerSymbol(isP1Turn); 
    }

    public void printBoard() {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }

    public void run() {
        boolean isP1Turn = true; 
        Scanner scan = new Scanner(System.in);
        int coords;
        do {
            isP1Turn = !isP1Turn;
            System.out.printf("%s's turn:\n", isP1Turn ? "Player1" : "Player2");

            coords = scan.nextInt();
            place(coords, isP1Turn);
            isP1Turn = !isP1Turn;
        }
        while (!checkWon(isP1Turn, coords));
        scan.close();
    }

    public static void main(String[] args) {
        new TicTacToe().run();
    }   
}