from os import walk,path,remove
from PyQt6.QtWidgets import (
    QApplication, QWidget, QFileDialog,
)
from PyQt6.QtCore import (
    Qt, pyqtSlot, QUrl, QCoreApplication,
)
from PyQt6.QtMultimedia import QSoundEffect

from kana2epub_ui import Ui_kana2epub
from kanasouphtml import *

class MainWindow(QWidget, Ui_kana2epub):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # 窗口无win风格框
        self.pushButton_8.setEnabled(False)  # 输出选择按钮
        self.connects()

        self.draggable = False  # 拖动窗口预设
        self.offset = None  # 拖动窗口预设
        self.epub_paths = None  # 读取的epub文件路径
        self.out_path = None  # epub输出路径
        self.saved_out_path = None  # 用户输入的输出路径
        self.language = 1  # 0中文 1英语 2日语
        self.show()

    def connects(self):
        self.pushButton_4.clicked.connect(self.window().close)
        self.pushButton_5.clicked.connect(self.window().showMinimized)
        self.checkBox.checkStateChanged.connect(self.check_change)

        self.pushButton_6.clicked.connect(self.open_file_dlg)  # 槽函数处理epub文件
        self.pushButton_8.clicked.connect(self.open_path_dlg)
        self.pushButton.clicked.connect(self.set_chinese)
        self.pushButton_2.clicked.connect(self.set_english)
        self.pushButton_3.clicked.connect(self.set_japanese)

    @pyqtSlot()
    def open_file_dlg(self):
        # 加载声音
        snd = QSoundEffect(QCoreApplication.instance())
        snd.setSource(QUrl.fromLocalFile(resource_path("./src/sound.wav")))
        snd.setLoopCount(1)
        snd.setVolume(5)

        snd2 = QSoundEffect(QCoreApplication.instance())
        snd2.setSource(QUrl.fromLocalFile(resource_path("./src/sound1.wav")))
        snd2.setLoopCount(1)
        snd2.setVolume(5)

        # 根据语言重设按键样式
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"            border: 1px solid rgba(155,155,155,255);\n"
"            border-radius: 1px;\n"
"            background-color: rgba(100, 100, 255, 100);\n"
"            color:rgb(86, 86, 86);}\n")
        match self.language:
            case 0:
                self.pushButton_6.setText("运行中...")
                self.label.setText("当前状态： 处理中，请稍等......")
                self.label.repaint()
            case 1:
                self.pushButton_6.setText("PROCESSING...")
                self.label.setText("status bar： processing please wait a moment")
                self.label.repaint()
            case 2:
                self.pushButton_6.setText("処理中...")
                self.label.setText("ステータスバー： 処理中，しばらくお待ちください......")
                self.label.repaint()

        # 创建文件拾取对话框
        file_dlg = QFileDialog(self)
        file_dlg.setFileMode(QFileDialog.FileMode.ExistingFiles)
        default_path = "C:"
        epub_filter = "epub(*.epub)"
        match self.language:
            case 0:
                epub_paths = QFileDialog.getOpenFileNames(file_dlg, "请选择epub文件", default_path, epub_filter)
            case 1:
                epub_paths = QFileDialog.getOpenFileNames(file_dlg, "please select epub files", default_path, epub_filter)
            case 2:
                epub_paths = QFileDialog.getOpenFileNames(file_dlg, "epubファイルを選択してください", default_path, epub_filter)
        self.epub_paths = epub_paths[0]  # 所有待处理文件路径
        if self.epub_paths == [] or self.epub_paths[0] == "":
            self.pushButton_6.setStyleSheet(
                "QPushButton{\n"
                "      border: 1px solid rgba(155,155,155,100);\n"
                "      border-radius: 1px;\n"
                "      background-color: rgba(45, 26, 255, 20);\n"
                "      color:rgb(86, 86, 86);}\n"
                "  QPushButton:hover{\n"
                "      background-color: rgba(45, 26, 255, 100);}\n"
                "  QPushButton:pressed{\n"
                "      background-color: rgba(205, 10, 155, 100);}")
            match self.language:
                case 0:
                    self.pushButton_6.setText("开始")
                case 1:
                    self.pushButton_6.setText("KANA2EPUB")
                case 2:
                    self.pushButton_6.setText("起動")
            match self.language:
                case 0:
                    self.label.setText("当前状态： 点击右下角开始按钮以选择文件")
                case 1:
                    self.label.setText("status bar： please push the kana2epub button to select epub files")
                case 2:
                    self.label.setText("ステータスバー： 起動ボタンを押してepubファイルを選択してください")
            return

        # 查看是否选择输出路径
        if self.saved_out_path is None:
            self.out_path = path.dirname(path.abspath(self.epub_paths[0]))
        else:
            self.out_path = self.saved_out_path

        ####################################################################################
        # extract the epub file by zipfile
        # epub文件解压缩
        str_len = len(self.epub_paths)
        i = 1
        for single_file in self.epub_paths:
            epub_name = path.basename(single_file.replace('.epub', ''))
            if path.exists(f'"{self.out_path}\\kanaepub_tmp"'):
                deldir(f'"{self.out_path}\\kanaepub_tmp"')
            try:
                raw_file = zipfile.ZipFile(single_file, 'r')
                if not os.path.exists(f"{self.out_path}/kanaepub_tmp"):
                    os.mkdir(f"{self.out_path}/kanaepub_tmp")
                for name in raw_file.namelist():
                    raw_file.extract(name, f"{self.out_path}/kanaepub_tmp")
            except Exception as e:
                print("oops...extract failed!")
                print(e)

            try:
                for root, dirs, files in walk(f"{self.out_path}/kanaepub_tmp"):
                    for file in files:
                        append_hirakana_to_webpage(path.join(root, file))  # 对文件夹内的所有html进行注音
            except Exception as e:
                print("oops...append failed!")
                print(e)

            # repackage the tmp folder into epub
            # epub重打包
            try:
                if path.exists(f"{self.out_path}/{epub_name + "(kana).epub"}"):
                    remove(f"{self.out_path}/{epub_name + "(kana).epub"}")
                zip_epub(f"{self.out_path}/kanaepub_tmp", f"{self.out_path}/{epub_name + "(kana).epub"}")
                deldir(f"{self.out_path}/kanaepub_tmp")
                snd2.play()
                match self.language:
                    case 0:
                        self.label.setText(f"当前状态： 处理中，请稍等......({i}/{str_len})")
                        self.label.repaint()
                    case 1:
                        self.label.setText(f"status bar： processing please wait a moment({i}/{str_len})")
                        self.label.repaint()
                    case 2:
                        self.label.setText(f"ステータスバー： 処理中，しばらくお待ちください......({i}/{str_len})")
                        self.label.repaint()
                i = i + 1
            except Exception as e:
                print("oops...repackage failed!")
                print(e)

        ######################################################################################
        # 结束交互
        snd.play()
        match self.language:
            case 0:
                self.label.setText("当前状态： EPUB转换完成")
            case 1:
                self.label.setText("status bar： EPUB Conversion Successful!")
            case 2:
                self.label.setText("ステータスバー： EPUB変換が完了しました")
        self.pushButton_6.setStyleSheet(
        "QPushButton{\n"
        "      border: 1px solid rgba(155,155,155,100);\n"
        "      border-radius: 1px;\n"
        "      background-color: rgba(45, 26, 255, 20);\n"
        "      color:rgb(86, 86, 86);}\n"
        "  QPushButton:hover{\n"
        "      background-color: rgba(45, 26, 255, 100);}\n"
        "  QPushButton:pressed{\n"
        "      background-color: rgba(205, 10, 155, 100);}")
        match self.language:
            case 0:
                self.pushButton_6.setText("开始")
            case 1:
                self.pushButton_6.setText("KANA2EPUB")
            case 2:
                self.pushButton_6.setText("起動")

    @pyqtSlot()
    def open_path_dlg(self):
        file_dlg = QFileDialog(self)
        path = "C:\\"
        self.saved_out_path = QFileDialog.getExistingDirectory(file_dlg, "请选择输出路径",path)
        self.lineEdit.setText(self.saved_out_path)

    @pyqtSlot()
    def check_change(self):
        if self.checkBox.isChecked():
            self.pushButton_8.setEnabled(True)
        else:
            self.pushButton_8.setEnabled(False)

    @pyqtSlot()
    def set_chinese(self):
        self.language = 0
        self.checkBox.setText("自定义输出路径")
        self.label.setText("当前状态： 点击右下角开始按钮以选择文件")
        self.pushButton_6.setText("开始")

    @pyqtSlot()
    def set_english(self):
        self.language = 1
        self.checkBox.setText("customize the output path")
        self.label.setText("status bar： please push the kana2epub button to select epub files")
        self.pushButton_6.setText("KANA2EPUB")

    @pyqtSlot()
    def set_japanese(self):
        self.language = 2
        self.checkBox.setText("出力パスをカスタマイズする")
        self.label.setText("ステータスバー： 起動ボタンを押してepubファイルを選択してください")
        self.pushButton_6.setText("起動")

    def mousePressEvent(self, event):
        # 窗口拖动预备
        if (event.button() == Qt.MouseButton.LeftButton) and event.pos().y() < 30:  # 鼠标在窗口上方
            self.draggable = True
            self.offset = (event.pos())

    def mouseMoveEvent(self, event):
        # 窗口拖动
        if self.draggable:
            self.move(self.mapToGlobal(event.pos()) - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.draggable = False

# 开启gui程序循环
a = QApplication(sys.argv)
window = MainWindow()
a.exec()