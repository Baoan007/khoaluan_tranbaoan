-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Máy chủ: localhost
-- Thời gian đã tạo: Th5 29, 2023 lúc 03:37 AM
-- Phiên bản máy phục vụ: 10.4.27-MariaDB
-- Phiên bản PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `my_khtn`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('562517d5a202');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `tuyen_sinh`
--

CREATE TABLE `tuyen_sinh` (
  `id` int(11) NOT NULL,
  `ten_nganh` varchar(1000) DEFAULT NULL,
  `khoa` varchar(100) DEFAULT NULL,
  `ma_chuyen_nganh` varchar(50) DEFAULT NULL,
  `chi_tieu` int(11) DEFAULT NULL,
  `hoc_phi_du_kien` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `tuyen_sinh`
--

INSERT INTO `tuyen_sinh` (`id`, `ten_nganh`, `khoa`, `ma_chuyen_nganh`, `chi_tieu`, `hoc_phi_du_kien`) VALUES
(69, 'Sinh học', 'Khoa Sinh học & Công nghệ Sinh học', '7420101', 220, 30400000),
(70, 'Sinh học (Chương trình Chất lượng cao)', 'Khoa Sinh học & Công nghệ Sinh học', '7420101_CLC', 80, 46000000),
(71, 'Công nghệ Sinh học', 'Khoa Sinh học & Công nghệ Sinh học', '7420201', 200, 30400000),
(72, 'Công nghệ Sinh học (Chương trình Chất lượng cao)', 'Khoa Vật lý – Vật lý Kỹ thuật', '7420201_CLC', 120, 46000000),
(73, 'Vật lý học', 'Khoa Vật lý – Vật lý Kỹ thuật', '7440102', 200, 24900000),
(74, 'Hóa học', 'Khoa Hóa học', '7440112', 220, 30400000),
(75, 'Hóa học (Chương trình Chất lượng cao)', 'Khoa Hóa học', '7440112', 120, 46000000),
(76, 'Khoa học Vật liệu', 'Khoa Khoa học và Công nghệ vật liệu', '7440122', 145, 30400000),
(77, 'Địa chất học', 'Khoa Địa chất ', '7440201', 50, 24900000),
(78, 'Hải dương học', 'Khoa Địa chất ', '7440228', 50, 24900000),
(79, 'Khoa học Môi trường', 'Khoa Môi trường', '7440301', 100, 24900000),
(80, 'Khoa học Môi trường (Chương trình Chất lượng cao)', 'Khoa Môi trường', '7440301_CLC', 30, 40000000),
(81, 'Nhóm ngành Toán học, Toán tin, Toán ứng dụng', 'Khoa Công nghệ thông tin', '7460101_NN', 210, 30400000),
(82, 'Khoa học máy tính (Chương trình tiên tiến)', 'Khoa Công nghệ thông tin', '7480101_TT', 80, 53000000),
(83, 'Khoa học Dữ liệu', 'Khoa Công nghệ thông tin', '7480109', 90, 30400000),
(84, 'Công nghệ thông tin (Chương trình Chất lượng cao)', 'Khoa Công nghệ thông tin', '7480201_CLC', 450, 39900000),
(85, 'Nhóm ngành máy tính và công nghệ thông tin( ngành công nghệ thông tin; ngành Kỹ thuật phần mềm; ngành Hệ thống thông tin; ngành Khoa học máy tính; ngành Trí tuệ nhân tạo)', 'Khoa Công nghệ thông tin', '7480201_NN', 450, 30400000),
(86, 'Công nghê Kỹ thuật Hóa học(CT Chất lượng cao)', 'Khoa Hóa học', '7510401_CLC', 120, 50800000),
(87, 'Công nghệ Vật liệu', 'Khoa Khoa học và Công nghệ vật liệu', '7510402', 55, 30400000),
(88, 'Công nghệ Kỹ thuật Môi trường', 'Khoa Môi trường', '7510406', 100, 24900000),
(89, 'Kỹ thuật Điện tử - Viễn thông', 'Khoa Điện tử Viễn thông', '7520207', 160, 30400000),
(90, 'Kỹ thuật Điện tử - Viễn thông(CT chất lượng cao)', 'Khoa Điện tử Viễn thông', '7520207_CLC', 80, 36000000),
(91, 'Kỹ thuật Hạt nhân', 'Khoa Vật lý – Vật lý Kỹ thuật', '7520402', 50, 24900000),
(92, 'Vật lý Y khoa', 'Khoa Vật lý – Vật lý Kỹ thuật', '7520403', 40, 30400000),
(93, 'Kỹ thuật Địa chất', 'Khoa Địa chất ', '7520501', 30, 24900000),
(94, 'Quản lý Tài nguyên và Môi trường', 'Khoa Môi trường', '7850101', 80, 24900000);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Chỉ mục cho bảng `tuyen_sinh`
--
ALTER TABLE `tuyen_sinh`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `tuyen_sinh`
--
ALTER TABLE `tuyen_sinh`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=95;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
