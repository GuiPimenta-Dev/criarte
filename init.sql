
CREATE TABLE products (
	id VARCHAR (255) PRIMARY KEY,
	type VARCHAR (255) NOT NULL, 
	printed_name VARCHAR (255) NOT NULL, 
	theme VARCHAR (255) NOT NULL, 
	price FLOAT NOT NULL, 
	sex VARCHAR (255) NOT NULL, 
	payment VARCHAR (255) NOT NULL, 
	day DATE NOT NULL, 
	client_name VARCHAR (255) NOT NULL, 
	client_address VARCHAR (255) NOT NULL, 
	client_state VARCHAR (255) NOT NULL,
    observations VARCHAR (255),  
	cover_status BOOLEAN NOT NULL, 
	core_status BOOLEAN NOT NULL, 
	timestamp timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL 
);