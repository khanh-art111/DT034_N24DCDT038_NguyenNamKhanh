import sys
import os
import unittest
from io import StringIO
from unittest.mock import patch

# ============================================================
#  ĐỀ TÀI : DT034 - Liệt kê hoán vị theo phương pháp sinh
#  BỘ KIỂM THỬ : 13 ca kiểm thử (Bao gồm 5 ca cần kiểm tra)
# ============================================================

# Đảm bảo tìm được thư mục gốc Bao_cao_CKI dù chạy từ đâu
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

from src.DeTai import kiem_tra_n, kiem_tra_mang, dao_doan, hoan_vi_tiep, liet_ke_hoan_vi


# ── Hiển thị PASS thay vì ok ────────────────────────────────
def _add_success_pass(self, test):
    self.successes = getattr(self, 'successes', [])
    self.successes.append(test)
    if self.showAll:
        self.stream.writeln("PASS")
    elif self.dots:
        self.stream.write(".")
        self.stream.flush()

unittest.TextTestResult.addSuccess = _add_success_pass


# ── Helper: gọi liet_ke_hoan_vi mà không in ra terminal ────
def _quiet(n):
    """Chạy liet_ke_hoan_vi nhưng chặn toàn bộ output print."""
    with patch('sys.stdout', new_callable=StringIO):
        return liet_ke_hoan_vi(n)


def _sinh_tat_ca_cau_hinh(n):
    """Sinh toàn bộ các cấu hình từ [1, ..., n] bằng hoan_vi_tiep."""
    a = list(range(1, n + 1))
    configs = [a.copy()]
    while hoan_vi_tiep(a):
        configs.append(a.copy())
    return configs


# ════════════════════════════════════════════════════════════
class TestHoanVi(unittest.TestCase):

    # ── NHÓM 1: CA VÍ DỤ TRÊN PHIẾU / YÊU CẦU ─────────────

    def test_vd01_n_bang_2(self):
        """VD01 [Ca 1] – n=2: thứ tự phải là [1, 2] rồi [2, 1]."""
        # 1. Kiểm tra thứ tự cấu hình sinh ra bằng hoan_vi_tiep
        configs = _sinh_tat_ca_cau_hinh(2)
        self.assertEqual(configs, [[1, 2], [2, 1]])

        # 2. Kiểm tra qua hàm tổng hợp liet_ke_hoan_vi
        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            result = liet_ke_hoan_vi(2)
            out = fake_out.getvalue()

        self.assertEqual(result["tong_so_cau_hinh"], 2)
        self.assertEqual(result["cau_hinh_cuoi"], [2, 1])
        # Đảm bảo in đúng thứ tự [1, 2] trước rồi đến [2, 1]
        pos1 = out.find("[1, 2]")
        pos2 = out.find("[2, 1]")
        self.assertTrue(pos1 != -1 and pos2 != -1 and pos1 < pos2)

    def test_vd02_n_bang_4(self):
        """VD02 [Ca 2] – n=4: có đúng 24 cấu hình, mỗi cấu hình đủ bốn số."""
        configs = _sinh_tat_ca_cau_hinh(4)

        # Có đúng 24 cấu hình (4! = 24)
        self.assertEqual(len(configs), 24)

        # Mỗi cấu hình đủ bốn số từ 1 đến 4, không trùng lặp
        for cfg in configs:
            self.assertEqual(len(cfg), 4, f"Cấu hình {cfg} không đủ 4 số.")
            self.assertEqual(sorted(cfg), [1, 2, 3, 4], f"Cấu hình {cfg} không đủ bộ số [1, 2, 3, 4].")

        # Kiểm tra qua hàm tổng hợp liet_ke_hoan_vi
        result = _quiet(4)
        self.assertEqual(result["tong_so_cau_hinh"], 24)
        self.assertEqual(result["cau_hinh_cuoi"], [4, 3, 2, 1])

    # ── NHÓM 2: CA TỰ THIẾT KẾ & TRUY VẾT ─────────────────

    def test_tk01_n_bang_3(self):
        """TK01 – n=3: sinh đúng 6 cấu hình."""
        result = _quiet(3)
        self.assertEqual(result["tong_so_cau_hinh"], 6)

    def test_tk02_truy_vet_mang(self):
        """TK02 [Ca 5] – a=[1, 3, 5, 4, 2]: kết quả đúng ví dụ hình trong sách ([1, 4, 2, 3, 5])."""
        a = [1, 3, 5, 4, 2]
        kiem_tra_mang(a)
        success = hoan_vi_tiep(a)
        self.assertTrue(success)
        self.assertEqual(a, [1, 4, 2, 3, 5])

    def test_tk03_cau_hinh_sau_132(self):
        """TK03 [Ca 3] – a=[1, 3, 2]: cấu hình sau là [2, 1, 3]."""
        a = [1, 3, 2]
        kiem_tra_mang(a)
        success = hoan_vi_tiep(a)
        self.assertTrue(success)
        self.assertEqual(a, [2, 1, 3])

    # ── NHÓM 3: CA BIÊN ───────────────────────────────────

    def test_bien01_n_bang_1(self):
        """BIEN01 – n=1 (tối thiểu): 1 cấu hình duy nhất [1]."""
        result = _quiet(1)
        self.assertEqual(result["tong_so_cau_hinh"], 1)
        self.assertEqual(result["cau_hinh_cuoi"], [1])

    def test_bien02_n_bang_8(self):
        """BIEN02 – n=8 (tối đa): sinh đúng 40320 cấu hình."""
        result = _quiet(8)
        self.assertEqual(result["tong_so_cau_hinh"], 40320)

    def test_bien03_cau_hinh_cuoi(self):
        """BIEN03 [Ca 4] – a=[3, 2, 1]: báo hết, không quay vòng sang [1, 2, 3]."""
        a = [3, 2, 1]
        kiem_tra_mang(a)
        success = hoan_vi_tiep(a)
        # Báo hết (không thể sinh tiếp)
        self.assertFalse(success)
        # Mảng giữ nguyên cấu hình cuối [3, 2, 1]
        self.assertEqual(a, [3, 2, 1])
        # Không quay vòng sang [1, 2, 3]
        self.assertNotEqual(a, [1, 2, 3])

    # ── NHÓM 4: CA LỖI (INPUT KHÔNG HỢP LỆ) ─────────────

    def test_loi01_n_vuot_qua_8(self):
        """LOI01 – n=9 vượt giới hạn: phải ném ValueError."""
        with self.assertRaises(ValueError):
            kiem_tra_n(9)

    def test_loi02_n_nho_hon_1(self):
        """LOI02 – n=0 nhỏ hơn giới hạn: phải ném ValueError."""
        with self.assertRaises(ValueError):
            kiem_tra_n(0)

    def test_loi03_n_sai_kieu(self):
        """LOI03 – n='abc' sai kiểu: phải ném TypeError."""
        with self.assertRaises(TypeError):
            kiem_tra_n("abc")

    def test_loi04_mang_trung_lap(self):
        """LOI04 – Mảng [1,2,2] có phần tử trùng: phải ném ValueError."""
        with self.assertRaises(ValueError):
            kiem_tra_mang([1, 2, 2])

    def test_loi05_mang_sai_gia_tri(self):
        """LOI05 – Mảng [1,5] sai giá trị (n=2 nhưng có số 5): phải ném ValueError."""
        with self.assertRaises(ValueError):
            kiem_tra_mang([1, 5])


# ════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 60)
    print("  ĐỀ TÀI : DT034 - Liệt kê hoán vị theo phương pháp sinh")
    print("  BỘ KIỂM THỬ : 13 ca (Gồm 5 ca yêu cầu & 8 ca mở rộng)")
    print("=" * 60)
    unittest.main(verbosity=2)
