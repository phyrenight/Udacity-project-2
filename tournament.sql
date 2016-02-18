-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
CREATE TABLE PLAYERS ( id SERIAL, name CHAR(80));
CREATE TABLE MATCHES( match_up SERIAL,  winner INTEGER,  loser INTEGER);

CREATE VIEW t_matches AS SELECT players.id, players.name,
    count(matches.match_up) AS total_matches FROM players
    LEFT OUTER JOIN matches ON (players.id = matches.winner
	OR players.id = matches.loser) GROUP BY (id, name);	
CREATE VIEW t_wins AS SELECT players.id, COUNT(matches.winner)
    AS total_wins FROM players LEFT OUTER JOIN matches ON
	(players.id = matches.winner) GROUP BY id;
CREATE VIEW standings AS SELECT t_wins.id, t_matches.name,
    t_wins.total_wins, t_matches.total_matches FROM t_wins
	LEFT OUTER JOIN matches ON (t_wins.id = t_matches.id) GROUP BY
	(t_wins.id, t_matches.name, t_wins.total_wins, t_matches.total_matches);