#try1 
import re
def solution(new_id):
    #1
    new_id = new_id.lower() 
    #2
    new_id = re.sub("[^a-zA-Z0-9-_.]","",new_id)
    #3
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    #4
    new_id = new_id.strip(".") 
    #5
    if len(new_id) == 0:
        new_id = "a"
    #6
    new_id = new_id[:15] 
    new_id = new_id.rstrip(".")
    #7
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id
    
#try2 : #7의 while문 없애기!
import re
def solution(new_id):
    #1
    new_id = new_id.lower() 
    #2
    new_id = re.sub("[^a-zA-Z0-9-_.]","",new_id)
    #3
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    #4
    new_id = new_id.strip(".") 
    #5
    if len(new_id) == 0:
        new_id = "a"
    #6
    new_id = new_id[:15] 
    new_id = new_id.rstrip(".")
    #7
    if len(new_id) < 3:
        new_id += new_id[-1] * (3-len(new_id))
    
    return new_id
 
#try3 : 정규식 연습
import re
def solution(new_id):
    #1
    new_id = new_id.lower() 
    #2
    new_id = re.sub("[^a-zA-Z0-9-_.]","",new_id)
    #3
    new_id = re.sub("\.+",".",new_id)
    #4
    new_id = re.sub("^[.]|[.]$","",new_id)
    #5
    new_id = "a" if len(new_id) == 0 else new_id[:15]
    #6
    new_id = re.sub("[.]$","",new_id)
    #7
    if len(new_id) < 3:
        new_id += new_id[-1] * (3-len(new_id))
    
    return new_id
  
#try 4 : 최종 나의 best = strip() 과 정규식의 콜라보!
import re
def solution(new_id):
    #1
    new_id = new_id.lower() 
    #2
    new_id = re.sub("[^a-zA-Z0-9-_.]","",new_id)
    #3
    new_id = re.sub("\.+",".",new_id)
    #4
    new_id = new_id.strip(".")
    #5
    new_id = "a" if len(new_id) == 0 else new_id[:15]
    #6
    new_id = new_id.rstrip(".")
    #7
    if len(new_id) < 3:
        new_id += new_id[-1] * (3-len(new_id))
    
    return new_id
  
