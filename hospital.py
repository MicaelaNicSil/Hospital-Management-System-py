from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import random
import time
import datetime
import mysql.connector


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0=0")

        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEfect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowtoUseMedication = StringVar()
        self.PatientId = StringVar()
        self.PatientNumber = StringVar()
        self.PatientName = StringVar()
        self.DateofBirth = StringVar()
        self.PatientAddress = StringVar()

        Ibltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                         fg="red", bg="white", font=("flamenco", 50, "bold"))
        Ibltitle.pack(side=TOP, fill=X)

        # Dataframe
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=(
            "times new roman", 12, "bold"), text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=(
            "times new roman", 12, "bold"), text="Patient Information")
        DataframeRight.place(z=990, y=5, width=460, height=350)

        # Buttons

        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        # Details

        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        # Data FrameLeft

        lbNameTablet = Label(DataframeLeft, text="Names of Tablet", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbNameTablet.grid(row=0, column=0)

        comNametablet = ttk.Combobox(DataframeLeft, textvariable=self.Nameoftablets, state="readonly", font=(
            "times new roman", 12, "bold"), width=33)
        comNametablet['value'] = (
            "Nice", "Corona Vaccine", "Acetminophen", "Adderall", "Amlodipine", "Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0, column=1)

        lblref = Label(DataframeLeft, font=("arial", 12, "bold"),
                       text="Reference No:", padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=1, column=1)

        lblOose = Label(DataframeLeft, font=(
            "arial", 12, "bold"), text="Dose:", padx=2, pady=4)
        lblOose.grid(row=1, column=0, sticky=W)
        txtDose = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtDose.grid(row=2, column=1)

        lblNoOfTablets = Label(DataframeLeft, font=(
            "arial", 12, "bold"), ext="No Of Tablets::", padx=2, pady=6)
        lblNoOfTablets.grid(row=3, column=0, sticky=W)
        txtNoOfTablets = Entry(DataframeLeft, font=(
            "arial", 13, "bold"), width=35)
        txtNoOfTablets.grid(row=3, column=1)

        lblLot = Label(DataframeLeft, font=("arial", 12, "bold"),
                       text="Issue Date:", padx=2, pady=6)
        lblLot.grid(row=5, column=0, sticky=W)
        txtLot = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtLot.grid(row=4, column=0)

        lblissueDate = Label(DataframeLeft, font=(
            "arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate = Entry(DataframeLeft, font=(
            "arial", 13, "bold"), width=35)
        txtissueDate.grid(row=4, column=0)

        lblExpDATE = Label(DataframeLeft, font=(
            "arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblExpDATE.grid(row=5, column=0, sticky=W)
        txtExpDate = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtExpDate.grid(row=4, column=0)

        lblDailyDose = Label(DataframeLeft, font=(
            "arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblDailyDose.grid(row=5, column=0, sticky=W)
        txtDailyDose = Entry(DataframeLeft, font=(
            "arial", 13, "bold"), width=35)
        txtDailyDose.grid(row=4, column=0)

        lblSideEffect = Label(DataframeLeft, font=(
            "arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblSideEffect.grid(row=5, column=0, sticky=W)
        txtSideEffect = Entry(DataframeLeft, font=(
            "arial", 13, "bold"), width=35)
        txtSideEffect.grid(row=4, column=0)

        lblFurtherinfo = Label(DataframeLeft, font=(
            "arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblFurtherinfo.grid(row=0, column=2, sticky=W)
        txtFurtherinfo = Entry(DataframeLeft, font=(
            "arial", 12, "bold"), width=35)
        txtFurtherinfo.grid(row=0, column=3)

        lblBloodPressure = Label(DataframeLeft, font=(
            "arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure = Entry(
            DataframeLeft, font=("arial", 12, "bold"), width=35)
        txtBloodPressure.grid(row=1, column=3)

        lblStorage = Label(DataframeLeft, font=(
            "arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
        txtStorage.grid(row=2, column=3)

        lblMedicine = Label(DataframeLeft, font=(
            "arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(DataframeLeft, font=(
            "arial", 12, "bold"), width=35)
        txtMedicine.grid(row=3, column=3)

        lblPatientId = Label(DataframeLeft, font=(
            "arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(DataframeLeft, font=(
            "arial", 12, "bold"), width=35)
        txtPatientId.grid(row=4, column=3)

        lblNhsNumber = Label(DataframeLeft, font=(
            "arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber = Entry(DataframeLeft, font=(
            "arial", 13, "bold"), width=35)
        txtNhsNumber.grid(row=5, column=3)

        lblPatientname = Label(DataframeLeft, font=(
            "arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblPatientname.grid(row=6, column=2, sticky=W)
        txtPatientname = Entry(DataframeLeft, font=(
            "arial", 13, "bold"), width=35)
        txtPatientname.grid(row=6, column=3)

        lblDailyDateofBirth = Label(DataframeLeft, font=(
            "arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblDailyDateofBirth.grid(row=7, column=2, sticky=W)
        txtDailyDateofBirth = Entry(
            DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtDailyDateofBirth.grid(row=7, column=3)

        lblDailyPatientAddress = Label(DataframeLeft, font=(
            "arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblDailyPatientAddress.grid(row=8, column=2, sticky=W)
        txtDailyPatientAddress = Entry(
            DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtDailyPatientAddress.grid(row=8, column=3)

        # Dataframe Right

        self.txtPrescription = Text(DataframeRight, font=(
            "aria", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # Buttons2
        btnPrespcription = Button(Buttonframe, command=self.iPrectioption, text="Prescription",
                                  bg="green", fg="withe", font=("aria", 12, "bold"), width=45, height=16, padx=2, pady=6)
        btnPrespcription.grid(row=0, column=0)

        btnPrespcriptionData = Button(Buttonframe, command=self.iPrectioptionData, text="Prescription Data",
                                      bg="green", fg="withe", font=("aria", 12, "bold"), width=45, height=16, padx=2, pady=6)
        btnPrespcriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, command=self.update_data, text="Update", bg="green",
                           fg="withe", font=("aria", 12, "bold"), width=45, height=16, padx=2, pady=6)
        btnPrespcription.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, command=self.idelete, text="Delete", bg="green", fg="withe", font=(
            "aria", 12, "bold"), width=45, height=16, padx=2, pady=6)
        btnPrespcription.grid(row=0, column=3)

        btnClear = Button(Buttonframe, command=self.clear, text="Clear", bg="green", fg="withe", font=(
            "aria", 12, "bold"), width=45, height=16, padx=2, pady=6)
        btnPrespcription.grid(row=0, column=4)

        btnExit = Button(Buttonframe, command=self.iExit, text="Exit", bg="green", fg="withe", font=(
            "aria", 12, "bold"), width=45, height=16, padx=2, pady=6)
        btnPrespcription.grid(row=0, column=0)

# ScrollBar
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(FrameDetails, column=("nameoftable", "ref", "dose", "nooftables", "lot", "issuedate", "expdate",
                                           "dailydose", "storage", "nhsnumber", "phname", "dob", "address"), xscrollcommand=scroll_y.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hostpital_table.heading("nameoftable", text="Name of Table")
        self.hostpital_table.heading("ref", text="Reference No.")
        self.hostpital_table.heading("dose", text="Dose")
        self.hostpital_table.heading("nooftables", text="No of Tables")
        self.hostpital_table.heading("lot", text="Lot")
        self.hostpital_table.heading("issuedate", text="Issue Date")
        self.hostpital_table.heading("expdate", text="Exp Date")
        self.hostpital_table.heading("dailydose", text="Daily Dose")
        self.hostpital_table.heading("storage", text="Storage")
        self.hostpital_table.heading("nhsnumber", text="NHS Number")
        self.hostpital_table.heading("pname", text="Patient Name")
        self.hostpital_table.heading("dob", text="DOB")
        self.hostpital_table.heading("address", text="Address")

        self.hostpital_table["show"] = "headings"

        self.hospital_table.pack(fill=BOTH, expand=1)

        self.hospital_table.column("nameoftable", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftables", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)

        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table_bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

        # Functionality Declaration

        def iPrescriptionData(self):
            if self.Nameoftablets.get() == "" or self.ref.get():
                messagebox.showerror("Error", "All fields are required")
            else:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Test123", database="my_data")
                my_cursor = conn.cursor()
        #!!carrefull from now on
                my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.Nameoftablets.get(),
                    self.ref.get(),
                    self.Dose.get(),
                    self.Numberoftablets.get(),
                    self.Lot.get(),
                    self.Issuedate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.StorageAdvice.get(),
                    self.nhsNumber.get(),
                    self.PatientName.get(),
                    self.DateofBirth.get(),
                    self.PatientAdress.get(),
                ))
                conn.commit()
                self.fetch_data
                conn.close()
                messagebox.showinfo("Success", "Record has been inserted")

        def update(self):
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Test123", database="my_data")
            my_cursor = conn.cursor()
            my_cursor.execute("update hospital set NameofTabkets=%s,Dose=%s,Lot=%s,Issue_Date=%s,Exp_Date=%s,Daily_Date=%s,Storage=%s,NHSNumber=%s,Patient_Name=%s,DOB=%s Where Reference_No=%s", (self.Nameoftablets.get(),
                                                                                                                                                                                                   self.ref.get(),
                                                                                                                                                                                                   self.Dose.get(),
                                                                                                                                                                                                   self.Numberoftablets.get(),
                                                                                                                                                                                                   self.Lot.get(),
                                                                                                                                                                                                   self.Issuedate.get(),
                                                                                                                                                                                                   self.ExpDate.get(),
                                                                                                                                                                                                   self.DailyDose.get(),
                                                                                                                                                                                                   self.StorageAdvice.get(),
                                                                                                                                                                                                   self.nhsNumber.get(),
                                                                                                                                                                                                   self.PatientName.get(),
                                                                                                                                                                                                   self.DateofBirth.get(),
                                                                                                                                                                                                   self.PatientAdress.get(),
                                                                                                                                                                                                   ))

        def fetch_data(self):
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Test123", database="my_data")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from hospital")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.hospital_table.delete(*self.hospital_table.get_childern())
                for i in rows:
                    self.hospital_table.insert("", END, values=i)
                    conn.commit()
                conn.close()

    def get_cursor(self, events=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.Numberoftablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateofBirth.set(row[11])
        self.PatientAdress.set(row[12])

    def iPrectioption(self):
        self.txtPrescription.insert(
            END, "Name of Tablets:\t\t\t" + self.Nameoftablets.get() + "\n")
        self.txtPrescription.insert(
            END, "Reference No:\t\t\t" + self.ref.get() + "\n")
        self.txtPrescription.insert(
            END, "Dose:\t\t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(
            END, "Number of Tablets:\t\t\t" + self.NumberofTablets.get() + "\n")
        self.txtPrescription.insert(END, "Lot:\t\t\t" + self.Lot.get() + "\n")
        self.txtPrescription.insert(
            END, "Issue Date:\t\t\t" + self.Issuedate.get() + "\n")
        self.txtPrescription.insert(
            END, "Exp date:\t\t\t" + self.ExpData.get() + "\n")
        self.txtPrescription.insert(
            END, "Daily Dose:\t\t\t" + self.DailyDose.get() + "\n")
        self.txtPrescription.insert(
            END, "Side Effect:\t\t\t" + self.sideEfect.get() + "\n")
        self.txtPrescription.insert(
            END, "Further Information:\t\t\t" + self.FurtherInformation.get() + "\n")
        self.txtPrescription.insert(
            END, "StorageAdvice:\t\t\t" + self.StorageAdvice.get() + "\n")
        self.txtPrescription.insert(
            END, "DrivingUsingMachine:\t\t\t" + self.DrivingUsingMachine.get() + "\n")
        self.txtPrescription.insert(
            END, "PatientId:\t\t\t" + self.PatientId.get() + "\n")
        self.txtPrescription.insert(
            END, "NHSNumber:\t\t\t" + self.nhsNumber.get() + "\n")
        self.txtPrescription.insert(
            END, "PatientName:\t\t\t" + self.PatientName.get() + "\n")
        self.txtPrescription.insert(
            END, "DateOfBirth:\t\t\t" + self.DateofBirth.get() + "\n")
        self.txtPrescription.insert(
            END, "PatientAdress:\t\t\t" + self.PatientAddress.get() + "\n")

    def idelete(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="Test123", database="my_data")
        my_cursor = conn.cursor()
        query = "delete from hospital where Reference_No=%s"
        value = (self.ref.get(),)
        my_cursor.execute(query, value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete", "Patient has been deleted")

    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.Numberoftablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.StorageAdvice.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateofBirth.set("")
        self.PatientAdress.set("")
        self.txtPrescription.delete("1.0", END)

    def iExit(self):
        iExit = messagebox.askyesno(
            "Hospital management system", "Confirm you want to exit")
        if iExit > 0:
            root.destroy()
            return
