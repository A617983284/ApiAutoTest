'''
个人中心->上传头像
'''
import  requests
#  上传一个图片文件
url = "http://www.httpbin.org/post"
file_path = r"C:\Users\DELL\Desktop\人脸识别的测试用例.png"
# with open(file_path,mode='rb') as f:
#     # 二元组：'name':file-tuple,  file-tuple为('filename', fileobj)
#     file = {"人脸识别的测试用例.png":(file_path,f)}
#     # 三元组 'name':file-tuple,  file-tuple为('filename', fileobj,'content_type')
#     # content_type是MIME类型
#     # file = {"人脸识别的测试用例.png": (file_path, f,'image/png')}
#     r = requests.post(url,files = file)
#     print(r.text)
#  上传多个文件
# url = "http://www.httpbin.org/post"
# file_path1 = r"C:\Users\DELL\Desktop\人脸识别的测试用例.png"
# file_path2 = r"C:\Users\DELL\Desktop\ttt.txt"
# with open(file_path1,mode='rb') as f1:
#     with open(file_path2, mode='r',encoding='UTF-8') as f2:
#         files = {"人脸识别的测试用例.png":(file_path1,f1,"image/png"),
#                  "ttt.txt":(file_path2,f2,"text/plain")}
#         r = requests.post(url, files=files)
#         print(r.text)

#  使用data参数上传文件，一次只能传一个文件
with open(file_path,mode='rb') as f:
    r = requests.post(url,data = f)
    print(r.text)



