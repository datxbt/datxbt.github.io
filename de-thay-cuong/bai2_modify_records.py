import tkinter as tk
from tkinter import messagebox
import sqlite3

con = sqlite3.connect("quanlynhanvien.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS nhanvien(empid INTEGER PRIMARY KEY, name TEXT, address TEXT, phone TEXT)")
cur.execute("INSERT OR IGNORE INTO nhanvien VALUES (1, 'Nguyen Van An', 'Ha Noi', '0912345678')")
cur.execute("INSERT OR IGNORE INTO nhanvien VALUES (2, 'Tran Thi Binh', 'Hai Phong', '0987654321')")
con.commit()


def tim(event):
    empid = txtId.get()
    if empid.isdigit() == False:
        messagebox.showerror("Loi", "Emp ID phai la so")
        return
    cur.execute("SELECT * FROM nhanvien WHERE empid = ?", (empid,))
    row = cur.fetchone()
    txtName.delete(0, tk.END)
    txtAddress.delete("1.0", tk.END)
    txtPhone.delete(0, tk.END)
    if row == None:
        messagebox.showerror("Loi", "Khong tim thay nhan vien")
        return
    txtName.insert(0, row[1])
    txtAddress.insert("1.0", row[2])
    txtPhone.insert(0, row[3])


def modify():
    empid = txtId.get()
    name = txtName.get()
    address = txtAddress.get("1.0", tk.END).strip()
    phone = txtPhone.get()
    if empid == "":
        messagebox.showerror("Loi", "Chua nhap Emp ID")
        return
    if name == "":
        messagebox.showerror("Loi", "Chua nhap Name")
        return
    if address == "":
        messagebox.showerror("Loi", "Chua nhap Address")
        return
    if phone == "":
        messagebox.showerror("Loi", "Chua nhap Phone")
        return
    if empid.isdigit() == False:
        messagebox.showerror("Loi", "Emp ID phai la so")
        return
    if phone.isdigit() == False:
        messagebox.showerror("Loi", "Phone phai la so")
        return
    cur.execute("UPDATE nhanvien SET name = ?, address = ?, phone = ? WHERE empid = ?", (name, address, phone, empid))
    con.commit()
    if cur.rowcount == 0:
        messagebox.showerror("Thong bao", "Cap nhat khong thanh cong")
    else:
        messagebox.showinfo("Thong bao", "Cap nhat thanh cong")


window = tk.Tk()
window.title("Modify Records")

tk.Label(window, text="Modify Records.....").grid(row=0, column=1)
tk.Label(window, text="Emp ID:").grid(row=1, column=0)
tk.Label(window, text="Name:").grid(row=2, column=0)
tk.Label(window, text="Address:").grid(row=3, column=0)
tk.Label(window, text="Phone:").grid(row=4, column=0)

txtId = tk.Entry(window)
txtId.grid(row=1, column=1)
txtName = tk.Entry(window)
txtName.grid(row=2, column=1)
txtAddress = tk.Text(window, width=20, height=4)
txtAddress.grid(row=3, column=1)
txtPhone = tk.Entry(window)
txtPhone.grid(row=4, column=1)

thanhcuon = tk.Scrollbar(window, command=txtAddress.yview)
thanhcuon.grid(row=3, column=2, sticky="ns")
txtAddress.config(yscrollcommand=thanhcuon.set)

tk.Button(window, text="Modify", width=8, height=4, command=modify).grid(row=2, column=3, rowspan=2, padx=20)

txtId.bind("<Return>", tim)

window.mainloop()
