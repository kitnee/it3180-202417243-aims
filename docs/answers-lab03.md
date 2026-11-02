# Câu hỏi thảo luận – Lab 03

### 1. Merge base là gì?

- **Định nghĩa:** Trong Git, `merge base` giữa hai commit (hoặc hai nhánh) là **tổ tiên chung gần nhất** (best common ancestor) của chúng trong đồ thị lịch sử commit Directed Acyclic Graph (DAG).
- **Vai trò trong quá trình merge:** Khi thực hiện hợp nhất hai nhánh `A` và `B`, Git sử dụng thuật toán **3-way merge** dựa trên 3 phiên bản: `Merge Base`, nhánh `A` (HEAD hiện tại), và nhánh `B` (nhánh được gộp).
  - Git so sánh sự khác biệt của `A` so với `Merge Base` và của `B` so với `Merge Base`.
  - Nếu thay đổi ở các vị trí khác nhau, Git tự động gộp thành công.
  - Nếu cả hai nhánh cùng sửa đổi một dòng theo cách khác nhau so với `Merge Base`, Git sẽ phát hiện và kích hoạt **Merge Conflict** để người dùng xử lý.

### 2. Vì sao trên nhánh `master` và `release/*` phải dùng `revert` thay vì `reset`?

- **`git reset` (Phá vỡ lịch sử):**
  - Lệnh này dời con trỏ nhánh lùi về quá khứ và **xóa bỏ hoàn toàn** các commit sau đó khỏi lịch sử.
  - Trên các nhánh công khai đã chia sẻ như `master` hay `release/*`, việc dùng `reset` đòi hỏi phải chạy lệnh `git push --force`. Hành động này ghi đè và làm phân kỳ lịch sử mã nguồn của các thành viên khác, gây mất code và vi phạm tính toàn vẹn của cấu hình.
- **`git revert` (Bảo toàn lịch sử):**
  - Lệnh này không xóa bỏ bất kỳ commit nào mà **tạo một commit mới** mang nội dung đảo ngược hoàn toàn thay đổi của commit cần hủy.
  - Lịch sử Git vẫn tiếp tục tiến về phía trước một cách minh bạch và tuyến tính. Mọi thành viên trong nhóm và hệ thống configuration audit đều truy vết được rõ ràng: tính năng đã được đưa vào ở commit nào và bị hoàn tác ở commit nào.
