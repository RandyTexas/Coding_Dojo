
CREATE TABLE books
(
  id           INT          NOT NULL AUTO_INCREMENT,
  created_at   timestamp    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at   timestamp    NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  title        VARCHAR(250) NOT NULL,
  num_of_pages INT          NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE favorites
(
  id         INT       NOT NULL AUTO_INCREMENT,
  created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  user_id    INT       NOT NULL,
  book_id    INT       NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE users
(
  id         INT          NOT NULL AUTO_INCREMENT,
  created_at timestamp    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp    NOT NULL DEFAULT CURRENT_TIMESTAMP ON  UPDATE CURRENT_TIMESTAMP,
  name       VARCHAR(100) NOT NULL,
  PRIMARY KEY (id)
);

ALTER TABLE favorites
  ADD CONSTRAINT FK_users_TO_favorites
    FOREIGN KEY (user_id)
    REFERENCES users (id);

ALTER TABLE favorites
  ADD CONSTRAINT FK_books_TO_favorites
    FOREIGN KEY (book_id)
    REFERENCES books (id);
        
      