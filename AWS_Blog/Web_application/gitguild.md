### GIT GUIDE


Manager/Leader (người khởi tạo repository):
_tạo new repository (kho lưu trữ) trên github
_Global setup:(chỉ cần setup 1 lần)
git config --global user.name "Nguyen"
git config --global user.email "..."
git config user.username "John Doe" (ten rieng cho 1 repository, phải vào cd vào local
repository)
+Kiểm tra sau khi khai báo name, email
git config --global user.name (kiem tra ten)
_Đẩy dự án mới lên github
+Khởi tạo repository local
git init
+kết nối local repository với remote repository
git remote add origin [đường dẫn trên github]
_Đẩy code lên:
+Thêm file vào local repo
git add file (file: tên file)
+Xác nhận và ghi chú thích
git commit -m "note"
_Đẩy file lên server (remote repo trên github)
(lệnh này chỉ dùng khi đẩy lên lần đầu tiên, những lên sau chỉ ghi: git push)
git push -u origin master
DEV/thành viên của dự án (Người tham gia vào repository):
_Copy remote repo về local (chỉ chạy 1 lần duy nhất khi chưa có repository)
git clone "đường dẫn trên github"
_Kéo code mới về
git pull
_Đẩy code lên:
+Thêm file vào local repo
git add file (file: tên file)
+Những cách khác để thêm file:
git add file1 file2 file3 (liệt kê từng file)
git add . (add tất cả