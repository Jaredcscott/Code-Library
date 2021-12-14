/**
 * @author Jared Scott ☯
 */

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Scanner;
import javafx.scene.text.Font;
import java.util.logging.Level;
import java.util.logging.Logger;
import javafx.animation.KeyFrame;
import javafx.animation.KeyValue;
import javafx.animation.Timeline;
import javafx.application.Application;
import javafx.beans.property.SimpleDoubleProperty;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Node;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.Tab;
import javafx.scene.control.TabPane;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Pane;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.web.WebView;
import javafx.stage.Stage;
import javafx.util.Duration;


public class WebBrowser extends Application {
    public static TabPane tabPane = new TabPane();
    static ArrayList<WebBrowser> browsers = new ArrayList<WebBrowser>();
    static VBox bookMarks = new VBox(); 
    public WebView webView;
    public String curPage;
    public String prevPage;
    Button backBtn;
    Button bookMarkBtn;
    TextField searchBar;
    Button srchBtn;
    Button bookMrksBtn;
    SimpleDoubleProperty width;
    Boolean bookmarksShown;
    BorderPane mainPane;
    VBox topGroup;
    Pane topBar;
    Scene scene;
    
    public WebBrowser() {
        this.webView = new WebView();
        this.curPage = "";
        this.prevPage = "";
        this.backBtn = new Button();
        this.bookMarkBtn = new Button();
        this.searchBar = new TextField();
        this.srchBtn = new Button();
        this.bookMrksBtn = new Button();
        this.width = new SimpleDoubleProperty();
        this.bookmarksShown = false;
        this.mainPane = new BorderPane();
        this.topGroup = new VBox();
        this.topBar = new Pane();
        this.topGroup.getChildren().add(this.topBar);
        
        //Setting up inital state
        this.loadPage("https://cs.usu.edu");
        //Setting up the back button with its needed logic. 
        this.backBtn.setText("Back");
        this.backBtn.setOnAction((ActionEvent event) -> {
            this.loadPage(this.prevPage);
        });
        
        this.bookMarkBtn.setText("Book Mark");
        this.bookMarkBtn.setOnAction((ActionEvent event) -> {
            new BookMark(this.curPage);
            try {
                bookmarkAnimation();
            } catch (InterruptedException ex) {
                Logger.getLogger(WebBrowser.class.getName()).log(Level.SEVERE, null, ex);
            }
        });
        
        this.searchBar.setPrefWidth(500);
        this.searchBar.setPromptText("Search Google or type a URL");
        this.searchBar.setOnKeyPressed((KeyEvent ke) -> {
            if (ke.getCode().equals(KeyCode.ENTER))
            {
                this.search(this.webView);
            }
        });
        
        this.srchBtn.setText("Search");
        this.srchBtn.setOnAction((ActionEvent event) -> {
            this.search(this.webView);
        });
        this.bookMrksBtn.setText("Bookmarks");
        this.bookMrksBtn.setOnAction((ActionEvent event) -> {
            if( !this.bookmarksShown ) {
                this.mainPane.setRight(bookMarks);
                this.bookmarksShown = true;
            }
            else {
                this.mainPane.setRight(null);
                this.bookmarksShown = false;
            }
        });
        this.topBar.getChildren().addAll(this.backBtn, this.bookMarkBtn, this.searchBar, this.srchBtn, this.bookMrksBtn);
        this.mainPane.setTop(this.topGroup);
        this.mainPane.setCenter(this.webView);
        this.adjustButtons();  
    }
    
    private void search(WebView webView){
        String searchBarText = this.searchBar.getText();
        if(searchBarText.startsWith("www")) {
            this.loadPage("https://" + searchBarText);
        }
        else {
            this.loadPage("https://www.google.com/search?q=" + searchBarText);
        }
    }
    
    private void loadPage(String url) {
        if(url.startsWith("www")) {
            this.webView.getEngine().load("https://" + url);
        }
        else if (url.startsWith("http")) {
            this.webView.getEngine().load(url);
        }
        else {
            System.out.println("Invalid URL supplied");
        }
        this.checkCurPage();
    }
    
    private void checkCurPage() {
        String page = this.webView.getEngine().getLocation();
        if ((page != null && (this.curPage) != null) && !page.equals(this.curPage)) {
            this.prevPage = this.curPage;
            this.curPage = page;
        }
    }
    
    private void adjustButtons() {
        this.bookMarkBtn.relocate(width.getValue() / 3 - 200,0);
        this.searchBar.relocate(width.getValue() / 3 - 125,0);
        this.srchBtn.relocate(width.getValue() / 3 + 375,0);
        this.bookMrksBtn.relocate(width.getValue() - 90,0);
    }  
    
    public class BookMark {
        HBox box;
        Button bookMark;
        Button remove;
        String url;
        public BookMark(String url) {
            this.url = url;
            this.box = new HBox();
            this.bookMark = new Button();
            this.bookMark.setText(url);
            this.bookMark.setOnAction((ActionEvent event) -> {
                WebBrowser curWebBrowser = browsers.get(Integer.parseInt(tabPane.getSelectionModel().getSelectedItem().getText()) - 1);
                System.out.println(curWebBrowser.curPage);
                curWebBrowser.loadPage(this.url);
            });
            this.remove = new Button();
            this.remove.setText("X");
            this.remove.setOnAction((ActionEvent event) -> {
                bookMarks.getChildren().remove(this.box);
                writeBookmarks();
            });
            this.box.getChildren().addAll(this.bookMark, this.remove);
            addToList();
        }
        private void addToList() {
            bookMarks.getChildren().add(this.box);
            writeBookmarks();
        }
    }
    
    public void loadBookmarks(String filePath) {
        try {
            Scanner reader = new Scanner(new File(filePath));
            while (reader.hasNextLine()) {
                new BookMark(reader.nextLine());
            }
            reader.close();
        } 
        catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    public void writeBookmarks() {
        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter("src/bookmarks.txt"));
            for (Node child : bookMarks.getChildren()) {
                HBox curBookmark = (HBox) child;
                Button button = (Button) curBookmark.getChildren().get(0);
                writer.write(button.getText());
                writer.write("\n");
            }

            writer.close();
        } 
        catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    public void bookmarkAnimation() throws InterruptedException {
        Label bookMarkLabel = new Label("Page Bookmarked");
        bookMarkLabel.setTextFill(Color.BLUE);
        bookMarkLabel.setFont(new Font("Arial", 15));
        this.topGroup.getChildren().add(bookMarkLabel);
        final Timeline timeline = new Timeline();
        timeline.setCycleCount(1);
        timeline.setAutoReverse(true);
        timeline.getKeyFrames().add(new KeyFrame(Duration.millis(3000), new KeyValue (bookMarkLabel.translateXProperty(), this.width.getValue())));
        timeline.play();
        timeline.setOnFinished(event -> 
            this.topGroup.getChildren().remove(bookMarkLabel)
        );
    }
    
    @Override
    public void start(Stage primaryStage) {
        loadBookmarks("src/bookmarks.txt");
        WebBrowser wb = new WebBrowser();
        wb.width.bind(primaryStage.widthProperty());
        browsers.add(wb);
        Tab tab = new Tab();
        tab.setText("1");
        tab.setContent(wb.mainPane);
        tabPane.getTabs().add(tab);
        //Adding a tab used for adding new tabs
        Tab add = new Tab();
        add.setText("+");
        tabPane.getTabs().add(add);
        tabPane.getSelectionModel().selectedItemProperty().addListener(new ChangeListener<Tab>() {  
                @Override  
                public void changed(ObservableValue<? extends Tab> observable,  
                          Tab oldSelectedTab, Tab newSelectedTab) {  
                     if ("+".equals(newSelectedTab.getText())) {
                        tabPane.getTabs().remove(add);
                        WebBrowser wb1 = new WebBrowser();
                        wb1.width.bind(primaryStage.widthProperty());
                        browsers.add(wb1);
                        Tab tab1 = new Tab();
                        tab1.setText("" + browsers.size());
                        tab1.setContent(wb1.mainPane);
                        tabPane.getTabs().add(tab1);
                        tabPane.getSelectionModel().select(tab1);
                        tabPane.getTabs().add(add);
                        wb1.adjustButtons();
                     }    
                }
            });
        scene = new Scene(tabPane, 1000, 750);
        scene.addEventFilter(MouseEvent.MOUSE_MOVED, new EventHandler<MouseEvent>() {
            @Override
            public void handle(MouseEvent mouseEvent) {
                WebBrowser curWebBrowser = browsers.get(Integer.parseInt(tabPane.getSelectionModel().getSelectedItem().getText()) - 1);
                curWebBrowser.checkCurPage();
            }
        });
        //This will listen to the width property of the stage and readjust the botton locations when the window is resized
        primaryStage.widthProperty().addListener((obs, oldVal, newVal) -> {
            for (WebBrowser browser : browsers) {
                browser.adjustButtons();
            }
        });
        primaryStage.setMinHeight(800);
        primaryStage.setMinWidth(800);
        primaryStage.setTitle("Web Surfer");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        launch(args);
    }
}