import sys

# Đảm bảo stdout hỗ trợ UTF-8 (tiếng Việt) trên mọi môi trường
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

# ============================================================
#  ĐỀ TÀI: DT034 - Liệt kê hoán vị theo phương pháp sinh
# ============================================================
DE_TAI = "DT034"

def kiem_tra_n(n: int) -> None:
    """Kiểm tra quy mô n có nằm trong khoảng hợp lệ theo phiếu giao đề (1..8) hay không."""
    if not isinstance(n, int):
        raise TypeError("n phải là số nguyên.")
    if not (1 <= n <= 8):
        raise ValueError("n phải nằm trong khoảng từ 1 đến 8 (theo giới hạn đề bài).")

def kiem_tra_mang(a: list) -> None:
    """Xác thực đầu vào nếu người dùng truyền một mảng hoán vị bất kỳ vào hàm."""
    n = len(a)
    if not (1 <= n <= 8):
        raise ValueError("Kích thước mảng phải từ 1 đến 8.")
    if len(set(a)) != n:
        raise ValueError("Mảng không hợp lệ: chứa giá trị trùng lặp.")
    for x in a:
        if not isinstance(x, int) or not (1 <= x <= n):
            raise ValueError(f"Phần tử {x} không hợp lệ. Phải là số nguyên từ 1 đến {n}.")

def dao_doan(a: list, l: int, r: int) -> None:
    """Đảo ngược các phần tử của mảng a từ chỉ số l đến r (tại chỗ)."""
    if not (0 <= l <= r < len(a)):
        raise IndexError("Chỉ số l hoặc r nằm ngoài giới hạn của mảng.")
        
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1

def hoan_vi_tiep(a: list) -> bool:
    """
    Sinh cấu hình kế tiếp trực tiếp trên mảng a theo thứ tự từ điển.
    Trả về True nếu sinh thành công, False nếu đã ở cấu hình giảm dần cuối cùng.
    """
    n = len(a)
    i = n - 2
    
    # 1. Tìm chốt i từ phải sang trái sao cho a[i] < a[i+1]
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1
        
    if i < 0:
        return False  # Toàn mảng đã giảm dần, không thể sinh tiếp
        
    # 2. Tìm phần tử thế chỗ j từ phải sang trái
    j = n - 1
    while a[j] <= a[i]:
        j -= 1
        
    # 3. Đổi chỗ chốt và phần tử thế
    a[i], a[j] = a[j], a[i]
    
    # 4. Đảo ngược đoạn đuôi để lấy cấu hình nhỏ nhất kế tiếp
    dao_doan(a, i + 1, n - 1)
    return True

def liet_ke_hoan_vi(n: int) -> dict:
    """
    Hàm tổng hợp: Khởi tạo mảng, gọi sinh hoán vị và đếm tổng số cấu hình.
    Trả về dict chứa tổng số cấu hình (tương tự kiểu dữ liệu trả về gộp của BFS).
    """
    kiem_tra_n(n)
    a = list(range(1, n + 1))
    count = 0
    
    print(f"--- BẮT ĐẦU SINH HOÁN VỊ (n = {n}) ---")
    while True:
        count += 1
        # Theo phiếu giao đề: n <= 8 thì in toàn bộ, lớn hơn thì có thể chỉ đếm
        if n <= 5:
            print(f"Cấu hình {count}: {a}")
            
        if not hoan_vi_tiep(a):
            break
            
    print(f"Tổng số cấu hình: {count}")
    return {"tong_so_cau_hinh": count, "cau_hinh_cuoi": a}

if __name__ == "__main__":
    # Đảm bảo hiển thị tốt tiếng Việt trên terminal
    if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
            sys.stdin.reconfigure(encoding='utf-8')
        except Exception:
            pass

    print(f"{'=' * 50}")
    print(f"  ĐỀ TÀI: {DE_TAI} - Liệt kê hoán vị theo phương pháp sinh")
    print(f"{'=' * 50}")

    try:
        nhap = input("Nhập số nguyên n (1 đến 8): ")
        n = int(nhap)
        liet_ke_hoan_vi(n)
    except ValueError as e:
        print(f"Lỗi Dữ Liệu: {e}")
    except TypeError as e:
        print(f"Lỗi Kiểu Dữ Liệu: {e}")
