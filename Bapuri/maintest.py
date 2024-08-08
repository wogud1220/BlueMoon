from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy, QStackedWidget
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
import os
from datetime import datetime
import pandas as pd

class ClickableLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clicked.emit()

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.resize(1200, 900)

        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")

        self.imageLabel = QLabel(self.page)
        pixmap = QPixmap("./main_image.jpeg")
        pixmap = pixmap.scaled(800, 600, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.imageLabel.setPixmap(pixmap)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.homeButton1 = ClickableLabel(self.page)
        home_pixmap = QPixmap("./home.png")
        home_pixmap = home_pixmap.scaled(50, 50, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.homeButton1.setPixmap(home_pixmap)
        self.homeButton1.setAlignment(QtCore.Qt.AlignLeft)
        self.homeButton1.clicked.connect(lambda: StackedWidget.setCurrentIndex(0))

        self.toolButton = self.createImageButton(self.page, "./apple.png", "매입매출", lambda: StackedWidget.setCurrentIndex(1))
        self.toolButton_2 = self.createImageButton(self.page, "./apple.png", "원가율", lambda: StackedWidget.setCurrentIndex(2))
        self.toolButton_3 = self.createImageButton(self.page, "./apple.png", "시장조사", lambda: StackedWidget.setCurrentIndex(3))
        self.toolButton_4 = self.createImageButton(self.page, "./apple.png", "발주서", lambda: StackedWidget.setCurrentIndex(4))

        self.pageLayout = QVBoxLayout(self.page)
        self.pageLayout.addWidget(self.homeButton1, alignment=QtCore.Qt.AlignLeft)
        self.pageLayout.addWidget(self.imageLabel, alignment=QtCore.Qt.AlignCenter)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.pageLayout.addItem(spacer)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.toolButton)
        self.buttonLayout.addWidget(self.toolButton_2)
        self.buttonLayout.addWidget(self.toolButton_3)
        self.buttonLayout.addWidget(self.toolButton_4)

        self.pageLayout.addLayout(self.buttonLayout)
        StackedWidget.addWidget(self.page)

        self.setupPurchaseSalePage(StackedWidget)
        self.setupCostRatePage(StackedWidget)
        self.setupOrderFormPage(StackedWidget)
        self.setupMarketResearchPage(StackedWidget)

    def createImageButton(self, parent, imagePath, text, clickHandler):
        label = ClickableLabel(parent)
        pixmap = QPixmap(imagePath)
        pixmap = pixmap.scaled(50, 50, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)

        label.setPixmap(pixmap)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet("background-color: rgb(230, 100, 30); color: white; font-size: 20px;")
        label.setMargin(10)

        layout = QVBoxLayout(label)
        textLabel = QLabel(text)
        textLabel.setAlignment(QtCore.Qt.AlignCenter)
        textLabel.setStyleSheet("color: white;")
        textLabel.setFont(QFont('Arial', 12))
        layout.addWidget(textLabel)

        label.clicked.connect(clickHandler)
        return label

    def setupPurchaseSalePage(self, StackedWidget):
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        
        self.homeButton2 = ClickableLabel(self.page_2)
        home_pixmap = QPixmap("./home.png")
        home_pixmap = home_pixmap.scaled(50, 50, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.homeButton2.setPixmap(home_pixmap)
        self.homeButton2.setAlignment(QtCore.Qt.AlignLeft)
        self.homeButton2.clicked.connect(lambda: StackedWidget.setCurrentIndex(0))
        
        self.page2Layout = QVBoxLayout(self.page_2)
        self.page2Layout.addWidget(self.homeButton2, alignment=QtCore.Qt.AlignLeft)
        # DualExcelViewer 추가 필요
        # self.dualExcelViewer = DualExcelViewer(data_path_purchase, data_path_sales)
        # self.page2Layout.addWidget(self.dualExcelViewer)
        
        StackedWidget.addWidget(self.page_2)

    def setupCostRatePage(self, StackedWidget):
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        
        self.homeButton4 = ClickableLabel(self.page_4)
        home_pixmap = QPixmap("./home.png")
        home_pixmap = home_pixmap.scaled(50, 50, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.homeButton4.setPixmap(home_pixmap)
        self.homeButton4.setAlignment(QtCore.Qt.AlignLeft)
        self.homeButton4.clicked.connect(lambda: StackedWidget.setCurrentIndex(0))

        self.label_5 = QLabel(self.page_4)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_5.setText("원가율 페이지")

        self.page4Layout = QVBoxLayout(self.page_4)
        self.page4Layout.addWidget(self.homeButton4, alignment=QtCore.Qt.AlignLeft)
        self.page4Layout.addWidget(self.label_5, alignment=QtCore.Qt.AlignCenter)

        # ReadOnlyExcelViewer 추가 필요
        # self.readOnlyExcelViewer = ReadOnlyExcelViewer(data_path_cost_ratio, '원가율')
        # self.page4Layout.addWidget(self.readOnlyExcelViewer)

        StackedWidget.addWidget(self.page_4)

    def setupOrderFormPage(self, StackedWidget):
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        
        self.homeButton5 = ClickableLabel(self.page_5)
        home_pixmap = QPixmap("./home.png")
        home_pixmap = home_pixmap.scaled(50, 50, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.homeButton5.setPixmap(home_pixmap)
        self.homeButton5.setAlignment(QtCore.Qt.AlignLeft)
        self.homeButton5.clicked.connect(lambda: StackedWidget.setCurrentIndex(0))

        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_6 = QLabel(self.page_5)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_6.setText("발주서 페이지")

        self.search_layout = QHBoxLayout()
        self.lineEdit = QLineEdit(self.page_5)
        self.lineEdit.setFixedSize(300, 40)
        self.lineEdit.setPlaceholderText("찾을 음식을 입력")
        self.search_button = QPushButton("검색", self.page_5)
        self.search_button.setFixedSize(100, 40)
        self.lineEdit.setStyleSheet("font-size: 20px;")
        self.lineEdit.returnPressed.connect(self.search_in_order_table)
        self.search_button.clicked.connect(self.search_in_order_table)
        self.search_layout.addWidget(self.lineEdit)
        self.search_layout.addWidget(self.search_button)

        self.topLayout = QHBoxLayout()
        self.topLayout.addWidget(self.homeButton5, alignment=QtCore.Qt.AlignLeft)
        self.topLayout.addWidget(self.label_6, alignment=QtCore.Qt.AlignCenter)
        self.topLayout.addItem(QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.topLayout.addLayout(self.search_layout)

        self.splitter = QSplitter(Qt.Horizontal)
        self.fixed_amount_table = QTableWidget(self.page_5)
        self.fixed_amount_table.setObjectName("fixed_amount_table")
        self.order_table = QTableWidget(self.page_5)
        self.order_table.setObjectName("order_table")
        self.order_table.itemDoubleClicked.connect(self.add_row_to_fixed_amount_table)
        self.splitter.addWidget(self.fixed_amount_table)
        self.splitter.addWidget(self.order_table)
        self.splitter.setSizes([self.width() - 50, self.width() + 50])

        self.export_button = QPushButton("엑셀로 내보내기", self.page_5)
