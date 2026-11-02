# Câu hỏi thảo luận – Lab 01

### 1. Vì sao dùng `git mv` thay vì di chuyển tệp bằng chuột hoặc lệnh hệ điều hành thông thường?

- Khi dùng `git mv`, Git hiểu ngay lập tức đây là thao tác đổi tên/di chuyển tệp (`rename`/`move`) và tự động đưa vào staging.
- Nếu di chuyển bằng chuột hoặc lệnh của hệ điều hành, Git sẽ nhìn nhận đó là hành vi xóa tệp cũ (`deleted`) và tạo một tệp mới không dấu vết (`untracked`). Khi commit, lịch sử thay đổi của tệp có thể bị gián đoạn, gây khó khăn cho việc truy vết sau này.

### 2. Nhánh `release/lab01` có phải là baseline không? Vì sao?

- Có. Vì trong Quản lý cấu hình phần mềm, **Baseline** là một trạng thái của cấu hình đã được kiểm tra, thống nhất và đóng băng tại một cột mốc quan trọng, chỉ được thay đổi thông qua quy trình kiểm soát thay đổi chính thức.
- Nhánh `release/lab01` đánh dấu cột mốc hoàn thành và nộp bài Lab 01. Nó đóng băng phiên bản này để giảng viên kiểm tra, trong khi quá trình phát triển các tính năng tiếp theo vẫn tiếp tục diễn ra độc lập trên nhánh `master`.

### 3. Vì sao không nên commit thẳng lên `master` dù làm việc một mình?

- **Xây dựng thói quen:** tuân thủ chuẩn quy trình chuẩn, giúp khi làm việc nhóm lớn sau này mượt mà hơn.
- **Cách ly rủi ro:** Khi mỗi nhánh phục vụ một mục đích duy nhất, nếu tính năng bị lỗi hoặc thử nghiệm thất bại, ta có thể dễ dàng hủy nhánh mà không làm hỏng trạng thái của `master`.
- **Ghi nhận ngữ cảnh:** Pull Request tạo ra một bản ghi có cấu trúc: mục đích, thay đổi, kiểm thử, liên kết Issue với mã nguồn, phục vụ việc kiểm tra lại cấu hình mà commit bình thường khó thể hiện đầy đủ.
