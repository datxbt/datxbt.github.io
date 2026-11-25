# Bài 2 (6 điểm): Form "Modify Records" cập nhật nhân viên (Tkinter + SQLite)
import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))     # CSDL nằm cạnh file này

# ===================== CƠ SỞ DỮ LIỆU quanlynhanvien =====================
con = sqlite3.connect("quanlynhanvien.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS nhanvien(empid INTEGER PRIMARY KEY, name TEXT, address TEXT, phone TEXT)")
con.commit()

# Bảng rỗng thì thêm vài nhân viên mẫu để thử chức năng tìm / sửa
cur.execute("SELECT COUNT(*) FROM nhanvien")
if cur.fetchone()[0] == 0:
    cur.executemany("INSERT INTO nhanvien VALUES (?, ?, ?, ?)", [
        (1, "Nguyễn Văn An", "12 Nguyễn Trãi, Thanh Xuân, Hà Nội", "0912345678"),
        (2, "Trần Thị Bình", "45 Giải Phóng, Hai Bà Trưng, Hà Nội", "0987654321"),
        (3, "Lê Minh Châu", "8 Cầu Giấy, Hà Nội", "0901122334"),
    ])
    con.commit()


# ===================== VALIDATE =====================
def kiemtra():
    empid = empid_entry.get().strip()
    name = name_entry.get().strip()
    address = address_text.get("1.0", tk.END).strip()
    phone = phone_entry.get().strip()

    # 1) Tất cả các trường đều phải nhập
    if empid == "" or name == "" or address == "" or phone == "":
        messagebox.showerror("Lỗi", "Tất cả các trường đều phải nhập dữ liệu")
        return False
    # 2) EmpID và Phone phải là số
    if not empid.isdigit():
        messagebox.showerror("Lỗi", "Emp ID phải là số")
        return False
    if not phone.isdigit():
        messagebox.showerror("Lỗi", "Phone phải là số")
        return False
    return True


def xoa_thong_tin():
    name_entry.delete(0, tk.END)
    address_text.delete("1.0", tk.END)
    phone_entry.delete(0, tk.END)


# ===================== NHẤN ENTER Ở Ô EMP ID =====================
def tim_nhanvien(event=None):
    empid = empid_entry.get().strip()
    if not empid.isdigit():
        messagebox.showerror("Lỗi", "Emp ID phải là số")
        return
    cur.execute("SELECT * FROM nhanvien WHERE empid = ?", (int(empid),))
    row = cur.fetchone()
    xoa_thong_tin()
    if row == None:
        messagebox.showwarning("Thông báo", "Không tìm thấy nhân viên có ID = " + empid)
        return
    name_entry.insert(0, row[1])
    address_text.insert("1.0", row[2])
    phone_entry.insert(0, row[3])


# ===================== NÚT MODIFY =====================
def modify():
    if kiemtra() == False:
        return
    try:
        cur.execute("UPDATE nhanvien SET name = ?, address = ?, phone = ? WHERE empid = ?",
                    (name_entry.get().strip(), address_text.get("1.0", tk.END).strip(),
                     phone_entry.get().strip(), int(empid_entry.get().strip())))
        con.commit()
    except sqlite3.Error as e:
        messagebox.showerror("Thất bại", "Cập nhật không thành công!\n" + str(e))
        return
    if cur.rowcount == 0:                         # không có dòng nào bị sửa
        messagebox.showerror("Thất bại", "Cập nhật không thành công: không có nhân viên ID = "
                             + empid_entry.get().strip())
    else:
        messagebox.showinfo("Thành công", "Cập nhật thành công!")


def thoat():
    con.close()
    window.destroy()


# ===================== GIAO DIỆN =====================
window = tk.Tk()
window.title("Modify Records")
window.geometry("520x330")

tk.Label(master=window, text="Modify Records.....", font=("Arial", 12, "italic")).grid(
    row=0, column=0, columnspan=3, pady=15)

tk.Label(master=window, text="Emp ID:").grid(row=1, column=0, padx=(40, 10), pady=6, sticky="w")
tk.Label(master=window, text="Name:").grid(row=2, column=0, padx=(40, 10), pady=6, sticky="w")
tk.Label(master=window, text="Address:").grid(row=3, column=0, padx=(40, 10), pady=6, sticky="nw")
tk.Label(master=window, text="Phone:").grid(row=4, column=0, padx=(40, 10), pady=6, sticky="w")

empid_entry = tk.Entry(master=window, width=30)
empid_entry.grid(row=1, column=1, pady=6, sticky="w")
name_entry = tk.Entry(master=window, width=30)
name_entry.grid(row=2, column=1, pady=6, sticky="w")

# Address: Text nhiều dòng + thanh cuộn dọc (như hình)
khung_address = tk.Frame(master=window)
khung_address.grid(row=3, column=1, pady=6, sticky="w")
address_text = tk.Text(master=khung_address, width=26, height=4, wrap="word")
address_text.pack(side="left")
cuon = tk.Scrollbar(master=khung_address, orient="vertical", command=address_text.yview)
cuon.pack(side="right", fill="y")
address_text.config(yscrollcommand=cuon.set)

phone_entry = tk.Entry(master=window, width=30)
phone_entry.grid(row=4, column=1, pady=6, sticky="w")

tk.Button(master=window, text="Modify", width=8, height=4, command=modify).grid(
    row=2, column=2, rowspan=2, padx=30)

empid_entry.bind("<Return>", tim_nhanvien)       # nhập id + Enter -> hiện thông tin
window.protocol("WM_DELETE_WINDOW", thoat)
empid_entry.focus()
window.mainloop()
