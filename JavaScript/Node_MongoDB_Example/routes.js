//@author Jared Scott ☯

const express = require("express");
const testModel = require("./models");
const app = express();

app.post("/add_test", async (request, response) => {
	const test = new testModel(request.body);
	try {
		await test.save();
		response.send(test);
	} catch (error) {
		response.status(500).send(error);
	} 
});

app.get("/tests", async (request, response) => {
	const tests = await testModel.find({});
	
	try {
		response.send(tests);
	} catch (error) {
		response.status(500).send(error);
	}
});

module.exports = app 