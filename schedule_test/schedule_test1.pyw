## pip install pystray
## pip install schedule

from pystray import Icon, MenuItem, Menu
from PIL import Image
import time
import threading
import schedule

class taskTray:
    def __init__(self, icon_image_file):
        self.status = False

        ## アイコンの画像
        image = Image.open(icon_image_file)
        ## 右クリックで表示されるメニュー
        menu = Menu(
                    MenuItem('Task', self.doTask),
                    MenuItem('Exit', self.stopProgram),
                )

        self.icon = Icon(name='nameTray', title='titleTray', icon=image, menu=menu)


    def doTask(self):
        print('実行しました。')

    def runSchedule(self):
        ## 5秒毎にタスクを実行する。
        schedule.every(5).seconds.do(self.doTask)
        ## status が True である間実行する。
        while self.status:
            schedule.run_pending()
            time.sleep(1)

    def stopProgram(self, icon):
        self.status = False

        ## 停止
        self.icon.stop()

    def runProgram(self):
        self.status = True

        ## スケジュールの実行
        task_thread = threading.Thread(target=self.runSchedule)
        task_thread.start()

        ## 実行
        self.icon.run()


if __name__ == '__main__':
    system_tray = taskTray(icon_image_file="pyIconImage2.png")
    system_tray.runProgram()