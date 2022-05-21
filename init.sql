CREATE TABLE IF NOT EXISTS products (
	id VARCHAR NOT NULL, 
	type VARCHAR NOT NULL, 
	printed_name VARCHAR NOT NULL, 
	theme VARCHAR NOT NULL, 
	price FLOAT NOT NULL, 
	sex VARCHAR NOT NULL, 
	payment VARCHAR NOT NULL, 
	day DATE NOT NULL, 
	client_name VARCHAR NOT NULL, 
	client_address VARCHAR NOT NULL, 
	client_state VARCHAR NOT NULL, 
	cover_status BOOLEAN NOT NULL, 
	core_status BOOLEAN NOT NULL, 
	timestamp DATETIME NOT NULL, 
	PRIMARY KEY (id)
);