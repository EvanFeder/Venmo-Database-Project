-- Setup the database for a very simple 'social network'.
-- Friends - Users - Messages 

\c postgres
DROP DATABASE IF EXISTS venmo;

CREATE database venmo;
\c venmo

\i create.SQL

\copy Users(user_id, email, balance)										FROM 'users.csv' csv header 
\copy Personal_Users(first_name, last_name, gender, age, user_id)			FROM 'personal_users.csv' csv header
\copy Business_Users(name, user_id)											FROM 'business_users.csv' csv header
\copy Transactions(amount, description, privacy, timestamp)					FROM 'transactions.csv' csv header
\copy P2P_Transactions(transaction_id, user_id_sender, user_id_receiver)	FROM 'p2p_transactions.csv' csv header
\copy P2B_Transactions(transaction_id, user_id_personal, user_id_business)	FROM 'p2b_transactions.csv' csv header
\copy Comments(comment, timestamp, user_id, transaction_id)					FROM 'comments.csv' csv header
\copy Likes(user_id, transaction_id, timestamp)								FROM 'likes.csv' csv header
\copy Banks(name)															FROM 'banks.csv' csv header
\copy Connect_With(user_id, bank_id)										FROM 'connect_with.csv' csv header
\copy Goods_Services(price, name)											FROM 'goods_services.csv' csv header
\copy Bought(transaction_id, item_id, quantity)								FROM 'bought.csv' csv header
\copy Employees(first_name, last_name, department)							FROM 'employees.csv' csv header
\copy Feedbacks(comment, timestamp, user_id)								    FROM 'feedback.csv' csv header
\copy Review(feedback_id, employee_id)										FROM 'review.csv' csv header
-- ============================================================
  
