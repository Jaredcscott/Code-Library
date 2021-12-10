/**
 * @author Jared Scott ☯
 * 
 */
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.concurrent.Semaphore;

public class ParallelPi {
	/**
	 * This class uses threads to calculate the digits of pi concurrently making the calculation more efficient 
	 */
    static long timeStart; //Used to measuring execution time 
   
    public static class Task {
		//Used to store the digit for use with the threads 
        int digitNum;
        public Task(int digitNum) {
            this.digitNum = digitNum;
        }
        
        public int getDigit() {
            return this.digitNum;
        }
    }
    
    public static class TaskQueue {
		//This is the queue of the remaining digits
        public Semaphore lock = new Semaphore(1); //This lock is used to control memory use 
        LinkedList<Task> digitQueue; //List to store the digit values 
        
        public TaskQueue() {
            digitQueue = new LinkedList<Task>();
        }
        
        public void addTask(Task task) {
            this.digitQueue.add(task);
        }  
    }
    
    public static class ResultTable {
		//This data structure stores the results of computing the digit at a specific location (the digits are not calculated in sequential order) 
        int digitsComputed = 0;
        public HashMap results;
        public Semaphore lock = new Semaphore(1); //Used to control memory use 
        
        public ResultTable() {
            this.results = new HashMap();
        }
    }
    
    public static class ComputeDigits implements Runnable {
		//This class is used to actually compute the digits of pi it implements runnable so that it can be used within the context of threads  
		
        public TaskQueue taskQueue;		//Stores the tasks 
        public ResultTable resultTable;	//Stores the results 
        public int goal;				//This is the goal number of digits to compute 
        
        public ComputeDigits(TaskQueue taskQueue, ResultTable resultTable, int goal) {
            this.taskQueue = taskQueue;
            this.resultTable = resultTable;
            this.goal = goal;
        }
        
        @Override
        public void run() {
			//This method is run by the thread. It contains the logic for managing the resources while computing Pi with the BPP class 
            int digit;
            boolean hasNum;
            try {
                if (taskQueue.digitQueue.size() > 0 && resultTable.results.size() < goal) {
                    taskQueue.lock.acquire();						//Obtaining lock to pull task (preserves memory)  
                    digit = taskQueue.digitQueue.pop().getDigit();	//Pulling a digit from the task queue 
                    taskQueue.lock.release();						//Releasing lock on task queue 
                    Bpp digitCalc = new Bpp();						//Instantiating Pi computation object	
                    int digitVal = digitCalc.getDecimal(digit);		//Calculating the digit at that location 
                    hasNum = true;									//Sentinal value 
                    while(hasNum){
                        try {
							//Placing the value into the results table
                            resultTable.lock.acquire(); 			//Obtaining the lock for the results table 
                            resultTable.results.put(digit, digitVal);
                            resultTable.digitsComputed += 1;		
                            if ((resultTable.digitsComputed % 10) == 0){
								//This simply gives the user an indication that the program is working
                                System.out.print(".");
                                System.out.flush();
                            }
                            if ((resultTable.digitsComputed % 250) == 0) {
								//A more expansive indicator for the user that the system is still processing, displays the computation time 
                                String modifier;
                                long curTime = (System.currentTimeMillis() - timeStart); //Calculating the current execution time 
                                if(curTime > 1000) {
                                    curTime /= 1000;
                                    modifier  = "s";
                                }
                                else {
                                    modifier  = "ms";
                                }
                                System.out.println("Executing [" + curTime  + modifier + "]");
                                System.out.flush();
                            }
                            resultTable.lock.release(); //Releasing the lock for the results table 
                            hasNum = false;
                        }
                        catch (Exception e) {
                        }
                    }
                }
            }
            catch (Exception e) {
            }
        }
    }
    
    public static void main(String[] args) {
		//Instantiating the needed objects for computation as well as an initial timestamp 
        timeStart = System.currentTimeMillis();
        ResultTable resultTable = new ResultTable();
        TaskQueue taskQueue = new TaskQueue();
        ArrayList<Integer> digits = new ArrayList<Integer>(); 	//Used to store the digit computation order 
        int digitCount = 1000; 									//How many digits you would like to compute  
        for (int i = 1 ; i <= digitCount + 1; i++) {
			//Adding the digits to array 
            digits.add(i);
        }
        java.util.Collections.shuffle(digits);					//Shuffling the array so the digits are calculated in a random order 
        for (Integer digit : digits) {
			//Adding the shuffled digits into an array for final processing 
            Task newTask = new Task(digit);
            taskQueue.addTask(newTask);
        }
        try {
			//Checking the available processors 
            int processors = Runtime.getRuntime().availableProcessors();
            Thread[] threadList = new Thread[processors]; //An array so store the threads 
            int thread = 0;
            while (!(taskQueue.digitQueue.isEmpty())) {
				//Chewing through the digits computing them using threads 
                if (thread == processors) {
                    thread = 0;
                }
                threadList[thread] = new Thread(new ComputeDigits(taskQueue, resultTable, digitCount));
                threadList[thread].start();
                thread++;
            }
        }
        catch (Exception ex) {
            System.out.println(ex); //Error during execution 
        }
        String pi = "3."; //Starting to build the final result string, initializing with 3.
		
        for (int i = 1; i < digitCount + 1; i++) {
            try{
				//Checking if the result is in the results table. 
				//If there was an error during execution the result may not have been found 
                int num = (int) resultTable.results.get(i);
                pi += num;
            }
            catch (Exception e) {
				//Calculating any digits not found in the results table 
                Bpp digitCalc = new Bpp();
                int digitVal = digitCalc.getDecimal(i);
                pi += digitVal;
            } 
        }
        System.out.println(pi); //Printing the result of the computation 
        long timeEnd = System.currentTimeMillis();	//Final timestamp 
        System.out.println("Pi Computation took " + (timeEnd - timeStart) + " ms"); //Printing execution time 
        System.exit(0);	//Exiting 
    }
}