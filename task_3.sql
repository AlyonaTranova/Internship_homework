-- 1. Найдите пару аэропортов, наиболее удалённых друг от друга.
SELECT a1.airport_name AS "из", a2.airport_name AS "в", a1.coordinates <@> a2.coordinates AS "расстояние"
  FROM airports a1 
  JOIN airports a2 ON a1.airport_name <> a2.airport_name
  ORDER BY "расстояние" DESC 
  LIMIT 1;
  
-- 2. Выведите название самолёта с наибольшим количеством мест на борт

SELECT s.aircraft_code, a.model, COUNT( * ) AS num_seats
  FROM seats s 
  JOIN aircrafts a ON s.aircraft_code = a.aircraft_code 
  GROUP BY 1, 2 
  ORDER BY 3 DESC 
  LIMIT 1; 
  
-- 3. Для заданного самолёта, перенумеруйте его места эконом-класса в алфавитном порядке, и для каждого места укажите его номер в этом перечислении. 
SELECT *, rank() OVER(PARTITION BY seats.fare_conditions ORDER BY seat_no) 
  FROM bookings.seats 
  WHERE seats.aircraft_code = '773' AND seats.fare_conditions = 'Economy' 
  ORDER BY seat_no collate "C";
  
-- запросы на pl/sql

EXPLAIN SELECT * FROM routes 
  WHERE routes.departure_airport = 'DME';
-- Nested Loop (cost=1032.14..1354.55 rows=150 width=195)

EXPLAIN SELECT * FROM bookings.routes, bookings.aircrafts_data 
  WHERE bookings.routes.aircraft_code = bookings.aircrafts_data.aircraft_code 
  LIMIT 5; 
-- Hash Join  (cost=2447.75..3038.10 rows=12 width=247)

EXPLAIN SELECT * FROM bookings.boarding_passes 
  INNER JOIN bookings.flights ON(bookings.boarding_passes.flight_id=bookings.flights.flight_id) 
  LIMIT 10;
-- Merge Join  (cost=0.71..40680.53 rows=579686 width=88)

EXPLAIN SELECT * FROM bookings.tickets 
  JOIN bookings.boarding_passes ON(bookings.tickets.ticket_no = bookings.boarding_passes.ticket_no) 
  JOIN bookings.flights ON(bookings.boarding_passes.flight_id = bookings.flights.flight_id) 
  WHERE bookings.tickets.passenger_name = 'VALERIY TIKHONOV' 
  ORDER BY flights.scheduled_departure 
  LIMIT 10;
-- Gather Merge  (cost=9290.79..9295.92 rows=44 width=200)

