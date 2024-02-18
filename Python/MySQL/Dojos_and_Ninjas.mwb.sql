
-- INSERT INTO dojos (name)
-- VALUES ("Austin"), ("Dallas"), ("Houston");

-- SET SQL_SAFE_UPDATES=0;
-- DELETE FROM dojos;

-- INSERT INTO dojos (name)
-- VALUES ("Austin"), ("Dallas"), ("Houston");

-- INSERT INTO ninjas (first_name, last_name, age, dojo_id)
-- VALUES ("Randall", "Wolfe", 28, 4), ("Terry", "Tillman", 31, 4), ("Natalie", "Toressdey", 32, 4),
-- 		("Randall", "Wolfe", 28, 5), ("Terry", "Tillman", 31, 5), ("Natalie", "Toressdey", 32, 5),
--         ("Randall", "Wolfe", 28, 6), ("Terry", "Tillman", 31, 6), ("Natalie", "Toressdey", 32, 6); 

-- SELECT * FROM dojos
-- LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
-- WHERE dojos.id = 4

-- SELECT * FROM dojos
-- LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
-- WHERE dojos.id = 6

-- SELECT dojos.id AS dojo_id, dojos.name AS dojo_name
-- FROM dojos
-- LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
-- ORDER BY ninjas.id DESC
-- LIMIT 1;

-- SELECT ninjas.id AS ninja_id, ninjas.first_name, ninjas.last_name, ninjas.age,
--        dojos.id AS dojo_id, dojos.name AS dojo_name
-- FROM ninjas
-- JOIN dojos ON ninjas.dojo_id = dojos.id
-- WHERE ninjas.id = 6;

-- SELECT ninjas.id AS ninja_id, ninjas.first_name, ninjas.last_name, ninjas.age,
--        dojos.id AS dojo_id, dojos.name AS dojo_name
-- FROM ninjas
-- JOIN dojos ON ninjas.dojo_id = dojos.id;



