def open_rpn_file():
    '''오픈-소스-파일 함수. 파일을 열고,
    읽은 줄을 리스트에 넣어서 반환한다.
    '''
    while True:
        try:
            fname = input('Enter RPN source: ')
            if not fname:
                return None
            f = open(fname, 'r')
            break
        except:
            print('File not found. Re-enter.')
    a_list = f.readlines()
    return a_list

def do_prints(s):
    '''문자열을 출력하여 PRINTS 지침을 수행한다.
    '''
    a_str = get_str(s)
    print(a_str, end=' ')
    
def do_println(s):
    '''PRINTLN 지침 수행: 만약 선택적인 문자열 인수가 주어지면
    이를 출력하고 나서, 무조건 개행문자를 출력한다.
    '''
    if s:
        do_prints(s)
    print()
    
def get_str(s):
    '''do_prints의 도우미 함수
    '''
    a = s.find("'")
    b = s.rfind("'")
    if a == -1 or b == -1:
        return ''
    return s[a+1:b]

def do_printvar(s, sym_tab):
    '''PRINTVAR 지침 수행: 변수 이름이 문자열 s에 있는지 찾아본 후
    심벌 테이블에 이 이름이 있는지 찾아본다.
    '''
    wrd = s.split()[0]
    print(sym_tab[wrd], end=' ')
    
def do_input(s, sym_tab):
    '''INPUT 지침 수행: 사용자에게 값을 입력받은 후
    심벌 테이블의 문자열 s 색인에 해당 값을 넣는다.
    '''
    wrd = input()
    sym_tab[s] = float(wrd)