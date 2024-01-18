-- File: Task 4
-- creates a trigger that decreases the quantity of an item after adding a new order.

DELIMITER //
CREATE TRIGGER decreases_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
//