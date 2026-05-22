from flask import Flask, session, render_template, request, redirect, url_for, flash, g
from db_config import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = "your_unique_secret_key_here"

# --- DATABASE MANAGEMENT ---

def get_db():
    """Provides a fresh database connection and cursor for the current request."""
    if 'db' not in g:
        g.db = get_db_connection()
        g.cursor = g.db.cursor(dictionary=True, buffered=True)
    return g.db, g.cursor

@app.teardown_appcontext
def close_db(error):
    """Automatically closes the database connection after the request is finished."""
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Temporary storage (will be replaced by DB later)
user_data = {}

# --- USER ROUTES ---

# Home 
@app.route("/")
def home():
    return render_template("index.html", page="home")

# Login 
@app.route("/login", methods=["GET", "POST"])
def login():
    db, cursor = get_db()
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()

        if user and check_password_hash(user["password"], password):            
            global user_data
            user_data = {
                "logged_in": True,
                "id": user["id"],
                "name": user["name"],
                "email": user["email"]
            }
            return redirect(url_for("stream_selection"))
        else:
            return render_template(
                "message.html",
                title="Login Failed!",
                message="Invalid email or password.",
                login_error=True
            )
    return render_template("login.html")

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    db, cursor = get_db()
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        hashed_password = generate_password_hash(password)

        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        existing = cursor.fetchone()

        if existing:
            return render_template(
                "message.html",
                title="Registration Failed!",
                message="Email already exists.",
                duplicate_reg=True
            )

        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (name, email, hashed_password)
        )
        db.commit()

        return render_template(
            "message.html",
            title="Registration Successful!",
            message=f"Thank you {name}, your account has been created."
        )
    return render_template("register.html")

# Stream Selection
@app.route("/stream-selection", methods=["GET", "POST"])
def stream_selection():
    db, cursor = get_db()
    if request.method == "POST":
        stream = request.form["stream"]
        user_data["stream"] = stream
        return redirect(url_for("career_selection"))

    cursor.execute("SELECT stream_name FROM streams")
    streams = [row["stream_name"] for row in cursor.fetchall()]

    return render_template("stream_selection.html", streams=streams, selected_stream=user_data.get("stream"))

# Career Selection
@app.route("/career-selection", methods=["GET", "POST"])
def career_selection():
    db, cursor = get_db()
    stream = user_data.get("stream")
    
    cursor.execute(
        "SELECT career_name FROM careers c JOIN streams s ON c.stream_id = s.id WHERE s.stream_name=%s",
        (stream,)
    )
    careers = [row["career_name"] for row in cursor.fetchall()]
    
    if request.method == "POST":
        career = request.form["career"]
        user_data["career"] = career
        return redirect(url_for("questionnaire"))
    
    return render_template(
        "career_selection.html",
        careers=careers,
        stream=stream,
        selected_career=user_data.get("career")
    )

# Questionnaire
@app.route("/questionnaire", methods=["GET", "POST"])
def questionnaire():
    db, cursor = get_db()
    career = user_data.get("career")

    cursor.execute(
        "SELECT question_text, weight FROM questions q JOIN careers c ON q.career_id=c.id WHERE c.career_name=%s",
        (career,)
    )
    questions = cursor.fetchall()

    if request.method == "POST":
        score = 0
        max_score = sum(q["weight"] for q in questions)
        for i, q in enumerate(questions, start=1):
            answer = request.form.get(f"q{i}")
            if answer == "Yes":
                score += q["weight"]

        percentage = round((score / max_score) * 100, 2) if max_score > 0 else 0
        
        if percentage >= 70:
            suitability = "High"
            explanation = f"<b>Excellent match!</b> Your responses strongly align with the requirements for <b>{career}</b>."
        elif percentage >= 40:
            suitability = "Medium"
            explanation = f"<b>Moderate compatibility.</b> You demonstrate some important qualities for <b>{career}</b>."
        else:
            suitability = "Low"
            explanation = f"Currently, your responses indicate <b>limited</b> alignment with <b>{career}</b>."

        user_data.update({"score": score, "percentage": percentage, "suitability": suitability, "explanation": explanation})

        cursor.execute("SELECT id FROM careers WHERE career_name=%s", (career,))
        career_row = cursor.fetchone()
        if career_row:
            cursor.execute(
                "INSERT INTO results (user_id, career_id, score, percentage, suitability) VALUES (%s, %s, %s, %s, %s)",
                (user_data["id"], career_row["id"], score, percentage, suitability)
            )
            db.commit()

        return redirect(url_for("result"))

    return render_template("questionnaire.html", career=career, questions=questions)

# Result
@app.route("/result")
def result():
    return render_template(
        "result.html",
        career=user_data.get("career"),
        percentage=user_data.get("percentage"),
        suitability=user_data.get("suitability"),
        explanation=user_data.get("explanation")
    )

# Results History
@app.route("/results-history")
def results_history():
    db, cursor = get_db()
    user_id = user_data.get("id")
    if not user_id:
        return redirect(url_for("login"))

    cursor.execute("""
        SELECT r.id, c.career_name, r.score, r.percentage, r.suitability, r.taken_at
        FROM results r
        JOIN careers c ON r.career_id = c.id
        WHERE r.user_id = %s
        ORDER BY r.taken_at DESC
    """, (user_id,))
    results = cursor.fetchall()

    return render_template("results_history.html", results=results)

@app.context_processor
def inject_user_status():
    return dict(
        user_logged_in=user_data.get("logged_in", False),
        user_name=user_data.get("name", ""),
        admin_logged_in=session.get("admin_logged_in", False),
        is_admin=session.get("is_admin", False)
    )

# Logout
@app.route("/logout")
def logout():
    user_data.clear()
    return redirect(url_for("home"))



# --- ADMIN ROUTES ---

# Admin 
@app.route('/admin')
def admin():
    return render_template('admin_login.html')

# Admin Login
@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    db, cursor = get_db()
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cursor.execute("SELECT * FROM admin WHERE username=%s AND password=%s", (username, password))
        admin = cursor.fetchone()

        if admin:
            session.update({"user_id": admin["id"], "admin_logged_in": True, "is_admin": True})
            return redirect(url_for("admin_dashboard"))
        else:
            return render_template("message.html", title="Login Failed!", message="Invalid Admin Credentials", admin_error=True)

    return render_template("admin_login.html")

# Admin Dashboard
@app.route("/admin_dashboard")
def admin_dashboard():
    if not session.get("admin_logged_in") or not session.get("is_admin"):
        return redirect(url_for("admin_login"))
    return render_template("admin_dashboard.html", admin_logged_in=True)

# Manage Users
@app.route('/view_users')
def view_users():
    db, cursor = get_db()
    query = """
    SELECT u.id, u.name, u.email, s.stream_name, c.career_name, r.score, r.percentage, r.taken_at
    FROM users u
    LEFT JOIN results r ON u.id = r.user_id
    LEFT JOIN careers c ON r.career_id = c.id
    LEFT JOIN streams s ON c.stream_id = s.id
    ORDER BY u.id DESC
    """
    cursor.execute(query)
    users = cursor.fetchall()

    # Format the date for each user
    for user in users:
        if user['taken_at']:
            # Formats date to '10-Mar-2026'
            user['formatted_date'] = user['taken_at'].strftime('%d-%b-%Y')
        else:
            user['formatted_date'] = 'Not Attempted'

    return render_template("view_users.html", users=users, admin_logged_in=True)

@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    db, cursor = get_db()
    try:
        cursor.execute("DELETE FROM results WHERE user_id = %s", (user_id,))
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        db.commit()
        flash("User deleted successfully!", "success")
    except Exception as e:
        db.rollback()
        flash(f"Error deleting user: {str(e)}", "danger")
    return redirect(url_for('view_users'))

# Manage Questions
@app.route('/view_questions')
def view_questions():
    db, cursor = get_db()
    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()
    return render_template("view_questions.html", questions=questions, admin_logged_in=True)

@app.route('/edit_question/<int:question_id>', methods=['GET', 'POST'])
def edit_question(question_id):
    db, cursor = get_db()
    cursor.execute("SELECT * FROM questions WHERE id=%s", (question_id,))
    q = cursor.fetchone()

    if not q:
        flash("Question not found!", "danger")
        return redirect(url_for('view_questions'))

    if request.method == 'POST':
        try:
            cursor.execute(
                "UPDATE questions SET question_text=%s, weight=%s WHERE id=%s",
                (request.form['question'], request.form['weight'], question_id)
            )
            db.commit()
            flash("Question updated successfully!", "success")
            return redirect(url_for('admin_questions', career_id=q['career_id']))
        except Exception as e:
            db.rollback()
            flash(f"Error updating question: {str(e)}", "danger")

    return render_template('edit_question.html', q=q, back_url=url_for('admin_questions', career_id=q['career_id']))

@app.route('/add_question/<int:career_id>', methods=['GET','POST'])
def add_question(career_id):
    db, cursor = get_db()
    if request.method == 'POST':
        try:
            cursor.execute(
                "INSERT INTO questions(question_text, weight, career_id) VALUES(%s,%s,%s)",
                (request.form['question'], request.form['weight'], career_id)
            )
            db.commit()
            flash("Question added successfully!", "success")
            return redirect(url_for('admin_questions', career_id=career_id))
        except Exception as e:
            db.rollback()
            flash(f"Error adding question: {str(e)}", "danger")

    return render_template("add_question.html", career_id=career_id, back_url=url_for('admin_questions', career_id=career_id), admin_logged_in=True)

@app.route("/delete_question/<int:id>")
def delete_question(id):
    db, cursor = get_db()
    
    # 1. Fetch the career_id before deleting so we know where to redirect back to
    cursor.execute("SELECT career_id FROM questions WHERE id=%s", (id,))
    question = cursor.fetchone()
    if question:
        career_id = question['career_id']
        # 2. Perform the deletion
        try:
            cursor.execute("DELETE FROM questions WHERE id=%s", (id,))
            db.commit()
            flash("Question deleted successfully!", "success")
            # 3. Redirect back to the specific career's question list
            return redirect(url_for("admin_questions", career_id=career_id))
        except Exception as e:
            db.rollback()
            flash(f"Error deleting question: {str(e)}", "danger")
            return redirect(url_for("admin_questions", career_id=career_id))
            
    return redirect(url_for("admin_streams"))

@app.route('/admin_streams')
def admin_streams():
    db, cursor = get_db()
    cursor.execute("SELECT * FROM streams")
    return render_template("admin_streams.html", streams=cursor.fetchall(), admin_logged_in=True)

@app.route('/admin_careers/<int:stream_id>')
def admin_careers(stream_id):
    db, cursor = get_db()
    cursor.execute("SELECT * FROM careers WHERE stream_id=%s", (stream_id,))
    return render_template("admin_careers.html", careers=cursor.fetchall(), admin_logged_in=True)

@app.route('/admin_questions/<int:career_id>')
def admin_questions(career_id):
    db, cursor = get_db()
    cursor.execute("SELECT * FROM questions WHERE career_id=%s", (career_id,))
    return render_template("view_questions.html", questions=cursor.fetchall(), career_id=career_id, admin_logged_in=True)

# Manage Streams
@app.route('/admin_manage_streams')
def admin_manage_streams():
    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))
    
    db, cursor = get_db()
    cursor.execute("SELECT * FROM streams")
    streams = cursor.fetchall()
    return render_template("admin_manage_streams.html", streams=streams, admin_logged_in=True)

@app.route('/add_stream', methods=['POST'])
def add_stream():
    db, cursor = get_db()
    stream_name = request.form.get('stream_name')
    
    if stream_name:
        try:
            cursor.execute("INSERT INTO streams (stream_name) VALUES (%s)", (stream_name,))
            db.commit()
            flash(f"Stream '{stream_name}' added successfully!", "success")
        except Exception as e:
            db.rollback()
            flash("Error: Stream might already exist.", "danger")
            
    return redirect(url_for('admin_manage_streams'))

@app.route('/edit_stream/<int:stream_id>', methods=['GET', 'POST'])
def edit_stream(stream_id):
    """Allows admin to rename a stream."""
    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))
        
    db, cursor = get_db()
    
    if request.method == 'POST':
        new_name = request.form.get('stream_name')
        if new_name:
            try:
                cursor.execute("UPDATE streams SET stream_name = %s WHERE id = %s", (new_name, stream_id))
                db.commit()
                flash(f"Stream updated to '{new_name}'", "success")
                return redirect(url_for('admin_manage_streams'))
            except Exception as e:
                db.rollback()
                flash("Error: Stream name might already exist.", "danger")
    
    # GET: Fetch the current stream data to populate the form
    cursor.execute("SELECT * FROM streams WHERE id = %s", (stream_id,))
    stream = cursor.fetchone()
    
    if not stream:
        flash("Stream not found.", "danger")
        return redirect(url_for('admin_manage_streams'))
        
    return render_template("edit_stream.html", stream=stream)

@app.route('/delete_stream/<int:stream_id>')
def delete_stream(stream_id):
    db, cursor = get_db()
    try:
        cursor.execute("DELETE FROM streams WHERE id = %s", (stream_id,))
        db.commit()
        flash("Stream deleted successfully!", "success")
    except Exception as e:
        db.rollback()
        flash(f"Could not delete stream: {str(e)}", "danger")
        
    return redirect(url_for('admin_manage_streams'))

# Manage Careers
@app.route('/admin_manage_careers_select')
def admin_manage_careers_select():
    """Step 1: Admin selects which stream's careers they want to manage."""
    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))
    
    db, cursor = get_db()
    cursor.execute("SELECT * FROM streams")
    streams = cursor.fetchall()
    return render_template("admin_manage_careers_select.html", streams=streams, admin_logged_in=True)

@app.route('/admin_manage_careers_list/<int:stream_id>')
def admin_manage_careers_list(stream_id):
    if not session.get("admin_logged_in"): 
        return redirect(url_for("admin_login"))
    db, cursor = get_db()
    cursor.execute("SELECT * FROM streams WHERE id = %s", (stream_id,))
    stream = cursor.fetchone()
    cursor.execute("SELECT * FROM careers WHERE stream_id = %s", (stream_id,))
    return render_template("admin_manage_careers_list.html", stream=stream, careers=cursor.fetchall(), admin_logged_in=True)

@app.route('/add_career/<int:stream_id>', methods=['POST'])
def add_career(stream_id):
    """Action: Adds a new career to a specific stream."""
    db, cursor = get_db()
    name = request.form.get('career_name')
    if name:
        try:
            cursor.execute("INSERT INTO careers (career_name, stream_id) VALUES (%s, %s)", (name, stream_id))
            db.commit()
            flash(f"Career '{name}' added successfully!", "success")
        except Exception as e:
            db.rollback()
            flash("Error adding career. It might already exist.", "danger")
            
    return redirect(url_for('admin_manage_careers_list', stream_id=stream_id))

@app.route('/edit_career/<int:career_id>', methods=['GET', 'POST'])
def edit_career(career_id):
    """Allows admin to rename a specific career."""
    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))
        
    db, cursor = get_db()
    
    # First, fetch the current career to know its name and which stream it belongs to
    cursor.execute("SELECT * FROM careers WHERE id = %s", (career_id,))
    career = cursor.fetchone()
    
    if not career:
        flash("Career not found.", "danger")
        return redirect(url_for('admin_manage_careers_select'))

    if request.method == 'POST':
        new_name = request.form.get('career_name')
        if new_name:
            try:
                cursor.execute("UPDATE careers SET career_name = %s WHERE id = %s", (new_name, career_id))
                db.commit()
                flash(f"Career updated to '{new_name}'", "success")
                # Redirect back to the list of careers for that specific stream
                return redirect(url_for('admin_manage_careers_list', stream_id=career['stream_id']))
            except Exception as e:
                db.rollback()
                flash("Error updating career. Name might be a duplicate.", "danger")
    
    return render_template("edit_career.html", career=career)

@app.route('/delete_career/<int:career_id>/<int:stream_id>')
def delete_career(career_id, stream_id):
    """Action: Deletes a career and stays on the same stream list."""
    db, cursor = get_db()
    try:
        cursor.execute("DELETE FROM careers WHERE id = %s", (career_id,))
        db.commit()
        flash("Career deleted successfully!", "success")
    except Exception as e:
        db.rollback()
        flash("Error deleting career.", "danger")
        
    return redirect(url_for('admin_manage_careers_list', stream_id=stream_id))

# Admin Logout
@app.route("/admin_logout")
def admin_logout():
    session.clear()
    return redirect(url_for("admin_login"))

if __name__ == "__main__":
    app.run(debug=True)