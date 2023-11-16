/*------------------------------
    Group 77: Michael Rigali & Derrick Higgins
    PokéCollect
    Michael Rigali & Derrick Higgins 
------------------------------*/

/*disable commits and foreign key checks*/
SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;

/*drop any possible existing tables*/
DROP TABLE IF EXISTS Users, Orders, Shipments, Payments, PokemonCardSpecs, PokemonCardSpecs_Orders;

/*------------------------------
    Create tables 
------------------------------*/

/*Create Users Table*/
CREATE TABLE Users (
    user_id int NOT NULL AUTO_INCREMENT UNIQUE,
    username varchar(50) NOT NULL UNIQUE,
    password varchar(256) NOT NULL,
    first_name varchar(15) NOT NULL,
    last_name varchar(15) NOT NULL,
    email varchar(255) NOT NULL UNIQUE,
    birthday DATE,
    address varchar(255),
    PRIMARY KEY (user_id)
);

/*Create Orders Table*/
CREATE TABLE Orders (
    order_id int NOT NULL AUTO_INCREMENT UNIQUE,
    user_id int,
    product_id int,
    shipping_id int,
    customer_name varchar(50),
    quantity_purchased int,
    transaction_date DATE,
    PRIMARY KEY (order_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (product_id) REFERENCES PokemonCardSpecs(product_id),
    FOREIGN KEY (shipping_id) REFERENCES Shipments(shipping_id)
);

/*Create Shipments Table*/
CREATE TABLE Shipments (
    shipping_id int UNIQUE,
    user_id int,
    delivery_time TIMESTAMP,
    carrier varchar(50),
    tracking_number int,
    PRIMARY KEY (shipping_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

/*Create Payments Table*/
CREATE TABLE Payments (
    payment_amount DECIMAL (10, 2) NOT NULL,
    order_id int NOT NULL,
    currency varchar(15) NOT NULL,
    payment_method varchar(15) NOT NULL,
    PRIMARY KEY (payment_amount),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);

/*Create PokemonCardSpecs Table*/
CREATE TABLE PokemonCardSpecs (
    product_id int NOT NULL,
    card_name varchar(50) NOT NULL,
    price DECIMAL (10, 2) NOT NULL,
    grade varchar(10) NOT NULL,
    holographic varchar(11),
    edition varchar(12),
    quantity_available int,
    card_set varchar(20),
    language varchar(20),
    PRIMARY KEY (product_id)
);

/*Create Intersection Table*/
CREATE TABLE PokemonCardSpecs_Orders (
    order_id int,
    product_id int,
	PRIMARY KEY (order_id, product_id),
	FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES PokemonCardSpecs(product_id) ON DELETE CASCADE
);

/*------------------------------
    Add data to tables
------------------------------*/

/* Insert Users Data*/
INSERT INTO Users (
    user_id,
    username,
    password,
    first_name,
    last_name,
    email,
    birthday,
    address
)
VALUES 
(
    1,
    "aketchum",
    "catchemall",
    "Ash",
    "Ketchum",
    "ash.ketchum@gmail.com",
    "1987-05-22",
    "123 Shimoda Way, Pallet Town, Kanto"
),
(
    2,
    "goak",
    "321cba",
    "Gary",
    "Oak",
    "gary.oak@gmail.com",
    "1947-05-12",
    "1 Oak Lab, Pallet Town, Kanto"
),
(
    3,
    "kasumi",
    "doyoumistme",
    "Misty",
    NULL,
    "kasumi@outlook.com",
    "1985-04-01",
    "151 Mermaid Street, Cerulean City, Kanto"
);

/*Insert Orders Data*/
INSERT INTO Orders (
    order_id,
    user_id,
    product_id,
    shipping_id,
    customer_name,
    quantity_purchased,
    transaction_date
)
VALUES
(
    1,
    1,
    1,
    25,
    "Ash Ketchum",
    3,
    "2015-11-27"
),
(
    2,
    2,
    2,
    15,
    "Gary Oak",
    1,
    "2020-03-01"
),
(
    3,
    3,
    3,
    10,
    "Misty",
    151,
    "2023-03-25"
);

/*Insert Shipments Data*/
INSERT INTO Shipments (
    shipping_id,
    user_id,
    delivery_time,
    carrier,
    tracking_number
)
VALUES
(
    10,
    3,
    "2023-04-01 15:57:01",
    "UPS",
    77777777
),
(
    15,
    2,
    "2020-03-23 09:17:23",
    "USPS",
    12345678
),
(
    25,
    1,
    "2015-12-23 20:20:20",
    "FEDEX",
    98765432
);

/*Insert Payments data*/
INSERT INTO Payments (
    payment_amount,
    order_id,
    currency,
    payment_method
)
VALUES
(
    1021.00,
    1,
    "USD",
    "Mastercard"
),
(
    1.51,
    2,
    "USD",
    "Visa"
),
(
    11.11,
    3,
    "JPY",
    "Cash"
);

/*Insert PokemonCardSpecs Data*/
INSERT INTO PokemonCardSpecs (
    product_id,
    card_name,
    price,
    grade,
    holographic,
    edition,
    quantity_available,
    card_set,
    language
)
VALUES
(
    1,
    "Charizard",
    10000.00,
    9,
    "holo",
    "first",
    1,
    "Base",
    "English"
),
(
    2,
    "Blastoise",
    7000.00,
    9,
    "holo",
    "first",
    2,
    "Base",
    "Japanese"
),
(
    3,
    "Venusaur",
    3000.00,
    9,
    "non-holo",
    "second",
    1,
    "Base",
    "English"
);


/*enable commits and foreign key checks*/
SET FOREIGN_KEY_CHECKS=1;
COMMIT;