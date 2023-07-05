-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Find crime scene description.
SELECT description FROM crime_scene_reports
WHERE month = 7 AND day = 28
AND street = 'Humphrey Street';
-- Look into transcript of the interviews of witnesses
SELECT transcript FROM interviews
WHERE month = 7 AND day = 28
AND transcript LIKE "%bakery%";

SELECT * FROM atm_transactions
WHERE month = 7 AND day = 28
AND atm_location = "Leggett Street";