# DT034 — Liệt kê hoán vị theo thứ tự từ điển

Dự án đề tài cá nhân học phần **Cấu trúc dữ liệu và giải thuật (INT13185 — Nhóm 03)** thực hiện tại **Học viện Công nghệ Bưu chính Viễn thông Cơ sở tại TP. Hồ Chí Minh (PTIT HCM)** — **Khoa Kỹ thuật Điện tử 2**.

## 1. Thông tin chung về đề tài và sinh viên thực hiện

- **Họ và tên sinh viên**: Nguyễn Nam Khánh
- **Mã số sinh viên (MSSV)**: `N24DCDT038`
- **Lớp**: `D24CQDT01-N`
- **Khoa / Ngành**: Khoa Kỹ thuật Điện tử 2 — Ngành Công nghệ Kỹ thuật Điện, Điện tử
- **Học phần và nhóm**: Cấu trúc dữ liệu và giải thuật (`INT13185` — Nhóm 03)
- **Giảng viên hướng dẫn**: ThS. Hồ Nhựt Minh
- **Mã đề và tên đề tài**: `DT034` — Liệt kê hoán vị theo thứ tự từ điển
- **Giáo trình căn cứ**: `Giao-trinh-Cau-truc-du-lieu-va-Giai-thuat-INT1306.pdf` (Chương 3: Mục 3.2.4 Sinh hoán vị; Hình 3.2; trang in 67–69; trang PDF 79–81)
- **Kho mã nguồn GitHub**: [https://github.com/khanh-art111/DT034_N24DCDT038_NguyenNamKhanh](https://github.com/khanh-art111/DT034_N24DCDT038_NguyenNamKhanh)
- **Ngôn ngữ và công nghệ sử dụng**: **Python 3.14.7** (thuật toán lõi thao tác trực tiếp trên mảng tại chỗ, kiểm thử tự động với `unittest`, giao diện dòng lệnh tương tác TUI và mô phỏng trực quan trên trình duyệt web HTML/JS).

---

## 2. Cấu trúc thư mục mã nguồn cá nhân (Phân tách rõ Thuật toán, Kiểm thử, Giao diện và Minh chứng)

Toàn bộ mã nguồn cá nhân được tổ chức thành các thư mục chuyên biệt để người đọc dễ dàng tra cứu đâu là phần thuật toán lõi, đâu là phần kiểm thử và đâu là minh chứng thực nghiệm:

```text
N24DCDT038_DT034_NguyenNamKhanh/
├── readme.md                         # Tài liệu tổng quan đề tài, giải thích cấu trúc thư mục và hướng dẫn chạy
├── demo.py                           # [KỊCH BẢN MINH HỌA CLI/TUI] Menu tương tác chạy ví dụ trên phiếu, ca tự thiết kế và ca biên
├── mo_phong.html                     # [GIAO DIỆN TRỰC QUAN WEB] Trang web mô phỏng từng bước đổi chỗ chốt và đảo đoạn hậu tố
├── run_web.py                        # [MÁY CHỦ CỤC BỘ] Script tự động mở giao diện mô phỏng trực quan trên trình duyệt
│
├── src/                              # [THƯ MỤC THUẬT TOÁN LÕI BẰNG PYTHON]
│   └── DeTai.py                      # Cài đặt hàm dao_doan, hoan_vi_tiep, liet_ke_hoan_vi và các hàm kiểm tra hợp lệ đầu vào
│
├── test/                             # [THƯ MỤC KIỂM THỬ TỰ ĐỘNG BẰNG PYTHON]
│   └── test_hoan_vi.py               # Bộ kiểm thử đơn vị unittest gồm 13 ca độc lập đạt PASS 100%
│
└── docs/                             # [THƯ MỤC MINH CHỨNG KẾT QUẢ & NHẬT KÝ THỰC THI]
    └── anh_ket_qua/                  # Lưu trữ đầy đủ 12 ảnh chụp màn hình thực thi cá nhân (A01 -> A12)
        ├── 01_vi_du_1.png            # [A01] Minh chứng Ví dụ 1 trên phiếu (n = 2, sinh 2 cấu hình)
        ├── 02_vi_du_2.png            # [A02] Minh chứng Ví dụ 2 trên phiếu (n = 4, sinh đủ 24 cấu hình)
        ├── 03_tu_thiet_ke_1.png      # [A03] Minh chứng ca tự thiết kế TK01 (n = 3, sinh 6 cấu hình)
        ├── 04_tu_thiet_ke_2.png      # [A04] Minh chứng ca truy vết TK02 / Ca phiếu 5 (a = [1, 3, 5, 4, 2] -> [1, 4, 2, 3, 5])
        ├── 05_tu_thiet_ke_3.png      # [A05] Minh chứng ca truy vết TK03 / Ca phiếu 3 (a = [1, 3, 2] -> [2, 1, 3])
        ├── 06_bien_1.png             # [A06] Minh chứng ca biên dưới BIEN01 (n = 1, sinh 1 cấu hình [1])
        ├── 07_bien_2.png             # [A07] Minh chứng ca biên trên BIEN02 (n = 8, sinh 40320 cấu hình)
        ├── 08_bien_3.png             # [A08] Minh chứng ca biên cuối BIEN03 / Ca phiếu 4 (a = [3, 2, 1], trả về False)
        ├── 09_input_khong_hop_le.png # [A09] Minh chứng 5 ca bắt lỗi input LOI01–LOI05 (ValueError / TypeError)
        ├── 10_tong_ket_kiem_thu.png  # [A10] Minh chứng chạy toàn bộ 13 ca unittest độc lập (13/13 PASS)
        ├── 11_clone_sach_chay_lai.png# [A11] Minh chứng clone sạch từ GitHub vào thư mục mới và chạy lại thành công
        └── 12_github_repo_commit.png # [A12] Ảnh chụp giao diện kho lưu trữ GitHub và lịch sử commit kiểm chứng