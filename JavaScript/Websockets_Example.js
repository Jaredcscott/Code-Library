// @author Jared Scott ☯
function sendCommand(command) {
	var HOST = '192.168.176.54';
	var PORT = '10321';
	var ws = new WebSocket("ws://" + HOST + ":" + PORT + "/");
	ws.onopen = () => ws.send("RUN TEST:I2-R5-T7");
}