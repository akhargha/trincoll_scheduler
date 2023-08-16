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

-- Retreive all courses by a specific user (Anupam in this case)
SELECT 'Retreive all courses by a specific user:' as Query;
SELECT C.course_name 
FROM UserCourses UC
JOIN Courses C ON UC.course_id = C.course_id
WHERE UC.user_id = 1;