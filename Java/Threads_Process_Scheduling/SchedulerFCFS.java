import java.util.LinkedList;

/**
 * Jared Scott 
 */
public class SchedulerFCFS extends SchedulerBase implements Scheduler {
    protected Platform platform;
    protected LinkedList<Process> processes;
    Process nextProcess;
    
    public SchedulerFCFS(Platform platform) {
        this.platform = platform;
        this.processes = new LinkedList<Process>(); 
    }

    @Override
    public void notifyNewProcess(Process p) {
        this.processes.addLast(p);
    }
    
    public Process getNextProcess() {
        Process nextProc = this.processes.poll();
        if (nextProc != null) {
            this.contextSwitches += 1;
            this.platform.log("Scheduled: " + nextProc.getName());
        }     
        return nextProc;
    }

    @Override
    public Process update(Process cpu) {
        nextProcess = null;
        if (cpu == null) {
            nextProcess = getNextProcess();
        }
        else if (!(cpu.isBurstComplete())) {
            
            nextProcess = cpu;
        }
        else if (cpu.isBurstComplete()) {
            this.contextSwitches += 1;
            this.platform.log("Process: " + cpu.getName() + " burst complete");
            if(cpu.isExecutionComplete()){
                this.platform.log("Process: " + cpu.getName() + " execution complete");
                this.processes.remove(cpu);
            }
            else {
                this.processes.addLast(cpu);
            }
            nextProcess = getNextProcess();
        }
        return nextProcess;
    } 
}