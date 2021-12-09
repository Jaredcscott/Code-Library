/**
 *
 * @author Jared Scott ☯
 * This class defines a Dragon entity. Each Dragon has a color, only Golden 
 * dragons have treasure, which is gold coins.   
 *
 */

public class Dragon extends Entity {
    public Dragon(String color, int xPos, int yPos) {
        //Calls Entity constructor
        super(xPos,yPos);
        this.color = color;
        if (color.equals("Golden")) {
            this.treasure = Treasure.Coins;
        }
    }

    public String getColor() {
        //Returns the color of the Dragon.
        return this.color;
    }
    
    public Treasure getTreasure() {
        //If the Dragon is golden, then this returns the treasure of coins.
        return this.treasure;
    }
    
    @Override
    public String toString() {
        return "The " + this.color + " dragon breathing fire at" + " (" + this.getPosition().x + ", " + this.getPosition().y + ")";
    }
	
	private String color;
    private Treasure treasure;
}