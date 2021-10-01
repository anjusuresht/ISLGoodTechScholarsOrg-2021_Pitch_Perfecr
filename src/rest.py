from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
from flask_mysqldb import MySQL

app = FlaskAPI(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'pitchperfect'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

mysql = MySQL(app)


@app.route("/v1/pitchperfect/idea", methods=['GET', 'POST'])
def ideas_list():
    """
    List or create ideas.
    """
    if request.method == 'POST':
        request_data = request.get_json()
        title = request_data['title']
        abstract = request_data['abstract']
        scope = request_data['scope']
        userid = request_data['userid']
        implementation_details = request_data['implementation_details']
        cursor = mysql.connection.cursor()
        addideasql = """INSERT INTO idea (title,ABSTRACT,SCOPE,implementation_details,userid) 
                             VALUES (%s,%s,%s,%s,%s)"""
        cursor.execute(addideasql, (title, abstract, scope, implementation_details, userid))
        mysql.connection.commit()
        cursor.close()
        return str(status.HTTP_201_CREATED)

    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        get_all_idea_sql = """SELECT * FROM idea"""
        cursor.execute(get_all_idea_sql)
        result = cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        return jsonify(result), status.HTTP_200_OK


@app.route("/v1/pitchperfect/idea/<idea_id>/<user_id>", methods=['DELETE'])
def delete_idea(idea_id,user_id):
    """
    Delete a idea
    """
    if request.method == 'DELETE':
        cursor = mysql.connection.cursor()
        select_idea_sql = """SELECT * FROM idea WHERE  ideaid = %s and userid= %s"""
        cursor.execute(select_idea_sql, (idea_id, user_id))
        select_result = cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        print (select_result)
        if select_result:
            cursor = mysql.connection.cursor()
            delete_idea_sql = """DELETE FROM idea WHERE  ideaid = %s and userid= %s"""
            cursor.execute(delete_idea_sql, (idea_id, user_id))
            result = cursor.fetchall()
            mysql.connection.commit()
            cursor.close()
            if result is None:
                raise exceptions.NotFound()
            return str(status.HTTP_204_NO_CONTENT)
        else:
            return str(status.HTTP_401_UNAUTHORIZED)


@app.route("/v1/pitchperfect/idea/<idea_id>", methods=['GET'])
def idea_details(idea_id,):
    """
    View idea
    """
    cursor = mysql.connection.cursor()
    get_idea_sql = """SELECT * FROM idea WHERE  ideaid = %s"""
    cursor.execute(get_idea_sql, (idea_id,))
    result = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    if result is None:
        raise exceptions.NotFound()
    return jsonify(result), status.HTTP_200_OK


@app.route("/v1/pitchperfect/idea/<idea_id>", methods=['PUT'])
def update_idea_details(idea_id):
    """
    Update a idea
    """
    request_data = request.get_json()
    idea_name = request_data['title']
    abstract = request_data['abstract']
    scope = request_data['scope']
    implementation_details = request_data['implementation_details']

    cursor = mysql.connection.cursor()
    update_idea_sql = """UPDATE idea SET title = %s, abstract = %s, scope = %s, implementation_details = %s
                            WHERE  ideaid = %s"""
    cursor.execute(update_idea_sql, (idea_name, abstract, scope, implementation_details, idea_id))
    result = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    if result is None:
        raise exceptions.NotFound()
    return str(status.HTTP_200_OK)


@app.route("/v1/pitchperfect/<user_id>/idea", methods=['GET'])
def display_user_ideas(user_id):
    """
    Display ideas of the user
    """
    cursor = mysql.connection.cursor()
    display_user_idea_sql = """SELECT * FROM idea WHERE USERID = %s"""
    cursor.execute(display_user_idea_sql, (user_id,))
    result = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    if result is None:
        raise exceptions.NotFound()
    return jsonify(result)


@app.route("/v1/pitchperfect/idea/<idea_id>/rate", methods=['POST', 'GET'])
def display_idea_rating(idea_id):
    """
    rates idea_id
    """
    if request.method == 'POST':
        request_data = request.get_json()
        investor_id = request_data['investor_id']
        rating = request_data['rating']

        cursor = mysql.connection.cursor()
        rate_idea_sql = """INSERT INTO rating (ideaid,investor_id,rate) 
                             VALUES (%s,%s,%s)"""
        cursor.execute(rate_idea_sql, (idea_id, investor_id, rating))
        mysql.connection.commit()
        cursor.close()
        return str(status.HTTP_201_CREATED)

    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        get_all_idea_rating_sql = """SELECT * FROM rating where ideaid = %s"""
        cursor.execute(get_all_idea_rating_sql, (idea_id,))
        result = cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        return jsonify(result), status.HTTP_200_OK


@app.route("/v1/pitchperfect/idea/<idea_id>/comment", methods=['POST', 'GET'])
def display_idea_comments(idea_id):
    """
    Comment on idea_id
    """
    if request.method == 'POST':
        request_data = request.get_json()
        investor_id = request_data['investor_id']
        comment = request_data['comment']

        cursor = mysql.connection.cursor()
        comment_idea_sql = """INSERT INTO comments (ideaid,investor_id,comments) 
                             VALUES (%s,%s,%s)"""
        cursor.execute(comment_idea_sql, (idea_id, investor_id, comment))
        mysql.connection.commit()
        cursor.close()
        return str(status.HTTP_201_CREATED)

    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        get_all_idea_comment_sql = """SELECT * FROM comments where ideaid = %s"""
        cursor.execute(get_all_idea_comment_sql, (idea_id,))
        result = cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        return jsonify(result), status.HTTP_200_OK


if __name__ == "main":
    app.run(debug=True)