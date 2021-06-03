import java.util.ArrayList;

/**
 * Jared Scott 
 */
public class SchedulerPriority extends SchedulerBase implements Scheduler  {
    protected Platform platform;
    protected ArrayList<Process> processes;
    Process nextProcess;
    
    public SchedulerPriority(Platform platform) {
        this.platform = platform;
        this.processes = new ArrayList<Process>();
    }

    @Override
    public void notifyNewProcess(Process p) {
        this.processes.add(p);
    }
    
    public Process getNextProcess() {
        int maxPriority = Integer.MAX_VALUE;
        Process maxPriorityProc = null;
        for (Process process : this.processes) {
            if (process.getPriority() < maxPriority && !(process.isExecutionComplete())) {
                maxPriority = process.getPriority();
                maxPriorityProc = process;
            }
        }
        if (maxPriorityProc != null) {
            this.contextSwitches += 1;
            this.platform.log("Scheduled: " + maxPriorityProc.getName());
        }
        return maxPriorityProc;
    }

    @Override
    public Process update(Process cpu) {
        this.nextProcess = null;
        if (cpu == null) {
            this.nextProcess = getNextProcess();
        }
        else if (!(cpu.isBurstComplete())) {
            
            this.nextProcess = cpu;
        }
        else if (cpu.isBurstComplete()) {
            this.contextSwitches += 1;
            this.platform.log("Process: " + cpu.getName() + " burst complete");
            if(cpu.isExecutionComplete()){
                this.platform.log("Process: " + cpu.getName() + " execution complete");
                this.processes.remove(cpu);
            }
            else {
                this.processes.add(cpu);
            }
            this.nextProcess = getNextProcess();
        }
        return this.nextProcess;
    }
}