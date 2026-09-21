# Kelas tambahan (Blueprint) agar objek pekerja boleh disahkan
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Fitur Wajib: Buat class Company
class Company:
    def __init__(self):
        # Gunakan enkapsulasi untuk array data karyawan
        self.__employees = []

    def add_employee(self, employee_obj):
        # Petunjuk Teknis: Manfaatkan fungsi bawaan isinstance(obj, ClassName)
        # untuk memvalidasi input object sebelum dimasukkan ke dalam list.
        if isinstance(employee_obj, Employee):
            self.__employees.append(employee_obj)
            print(f"Pekerja '{employee_obj.name}' berjaya ditambah ke dalam sistem.")
        else:
            print("Ralat: Input yang dimasukkan bukan dari kelas Employee.")

    # Buat private method __calculate_payroll() yang hanya bisa dipanggil dari dalam class
    def __calculate_payroll(self):
        total_payroll = 0
        for emp in self.__employees:
            total_payroll += emp.salary
        return total_payroll

    # Kaedah awam (public method) yang memanggil private method dari dalam kelas
    def process_payroll(self):
        total = self.__calculate_payroll()
        print(f"Jumlah Pembayaran Gaji (Payroll): RM{total}")
        return total

# --- Sesi Pengujian (Bebas Ralat) ---
if __name__ == "__main__":
    my_company = Company()

    # Membina objek dari kelas Employee
    emp1 = Employee("Ali", 5000)
    emp2 = Employee("Aminah", 6500)

    # 1. Menguji fungsi tambah pekerja (Input sah)
    my_company.add_employee(emp1)
    my_company.add_employee(emp2)

    # 2. Menguji fungsi isinstance (Input tidak sah - bukan objek Employee)
    my_company.add_employee("Pekerja Sambilan")

    # 3. Menguji panggilan ke private method melalui kaedah awam
    my_company.process_payroll()
    
    # Nota: Jika my_company.__calculate_payroll() dipanggil secara terus di luar kelas, 
    # Python akan memaparkan ralat 'AttributeError' sebagai bukti enkapsulasi berfungsi.