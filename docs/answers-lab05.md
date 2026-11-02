# Câu hỏi thảo luận – Lab 05

### 1. So sánh ưu, nhược điểm của mô hình Upstream First so với Release First?

- **Mô hình Release First (Áp dụng trong học phần):**
  - **Cách làm:** Khi phát hiện lỗi ở bản phát hành cũ (ví dụ `v1.0.0`), lập trình viên tạo nhánh `hotfix/*` từ chính nhánh `release/lab04`, sửa và phát hành bản vá `v1.0.1` ngay lập tức, sau đó dùng `cherry-pick -x` để lan truyền bản sửa về `master` và các nhánh release khác.
  - **Ưu điểm:** Tốc độ phản hồi cực nhanh, ưu tiên giải quyết sự cố cho khách hàng/người dùng đang chạy bản production mà không bị phụ thuộc vào trạng thái mã nguồn đang phát triển dở dang trên `master`.
  - **Nhược điểm:** Phải ghi nhớ và có quy trình kiểm soát chặt chẽ việc lan truyền ngược lại `master`; nếu sơ suất quên cherry-pick, lỗi sẽ bị tái diễn (hồi quy - regression) ở các bản phát hành tương lai.
- **Mô hình Upstream First (Microsoft / Nhân Linux):**
  - **Cách làm:** Mọi bản sửa lỗi luôn phải được commit và kiểm thử trên nhánh chính `master` (upstream) trước, sau đó mới `cherry-pick` ngược về các nhánh `release/*` đang cần bảo trì.
  - **Ưu điểm:** Đảm bảo nhánh chính không bao giờ bị sót lỗi, triệt tiêu nguy cơ lỗi hồi quy trên dòng phát triển tương lai.
  - **Nhược điểm:** Nếu mã nguồn trên `master` đã tái cấu trúc quá nhiều so với bản release cũ, việc cherry-pick ngược về release có thể gặp xung đột rất phức tạp và đòi hỏi sửa lại nhiều lần.

### 2. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện?

- **Cách 1 – Vòng lặp kiểm toán hành vi đa phiên bản:**
  ```bash
  for ref in v1.0.1 v1.1.0 master; do
    git switch --detach -q $ref
    python -c "from aims.dvd import DigitalVideoDisc as D; from aims.search import search_by_title; \
    print(len(search_by_title([D('The Lion King')], 'lion')))"
  done
  ```
  Nếu quên lan truyền sang `release/lab05`, tại mốc `v1.1.0` câu lệnh trên sẽ in ra **`0`** (tìm không thấy đĩa do lỗi phân biệt hoa-thường), giúp phát hiện ngay lập tức.
- **Cách 2 – Dùng lệnh so sánh commit giữa hai nhánh:**
  ```bash
  git cherry -v origin/release/lab05 origin/release/lab04
  ```
  Hoặc kiểm tra dấu vết cherry-pick:
  ```bash
  git log origin/release/lab05 --grep "cherry picked from commit <FIX_SHA>"
  ```
  Nếu không có commit nào được tìm thấy trên `release/lab05`, chứng tỏ bản sửa lỗi chưa được lan truyền.
