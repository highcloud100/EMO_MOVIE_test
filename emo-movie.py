from flask import Flask, jsonify, request, redirect
app = Flask(__name__)


# <!DOCTYPE html>
# <html>
#   <head>
#     <title></title>
#   </head>
#   <body>
#     <div>POST test</div>
#     <form action="post_result.php" method="post">
#       <input type="text" name="id" placeholder="Enter id here">
#       <input type="text" name="age" placeholder="Enter age here">
#       <input type="submit" value="Submit">
#     </form>
#   </body>
# </html>






#메모장 열기
File = open("tasks.txt", "w")
with open ('tasks.txt', 'w') as File:
    File.write('/*파라미터 들어갈 예정*/') #DB


with open ('tasks.txt') as tasks:
    for chore in tasks:
        print(chore, end="")

