from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

user = {
    0: ['User ID 1', 'Email ID 1', 'Password 1', 'Company 1'],
    1: ['User ID 2', 'Email ID 2', 'Password 2', 'Company 2'],
    2: ['User ID 3', 'Email ID 3', 'Password 3', 'Developer 1'],
}

projects = {
    0: ['Project 1', 'Project Name 1', 'Abstract 1', 'Documents Path 1'],
    1: ['Project 2', 'Project Name 2', 'Abstract 2', 'Documents Path 2'],
    2: ['Project 3', 'Project Name 3', 'Abstract 3', 'Documents Path 3'],
}

interest = {
    0: ['Interest ID 1', 'User ID 1', 'User ID 2', 'Status 1'],
    1: ['Interest ID 2', 'User ID 3', 'User ID 4', 'Status 2'],
    2: ['Interest ID 3', 'User ID 5', 'User ID 6', 'Status 3'],
}

def project_repr(key):
    return {
        'url': request.host_url.rstrip('/') + url_for('projects_detail', key=key),
        'text': projects[key]
    }

@app.route("/login", methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    return username + ' ' + password

@app.route("/interest", methods=['GET', 'POST'])
def interest_list():
    return interest

@app.route("/users", methods=['GET', 'POST'])
def user_list():
    return user

@app.route("/", methods=['GET', 'POST'])
def projects_list():
    """
    List or create projects.
    """
    if request.method == 'POST':
        project = str(request.data.get('text', ''))
        idx = max(projects.keys()) + 1
        projects[idx] = project
        return project_repr(idx), status.HTTP_201_CREATED

    # request.method == 'GET'
    return [project_repr(idx) for idx in sorted(projects.keys())]


@app.route("/<int:key>/", methods=['GET', 'PUT', 'DELETE'])
def projects_detail(key):
    """
    Retrieve, update or delete project instances.
    """
    if request.method == 'PUT':
        project = str(request.data.get('text', ''))
        projects[key] = project
        return project_repr(key)

    elif request.method == 'DELETE':
        projects.pop(key, None)
        return '', status.HTTP_204_NO_CONTENT

    # request.method == 'GET'
    if key not in projects:
        raise exceptions.NotFound()
    return project_repr(key)


if __name__ == "__main__":
    app.run(debug=True)
