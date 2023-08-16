# Trinity College Course Scheduler
Project by Anupam Khargharia.

## Overview
This course scheduler is a course scheduler and sharing tool to streamline the process of course scheduling and planning events/meetings with friends. This scheduler adds visualizations to your schedule and acts as a platform to share your schedule with your friends so that they are aware of your time commitments when making plans (and vice-versa!)

## Key Features
1. (TBD)<ins>Course Input:</ins> Input your course code and the app will auto-fetch all the course details. No need to manually enter course details like times and names now!

2. (TBD)<ins>Visual Schedule Representation:</ins> Get a clean and color-coded visualization of your weekly schedule.

3. (TBD)<ins>Social Tools:</ins> Share your schedule with your friends using the social tool in the webapp. This is especially helpful when you are planning an event and have to take schedules of multiple people into consideration.

4. (TBD)<ins>Secure User Management:</ins> Robust user authentication and care for your data and privacy.

## Entities
* <ins>Users:</ins> Represents registered users on the platform.
* <ins>Courses:</ins> Courses available to add to your schedule.
* <ins>UserCourses:</ins> Courses that users have in their schedule.
* <ins>Friends:</ins> Represents friend relationship between users.
* <ins>Course AuditTrial:</ins> Represents an audit trial for courses added by friends.

## Database Schema
* <ins>Users:</ins>
* * user_id: INTEGER, Primary Key, Auto Increment
  * username: STRING, Unique
  * email: STRING, Unique
  * password: STRING (Hashed and salted)
  * first_name: STRING
  * last_name: STRING
* <ins>Courses:</ins>
* * course_id: INTEGER, Primary Key, Auto Increment
  * course_code: STRING, Unique
  * course_name: STRING
  * course_time_start: TIME
  * course_time_end: TIME
  * course_days: STRING (e.g., "MWF" for Monday-Wednesday-Friday)
* <ins>UserCourses:</ins>
* * user_course_id: INTEGER, Primary Key, Auto Increment
  * user_id: INTEGER, Foreign Key referencing Users
  * course_id: INTEGER, Foreign Key referencing Courses
* <ins>Friends:</ins>
* * friend_id: INTEGER, Primary Key, Auto Increment
  * user_id1: INTEGER, Foreign Key linking to user_id in the Users table
  * user_id2: INTEGER, Foreign Key linking to user_id in the Users table
  * permission_to_add_course: BOOLEAN, Default to false
* <ins>Course AuditTrial:</ins>
* * audit_id: INTEGER, Primary Key, Auto Increment
  * user_id: INTEGER, Foreign Key linking to user_id in the Users table (refers to the user whose data was changed)
  * friend_id: INTEGER, Foreign Key linking to user_id in the Users table (refers to the friend who made the change)
  * action: STRING (e.g., "Added Course") with a default value of "Added Course"
  * course_id: INTEGER, Foreign Key linking to course_id in the Courses table (refers to the course that was added/affected, if applicable)
  * timestamp: TIMESTAMP, Default to current date and time

