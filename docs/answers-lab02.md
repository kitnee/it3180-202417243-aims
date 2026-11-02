# Câu hỏi thảo luận – Lab 02

### 1. Vì sao phải đồng bộ `master` trước khi gửi PR?

- Đảm bảo nhánh tính năng hoạt động tương thích với mã nguồn mới nhất trên `master` ngay tại máy local (chạy thử chương trình, chạy test), tránh đưa lỗi hồi quy lên nhánh chính.
- Nếu có merge conflict thì người sở hữu nhánh sẽ giải quyết trực tiếp trước khi tạo PR, giúp người review xem được mã sạch và nút merge trên GitHub không bị khóa vì conflict.

### 2. Khi nào không được rebase?

- Không được rebase trên các nhánh công khai như `master`, `release/*` hoặc nhánh chung đang làm việc cùng người khác.
- **Nguyên nhân:** Lệnh rebase sẽ viết lại lịch sử commit (thay đổi toàn bộ mã băm SHA của các commit). Nếu người khác đã kéo nhánh này về máy, việc rebase sẽ làm phân kỳ lịch sử, từ đó gây conflict khi đồng bộ lại. Chỉ nên rebase trên nhánh tính năng cá nhân cục bộ chưa chia sẻ hoặc khi được sự thống nhất của cả nhóm.

### 3. Nhánh `feature/*` khác `topic/*` ra sao?

- **`feature/*` (Feature branch):** Dành cho việc phát triển các **tính năng nghiệp vụ phần mềm** mà người dùng hoặc hệ thống yêu cầu (ví dụ: `feature/cart-print`, `feature/search-by-title`). Các nhánh này thường có logic mã nguồn, kiểm thử tương ứng và có thể kéo dài qua nhiều lần commit.
- **`topic/*` (Topic branch):** Dành cho các **chủ đề công việc phụ trợ, cấu hình hoặc tài liệu** ngắn hạn (ví dụ: `topic/pr-template`, `topic/use-case-diagram`, `topic/ci-unit-tests`). Chúng có phạm vi hẹp, giải quyết một nhiệm vụ cụ thể không phải tính năng nghiệp vụ của phần mềm và thường có vòng đời rất ngắn.
