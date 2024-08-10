def load_excel(self):
    file_name = './매입.xlsx'
    try:
        self.excel_data = pd.read_excel(file_name, sheet_name=None)
        self.df_buy = self.excel_data['물품목록list']
    except Exception as e:
        QMessageBox.critical(self, 'Error', str(e))
    self.df_buy['종류'] = '매입'

    self.df_market = pd.read_excel('./시장조사.xlsx')
    self.df_market['종류'] = '시장'

    self.df_buy['일자'] = pd.to_datetime(self.df_buy['일자'], errors='coerce').dt.date
    self.df_market['일자'] = pd.to_datetime(self.df_market['일자'], errors='coerce').dt.date

    self.df = pd.concat([self.df_market, self.df_buy], ignore_index=True)
    
def search_food(self):
    user_input = self.lineEdit.text() ###################################(수정필요) 검색 단어 할당 
    if user_input and self.df is not None:
        self.filtered_df = self.df[self.df.apply(lambda row: row.astype(str).str.contains(user_input).any(), axis=1)]
        self.not_filtered_df = self.df[
            ~self.df.apply(lambda row: row.astype(str).str.contains(user_input).any(), axis=1)]

        # 중복된 항목을 그룹화하여 일자가 가장 높은 행을 남기기
        df_sorted = self.filtered_df.sort_values('일자', ascending=False)
        df_unique = df_sorted.drop_duplicates(subset=['품목', '단가', '업체명'], keep='first')  # 중복 제거됨
        df_duplicates = self.filtered_df[~self.filtered_df.index.isin(df_unique.index)]  # 중복 되었던 행 모음

        # 데이터프레임 합치기
        self.filtered_df = df_unique
        self.not_filtered_df = pd.concat([self.not_filtered_df, df_duplicates], ignore_index=True)

        self.sort_input()
        self.display_data(self.filtered_df)
    if user_input == '':
        self.filtered_df = self.df
        self.not_filtered_df = pd.DataFrame()
        self.display_data(self.filtered_df)

def sort_input(self):
    current_date = datetime.strptime(QDate.currentDate().toString('yyyy-MM-dd'), '%Y-%m-%d')

    def calculate_priority1(row_date):
        if pd.isnull(row_date):
            return 0
        date_diff = (current_date - row_date).days
        if date_diff <= 0:
            return 0
        elif date_diff <= 90:
            return 1
        elif date_diff <= 180:
            return 2
        elif date_diff <= 270:
            return 3
        elif date_diff <= 365:
            return 4
        else:
            return 5

    # 슬라이스된 데이터 프레임을 명시적으로 복사본을 만듭니다.
    self.filtered_df = self.filtered_df.copy()

    self.filtered_df.loc[:, '우선순위1'] = pd.to_datetime(self.filtered_df['일자']).apply(calculate_priority1)

    temp_df = self.filtered_df.groupby('우선순위1')['단가'].rank(method='min', ascending=True).astype(int)
    self.filtered_df = self.filtered_df.assign(우선순위2=temp_df)

    self.filtered_df = self.filtered_df.sort_values(by=['우선순위1', '우선순위2']).reset_index(drop=True)
    self.filtered_df.drop(columns=['우선순위1', '우선순위2'], inplace=True)