"""
學習目標:
1. 學習撰寫模組，在python，一個檔案或是一個資料夾都可被視為一個模組。
2. 用test_case來測試自己寫的東西對不對
核心概念:先畫靶再射箭，先設定好自己要的結果，再開始coding。
"""


def get_constellation(month, day) -> str:
    """
    根據生日回傳正確的星座
    牡羊座	3月21日～4月20日
    金牛座	4月21日～5月20日
    雙子座	5月21日～6月20日
    巨蟹座	6月21日～7月22日
    獅子座	7月23日～8月22日
    處女座	8月23日～9月22日
    天秤座	9月23日～10月22日
    天蠍座	10月23日～11月22日
    射手座	11月23日～12月22日
    魔羯座	12月23日～1月21日
    水瓶座	1月22日～2月19日
    雙魚座	2月20日～3月20日
    """
    if month==1:
        if day<=21:
            anwser="魔羯座"
        else:
            anwser="水瓶座"
    if month==2:
        if day<=19:
            anwser="水瓶座"
        else:
            anwser="雙魚座"
    if month==3:
        if day<=20:
            anwser="雙魚座"
        else:
            anwser="牡羊座"
    if month==4:
        if day<=20:
            anwser="牡羊座"
        else:
            anwser="金牛座"
    if month==5:
        if day<=20:
            anwser="金牛座"
        else:
            anwser="雙子座"
    if month==6:
        if day<=20:
            anwser="雙子座"
        else:
            anwser="巨蟹座"
    if month==7:
        if day<=22:
            anwser="巨蟹座"
        else:
            anwser="獅子座"
    if month==8:
        if day<=22:
            anwser="獅子座"
        else:
            anwser="處女座"
    if month==9:
        if day<=22:
            anwser="處女座"
        else:
            anwser="天秤座"
    if month==10:
        if day<=22:
            anwser="天秤座"
        else:
            anwser="天蠍座"
    if month==11:
        if day<=22:
            anwser="天蠍座"
        else:
            anwser="射手座"
    if month==12:
        if day<=22:
            anwser="射手座"
        else:
            anwser="魔羯座"
    return anwser


def get_each_number(number: int) -> []:
    """
    輸入一個正整數，然後將每一位數分開。
    ex get_each_number(1920) 
    return [1,9,2,0]
    """
    string=str(number)
    result=[]
    for i in range(len(string)):
        result.append(int(string[i]))

    return result


def get_life_number(year=1900, month=1, day=1) -> int:
    """
    會回傳一個生命靈數，生命靈數的計算方式是出生年月日的每一個數字的總和，不斷加總至個位數。
    ex 1995 12 13 -> 1+9+9+5+1+2+1+3 = 31 -> 3+1 =4
    這樣生命靈數就是4
    """
    life_num = 10

    return life_num

