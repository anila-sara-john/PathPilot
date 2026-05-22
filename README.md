# **PathPilot – Career Suitability Evaluation Web Application**
PathPilot is a simple web-based career suitability evaluation system developed as a mini project as part of our Computer Science academic journey.

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

## **Technologies Used**
- HTML - Used to strucutre the web pages of the application.
- CSS - Used to design and style the user interface.
- Flask - Used as the backend framework to handle routing and application logic.
- MySQL - Used as the database to store users, careers, questions, and results data.

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
   git clone <[repository_url](https://github.com/anila-sara-john/PathPilot)>
   ```
2. Navigate to the project folder
   ```bash
   git clone <cd PathPilot>
   ```

3. Configure MySQL database
   - Create a MySQL database
   - Import/create required tables
   - Update database credentials in app.py
4. Run the application
   ```bash
   python app.py
   ```

## **Future Improvements**
- Dynamic questionnaires
- More career domains and streams
- Advanced recommendation logic
- Improved UI/UX
- Analytics Dashboard
  


