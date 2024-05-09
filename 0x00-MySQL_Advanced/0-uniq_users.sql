--a sql script that creates a table users
--if the table already exits, the script fails
DELIMITER $$
CREATE TRIGGER confirm BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END $$
DELIMITER;