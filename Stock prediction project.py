import yfinance as yf
import matplotlib.pyplot as plt
import tkinter as tk

def web_scrape():
    data = yf.download(tf.get(), start=f'{strt_dt_yr_clicked.get()}-{strt_dt_mnth_clicked.get()}-{strt_dt_day_clicked.get()}', end=f'{end_dt_yr_clicked.get()}-{end_dt_mnth_clicked.get()}-{end_dt_day_clicked.get()}')

    data['Adj Close'].plot()
    plt.show()

root = tk.Tk()
root.title("Stock prediction")
dt_options = [str(i) for i in range(1, 32)]

mnth_options = [str(i) for i in range(1, 13)]

yr_options = [str(i) for i in range(2000, 2025)]

stock_label = tk.Label(root, text="Please enter the stock you want to check for: ")

tf = tk.Entry(root)

strt_dt_label = tk.Label(root, text="Start date for stock price analysis: ")
strt_dt_day_clicked = tk.StringVar()
strt_dt_day_clicked.set('1')
strt_dt_day = tk.OptionMenu(root, strt_dt_day_clicked, *dt_options)
strt_dt_mnth_clicked = tk.StringVar()
strt_dt_mnth_clicked.set('1')
strt_dt_mnth = tk.OptionMenu(root, strt_dt_mnth_clicked, *mnth_options)
strt_dt_yr_clicked = tk.StringVar()
strt_dt_yr_clicked.set('2000')
strt_dt_yr = tk.OptionMenu(root, strt_dt_yr_clicked, *yr_options)

end_dt_label = tk.Label(root, text="End date for stock price analysis: ")
end_dt_day_clicked = tk.StringVar()
end_dt_day_clicked.set('1')
end_dt_day = tk.OptionMenu(root, end_dt_day_clicked, *dt_options)
end_dt_mnth_clicked = tk.StringVar()
end_dt_mnth_clicked.set('1')
end_dt_mnth = tk.OptionMenu(root, end_dt_mnth_clicked, *mnth_options)
end_dt_yr_clicked = tk.StringVar()
end_dt_yr_clicked.set('2000')
end_dt_yr = tk.OptionMenu(root, end_dt_yr_clicked, *yr_options)

sbmtbutton = tk.Button( root , text = "Submit" , command = web_scrape, activebackground='blue' )

stock_label.grid(row=0,column=0,sticky="e")
tf.grid(row=0,column=1)
strt_dt_label.grid(row=1, column=0, sticky="e")
strt_dt_day.grid(row=1, column=1)
strt_dt_mnth.grid(row=1, column=2)
strt_dt_yr.grid(row=1, column=3)
end_dt_label.grid(row=2, column=0, sticky="e")
end_dt_day.grid(row=2, column=1)
end_dt_mnth.grid(row=2, column=2)
end_dt_yr.grid(row=2, column=3)
sbmtbutton.grid(row=3,column=0,columnspan=4,pady=10)

root.mainloop()