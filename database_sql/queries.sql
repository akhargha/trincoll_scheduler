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

-- Retreive all friends of a specific user (Lily in this case)
SELECT 'Retreive all friends of a specific user:' as Query;
SELECT U.username AS friend_name 
FROM Friends F
JOIN Users U ON (F.user_id = U.user_id OR F.friend_id = U.user_id)
WHERE (F.user_id = 2 OR F.friend_id = 2) AND U.user_id != 2 AND F.status = 'Accepted';

-- Retreive all pending friend requests of a specific user (Lily in this case)
SELECT 'Retreive all pending friend requests of a specific user' as Query;
SELECT U.username AS friend_request_from, F.date_sent 
FROM Friends F
JOIN Users U ON F.user_id = U.user_id
WHERE F.friend_id = 2 AND F.status = 'Pending';

-- Retreive all courses added by friends for a specific user (in this case, for Anupam)
SELECT 'Retreive all courses added by friends for a specific user' as Query;
SELECT C.course_name, U.username AS added_by, A.timestamp AS date_added
FROM AuditTrail A
JOIN Courses C ON A.course_id = C.course_id
JOIN Users U ON A.friend_id = U.user_id
WHERE A.user_id = 1;
