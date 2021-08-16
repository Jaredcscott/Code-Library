/**
 *
 * @author Jared Scott
 * This class an Entity. Each Entity has a position
 * Super-class for Hero, Dragon, and Crate
 *
 */

public class Entity {    
    public Entity (int xPos, int yPos) {
        this.position = new Position(xPos,yPos);
    }

    public Position getPosition() {
        return this.position;
    }

    public void setPosition(int xPos, int yPos) {
        this.position = new Position(xPos,yPos);
    }
	
	private Position position;
}