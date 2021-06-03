import java.util.ArrayList;

/**
 * Jared Scott 
 */
public class SchedulerSJF extends SchedulerBase implements Scheduler {
    protected Platform platform;
    protected ArrayList<Process> processes;
    Process nextProcess;
    
    public SchedulerSJF(Platform platform) {
        this.platform = platform;
        this.processes = new ArrayList<Process>(); 
    }

    @Override
    public void notifyNewProcess(Process p) {
        this.processes.add(p);
    }
    
    public Process getNextProcess() {
        int shortestJob = Integer.MAX_VALUE;
        Process shortestJobProc = null;
        for (Process process : processes) {
            if (process.getTotalTime() < shortestJob && !(process.isExecutionComplete())) {
                shortestJob = process.getTotalTime();
                shortestJobProc = process;
            }
        }
        if (shortestJobProc != null) {
            this.contextSwitches += 1;
            this.platform.log("Scheduled: " + shortestJobProc.getName());
        }
        return shortestJobProc;
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