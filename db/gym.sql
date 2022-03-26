DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS fitness_classes;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    premium BOOLEAN,
    active BOOLEAN
);

CREATE TABLE fitness_classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    day VARCHAR(255) NOT NULL,
    time VARCHAR(255) NOT NULL,
    active BOOLEAN,
    premium BOOLEAN
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    fitness_class_id INT REFERENCES fitness_classes(id) ON DELETE CASCADE,
    arrived BOOLEAN
);

ALTER TABLE members ALTER COLUMN premium SET DEFAULT False;
ALTER TABLE members ALTER COLUMN active SET DEFAULT True;
ALTER TABLE fitness_classes ALTER COLUMN premium SET DEFAULT False;
ALTER TABLE fitness_classes ALTER COLUMN active SET DEFAULT True;
ALTER TABLE bookings ALTER COLUMN arrived SET DEFAULT False;


-- Commands used for testing database:

-- INSERT INTO members (first_name, last_name, address, email) VALUES ('Jessica', 'Fletcher', '698 Candlewood Lane, Cabot Cove', 'jessica.fletcher@email.com');
-- INSERT INTO members (first_name, last_name, address, email) VALUES ('Sherlock', 'Holmes', '221b Baker Street, London', 'sherlock.holmes@email.com');

-- INSERT INTO fitness_classes (name, category, day, time) VALUES ('Yoga', 'Mind & Body', 'Monday', '19:00');
-- INSERT INTO fitness_classes (name, category, day, time) VALUES ('Circuits', 'Gym', 'Tuesday', '07:00');

-- INSERT INTO bookings (member_id, fitness_class_id) VALUES (1, 1);
-- INSERT INTO bookings (member_id, fitness_class_id) VALUES (1, 2);
-- INSERT INTO bookings (member_id, fitness_class_id) VALUES (2, 2);

-- SELECT fitness_classes.* FROM fitness_classes INNER JOIN bookings ON bookings.fitness_class_id = fitness_classes.id INNER JOIN members ON members.id = bookings.member_id WHERE bookings.member_id = 1;
-- SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id INNER JOIN fitness_classes ON fitness_classes.id = bookings.fitness_class_id WHERE bookings.fitness_class_id = 2;
-- SELECT bookings.* FROM bookings INNER JOIN members ON bookings.member_id = members.id WHERE bookings.member_id = 2;
-- SELECT bookings.* FROM bookings INNER JOIN fitness_classes ON bookings.fitness_class_id = fitness_classes.id WHERE bookings.fitness_class_id = 2;