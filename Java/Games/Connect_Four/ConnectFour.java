/**
 * @author Jared Scott ☯ 
 * 
 * Connect Four
 * 
 */

import java.util.ArrayList;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Rectangle;
import javafx.scene.text.Font;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class ConnectFour extends Application {
    //Holds the positions of the circles in a 2d array each array is a column of the game 
    ArrayList<ArrayList<ConnectFourCircle>> grid = new ArrayList<ArrayList<ConnectFourCircle>>();
    static int player = 1; 
    static Text playerLab = new Text("Player " + player + "'s turn: Red");
    static Text victoryLab = new Text("");
    static boolean victory = false;
    static int validMoves = 0;
    
    
    public static void setPlayerText() {
        if (player == 1) {
            playerLab.setText("Player " + player + "'s turn: Red");
        }
        else {
            playerLab.setText("Player " + player + "'s turn: Yellow");
        }
    }
    
    
    public static void changePlayer() {
        if (player == 1) {
            player = 2;
        }
        else {
            player = 1;
        }
        setPlayerText();
    }
    
    public boolean checkVert() {
        //Array containing the winning circles
        ArrayList<ConnectFourCircle> victoryList = new ArrayList<ConnectFourCircle>();
        int curCount = 0;
        for (ArrayList<ConnectFourCircle> col : grid) {
            //Pulling each column out of the grid 
            if (col.get(0).curColor != Color.WHITE) {
                Color curColor = col.get(0).curColor;
                //Crawling up the column;
                for (ConnectFourCircle circle : col) {
                    if (circle.curColor == curColor && circle.curColor != Color.WHITE) {
                        victoryList.add(circle);
                        curCount += 1;
                    }
                    else if (circle.curColor != Color.WHITE) {
                        victoryList.clear();
                        victoryList.add(circle);
                        curColor = circle.curColor;
                        curCount = 1;
                    }
                    if (curCount == 4) {
                        for (ConnectFourCircle circ : victoryList) {
                            circ.setFill(Color.BLUE);
                        }
                        return true;
                    }
                }
                curCount = 0;
                victoryList.clear();
            }
        }
        return false;
    }
    
    public boolean checkHor() {
        ArrayList<ConnectFourCircle> rowList = new ArrayList<ConnectFourCircle>();
        ArrayList<ConnectFourCircle> victoryList = new ArrayList<ConnectFourCircle>();
        int curCount = 0;
        for (int row = 0; row < 6; row++) {
            for (int col = 0; col < 7; col++) {
                rowList.add(grid.get(col).get(row));
            }
            Color curColor = rowList.get(0).curColor;
            //Crawling through the row
            for (ConnectFourCircle circle : rowList) {
                if (circle.curColor == curColor && circle.curColor != Color.WHITE) {
                    victoryList.add(circle);
                    curCount += 1;
                }
                else {
                    victoryList.clear();
                    victoryList.add(circle);
                    curColor = circle.curColor;
                    curCount = 1;
                }
                if (curCount == 4) {
                    for (ConnectFourCircle circ : victoryList) {
                        circ.setFill(Color.BLUE);
                    }
                    return true;
                }
            }
            curCount = 0;
            victoryList.clear();
            rowList.clear();
        }
        return false;
    }
    
    public boolean checkDiagRight() {
            int curCount = 0;
            Color curColor;
            ArrayList<ConnectFourCircle> diag = new ArrayList<ConnectFourCircle>();//Holds the circles that are within that diagonal
            for (int row = 0; row < 3; row++) {
                for (int col = 0; col < 4; col++) {
                    //Grabbing diagonal
                    diag.add(grid.get(col).get(row));
                    diag.add(grid.get(col+1).get(row+1));
                    diag.add(grid.get(col+2).get(row+2));
                    diag.add(grid.get(col+3).get(row+3));
                    curColor = diag.get(0).curColor;
                    for (ConnectFourCircle circle: diag) {
                        if (circle.curColor == curColor && circle.curColor != Color.WHITE) {
                            curCount += 1;
                        }
                        else {
                            curCount = 0;
                            break; //All 4 circles must be the same color as the "root" of the diagonal
                        }
                        if (curCount == 4) {
                            for(ConnectFourCircle circle1 : diag) {
                                circle1.setFill(Color.BLUE);
                            }
                            return true;
                        }
                    }
                    diag.clear();
                }
                diag.clear();

            }
            return false;

        }
    
    public boolean checkDiagLeft() {
        int curCount = 0;
        Color curColor;
        ArrayList<ConnectFourCircle> diag = new ArrayList<ConnectFourCircle>();//Holds the circles that are within that diagonal
        for (int row = 0; row < 3; row++) {
            for (int col = 3; col < 7; col++) {
                //Grabbing diagonal
                diag.add(grid.get(col).get(row));
                diag.add(grid.get(col-1).get(row+1));
                diag.add(grid.get(col-2).get(row+2));
                diag.add(grid.get(col-3).get(row+3));
                curColor = diag.get(0).curColor;
                for (ConnectFourCircle circle: diag) {
                    if (circle.curColor == curColor && circle.curColor != Color.WHITE) {
                        curCount += 1;
                    }
                    else {
                        curCount = 0;
                        break; //All 4 circles must be the same color as the "root" of the diagonal
                    }
                    if (curCount == 4) {
                        for(ConnectFourCircle circle1 : diag) {
                            circle1.setFill(Color.BLUE);
                        }
                        return true;
                    }
                    
                }
                diag.clear();
            }
            diag.clear();
            
        }
        return false;
        
    }
   
    public void checkVictory() {
        boolean vert = checkVert();
        boolean hor = checkHor();
        boolean diagLeft = checkDiagLeft();
        boolean diagRight = checkDiagRight();  
        if(vert || hor || diagLeft || diagRight) {
            victoryLab.setText("VICTORY!!!" + " PLAYER " + player + " WINS!!");
            victory = true;
        }        
    } 
    
    public void attemptMove(ConnectFourCircle moveAttempt) {
        //Storing values of row and col in seperate variables for short reference
        int col = moveAttempt.col;
        int row = moveAttempt.row;
        boolean valid = false;
        int curInCol = 0;
        if (!victory){
            for (ConnectFourCircle circle : grid.get(col)){
                if (circle.curColor != Color.WHITE) {
                    curInCol += 1;
                }
                
                if (curInCol == row && moveAttempt.curColor == Color.WHITE) {
                    valid = true;
                }
            }
            
            if (valid){
                if (player == 1) {
                    moveAttempt.setFill(Color.RED);
                    moveAttempt.curColor = Color.RED;
                }
                else {
                    moveAttempt.setFill(Color.YELLOW);
                    moveAttempt.curColor = Color.YELLOW;
                }
                checkVictory();
                if (!victory){
                    validMoves += 1;
                    changePlayer();
                    if (validMoves == 42) {
                        victoryLab.setText("VICTORY!!! PLAYER " + player + " WINS!!");
                        victoryLab.setText("DRAW! :( NO PLAYER WINS!");
                    }
                }
            }
        }
    }
    
    public class ConnectFourCircle extends Circle {
        Color curColor;
        int num;
        int col;
        int row;

        public ConnectFourCircle(int xPos, int yPos, int num, int col, int row){
            super(xPos, yPos, 30);
            this.col = col;
            this.row = row;
            this.num = num;
            this.curColor = Color.WHITE;
            this.setFill(curColor);
            this.addEventHandler(MouseEvent.MOUSE_CLICKED, e -> {
                attemptMove(this);
            });
        }
    }
    
    
    @Override
    public void start(Stage primaryStage) {
        int yOffset = 6;
        //Setting up the Labels
        playerLab.setX(7);
        playerLab.setY(450);
        playerLab.setFont(Font.font ("Verdana", 18));
        victoryLab.setX(230);
        victoryLab.setY(450);
        victoryLab.setFont(Font.font ("Verdana", 18));
        //Creating main pane
        Pane mainPane = new Pane();
        Rectangle background = new Rectangle(0,0,500,500);
        background.setFill(Color.GREY);
        mainPane.getChildren().addAll(background, playerLab, victoryLab);
        int count = 0;
        for (int i = 1 ;i < 8 ; i++) {
            ArrayList<ConnectFourCircle> col = new ArrayList<ConnectFourCircle>();
            for (int j = 6; j > 0; j--) {
                col.add(new ConnectFourCircle((70 * i) - 30, (70 * (j)) - 30, count, i-1, (j-yOffset)*-1));
                count += 1;
            }
            grid.add(col);
        }
        //Adding circles onto the pane
        for (ArrayList<ConnectFourCircle> col : grid) {
            for(Circle circle : col) {
                mainPane.getChildren().add(circle);
            }
        }        
        //Setting up Scene
        Scene scene = new Scene(mainPane, 500, 460);
        primaryStage.setTitle("Connect Four");
        primaryStage.setScene(scene);
        primaryStage.setResizable(false);
        primaryStage.sizeToScene();
        primaryStage.show();
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        launch(args);
    }
}