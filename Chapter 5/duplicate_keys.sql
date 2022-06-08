
CREATE TABLE IF NOT EXISTS `Features` (
  `key` int(6) NOT NULL,
  `F1` int(6) NOT NULL,
  `F2` int(6) NOT NULL
) DEFAULT CHARSET=utf8;

INSERT INTO `Features` (`key`, `F1`, `F2`) VALUES
  (0, '3', '2'),
  (1, '5', '4');

 INSERT INTO `Features` (`key`, `F1`, `F2`) VALUES
  (0, '3', '3'),
  (1, '5', '5');

CREATE TABLE IF NOT EXISTS `Predictions` (
  `key` varchar(50) NOT NULL,
  `Price` int(8) NOT NULL
) DEFAULT CHARSET=utf8;
INSERT INTO `Predictions` (`key`, `price`) VALUES
  (1, '500'),
  (0, '300');

  INSERT INTO `Predictions` (`key`, `price`) VALUES
  (0, '320'),
  (1, '550');


  SELECT f.key, f.F1, f.F2, p.price
	FROM Features f
    	JOIN Predictions p
        	on f.key=p.key
            	order by f.key;



