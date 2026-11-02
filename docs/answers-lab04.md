# Câu hỏi thảo luận – Lab 04

### 1. Vì sao `release/*` không bao giờ merge ngược vào `master`? So sánh với GitFlow.

- **Trong Release Flow:**
  - Nhánh `master` là single source of truth và liên tục tiến về phía trước. Nhánh `release/*` chỉ được tạo ra để đóng băng và duy trì một phiên bản bàn giao cụ thể.
  - Nếu merge `release/*` ngược vào `master`, ta có thể vô tình mang các tệp cấu hình phiên bản cũ hoặc các sửa đổi tạm thời của bản release đè lên mã nguồn mới của `master`, gây xung đột và làm rối loạn lịch sử commit. Khi có bản vá lỗi trên release, ta dùng `cherry-pick` để chọn lọc đúng commit sửa lỗi đưa sang `master`.
- **So sánh với GitFlow:**
  - Trong **GitFlow**, tồn tại song song 2 nhánh chính là `main`/`master` (chứa mã production) và `develop` (chứa mã phát triển). Nhánh `release/*` được tạo từ `develop`, sau khi hoàn thiện sẽ phải **merge vào cả 2 nhánh**: merge vào `master` để gắn tag phát hành và merge ngược vào `develop` để giữ mã nguồn đồng bộ.
  - **Release Flow** tinh gọn hơn: chỉ có 1 nhánh chính `master`, không có nhánh `develop`, và nhánh `release/*` hoạt động độc lập một chiều mà không bao giờ merge ngược vào `master`.

### 2. Vì sao phiên bản này được đặt là 1.0.0 mà không phải 0.4.0?

- **Theo quy tắc Semantic Versioning (SemVer):**
  - Dải phiên bản `0.y.z` là giai đoạn phát triển thử nghiệm ban đầu (initial development), mã nguồn và cấu trúc phần mềm chưa ổn định, có thể thay đổi bất kỳ lúc nào (`v0.1.0` đến `v0.3.0` tương ứng với Lab 01 – Lab 03).
  - Phiên bản **`1.0.0`** là cột mốc đánh dấu **Baseline chính thức đầu tiên** của sản phẩm (General Availability / Production-ready). Tại thời điểm này, phần mềm đã hội tụ đầy đủ các chức năng cốt lõi (quản lý giỏ hàng, tìm kiếm, tính giảm giá, kiểm thử tự động, tài liệu use-case) và cam kết giao diện API ổn định. Từ thời điểm này, việc tăng số phiên bản sẽ tuân thủ chặt chẽ nguyên tắc: MAJOR (phá vỡ tương thích), MINOR (thêm tính năng mới), PATCH (sửa lỗi).
