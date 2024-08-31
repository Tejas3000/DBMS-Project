from flask import Flask, render_template, request, redirect, url_for, session, g, flash
import mysql.connector
from random import randint
from functools import wraps

app = Flask(__name__)
app.secret_key = 'its_a_secret'

db_config = {
    'user': 'root',
    'password': 'root123',
    'host': 'localhost',
    'database': 'internship_management',
    'auth_plugin':'mysql_native_password'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.before_request
def before_request():
    g.logged_in = session.get('logged_in')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if user:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            return render_template('login.html',error_msg='Invalid credentials! Try again')
    return render_template('login.html')

@app.route('/')
@login_required
def index():
    return render_template('base.html')

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/add_intern', methods=['GET', 'POST'])
@login_required
def add_intern():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        project_id = request.form['project_id']
        gender = request.form['gender']
        yof = request.form['yof']
        inst = request.form['institution']
        phone = request.form['phone_no']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO interns (name, email, gender, years_of_experience, institution, phone_no) VALUES (%s, %s, %s, %s, %s, %s)", (name, email, gender, yof, inst, phone))
        cursor.execute("select id from interns order by id desc limit 1")
        new_intern_id = cursor.fetchone()[0]
        cursor.execute("INSERT INTO works_in(intern_id, project_id) VALUES (%s, %s)", (new_intern_id, project_id))
        cursor.execute("SELECT c.department_id FROM controls c LEFT JOIN departments d ON c.department_id=d.id WHERE c.project_id = %s", (project_id,))
        dept_id=cursor.fetchone()[0]
        print(dept_id)
        cursor.execute("INSERT INTO works_for(intern_id, department_id) VALUES (%s, %s)", (new_intern_id, dept_id))
        team_no=randint(1,10)
        cursor.execute("INSERT INTO belongs_to VALUES(%s, %s)",(new_intern_id, '1'))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('view_interns'))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM Projects")
    projects = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('add_intern.html', projects=projects)

@app.route('/update_intern/<int:intern_id>', methods=['GET', 'POST'])
@login_required
def update_intern(intern_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        institution = request.form['institution']
        gender = request.form['gender']
        phone_no = request.form['phone_no']
        years_of_experience = request.form['years_of_experience']

        cursor.execute("UPDATE interns \
            SET name = %s, email = %s, institution = %s, gender = %s, phone_no = %s, years_of_experience = %s \
            WHERE id = %s", (name, email, institution, gender, phone_no, years_of_experience, intern_id))

        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('view_database'))

    cursor.execute("SELECT * FROM interns WHERE id = %s", (intern_id,))
    intern = cursor.fetchone()
    cursor.close()
    conn.close()

    return render_template('update_intern.html', intern=intern)

@app.route('/delete_intern/<int:intern_id>', methods=['GET', 'POST'])
@login_required
def delete_intern(intern_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        cursor.execute("DELETE FROM interns WHERE id = %s", (intern_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('view_database'))

    cursor.execute("SELECT * FROM interns WHERE id = %s", (intern_id,))
    intern = cursor.fetchone()
    cursor.close()
    conn.close()

    return render_template('delete_intern.html', intern=intern)

@app.route('/view_interns', methods=['GET', 'POST'])
@login_required
def view_interns():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    name_filter = request.form.get('name_filter', '')
    dept_filter = request.form.get('dept_filter', '')
    team_filter = request.form.get('team_filter', '')

    query = """
        SELECT i.name, d.name, b.team_no 
        FROM interns i 
        LEFT JOIN works_for w ON w.intern_id = i.id 
        LEFT JOIN departments d ON w.department_id = d.id 
        LEFT JOIN belongs_to b ON b.intern_id = i.id
        WHERE i.name LIKE %s AND d.name LIKE %s AND b.team_no LIKE %s
    """
    filters = (f'%{name_filter}%', f'%{dept_filter}%', f'%{team_filter}%')

    cursor.execute(query, filters)
    interns = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('view_interns.html', interns=interns, name_filter=name_filter, dept_filter=dept_filter, team_filter=team_filter)

@app.route('/add_project', methods=['GET', 'POST'])
@login_required
def add_project():
    if request.method == 'POST':
        name = request.form['title']
        description = request.form['Description']
        dept = request.form['dept']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Projects (name, description) VALUES (%s, %s)", (name, description))
        cursor.execute("SELECT id FROM  projects order by id desc limit 1")
        proj_id = cursor.fetchone()[0]
        cursor.execute("select id from departments where name = %s",(dept,))
        dept_id = cursor.fetchone()[0]
        cursor.execute("INSERT INTO controls values (%s, %s)", (proj_id, dept_id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('view_projects'))
    return render_template('add_project.html')

@app.route('/view_projects')
@login_required
def view_projects():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("select p.name,p.description,d.name,(SELECT COUNT(*) from works_in w where w.project_id=p.id) from controls cnt \
                   left join projects p on cnt.project_id=p.id \
                   left join departments d on cnt.department_id=d.id;")
    projects = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view_projects.html', projects=projects)

@app.route('/view_departments')
@login_required
def view_departments():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = "SELECT d.id, d.name, managers.name FROM manages m LEFT JOIN departments d ON m.department_id=d.id LEFT JOIN managers ON m.manager_id=managers.id"
    cursor.execute(query)
    departments = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('view_departments.html', departments=departments)

@app.route('/view_database', methods=['GET', 'POST'])
@login_required
def view_database():
    conn = get_db_connection()
    cursor = conn.cursor()

    base_query = """
    SELECT interns.id, interns.name as name, interns.email, interns.institution, interns.gender, projects.name as project, interns.phone_no, interns.years_of_experience
    FROM interns
    LEFT JOIN works_in ON interns.id = works_in.intern_id
    LEFT JOIN projects ON works_in.project_id = projects.id
    """
    
    cursor.execute(base_query)
    interns = cursor.fetchall()
    
    count_query = "SELECT COUNT(*) FROM ({}) as query".format(base_query)
    cursor.execute(count_query)
    total_interns = cursor.fetchone()[0]
    
    male_count_query = "SELECT COUNT(*) FROM ({}) as query WHERE gender='Male'".format(base_query)
    cursor.execute(male_count_query)
    male_interns = cursor.fetchone()[0]
    
    female_count_query = "SELECT COUNT(*) FROM ({}) as query WHERE gender='Female'".format(base_query)
    cursor.execute(female_count_query)
    female_interns = cursor.fetchone()[0]
    
    if request.method == 'POST':
        name_filter = request.form.get('name_filter', '')
        email_filter = request.form.get('email_filter', '')
        project_filter = request.form.get('project_filter', '')
        institution_filter = request.form.get('institution_filter', '')
        gender_filter = request.form.get('sex_filter', '')
        phone_filter = request.form.get('phone_filter', '')
        experience_filter = request.form.get('experience_filter', '')
        
        filters = (
            f'%{name_filter}%', f'%{email_filter}%', f'%{project_filter}%', f'%{institution_filter}%', 
            f'%{gender_filter}%', f'%{phone_filter}%', f'%{experience_filter}%'
        )
        
        filtered_query = base_query + "WHERE interns.name LIKE %s AND interns.email LIKE %s AND projects.name LIKE %s AND \
            interns.institution LIKE %s AND interns.gender LIKE %s AND interns.phone_no LIKE %s AND interns.years_of_experience LIKE %s"
        
        cursor.execute(filtered_query, filters)
        interns = cursor.fetchall()
        
        count_filtered_query = "SELECT COUNT(*) FROM ({}) as query".format(filtered_query)
        cursor.execute(count_filtered_query, filters)
        total_interns = cursor.fetchone()[0]
        
        male_filtered_query = "SELECT COUNT(*) FROM ({}) as query WHERE gender='Male'".format(filtered_query)
        cursor.execute(male_filtered_query, filters)
        male_interns = cursor.fetchone()[0]
        
        female_filtered_query = "SELECT COUNT(*) FROM ({}) as query WHERE gender='Female'".format(filtered_query)
        cursor.execute(female_filtered_query, filters)
        female_interns = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return render_template('view_database.html', interns=interns, total_interns=total_interns, male_interns=male_interns, female_interns=female_interns)

if __name__ == '__main__':
    app.run(debug=True)
