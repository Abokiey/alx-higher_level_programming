-- lists all cities contained in database

USE hbtn_0d_usa;
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
JOIN states ON cities.state_id = state.id
ORDER BY cities.id ASC;
