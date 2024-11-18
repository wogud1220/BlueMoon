import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtGui import QFont

class MySemaphore: # 1. 세마포어 클래스 ==========================================================================================================
    # 값(깃발)과 대응되는 큐를 묶어서 관리함
    def __init__(self, name, s, q):
        self.name = name
        self.s= s
        self.q = q

# 지역 변수     
N_time = -1
N = 4 # 원형 버퍼 크기
buffer = [None] * N  # 원형 버퍼
in_idx = 0  # 생산자 인덱스
out_idx = 0  # 소비자 인덱스
count_num = 0

# 큐
QmutexP = []  # mutexP 큐
QmutexC = []  # mutexC 큐
Qnrfull = []  # nrfull 큐
Qnrempty = []  # nrempty 큐

# 세마포어
mutexP = MySemaphore("mutexP", 1, QmutexP) # 생산자 동기화를 위한 락
mutexC = MySemaphore("mutexC", 1, QmutexC) # 소비자 동기화를 위한 락
nrfull = MySemaphore("nrfull", 0, Qnrfull)  # 버퍼가 가득 찬 상태를 나타내는 변수
nrempty = MySemaphore("nrempty", N, Qnrempty)  # 버퍼가 비어있는 상태를 나타내는 변수

class MyApp(QWidget): # 2. 메인 윈도우  클래스 ===================================================================================================
    def __init__(self): # 2-1. 생성자 ============================================================================================================
        super().__init__()
        self.initUI()

        self.update_labels()

    def initUI(self): # 2-2. UI 설정 =============================================================================================================
        self.setWindowTitle('Value Display')
        self.setGeometry(50, 100, 1800, 800)

        self.layout = QGridLayout()

        # 변수 초기값 설정
        global N, mutexP, mutexC, nrfull, nrempty, in_idx, out_idx, buffer
        
        self.a = 1
        self.b = 1
        self.c = 0
        self.d = 4
        self.aa = []
        self.bb = []
        self.cc = []
        self.dd = []
        self.e = 0
        self.f = 0
        self.arr = []

        self.label_aa_list = []  # aa 라벨들을 저장할 리스트
        self.label_bb_list = []  # bb 라벨들을 저장할 리스트
        self.label_cc_list = []  # cc 라벨들을 저장할 리스트
        self.label_dd_list = []  # dd 라벨들을 저장할 리스트
        self.label_arr_list = []  # arr 라벨들을 저장할 리스트

        self.number = [] # 입력 순서 저장
        self.label_number_list = [] # number 라벨들을 저장할 리스트



        # 변수 배치 ---------------------------------------------------------
        # 변수 a의 라벨 배치
        self.label_a = QLabel('0', self)
        self.label_a.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_a, 15, 13)

        # 변수 b의 라벨 배치
        self.label_b = QLabel('0', self)
        self.label_b.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_b, 15, 18)

        # 변수 c의 라벨 배치
        self.label_c = QLabel('0', self)
        self.label_c.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_c, 17, 13)

        # 변수 d의 라벨 배치
        self.label_d = QLabel('0', self)
        self.label_d.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_d, 17, 18)

        # 변수 e의 라벨 배치
        self.label_e = QLabel('0', self)
        self.label_e.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_e, 13, 13)

        # 변수 f의 라벨 배치
        self.label_f = QLabel('0', self)
        self.label_f.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_f, 13, 18)


        # 버튼 배치 ---------------------------------------------------------
        # producer 버튼 배치
        self.button_producer = QPushButton('producer', self)
        self.button_producer.clicked.connect(self.producer_values)
        self.layout.addWidget(self.button_producer, 20, 10, 1, 4)

        # consumer 버튼 배치
        self.button_consumer = QPushButton('consumer', self)
        self.button_consumer.clicked.connect(self.consumer_values)
        self.layout.addWidget(self.button_consumer, 20, 18, 1, 4)


        # consumer 버튼 배치
        self.button_time1 = QPushButton('skip', self)
        self.button_time1.clicked.connect(self.time_values1)
        self.layout.addWidget(self.button_time1, 2, 1, 1, 1)

        # consumer 버튼 배치
        self.button_time2 = QPushButton('1sec', self)
        self.button_time2.clicked.connect(self.time_values2)
        self.layout.addWidget(self.button_time2, 3, 1, 1, 1)

        # consumer 버튼 배치
        self.button_time3 = QPushButton('3sec', self)
        self.button_time3.clicked.connect(self.time_values3)
        self.layout.addWidget(self.button_time3, 4, 1, 1, 1)

        # 글자 배치 ---------------------------------------------------------
        # (14, 13) 위치에 'mutexP' 텍스트를 표시하는 QLabel 추가
        label_mutexP = QLabel('mutexP', self)
        label_mutexP.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(label_mutexP, 14, 13)

        # (14, 18)위치에 'mutexC' 텍스트를 표시하는 QLabel 추가
        label_mutexC = QLabel('mutexC', self)
        label_mutexC.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(label_mutexC, 14, 18)

        # (16, 13) 위치에 'nrfull' 텍스트를 표시하는 QLabel 추가
        label_nrfull = QLabel('nrfull', self)
        label_nrfull.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(label_nrfull, 16, 13)

        # (16, 18)위치에 'nrempty' 텍스트를 표시하는 QLabel 추가
        label_nrempty = QLabel('nrempty', self)
        label_nrempty.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(label_nrempty, 16, 18)

        # (12, 13) 위치에 'in' 텍스트를 표시하는 QLabel 추가
        label_in = QLabel('in', self)
        label_in.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(label_in, 12, 13)

        # (12, 18)위치에 'out' 텍스트를 표시하는 QLabel 추가
        label_out = QLabel('out', self)
        label_out.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(label_out, 12, 18)

        # 변수 arr_n의 라벨 배치
        positions = [(3, 21), (8, 21), (8, 10), (3, 10)]
        for index in range(4):
            row, col = positions[index]
            self.label_arr_n = QLabel('buffer[' + str(index) + ']', self)
            self.label_arr_n.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(self.label_arr_n, row, col)

        # 번호 number의 라벨 배치 (22행 1부터 31열 까지)
        for index in range(1,32):
            self.label_number = QLabel(str(index), self)
            self.label_number.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(self.label_number, 22, index)

        # (1, 1)위치에 'speed' 텍스트를 표시하는 QLabel 추가
        label_out = QLabel('speed', self)
        label_out.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(label_out, 1, 1)

        # 나머지 행에 빈 QLabel 배치
        for row in range(25):
            for col in range(33):
                if (row, col) not in [(13, 13), (13, 18), (15, 13), (15, 18), (17, 13), (17, 18), \
                                      (12, 13), (12, 18), (14, 13), (14, 18), (16, 13), (16, 18), \
                                      (20, 10), (20, 11), (20, 12), (20, 13), \
                                      (20, 18), (20, 19), (20, 20), (20, 21), \
                                      (15, 21), (15, 22), (15, 23), (15, 24), (15, 25), (15, 26), (15, 27), (15, 28), (15, 29), (15, 30) , (15, 31), \
                                      (17, 21), (17, 22), (17, 23), (17, 24), (17, 25), (17, 26), (17, 27), (17, 28), (17, 29), (17, 30) , (17, 31), \
                                      (15, 1), (15, 2), (15, 3), (15, 4), (15, 5), (15, 6), (15, 7), (15, 8), (15, 9), (15, 10) , (15, 11), \
                                      (17, 1), (17, 2), (17, 3), (17, 4), (17, 5), (17, 6), (17, 7), (17, 8), (17, 9), (17, 10) , (17, 11), \
                                      (3, 17), (8, 17), (8, 14), (3, 14), \
                                      (3, 21), (8, 21), (8, 10), (3, 10), \
                                      (22, 1), (22, 2), (22, 3), (22, 4), (22, 5), (22, 6), (22, 7), (22, 8), (22, 9), (22, 10), \
                                      (22, 11), (22, 12), (22, 13), (22, 14), (22, 15), (22, 16), (22, 17), (22, 18), (22, 19), (22, 20), \
                                      (22, 21), (22, 22), (22, 23), (22, 24), (22, 25), (22, 26), (22, 27), (22, 28), (22, 29), (22, 30), (22, 31), \
                                      (23, 1), (23, 2), (23, 3), (23, 4), (23, 5), (23, 6), (23, 7), (23, 8), (23, 9), (23, 10), \
                                      (23, 11), (23, 12), (23, 13), (23, 14), (23, 15), (23, 16), (23, 17), (23, 18), (23, 19), (23, 20), \
                                      (23, 21), (23, 22), (23, 23), (23, 24), (23, 25), (23, 26), (23, 27), (23, 28), (23, 29), (23, 30), (23, 31), \
                                      (1, 1), (2, 1), (3, 1), (4, 1)]:
                    empty_label = QLabel('', self)
                    self.layout.addWidget(empty_label, row, col)
    

        self.setLayout(self.layout)
        self.show()

    def paintEvent(self, event): # 2-3. 그리기 ==============================================================================================================
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 변수 a의 사각형 그리기
        rect_a = self.label_a.geometry()
        painter.setBrush(QBrush(QColor(135, 206, 250)))  # 하늘색
        painter.drawRect(rect_a)

        # 변수 b의 사각형 그리기
        rect_b = self.label_b.geometry()
        painter.setBrush(QBrush(QColor(255, 182, 193)))  # 연한 핑크색
        painter.drawRect(rect_b)

        # 변수 c의 사각형 그리기
        rect_c = self.label_c.geometry()
        painter.setBrush(QBrush(QColor(255, 182, 193)))  # 연한 핑크색
        painter.drawRect(rect_c)

        # 변수 a의 사각형 그리기
        rect_d = self.label_d.geometry()
        painter.setBrush(QBrush(QColor(135, 206, 250)))  # 하늘색
        painter.drawRect(rect_d)

        # aa Draw a blue rectangle spanning 10 cells (from row 15, column 20 to row 15, column 29)
        rect = self.layout.cellRect(15, 1).united(self.layout.cellRect(15, 11))
        painter.setBrush(QBrush(QColor(135, 206, 250)))  # Sky blue color
        painter.drawRect(rect)

        # bb Draw a blue rectangle spanning 10 cells (from row 15, column 20 to row 15, column 29)
        rect = self.layout.cellRect(15, 21).united(self.layout.cellRect(15, 31))
        painter.setBrush(QBrush(QColor(255, 182, 193)))  # 연한 핑크색
        painter.drawRect(rect)

        # cc Draw a blue rectangle spanning 10 cells (from row 15, column 20 to row 15, column 29)
        rect = self.layout.cellRect(17, 1).united(self.layout.cellRect(17, 11))
        painter.setBrush(QBrush(QColor(255, 182, 193)))  # 연한 핑크색
        painter.drawRect(rect)

        # dd Draw a blue rectangle spanning 10 cells (from row 15, column 20 to row 15, column 29)
        rect = self.layout.cellRect(17, 21).united(self.layout.cellRect(17, 31))
        painter.setBrush(QBrush(QColor(135, 206, 250)))  # Sky blue color
        painter.drawRect(rect)

        #number의 번호 사각형 그리기 (22행, 23행 1열부터 31열까지)
        rect = self.layout.cellRect(22, 1).united(self.layout.cellRect(23, 31))
        painter.setBrush(QBrush(QColor(192, 192, 192))) # 회색
        painter.drawRect(rect)

        # 변수 e의 사각형 그리기
        rect_e = self.label_e.geometry()
        painter.setBrush(QBrush(QColor(255, 255, 255)))  # 흰색
        painter.drawRect(rect_e)

        # 변수 f의 사각형 그리기
        rect_f = self.label_f.geometry()
        painter.setBrush(QBrush(QColor(255, 255, 255)))  # 흰색
        painter.drawRect(rect_f)
    
        # (1, 11)부터 (10, 20) 위치까지 큰 원 그리기
        painter.setBrush(QBrush(QColor(255, 255, 0)))  # 노란색
        center_x = (self.layout.cellRect(5, 15).center().x() + self.layout.cellRect(6, 16).center().x()) // 2
        center_y = (self.layout.cellRect(5, 15).center().y() + self.layout.cellRect(6, 16).center().y()) // 2
        radius = 7 * min(self.layout.cellRect(5, 15).width(), self.layout.cellRect(5, 15).height())
        painter.drawEllipse(center_x - radius, center_y - radius, 2 * radius, 2 * radius)

        painter.setPen(QColor(0, 0, 0))  # 검은색
        painter.drawLine(center_x - radius, center_y, center_x + radius, center_y)  # 가로선
        painter.drawLine(center_x, center_y - radius, center_x, center_y + radius)  # 세로선

        painter.setBrush(QBrush(QColor(220, 220, 220)))  # Light gray color
        center_x = (self.layout.cellRect(5, 15).center().x() + self.layout.cellRect(6, 16).center().x()) // 2
        center_y = (self.layout.cellRect(5, 15).center().y() + self.layout.cellRect(6, 16).center().y()) // 2
        radius = 3 * min(self.layout.cellRect(5, 15).width(), self.layout.cellRect(5, 15).height())
        painter.drawEllipse(center_x - radius, center_y - radius, 2 * radius, 2 * radius)

    def update_variable(self): # 2-4. 값 업데이트  =======================================================================================================
        global mutexP, mutexC, nrfull, nrempty, in_idx, out_idx, buffer
        self.a = mutexP.s
        self.b = mutexC.s
        self.c = nrfull.s
        self.d = nrempty.s
        self.aa = []
        self.bb = []
        self.cc = []
        self.dd = []
        for i in range(len(mutexP.q)):
            self.aa.append(mutexP.q[i][0])
        for i in range(len(mutexC.q)):
            self.bb.append(mutexC.q[i][0])
        for i in range(len(nrfull.q)):
            self.cc.append(nrfull.q[i][0])
        for i in range(len(nrempty.q)):
            self.dd.append(nrempty.q[i][0])

        self.e = in_idx
        self.f = out_idx
        self.arr = buffer

    def update(self):  # 2-5. 창 업데이트1  =======================================================================================================
        # 창을 업데이트하여 변경된 값이 표시되도록 함
        self.repaint()
        QApplication.processEvents()

    def update_labels(self): # 2-6. 창 업데이트2  =======================================================================================================
        if(N_time != -1): time.sleep(N_time)
        self.update_variable()
        
        # aa
        # 기존의 라벨 제거
        for label_aa in self.label_aa_list:
            self.layout.removeWidget(label_aa)
            label_aa.deleteLater()
        self.label_aa_list = []  # 라벨 리스트 초기화

        # 리스트의 값 업데이트
        for index, value in enumerate(self.aa):
            if(index > 10): break
            label_aa = QLabel(str(value), self)
            label_aa.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(label_aa, 15, 11 - index)
            self.label_aa_list.append(label_aa)

        
        # bb
        # 기존의 라벨 제거
        for label_bb in self.label_bb_list:
            self.layout.removeWidget(label_bb)
            label_bb.deleteLater()
        self.label_bb_list = []  # 라벨 리스트 초기화
        
        
        # 리스트의 값 업데이트
        for index, value in enumerate(self.bb):
            if(index > 10): break
            label_bb = QLabel(str(value), self)
            label_bb.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(label_bb, 15, 21 + index)
            self.label_bb_list.append(label_bb)
        
        # cc
        # 기존의 라벨 제거
        for label_cc in self.label_cc_list:
            self.layout.removeWidget(label_cc)
            label_cc.deleteLater()
        self.label_cc_list = []  # 라벨 리스트 초기화

        # 리스트의 값 업데이트
        for index, value in enumerate(self.cc):
            if(index > 10): break
            label_cc = QLabel(str(value), self)
            label_cc.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(label_cc, 17, 11 - index)
            self.label_cc_list.append(label_cc)

        # dd
        # 기존의 라벨 제거
        for label_dd in self.label_dd_list:
            self.layout.removeWidget(label_dd)
            label_dd.deleteLater()
        self.label_dd_list = []  # 라벨 리스트 초기화

        # 리스트의 값 업데이트
        for index, value in enumerate(self.dd):
            if(index > 10): break
            label_dd = QLabel(str(value), self)
            label_dd.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(label_dd, 17, 21 + index)
            self.label_dd_list.append(label_dd)

        # arr
        # 기존의 라벨 제거
        for label_arr in self.label_arr_list:
            self.layout.removeWidget(label_arr)
            label_arr.deleteLater()
        self.label_arr_list = []  # 라벨 리스트 초기화

        # 리스트의 값 업데이트
        positions = [(3, 17), (8, 17), (8, 14), (3, 14)]
        for index, value in enumerate(self.arr):
            if value is not None:
                row, col = positions[index]
                label_arr = QLabel(str(value), self)
                label_arr.setAlignment(Qt.AlignCenter)
                self.layout.addWidget(label_arr, row, col)
                self.label_dd_list.append(label_arr)

        # number
        # 기존의 라벨 제거
        for label_number in self.label_number_list:
            self.layout.removeWidget(label_number)
            label_number.deleteLater()
        self.label_number_list = []  # 라벨 리스트 초기화

        # 리스트의 값 업데이트
        for index, value in enumerate(self.number):
            if(index > 30): break
            label_number = QLabel(str(value), self)
            label_number.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(label_number, 23, index + 1)
            self.label_number_list.append(label_number)

        # 변수의 값 업데이트
        self.label_a.setText(str(self.a))
        self.label_b.setText(str(self.b))
        self.label_c.setText(str(self.c))
        self.label_d.setText(str(self.d))
        self.label_e.setText(str(self.e))
        self.label_f.setText(str(self.f))


        self.layout.update()  # 레이아웃 업데이트
        
        self.update()

        
    def keyPressEvent(self, event): # 2-7. 키보드 이벤트 처리  ============================================================================================
        if event.key() == Qt.Key_Escape:
            self.close()
 
    def time_values1(self): # 2-8. 진행 속도 버튼 3개 ======================================================================================================
        global N_time
        N_time = -1

    def time_values2(self):
        global N_time
        N_time = 1

    def time_values3(self):
        global N_time
        N_time = 3

    def producer_values(self): # 2-9. 생산자 버튼  ========================================================================================================
        global count_num

        self.number.append('P')
        self.update_labels()

        count_num += 1
        self.producer(count_num)
        self.update_labels()



    def consumer_values(self): # 2-10. 소비자 버튼  ========================================================================================================
        global count_num

        self.number.append('C')
        self.update_labels()
        
        count_num += 1
        self.consumer(count_num)
        self.update_labels()




    # 3. 원형 다중 버퍼를 사용하는 생산자 소비자 문제 해결  ===========================================================================================
    def P(self, S, n): # 3-1. P연산  ==================================================================================================================
        global mutexP, mutexC, nrfull, nrempty, N_time

        if S.s > 0:
            S.s -= 1
            self.update_labels()
            return True
        else:
            if S.name == "mutexP":
                S.q.append(("P" + str(n), n, 1))
            elif S.name == "nrempty":
                S.q.append(("P" + str(n), n, 2))
            elif S.name == "mutexC":
                S.q.append(("C" + str(n), n, 3))
            elif S.name == "nrfull":
                S.q.append(("C" + str(n), n, 4))
            self.update_labels()
            return False

    def V(self, S, n): # 3-2. V연산  ==================================================================================================================
        global mutexP, mutexC, nrfull, nrempty, N_time

        if len(S.q) > 0:
            target, n_t, step_t = S.q.pop(0)
            self.update_labels()
            return (n_t, step_t)
        else:
            S.s += 1
            self.update_labels()
            return (-1, -1)

    def producer(self, n, step=0): # 3-3. 생산자  ======================================================================================================
        global in_idx, nrempty, nrfull, mutexP, mutexC, N_time
        print("Producer", n)

        # step 0 시작 지점
        if(step == 0):
            if(not self.P(mutexP, n)):
                return

        # step 1 시작 지점
        if(step == 0 or step == 1):
            if(not self.P(nrempty, n)):
                return

        # step 2 시작 지점
        buffer[in_idx] = "M" + str(n)
        in_idx = (in_idx + 1) % N
        self.update_labels()

        n_t, step_t = self.V(nrfull, n)
        if(step_t != -1):
            self.consumer(n_t, step_t)

        n_t, step_t = self.V(mutexP, n)
        if(step_t != -1):
            self.producer(n_t, step_t)

    def consumer(self, n, step=0): # 3-4. 소비자  ======================================================================================================
        global out_idx, nrfull, nrempty, mutexP, mutexC, N_time
        print("Consumer", n)

        # step 0 시작 지점
        if(step == 0):
            if(not self.P(mutexC, n)):
                return

        # step 3 시작 지점
        if(step == 0  or step == 3):
            if(not self.P(nrfull, n)):
                return

        # step 4 시작 지점
        message = buffer[out_idx]
        buffer[out_idx] = None
        out_idx = (out_idx + 1) % N
        self.update_labels()

        n_t, step_t = self.V(nrempty, n)
        if(step_t != -1):
            self.producer(n_t, step_t)

        n_t, step_t = self.V(mutexC, n)
        if(step_t != -1):
            self.consumer(n_t, step_t)



# 4. main ================================================================================================================================================
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

    
