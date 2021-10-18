const mongoose = require("mongoose");
const TestSchema = new mongoose.Schema({
	category: {
		type: String, 
		//required: true,
	},
	name: {
		type: String, 
		//required: true, 
	}
});

const Test = mongoose.model("Test",TestSchema);

module.exports = Test;