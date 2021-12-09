/**
 *
 * @author Jared Scott ☯
 * This class defines a Hero entity. The hero has an array containing 
 * treasures. The Hero can also attack other entities claiming their treasure 
 * or removing them from the arena. 
 *
 */

import java.util.ArrayList;

public class Hero extends Entity {   
    public Hero(String name, int xPos, int yPos) {
        super(xPos, yPos);
        this.name = name;
    }

    public ArrayList<Treasure> getTreasures() {
        return this.treasures;
    }

    public String getName() {
        return this.name;
    }

    public void attack(Entity entity) {
        if (entity instanceof Dragon) {
            if (((Dragon) entity).getTreasure() == Treasure.Coins) {
                System.out.printf("%s bravely defeated the %s dragon and came away with gold coins as a prize.\n",this.name,((Dragon) entity).getColor());
                this.treasures.add(((Dragon) entity).getTreasure());
            }
            else {
                System.out.printf("%s bravely defeated the %s dragon.\n",this.name,((Dragon) entity).getColor());
            }
        }
        else if (entity instanceof Crate) {
            System.out.printf("%s crushed the crate into bits and found %s.\n",this.name,((Crate) entity).getTreasure());
            this.treasures.add(((Crate) entity).getTreasure());
        }
    }
    
    @Override
    public String toString() {
        return this.name + " standing at" + " (" + this.getPosition().x + ", " + this.getPosition().y + ")";
    }
	
	private String name;
    private ArrayList<Treasure> treasures = new ArrayList<>();
}