from __future__ import unicode_literals
from bottle import Bottle, request, response
from mypkg import analyse_data


# http://www.reddit.com/r/learnpython/comments/1037g5/whats_the_best_lightweight_web_framework_for/
# http://bottlepy.org/docs/dev/tutorial.html
app = Bottle()


template = """<html>
<head><title>Home</title></head>
<body>
<h1>Upload a file</h1>
<form method="POST" enctype="multipart/form-data" action="/">
<label>Level:</label> <input type="text" name="level" value="42"><br>
<input type="file" name="uploadfile" /><br>
<input type="submit" value="Submit" />
</form>
</body>
</html>"""


@app.get('/')
def home():
    return template


@app.post('/')
def upload():
    # A file-like object open for reading.
    upload_file = request.POST['uploadfile']
    level = int(request.POST['level'])
    
    # Your analyse_data function takes a file-like object and returns a new
    # file-like object ready for reading.
    converted_file = analyse_data(data=upload_file.file, level=level)
    response.set_header('Content-Type', 'text/csv')
    response.set_header('Content-Disposition', 'attachment; filename=converted.csv')
    
    # Return a file-like object.
    return converted_file


if __name__ == "__main__":
    app.run(debug=True)
