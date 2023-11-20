/*------------------------------
    Group 77: Michael Rigali & Derrick Higgins
    PokéCollect
    Michael Rigali & Derrick Higgins 
------------------------------*/

-- SELECT
-- select all Users
SELECT * FROM Users;
-- select all Cats
SELECT customer_name, quantity_purchased, transaction_date FROM Orders;
-- select all Shipments
SELECT delivery_time, carrier, tracking_number FROM Shipments;
-- select all Payments
SELECT payment_amount, currency, payment_method FROM Payments;
-- select all PokemonCardSpecs
SELECT card_name, price, grade, holographic, edition, quantity_available, card_set, language FROM Room_Types;

-- INSERT
-- insert a user
INSERT INTO Users (username, password, first_name, last_name, email, birthday, address) VALUES (:username, :password, :first_name, :last_name, :email, :birthday, :address);
-- insert an order
INSERT INTO Orders (customer_name, quantity_purchased, transaction_date) VALUES (:customer_name, :quantity_purchased, :transaction_date);
-- insert a shipment
INSERT INTO Shipments (delivery_time, carrier, tracking_number) VALUES (:delivery_time, :carrier, :tracking_number);
-- insert a payment
INSERT INTO Payments (payment_amount, currency, payment_method, order_id) VALUES (:payment_amount, :currency, :payment_method, order_id_input_from_dropdown);
-- insert a pokemoncardspec
INSERT INTO PokemonCardSpecs (card_name, price, grade, holographic, edition, quantity_available, card_set, language) VALUES (:card_name, :price, :grade, :holographic, :edition, :quantity_available, :card_set, :language);
-- insert a new PokemonCardSpecs_Orders relationship
INSERT INTO PokemonCardSpecs_Orders (order_id, product_id) VALUES (:order_id, :product_id);

-- UPDATE
-- Update a user
UPDATE Users SET username = :username, password = :password, first_name = :first_name, last_name = :last_name, email = :email, birthday = :birthday, address = :address WHERE user_id = :user_id;
-- update an order
UPDATE Orders SET customer_name = :customer_name, quantity_purchased = :quantity_purchased, transaction_date = :transaction_date WHERE order_id = :order_id;
-- update a shipment
UPDATE Shipments SET delivery_time = :delivery_time, carrier = :carrier, tracking_number = :tracking_number WHERE shipping_id = :shipping_id;
-- update a paymenmt
UPDATE Payments SET currency = :currency, payment_method = :payment_method WHERE payment_amount = :payment_amount;
-- update a PokemonCardSpec
UPDATE PokemonCardSpecs SET card_name = :card_name, price = :price, grade = :grade, holographic = :holographic, edition = :edition, quantity_available = :quantity_available, card_set = :card_set, language = :language WHERE product_id = :product_id;
-- update a PokemonCardSpecs_Orders relationship
UPDATE PokemonCardSpec_Order SET new_order_id = :new_order_id , new_product_id = :new_product_id, quantity = :new_quantity WHERE order_id = :order_id AND product_id = product_id;


-- DELETE
-- delete a user
DELETE FROM Users WHERE user_id = :user_id;
-- delete an order
DELETE FROM Orders WHERE order_id = :order_id;
-- delete a shipment
DELETE FROM Shipments WHERE shipping_id = :shipping_id;
-- delete a payment
DELETE FROM Payments WHERE payment_amount = :payment_amount;
-- delete a PokemonCardSpec
DELETE FROM PokemonCardSpecs WHERE product_id = :product_id;
-- delete a PokemonCardSpec_Order relationship
DELETE FROM PokemonCardSpecs_Orders WHERE product_id = :product_id AND order_id = :order_id;