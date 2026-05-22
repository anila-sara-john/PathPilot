# **PathPilot – Career Suitability Evaluation Web Application**
PathPilot is a simple web-based career suitability evaluation system developed as a mini project.

The project helps users evaluate how suitable they are for a selected career using a questionnaire-based weighted scoring system. Users can choose a stream and career of interest, answer career-specific questions, and receive a suitability evaluation along with suggestions.

## **Features**
- User registration and login authentication
- Stream selection
- Career selection based on stream
- Career-specific questionnaire system
- Weighted score calculation
- Suitability evaluation (High/Medium/Low)
- Result display
- Results history tracking for previous evaluations

## **Admin Features**
- Admin login
- Manage users
- Add/Edit/Delete streams
- Add/Edit/Delete careers
- Add/Edit/Delete questionnaires

## **Tools and Technologies Used**
- HTML - Used to structure the web pages of the application.
- CSS - Used to design and style the user interface.
- Flask - Used as the backend framework to handle routing and application logic.
- MySQL - Used as the database to store users, careers, questions, and results data.
- Visual Studio Code - Used for project development and code editing.
- MySQL Workbench – Used for database management and SQL operations.

## **How the System Works**
1. User registers and logs into the system.
2. User selects a stream and career of interest.
3. The system displays predefined career-specific questions.
4. Each “Yes” response adds the weight assigned to that question.
5. The compatibility score is calculated using: $$Compatibility Score = (Total Points Obtained / Maximum Possible Points) × 100$$
6. Based on the final score, the system determines suitability:
   - High (if Compatibility Score >= 70)
   - Medium (if Compatibility Score >= 40)
   - Low (if Compatibility Score < 40)
7. The result is displayed and stored in the results history.

## **Installation & Setup**
1. Clone the repository
   ```bash
   git clone https://github.com/anila-sara-john/PathPilot.git
   ```
2. Navigate to the project folder
   ```bash
   cd PathPilot
   ```

3. Configure MySQL database
   - Install and set up MySQL Workbench
   - Create a MySQL database
   - Import the SQL dump file located in:
     ` database/Dump20260306.sql `
   - Update the database credentials in app.py
5. Run the application
   ```bash
   python app.py
   ```

## **Future Improvements**
- Dynamic questionnaires
- More career domains and streams
- Advanced recommendation logic
- Improved UI/UX
- Analytics Dashboard

## **Credits**

This project was developed with the help of the following learning resources and references:

- **Flask Tutorial Guidance:**  
  [Flask Tutorial by Yes Tech Media](https://www.youtube.com/@YesTechMedia) — Helped in understanding Flask fundamentals and backend development concepts.

- **MySQL Workbench Setup Reference:**  
  [Learn how to download and install MySQL 8.0.40 on Windows 11 by Amit Thinks](https://www.youtube.com/watch?v=hiS_mWZmmI0&t=123s) — Helped in setting up and configuring MySQL Workbench.

- **Flask-MySQL Connectivity Guidance:**  
  [How to connect MySQL Database with Flask tutorial by United Top Tech](https://www.youtube.com/watch?v=14HTiBQEQ9M&t=386s) — Helped in connecting the Flask application with the MySQL database.

- **Project Idea and Implementation:**  
  Developed collaboratively by Anila Sara John, Anjaleena Joseph, Dhanalakshmi Pullarkatt Prasanth, and Drutha G Shenoy as part of a mini project.
