-- Простые запросы на sql

SELECT * FROM airports WHERE airports.city = 'Москва';
SELECT * FROM routes WHERE routes.departure_airport = 'DME';
SELECT * FROM bookings.tickets WHERE bookings.tickets.passenger_name = 'MAKSIM ZHUKOV';


EXPLAIN SELECT * FROM routes 
  WHERE routes.departure_airport = 'DME';
-- Nested Loop (cost=1032.14..1354.55 rows=150 width=195)

EXPLAIN SELECT * FROM bookings.routes, bookings.aircrafts_data 
  WHERE bookings.routes.aircraft_code = bookings.aircrafts_data.aircraft_code 
  LIMIT 5; 
-- Hash Join  (cost=2447.75..3038.10 rows=12 width=247)

-- С использованием INNER JOIN
EXPLAIN SELECT * FROM bookings.boarding_passes 
  INNER JOIN bookings.flights ON(bookings.boarding_passes.flight_id=bookings.flights.flight_id) 
  LIMIT 10;
-- Merge Join  (cost=0.71..40680.53 rows=579686 width=88)

SELECT * FROM bookings.tickets 
  JOIN bookings.boarding_passes ON(bookings.tickets.ticket_no = bookings.boarding_passes.ticket_no) 
  JOIN bookings.flights ON(bookings.boarding_passes.flight_id = bookings.flights.flight_id) 
  WHERE bookings.tickets.passenger_name = 'VALERIY TIKHONOV' 
  ORDER BY flights.scheduled_departure 
  LIMIT 10;
-- Gather Merge  (cost=9290.79..9295.92 rows=44 width=200)
