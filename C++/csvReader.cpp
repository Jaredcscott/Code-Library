void read_csv( void ) {
	
	//Start of csv reader
	std::string filename = "INSERT PATH TO FILE"; 	           //<-----------------------CHANGE VALUE HERE
	std::ifstream file( filename, std::ios::in );
	if( !file )
	{ 
		//Checking if the file exists
		std::cout << "Error: " << filename << " File Not Found. " << std::endl; 
		exit(-1);
	}
	std::string line;
	while (std::getline(file, line))
	{
		//Reading lines 
		std::vector<double> data;
		csv_to_vector( line.c_str() , data ); 

		if( data.size() != <Insert Expected Data Array Size> ) //<-----------------------CHANGE VALUE HERE 
		{
			//																		   \/CHANGE VALUE HERE\/
			std::cout << "Error! Importing data from a CSV file expects each row to be <INSERT DATA FORMAT>." << std::endl;  
			exit(-1);
		}
		//Insert logic to interact with the data 				 <-----------------------CHANGE VALUE HERE
	}
	file.close();  //Closing file 
}