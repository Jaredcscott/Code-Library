/**
 *
 * @author Jared Scott
 * This class defines the x and y position of an entity's in the arena.  
 *
 */

public class Position {
    public int x;
    public int y;

    public Position(int xPos, int yPos) {
        this.x = xPos;
        this.y = yPos;
    }

    @Override
    public String toString() {
        return "(" + (this.x) + ", " + (this.y) + ")";
    }
}