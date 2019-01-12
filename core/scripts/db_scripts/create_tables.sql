CREATE TABLE words(
	id INTEGER NOT NULL AUTO_INCREMENT,
	word VARCHAR(255),
	pronunciation VARCHAR(255),
	origin VARCHAR(255),
	sound_fp VARCHAR(255),
	PRIMARY KEY (id),
	UNIQUE (word)
);


