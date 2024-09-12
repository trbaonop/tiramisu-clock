import tkinter as tk
import time
import math

def update_clock():
    canvas.delete("clockhand")
    
    # Lấy thời gian hiện tại
    current_time = time.localtime()
    second = current_time.tm_sec
    minute = current_time.tm_min
    hour = current_time.tm_hour  # Giờ 24 giờ

    # Tính toán vị trí của kim giây, kim phút và kim giờ
    sec_x = 400 + 240 * math.sin(math.radians(second * 6))
    sec_y = 400 - 240 * math.cos(math.radians(second * 6))

    min_x = 400 + 200 * math.sin(math.radians(minute * 6))
    min_y = 400 - 200 * math.cos(math.radians(minute * 6))

    hour_x = 400 + 160 * math.sin(math.radians(hour * 15 + minute * 0.25))
    hour_y = 400 - 160 * math.cos(math.radians(hour * 15 + minute * 0.25))

    # Vẽ kim giây, kim phút và kim giờ
    canvas.create_line(400, 400, sec_x, sec_y, width=2, fill='red', tags="clockhand")
    canvas.create_line(400, 400, min_x, min_y, width=4, fill='black', tags="clockhand")
    canvas.create_line(400, 400, hour_x, hour_y, width=6, fill='black', tags="clockhand")
    
    # Cập nhật sau mỗi 1000ms (1 giây)
    root.after(1000, update_clock)

def create_schedule(canvas):
    # Các hoạt động với góc bắt đầu và kết thúc
    activities = [  
        ("ngủ", 90, 0), 
        ("vệ sinh",0,-10),
        ("sáng",-10,-15),
        ("học bài",-15,-90),
        (" trưa",-90,-105),
        ("chơi",-105,-130),
        ("học",-130,-180),
        ("chơi",-180,-210),
        ("tắm",-210,-225),
        ("tối",-225,-245),
        ("học",-245,-275)


          
    ]
    
    for activity, start_angle, end_angle in activities:
        # Tính toán góc bắt đầu và góc kết thúc
        angle_extent = end_angle - start_angle

        # Vẽ phần lịch trình
        canvas.create_arc(150, 150, 650, 650, start=start_angle, extent=angle_extent, fill="white", outline="black")
        canvas.create_oval(150, 150, 650, 650, outline="black")
        
        # Tính toán vị trí để đặt tên hoạt động
        mid_angle = math.radians(start_angle + angle_extent / 2)
        text_x = 400 + 200 * math.cos(mid_angle)
        text_y = 400 - 200 * math.sin(mid_angle)
        canvas.create_text(text_x, text_y, text=activity, fill="black", font=('Helvetica', 14, 'bold'))
        
        # Vẽ vách ngăn giữa các hoạt động
        end_x = 400 + 250 * math.cos(math.radians(end_angle))
        end_y = 400 - 250 * math.sin(math.radians(end_angle))
        canvas.create_line(400, 400, end_x, end_y, fill="black", width=2)
def draw_hours(canvas):
    for i in range(1, 25):
        angle = math.radians(i * 15)  # 15 độ cho mỗi giờ (360 / 24 = 15)
        hour_x = 400 + 290 * math.sin(angle)
        hour_y = 400 - 290 * math.cos(angle)
        canvas.create_text(hour_x, hour_y, text=str(i), font=('Helvetica', 16, 'bold'))

root = tk.Tk()
root.title("Tiramisu clock")

canvas = tk.Canvas(root, width=800, height=800, bg='yellow')
canvas.pack()

# Vẽ mặt đồng hồ và lịch trình
draw_hours(canvas)
create_schedule(canvas)

# Cập nhật đồng hồ thời gian thực
update_clock()

root.mainloop()
