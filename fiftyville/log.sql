-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Find crime scene description.
SELECT description FROM crime_scene_reports
WHERE month = 7 AND day = 28
AND street = 'Humphrey Street';
-- Look into transcript of the interviews of witnesses
SELECT transcript FROM interviews
WHERE month = 7 AND day = 28
AND transcript LIKE "%bakery%";
-- See transactions of the thief before the theft
SELECT * FROM atm_transactions
WHERE month = 7 AND day = 28
AND atm_location = "Leggett Street";
-- See license plate of the suspect car
SELECT * FROM bakery_security_logs
WHERE month = 7 AND day = 28;
-- Look into phone calls that were made this time
SELECT * FROM phone_calls
WHERE month = 7 AND day = 28
AND duration < 60;
-- Look into a person with the same license plate
SELECT * FROM people
WHERE license_plate = "0NTHK55";
--Finding tickets
SELECT * FROM airports
WHERE city = "Fiftyville";

SELECT * FROM flights
JOIN airports ON airports.id = flights.origin_airport_id
WHERE airports.id = 8
AND month = 7 AND day = 29 ORDER BY hour ASC;
--Finding SUSPECT's accomplice
SELECT * FROM people
WHERE phone_number = "(717) 555-1342";
--Looking into passengers
SELECT * FROM passengers
JOIN flights ON flights.id = passengers.flight_id
JOIN people ON people.passport_number = passengers.passport_number
WHERE passengers.passport_number = "8294398571";
--Finding city where SUSPECT escaped to
SELECT * FROM airports
   ...> WHERE id = 4;

