import java.util.LinkedList;

/**
 * Jared Scott 
 */
public class SchedulerRR extends SchedulerBase implements Scheduler {
    protected Platform platform;
    protected LinkedList<Process> processes;
    protected Process nextProcess;
    int timeQuan;
    int curCount;
    public SchedulerRR(Platform platform, int timeQuan) {
        this.platform = platform;
        this.processes = new LinkedList<Process>();
        this.timeQuan = timeQuan;
        this.curCount = 1;
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
        else {
            if(cpu.isExecutionComplete()){
                this.curCount = 1;
                this.contextSwitches += 1;
                this.platform.log("Process: " + cpu.getName() + " execution complete");
                return getNextProcess();
            }
            if ((this.curCount < this.timeQuan) ) {
                this.curCount += 1;
                nextProcess = cpu;
            }
            else if ((this.curCount == this.timeQuan) ) {
                this.curCount = 1;
                this.contextSwitches += 1;
                this.processes.addLast(cpu);
                this.platform.log("Time quantum complete for process: " + cpu.getName());
                nextProcess = getNextProcess();
            }
        }
        if(nextProcess.isExecutionComplete()){
            this.contextSwitches += 1;
            this.platform.log("Process: " + nextProcess.getName() + " execution complete");
            return getNextProcess();
        }
        return nextProcess;
    } 
}