
DROP KEYSPACE if  exists  k1;
CREATE KEYSPACE if not exists  k1
  WITH REPLICATION = { 
   'class' : 'SimpleStrategy', 
   'replication_factor' : 1 
  };

use k1

 Create table user(
				id int,
				username text,
				password text,
				twitter_api_token text, 
				twitter_api_token_secret text,
				limit_val int,
				reset_time date,
				primary key(id));

INSERT INTO user(id,username,password,twitter_api_token,twitter_api_token_secret)  VALUES ('0', 'root', '1234','2288544008-lgy6s9tdgKyeZqxa2QUAZyrnptB8S7NQEF8RNbw','koXqZyKO5Nx5W2OAqGrVsXa8pObQg6ZyzvyJusUEUReP3' );

Create table userApp(
					author_id text,
					appToken text,
					appSecret text,
					primary key(author_id)
);

Create table dataset(
					id uuid,
					creator_id text,
					description text,
					creation_date date,
					primary key(id,creator_id)
);
Create table avalible_tokens(
						id int,
						user_id int,
						primary key(id,user_id)
);
					
Create table tweets(
				id text,
				data text,
				author_id text,
				primary key(id,author_id)
);
