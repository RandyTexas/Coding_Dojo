CREATE TABLE friendships
(
  id         INT       NOT NULL AUTO_INCREMENT,
  created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  user_id    INT       NOT NULL,
  friend_id  INT       NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE users
(
  id         INT          NOT NULL AUTO_INCREMENT,
  created_at timestamp    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp    NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  first_name VARCHAR(100) NOT NULL,
  last_name  VARCHAR(100) NOT NULL,
  PRIMARY KEY (id)
);

ALTER TABLE friendships
  ADD CONSTRAINT FK_users_TO_friendships
    FOREIGN KEY (user_id)
    REFERENCES users (id);

ALTER TABLE friendships
  ADD CONSTRAINT FK_users_TO_friendships1
    FOREIGN KEY (friend_id)
    REFERENCES users (id);

        
      