-- Link to Db Fiddle https://www.db-fiddle.com/f/4pyrD3WoUqg8MWoCEkMnXB/0--
CREATE TABLE IF NOT EXISTS `Features` (
  `key` varchar(50) NOT NULL,
  `F1` int(6) NOT NULL,
  `F2` int(6) NOT NULL,
  PRIMARY KEY (`key`)
) DEFAULT CHARSET=utf8;

INSERT INTO `Features` (`key`, `F1`, `F2`) VALUES
  ('k1', '3', '3'),
  ('k2', '5', '4'),
  ('k3', '4', '3'),
  ('k4', '4', '2');

CREATE TABLE IF NOT EXISTS `Predictions` (
  `key` varchar(50) NOT NULL,
  `Price` int(8) NOT NULL
) DEFAULT CHARSET=utf8;
INSERT INTO `Predictions` (`key`, `price`) VALUES
  ('k2', '500'),
  ('k4', '350'),
  ('k3', '400'),
  ('k1', '300');

SELECT f.key, f.F1, f.F2, p.price
        FROM Features f
            JOIN Predictions p
                on f.key=p.key;
