import java.util.ArrayList;

/**
 * @author Jared Scott ☯
 */
public class SchedulerSRTF extends SchedulerBase implements Scheduler {
    protected Platform platform;
    protected ArrayList<Process> processes;
    Process nextProcess;
    boolean reCheck;
    
    public SchedulerSRTF(Platform platform) {
        this.platform = platform;
        this.processes = new ArrayList<Process>();
        this.reCheck = false;
    }
    
    @Override
    public void notifyNewProcess(Process p) {
        this.processes.add(p);
        if (processes.size() > 1) {
            this.reCheck = true;
        }
    }
    
    public Process getNextProcess() {
        int shortestJob = Integer.MAX_VALUE;
        Process shortJobProc = null;
        for (Process process : processes) {
            if ((process.getTotalTime() - process.getElapsedTotal()) < shortestJob && !(process.isExecutionComplete())) {
                shortestJob = (process.getTotalTime() - process.getElapsedTotal());
                shortJobProc = process;
                
            }
        }
        if (shortJobProc != null) {
            this.contextSwitches += 1;
            this.platform.log("Scheduled: " + shortJobProc.getName());
        }
        return shortJobProc;
    }

    @Override
    public Process update(Process cpu) {
        this.nextProcess = null;
        if (!reCheck) {
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
        else{
            if (cpu != null){
                int shortestJob = Integer.MAX_VALUE;
                Process shortJobProc = null;
                for (Process process : processes) {
                    if ((process.getTotalTime() - process.getElapsedTotal()) < shortestJob && !(process.isExecutionComplete())) {
                        shortestJob = (process.getTotalTime() - process.getElapsedTotal());
                        shortJobProc = process;
                    }
                }
                this.nextProcess = shortJobProc;
                if (this.nextProcess != cpu) {
                    this.platform.log("Preemptively removed: " + cpu.getName());
                    this.platform.log("Scheduled: " + nextProcess.getName());
                    this.contextSwitches += 2;
                }
                reCheck = false;
            }
            return this.nextProcess;
        }
    } 
}