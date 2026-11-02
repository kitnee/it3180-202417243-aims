# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.1] - 2026-11-02
### Fixed
- Tìm kiếm DVD theo tiêu đề không phân biệt chữ hoa, chữ thường (`search_by_title`) (Refs #20).

## [1.0.0] - 2026-11-02
### Added
- `Cart.print_cart()`: Hiển thị danh sách các đĩa đã đặt và tổng chi phí.
- `search_by_title()`: Tìm kiếm đĩa DVD theo tiêu đề.
- `total_cost_with_discount()`: Tính tổng chi phí giỏ hàng kèm áp dụng giảm giá.
- `docs/use-case.md`: Tài liệu và sơ đồ Use Case của hệ thống AIMS-mini.
- `tests/`: Bộ kiểm thử tự động với 4 unit tests.

### Fixed
- Giỏ hàng nhận đĩa thứ 21 vượt quá giới hạn tối đa (#7).
- Sửa công thức tính phần trăm giảm giá và validate khoảng `[0, 100]`.
