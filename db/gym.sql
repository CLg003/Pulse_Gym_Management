DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS fitness_classes;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    address VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE fitness_classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(255),
    day VARCHAR(255),
    time VARCHAR(255)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id),
    fitness_class_id INT REFERENCES fitness_classes(id)
);

-- INSERT INTO members (first_name, last_name, address, email) VALUES ('Jessica', 'Fletcher', '698 Candlewood Lane, Cabot Cove', 'jessica.fletcher@email.com');
-- INSERT INTO members (first_name, last_name, address, email) VALUES ('Sherlock', 'Holmes', '221b Baker Street, London', 'sherlock.holmes@email.com');

-- INSERT INTO fitness_classes (name, category, day, time) VALUES ('Yoga', 'Mind & Body', 'Monday', '19:00');
-- INSERT INTO fitness_classes (name, category, day, time) VALUES ('Circuits', 'Gym', 'Tuesday', '07:00');

-- INSERT INTO bookings (member_id, fitness_class_id) VALUES (1, 1);
-- INSERT INTO bookings (member_id, fitness_class_id) VALUES (2, 1);
-- INSERT INTO bookings (member_id, fitness_class_id) VALUES (2, 2);


