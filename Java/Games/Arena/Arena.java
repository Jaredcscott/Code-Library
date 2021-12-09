/**
 *
 * @author Jared Scott ☯
 * This class defines an Arena class. An Arena is a 2 dimensional grid of  empty
 * spaces and Entity objects. The Arena's size is dynamically determined when it 
 * is created. Defines the needed methods to add entities to the arena, as well as move them
 * to other locations. 
 *
 */

import java.util.ArrayList;

public class Arena {
    public Arena(int x, int y) {
        this.x = x;
        this.y = y;
        for (int i = 0; i < this.x; i++) {
            arena.add(new Entity[this.y]);
        }
    }

    public int getTreasureCount(Treasure treasureType) {
        //Returns the appropriate count associated with that treasure type.
        switch (treasureType) {
            case Wood:
                return this.woodCount;
            case Statue:
                return this.statueCount;
            case Food:
                return this.foodCount;
            case Coins:
                return this.coinsCount;
            case Rags:
                return this.ragsCount;
        }
        return 0;
    }

    public int getEntityCount() {
        //Returns the total count of entities
        return this.entityCount;
    }

    public int getDragonCount() {
        //Returns the amount of dragons
        return this.dragonCount;
    }
    
    public ArrayList<Entity[]> getGrid() {
        //Returns the Arena grid.
        return this.arena;
    }
    
    public Hero getHero() {
        //Returns the Hero for the Arena. 
        return this.hero;
    }
    
    public void moveHero(int x, int y) {
        //Moves the hero to the provided location. 
        if (arena.get(x)[y] == null) {
            changeEntityLocation(this.hero,x,y);
            System.out.printf("%s moved to (%d, %d)\n",this.hero.getName(),this.hero.getPosition().x,this.hero.getPosition().y);
        }
        else if (arena.get(x)[y] instanceof Dragon) {
            this.hero.attack(arena.get(x)[y]);
            changeEntityLocation(this.hero,x,y);
            System.out.printf("%s moved to (%d, %d)\n",this.hero.getName(),this.hero.getPosition().x,this.hero.getPosition().y);
        }
        else if (arena.get(x)[y] instanceof Crate) {
            this.hero.attack(arena.get(x)[y]);
            changeEntityLocation(this.hero,x,y);
            System.out.printf("%s moved to (%d, %d)\n",this.hero.getName(),this.hero.getPosition().x,this.hero.getPosition().y);
        }
        alterEntityCount();
    }
    
    public void reportHero() {
        //Reports the Hero's position and treasure list.
        System.out.printf("--- Hero report for %s ---\n",this.hero.getName());
        System.out.printf("Position: (%d, %d)\n",this.hero.getPosition().x,this.hero.getPosition().y);
        System.out.println("Treasures:");
        for (int i = 0; i < this.hero.getTreasures().size(); i++) {
            System.out.println("  " + this.hero.getTreasures().get(i));
        }
        System.out.println();
    }
    
    public boolean add(Entity entity) {
        //Attempts to add the provided entity to the Arena grid
        //Returns a boolean if the attempt was successful.
        if (entity instanceof Hero && this.heroCount > 0) {
            System.out.println("Could not add '" + entity + "' because there is already a hero in the arena.");
            return false;
        }
        if (arena.get(entity.getPosition().x)[entity.getPosition().y] == null) {
            arena.get(entity.getPosition().x)[entity.getPosition().y] = entity;
            System.out.println("Successfully added '" + entity + "' to the game arena.");
            if (entity instanceof Hero) {
                this.hero = (Hero) entity;
            }
            alterEntityCount();
            return true;
        }
        else {
            System.out.println("Could not add '" + entity + "' because another entity is already there.");
            return false;
        }
    }
    
    public void alterEntityCount() {
        //Adjusts the count of the various entity 
        this.resetVals();
        for (int i = 0 ;i < this.x; i++) {
            for (int j = 0; j < this.y; j++) {
                if(this.arena.get(i)[j] == null) {
                    continue;
                }
                else {
                    this.entityCount += 1;
                    if (this.arena.get(i)[j] instanceof Hero) {
                        this.heroCount += 1;
                    }
                    else if (this.arena.get(i)[j] instanceof Dragon) {
                        this.dragonCount += 1;
                    }
                    else if (this.arena.get(i)[j] instanceof Crate) {
                        Crate crate = (Crate) this.arena.get(i)[j];
                        if (crate.getTreasure() == Treasure.Wood) {
                            this.woodCount += 1;
                        }
                        else if (crate.getTreasure() == Treasure.Statue) {
                            this.statueCount += 1;
                        }
                        else if (crate.getTreasure() == Treasure.Food) {
                            this.foodCount += 1;
                        }
                        else if (crate.getTreasure() == Treasure.Coins) {
                            this.coinsCount += 1;
                        }
                        else if (crate.getTreasure() == Treasure.Rags) {
                            this.ragsCount += 1;
                        }
                    }
                }
            }
        }
    }
    
    public void changeEntityLocation (Entity entity,int x, int y) {
        //Adjusts the position of the provided entity. 
        arena.get(entity.getPosition().x)[entity.getPosition().y] = null;
        this.hero.setPosition(x,y);
        arena.get(x)[y] = entity;
    }

    public void resetVals() {
        //Resets the entity count values back to 0
        this.entityCount = 0;
        this.dragonCount =0;
        this.heroCount = 0;
        this.woodCount = 0;
        this.statueCount = 0;
        this.foodCount = 0;
        this.coinsCount = 0;
        this.ragsCount = 0;
    }
	
	private int entityCount;
    private int dragonCount;
    private int heroCount;
    private int woodCount;
    private int statueCount;
    private int foodCount;
    private int coinsCount;
    private int ragsCount;
    private int x;
    private int y;
    private ArrayList<Entity[]> arena = new ArrayList<>();
    private Hero hero;
}