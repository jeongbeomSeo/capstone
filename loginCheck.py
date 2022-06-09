from sejong_univ_auth import (
  auth,
  ClassicSession
)

def loginCheck(request):
  if request.method == 'POST':
    id = str(request.form['id'])
    password = str(request.form['password'])
    result = auth(id= id, password=password, methods=ClassicSession)
    if(result.is_auth):
      studentId = id;
      major = result.body["major"]
      name = result.body["name"]
      grade = result.body["grade"]
      status = result.body["status"]
      student = {
        "id": studentId,
        "major": major,
        "name": name,
        "grade": grade,
        "status": status
      }
      return student
    else:  
      result.is_auth
