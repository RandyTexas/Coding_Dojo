
        
CREATE TABLE dojos
(
  id         INT          NOT NULL AUTO_INCREMENT,
  created_at timestamp    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp    NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  name       VARCHAR(225) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE dojos_ninjas
(
  id         INT       NOT NULL AUTO_INCREMENT,
  created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  dojo_id    INT       NOT NULL,
  ninja_id   INT       NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE ninjas
(
  id         INT          NOT NULL AUTO_INCREMENT,
  created_at timestamp    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp    NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  first_name VARCHAR(225) NOT NULL,
  last_name  VARCHAR(225) NOT NULL,
  age        INT          NOT NULL,
  PRIMARY KEY (id)
);

ALTER TABLE dojos_ninjas
  ADD CONSTRAINT FK_dojos_TO_dojos_ninjas
    FOREIGN KEY (dojo_id)
    REFERENCES dojos (id);

ALTER TABLE dojos_ninjas
  ADD CONSTRAINT FK_ninjas_TO_dojos_ninjas
    FOREIGN KEY (ninja_id)
    REFERENCES ninjas (id);
