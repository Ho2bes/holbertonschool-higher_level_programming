-- Find the cities in the state of 'California' and order them by their id.
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id AND states.name = 'California'
ORDER BY cities.id;
