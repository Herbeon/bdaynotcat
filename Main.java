import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.StackPane;
import javafx.stage.*;
import javafx.scene.paint.Color;

public class Main extends Application {

    @Override
    public void start(Stage stage) {

        // Text whee = new Text("HELO");
        Label l = new Label("hihihihi");
        StackPane root = new StackPane(l);
        // root.add(whee);
        Scene scene = new Scene(root, 300, 200);
        scene.setFill(Color.GREEN);
        stage.setScene(scene);
        stage.setOpacity(0.5);  // Set opacity to achieve transparency
        stage.setMaximized(true);
        stage.initStyle(StageStyle.TRANSPARENT);

        stage.show();
    }


    public static void main(String[] args) {
        launch();
    }

}
