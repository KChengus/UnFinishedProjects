import javafx.event.EventHandler;
import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.control.Label;
import javafx.scene.control.ProgressBar;
import javafx.scene.Scene;
import javafx.event.ActionEvent;


import javafx.scene.layout.VBox;

import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.stage.Stage;
import javafx.scene.control.Button;
import java.net.*;
// import javafx.application.Platform;
// import javafx.scene.layout.StackPane;
public class MainGUI extends Application {
    Calc calc = new Calc();
    boolean showExpression = false;

    public void start(Stage stage) {
        
        initUI(stage);
    }

    private void initUI(Stage stage) {
        var root = new VBox();
        var btn = new Button();
        var scene = new Scene(root, 800, 600);
        var lbl = new Label("Simple JavaFX application.");
        

        root.getChildren().add(lbl);
        root.setAlignment(Pos.CENTER);

        lbl.setFont(Font.font("Serif", FontWeight.NORMAL, 25));
        lbl.setPadding(new Insets(50));



        // // create a tile pane
        // TilePane r = new TilePane();
    
        // action event

        btn.setText("Next");
        
        btn.setOnAction((ActionEvent event) -> {
            if (showExpression) {
                lbl.setText(calc.expressions.exp + " = " + String.valueOf(calc.getAnswer()));    
            } else {
                calc.expressions.generateRandomExpression();
                lbl.setText(calc.expressions.exp);    
            }
            showExpression = !showExpression;
        });
        root.getChildren().add(btn);
        stage.setTitle("Simple application");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}