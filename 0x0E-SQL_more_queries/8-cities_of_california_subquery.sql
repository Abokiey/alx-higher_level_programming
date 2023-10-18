-- lists all cities found in the database

SELECT id, name FROM CITIES
WHERE state_id = (SELECT id FROM states WHERE name = "California")
ORDER BY id;
