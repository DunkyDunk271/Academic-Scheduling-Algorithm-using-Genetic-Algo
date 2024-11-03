# Academic Scheduling Algorithm
## Introduction:
This project addresses the University Timetable Problem (UTP), which involves creating a complete weekly timetable given the data of timeslots, professors, and courses. The UTP is known for its complexity and is classified as NP-hard, meaning it cannot be solved within reasonable time complexity using a deterministic algorithm. Various educational institutions have explored this complex problem using different approaches. 

Despite the efficiency of these existing methods, they are not optimal when dealing with large data inputs due to the NP-hard nature of the problem. Our work aims to find improvements based on Dahiya's Course Scheduling Algorithm. By addressing these gaps, we hope to develop an efficient algorithm for Vin University and lay a foundation for further research projects. 

To address the inefficiency and create a more balanced learning experience, we propose developing an algorithm that optimizes class scheduling and teaching assignments. This approach aims to ensure a balanced workload distribution throughout the week, enabling students to manage their time more effectively and maximize their learning potential. 

## I. Set up the Flask application

1. Using venv (Built-in Python Module):
  - Open a terminal or command prompt.
  - Navigate to the directory where you want to create your Flask project.
  - Run the following command to create a virtual environment(replace myenv with your desired environment name):

    `python -m venv myenv`

  - Activate the virtual environment based on your operating system:

    Windows:

    `myenv\Scripts\activate`

    Linux/macOS:

    `source myenv/bin/activate`

2. Using virtualenv:
  - Install virtualenv if you haven’t already:

    `pip install virtualenv`

  - Navigate to your project directory.
  - Create a virtual environment:

    `virtualenv myenv`

  - Activate the environment:

    Windows:

    `myenv\Scripts\activate`

    Linux/macOS:

    `source myenv/bin/activate`

## II. Install the requirement:
Install the required libraries for running application.

  `pip install -r "requirements.txt"`

## III. Create the database:
1. Install MySQL from this link:  
[MySQL for Window](https://dev.mysql.com/downloads/installer/)

2. Table structure for table `events`:
  ``` 
  CREATE TABLE `events` (
      `id` int unsigned NOT NULL AUTO_INCREMENT,
      `course` varchar(255) NOT NULL,
      `credits` int NOT NULL DEFAULT '1',
      `professor` varchar(255) NOT NULL,
      `room` varchar(255) NOT NULL,
      `start` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      `end` timestamp NOT NULL,
      PRIMARY KEY (`id`)
  ) ENGINE = InnoDB AUTO_INCREMENT = 114 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci
  ```
3. Table structure for table `events`:
```
CREATE TABLE `user` (
    `userid` int unsigned NOT NULL AUTO_INCREMENT,
    `name` varchar(100) NOT NULL,
    `email` varchar(100) NOT NULL,
    `password` varchar(100) NOT NULL,
    PRIMARY KEY (`userid`)
) ENGINE = InnoDB AUTO_INCREMENT = 3 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci
```
## IV. Run the application:
1. First check all the requirements and database:
- With requirements, check it using command below:

  `flask --version`
2. Open the terminal of project folder and run the command:

   `flask run`

3. Open the link to application and create the user.
4. Then back to login interface and login in.
5. Click on "Generate" button to run the algorithm and result will show on the calendar.
