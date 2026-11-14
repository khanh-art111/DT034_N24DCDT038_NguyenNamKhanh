import sys

# Đảm bảo hiển thị tốt tiếng Việt trên terminal Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stdin.reconfigure(encoding='utf-8')
    except Exception:
        pass

def dao_doan(a: list, l: int, r: int) -> None:
    """Đảo ngược các phần tử của mảng a từ chỉ số l đến r."""
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1


def hoan_vi_tiep(a: list) -> bool:
    """
    Sinh cấu hình kế tiếp trực tiếp trên mảng a.
    Trả về True nếu sinh thành công, False nếu đã ở cấu hình cuối cùng.
    """
    n = len(a)
    i = n - 2
    # 1. Tìm i từ phải sang trái sao cho a[i] < a[i+1]
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1
        
    if i < 0:
        return False # Đã đến cấu hình giảm dần cuối cùng
        
    # 2. Tìm j từ phải sang trái sao cho a[j] > a[i]
    j = n - 1
    while a[j] <= a[i]:
        j -= 1
        
    # 3. Đổi chỗ a[i] và a[j]
    a[i], a[j] = a[j], a[i]
    
    # 4. Đảo đoạn từ i+1 đến cuối mảng
    dao_doan(a, i + 1, n - 1)
    return True

def liet_ke_hoan_vi(n: int) -> None:
    """Khởi tạo và in toàn bộ hoán vị của n phần tử."""
    a = list(range(1, n + 1)) # Tạo mảng [1, 2, ..., n]
    count = 0
    
    while True:
        count += 1
        print(f"Cấu hình {count}: {a}")
        if not hoan_vi_tiep(a):
            break
            
    print(f"Tổng số cấu hình: {count}")


if __name__ == "__main__":
    n = int(input("Nhập n (ví dụ: 3): "))
    liet_ke_hoan_vi(n)
