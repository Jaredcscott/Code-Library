/**
 *
 * @author Jared Scott
 * This class defines a Crate entity. Each crate contains a single treasure. 
 *
 */

public class Crate extends Entity{
    public Crate(Treasure treasureType, int xPos, int yPos) {
        //Calls the Entity constructor
        super(xPos, yPos);
        this.treasure = treasureType;
    }

    public Treasure getTreasure() {
        //Returns the treasure type of the crate in question.
        return this.treasure;
    }
    
    @Override
    public String toString() {
        return "Crate with " + this.treasure + " at (" + this.getPosition().x + ", " + this.getPosition().y + ")";
    }
	
	private Treasure treasure;
}