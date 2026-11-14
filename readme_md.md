# DT034 — Liệt kê hoán vị theo thứ tự từ điển

Dự án đề tài cá nhân học phần **Cấu trúc dữ liệu và giải thuật (INT13185 — Nhóm 03)** thực hiện tại **Học viện Công nghệ Bưu chính Viễn thông Cơ sở tại TP. Hồ Chí Minh (PTIT HCM)** — **Khoa Kỹ thuật Điện tử 2**.

## 1. Thông tin chung về đề tài và sinh viên thực hiện

- **Họ và tên sinh viên**: Nguyễn Nam Khánh
- **Mã số sinh viên (MSSV)**: `N24DCDT038`
- **Lớp**: `D24CQDT01-N`
- **Khoa / Ngành**: Khoa Kỹ thuật Điện tử 2 — Ngành Kỹ thuật Điện, Điện tử
- **Học phần và nhóm**: Cấu trúc dữ liệu và giải thuật (`INT13185` — Nhóm 03)
- **Giảng viên hướng dẫn**: ThS. Hồ Nhựt Minh
- **Mã đề và tên đề tài**: `DT034` — Liệt kê hoán vị theo thứ tự từ điển
- **Giáo trình căn cứ**: `Giao-trinh-Cau-truc-du-lieu-va-Giai-thuat-INT1306.pdf` (Chương 3: Mục 3.2.4 Sinh hoán vị; Hình 3.2; trang in 67–69; trang PDF 79–81)
- **Kho mã nguồn GitHub**: `https://github.com/<tai_khoan_github>/DT034_N24DCDT038_NguyenNamKhanh`
- **Ngôn ngữ và công nghệ sử dụng**: **Python 3.14.7** (thuật toán lõi thao tác trực tiếp trên mảng, kiểm thử tự động với `unittest`, giao diện dòng lệnh tương tác TUI).

## 2. Cấu trúc thư mục mã nguồn cá nhân (Phân tách rõ Thuật toán, Kiểm thử, Giao diện và Minh chứng)

Toàn bộ mã nguồn cá nhân được tổ chức thành các thư mục chuyên biệt để người đọc dễ dàng tra cứu đâu là phần thuật toán lõi, đâu là phần kiểm thử và đâu là kịch bản chạy demo:

```text
DT034_N24DCDT038_NguyenNamKhanh/
├── .gitignore                        # Cấu hình Git bỏ qua các tệp tạm và bộ nhớ đệm
├── README.md                         # Tài liệu tổng quan đề tài, giải thích cấu trúc thư mục và hướng dẫn chạy
├── demo.py                           # [KỊCH BẢN MINH HỌA CLI/TUI] Menu tương tác chạy 2 ví dụ trên phiếu, ca tự thiết kế và ca biên A01–A08
│
├── src/                              # [THƯ MỤC THUẬT TOÁN LÕI BẰNG PYTHON]
│   └── hoan_vi.py                    # Cài đặt hàm dao_doan, hoan_vi_tiep, liet_ke_hoan_vi và các hàm kiểm tra hợp đồng đầu vào (validator)
│
├── test/                             # [THƯ MỤC KIỂM THỬ TỰ ĐỘNG BẰNG PYTHON]
│   └── test_hoan_vi.py               # Bộ kiểm thử đơn vị unittest gồm 12 ca độc lập đạt PASS 100%
│
└── docs/                             # [THƯ MỤC MINH CHỨNG KẾT QUẢ & NHẬT KÝ THỰC THI]
    └── anh_ket_qua/                  # Lưu trữ đầy đủ 11 ảnh chụp màn hình thực thi cá nhân (01_vi_du_1.png -> 11_github_repo_commit.png)
```

### Giải thích chi tiết vai trò của từng thư mục trong mã nguồn:
- **Thư mục `src/` (Thuật toán lõi Python)**: Chứa tệp `src/hoan_vi.py` cài đặt toàn bộ logic thao tác mảng tại chỗ (`in-place`), hàm tìm chốt $i$, tìm phần tử đổi chỗ $j$, đảo đoạn hậu tố và hàm liệt kê tổng hợp.
- **Thư mục `test/` (Kiểm thử tự động Python)**: Chứa tệp `test/test_hoan_vi.py` thực thi 12 ca kiểm thử độc lập bao gồm ví dụ chuẩn, ca tự thiết kế, ca biên và ca kiểm soát lỗi input.
- **Tệp `demo.py` (Giao diện dòng lệnh TUI)**: Cung cấp menu tương tác trực quan cho phép người dùng lựa chọn nhanh các ca ví dụ, truyền mảng truy vết hoặc nhập giá trị $n$ tùy ý từ bàn phím.
- **Thư mục `docs/anh_ket_qua/` (Minh chứng thực nghiệm)**: Lưu trữ 11 ảnh chụp kết quả chạy thực tế (`A01` đến `A11`) phục vụ chấm điểm báo cáo.

## 3. Nội dung chuyên môn đã thực hiện trong đề tài DT034

### 3.1. Mô hình dữ liệu và các thao tác tự cài đặt
- **Biểu diễn mảng**: Sử dụng mảng một chiều (`list` trong Python) chứa đúng $n$ số nguyên phân biệt từ $1$ đến $n$ với quy mô giới hạn $1 \le n \le 8$.
- **Đảo đoạn tại chỗ (`dao_doan`)**: Dùng hai con trỏ tiến từ hai đầu mảng lùi dần vào giữa để đảo ngược trật tự đoạn hậu tố trong thời gian $O(n)$ và bộ nhớ phụ $O(1)$.
- **Sinh hoán vị kế tiếp (`hoan_vi_tiep`)**: Thực hiện 4 bước chuẩn: (1) tìm chốt $i$ từ phải sang trái sao cho $a[i] < a[i+1]$; (2) tìm phần tử thế chỗ $j$ lớn hơn $a[i]$; (3) đổi chỗ $a[i]$ và $a[j]$; (4) đảo ngược đoạn từ $i+1$ đến cuối mảng.
- **Liệt kê toàn bộ (`liet_ke_hoan_vi`)**: Khởi tạo mảng tăng dần nhỏ nhất, lặp gọi hàm sinh kế tiếp, đếm tổng số cấu hình đạt được (đạt đúng $n!$) và in kết quả ra màn hình terminal.

### 3.2. Kiểm chứng thực nghiệm trên các ca kiểm thử
- **Ví dụ 1 và Ví dụ 2**: Kiểm chứng thành công với $n=2$ (2 cấu hình) và $n=4$ (24 cấu hình).
- **Ca truy vết thủ công**: Kiểm chứng chi tiết mảng truyền vào $a = [1, 3, 5, 4, 2]$ ra kết quả liền kề $a = [1, 4, 2, 3, 5]$.
- **Bộ 12 ca kiểm thử độc lập**: Đã thiết kế và chạy thành công 100% các ca kiểm thử gồm ví dụ chuẩn, ca tự thiết kế, ca biên ($n=1, n=8$, mảng giảm dần cực đại) và ca bắt lỗi input sai định dạng (`LOI01`).

## 4. Hướng dẫn cách chạy chương trình Python

Mở cửa sổ **PowerShell** hoặc **Terminal** tại thư mục gốc của dự án và chạy các lệnh sau:

```powershell
# Bước 1: Kiểm tra phiên bản Python
python --version

# Bước 2: Chạy chương trình giao diện demo tương tác
python demo.py

# Bước 3: Chạy bộ kiểm thử tự động 12 ca độc lập (đạt PASS 100%)
python -m unittest test/test_hoan_vi.py -v
```