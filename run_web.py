"""
Script khởi chạy trang web mô phỏng thuật toán hoán vị Narayana
Dành cho sinh viên: Nguyễn Nam Khánh - MSSV: N24DCDT038
Học phần: Cấu trúc dữ liệu và giải thuật (INT13185) - Nhóm 3
Giảng viên hướng dẫn: ThS. Hồ Nhựt Minh
"""

import os
import sys
import webbrowser
import http.server
import socketserver
import threading
import time

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(base_dir, "mo_phong.html")

    if not os.path.exists(html_file):
        print(f"[LỖI] Không tìm thấy tệp {html_file}")
        input("Nhấn Enter để thoát...")
        return

    print("=" * 64)
    print("  HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG (PTIT HCM)")
    print("  KHOA KỸ THUẬT ĐIỆN TỬ 2 - NGÀNH KỸ THUẬT ĐIỆN TỬ")
    print("=" * 64)
    print("  Họ và tên SV : Nguyễn Nam Khánh")
    print("  Mã sinh viên : N24DCDT038")
    print("  Lớp          : D24CQDT01-N")
    print("  Học phần     : Cấu trúc dữ liệu và giải thuật (INT13185) - Nhóm 3")
    print("  GV hướng dẫn : ThS. Hồ Nhựt Minh")
    print("  Đề tài       : DT034 - Sinh hoán vị theo thứ tự từ điển")
    print("=" * 64)
    print("\n[+] Đang mở trang web mô phỏng trên trình duyệt mặc định...")

    # Mở trực tiếp file HTML trên trình duyệt
    webbrowser.open(f"file:///{html_file.replace(os.sep, '/')}")
    print("[THÀNH CÔNG] Trang mô phỏng đã được mở!")
    print("Nếu trình duyệt chưa tự mở, bạn có thể nhấp đúp trực tiếp vào file:")
    print(f"-> {html_file}\n")

if __name__ == "__main__":
    main()

