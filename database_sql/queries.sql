-- Retreive all users
SELECT 'Retreive all users:' as Query;
SELECT * FROM Users;

-- Retreive all courses
SELECT 'Retreive all courses:' as Query;
SELECT * FROM Courses;

-- Course Search
SELECT 'Search for Course using course code:' as Query;
SELECT * 
FROM Courses 
WHERE course_code = '101';