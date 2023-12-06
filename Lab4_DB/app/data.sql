-- Inserting data into Movie
INSERT INTO Movie (name, genre, release_date, director, duration_minutes) VALUES
('Inception', 'Sci-Fi', '2010-07-16', 'Christopher Nolan', 148),
('The Shawshank Redemption', 'Drama', '1994-09-23', 'Frank Darabont', 142),
('The Dark Knight', 'Action', '2008-07-18', 'Christopher Nolan', 152),
('Pulp Fiction', 'Crime', '1994-10-14', 'Quentin Tarantino', 154),
('Forrest Gump', 'Drama', '1994-07-06', 'Robert Zemeckis', 142),
('The Godfather', 'Crime', '1972-03-24', 'Francis Ford Coppola', 175),
('The Matrix', 'Action', '1999-03-31', 'The Wachowskis', 136),
('Schindler''s List', 'Biography', '1993-11-30', 'Steven Spielberg', 195),
('Fight Club', 'Drama', '1999-10-15', 'David Fincher', 139),
('Inglourious Basterds', 'Adventure', '2009-08-21', 'Quentin Tarantino', 153);

-- Inserting data into BoxOffice
INSERT INTO BoxOffice (total_gross, opening_weekend, movie_id) VALUES
(829895144, 62785337, 1),
(289317794, 7273270, 2),
(1004558444, 158411483, 3),
(213928762, 93000, 4),
(678226205, 24717811, 5),
(246120986, 3023932, 6),
(465343787, 27788348, 7),
(322208889, 6566364, 8),
(100851705, 11045010, 9),
(321455689, 38403780, 10);

-- Inserting data into Review
INSERT INTO Review (review_text, rating, visit_date, user_id, movie_id) VALUES
('Mind-bending plot!', 4.5, '2023-11-15', 1, 1),
('A masterpiece.', 4.7, '2023-11-20', 2, 2),
('Thrilling action!', 4.9, '2023-10-05', 4, 3),
('Cinematic excellence.', 4.6, '2023-10-10', 3, 4),
('Heartwarming story.', 4.8, '2023-10-25', 5, 5),
('Twists and turns.', 4.4, '2023-10-30', 6, 6),
('Captivating performances.', 4.3, '2023-11-01', 7, 7),
('Emotional journey.', 4.5, '2023-11-05', 8, 8),
('Thought-provoking.', 4.2, '2023-11-10', 9, 9),
('Quentin brilliance.', 4.7, '2023-11-20', 10, 10);
