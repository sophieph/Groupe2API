create table user (
  id integer primary key autoincrement,
  username varchar(250),
  email varchar(15),
  password text
);

create table favourite (
    id integer primary key autoincrement,
    pokemon varchar(250),
    user_id int,
    FOREIGN KEY (user_id) REFERENCES user(id)
);
