-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- deletes previous p[layers and Matches tables
DROP DATABASE TOURNAMENT;

--create database
CREATE DATABASE TOURNAMENT;
\connect tournament
-- creates the tournament tables
CREATE TABLE PLAYERS ( id SERIAL PRIMARY KEY, name TEXT);
CREATE TABLE MATCHES( match_up SERIAL PRIMARY KEY,  winner INTEGER REFERENCES PLAYERS(id),  loser INTEGER REFERENCES PLAYERS(id);

-- create the views for the tournament
CREATE VIEW T_MATCHES AS SELECT PLAYERS.id AS id, PLAYERS.name AS name,
    COUNT(MATCHES.match_up) AS total_matches FROM PLAYERS
    LEFT OUTER JOIN MATCHES ON (PLAYERS.id = MATCHES.winner
	OR PLAYERS.id = MATCHES.loser) GROUP BY id, name;	
CREATE VIEW T_WINS AS SELECT PLAYERS.id, COUNT(MATCHES.winner)
    AS total_wins FROM PLAYERS LEFT OUTER JOIN MATCHES ON
	(players.id = matches.winner) GROUP BY id;
CREATE VIEW STANDINGS AS SELECT T_WINS.id, T_MATCHES.name,
    T_WINS.total_wins, T_MATCHES.total_matches FROM T_WINS
	LEFT OUTER JOIN T_MATCHES ON (T_WINS.id = T_MATCHES.id) GROUP BY
	T_WINS.id, T_MATCHES.name, T_WINS.total_wins, T_MATCHES.total_matches;
