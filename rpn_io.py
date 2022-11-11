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
    '''문자열을 출력함수.
    개행 문자 추가 없이 문자열 인수 s 출력.
    '''
    a_str = get_str(s)
    print(a_str, end=' ')
    
def do_println(s):
    '''줄 출력 함수.
    (선택적인) 문자열을 출력하고, 개행 문자를 추가한다.
    '''
    if s:
        do_prints(s)
        print()
    
def get_str(s):
    '''문자열 도우미 함수 가져오기.
    첫 번째 작은따옴표에서 마지막 작은따옴표까지
    텍스트를 읽어온다. 읽을 텍스트가 없으면
    빈 문자열을 반환한다.
    '''
    a = s.find("'")
    b = s.rfind("'")
    if a == -1 or b == -1:
        return ''
    return s[a+1:b]

def do_printvar(s, sym_tab):
    '''변수 출력 함수.
    메인 모듈에서 전달받은 sym_tab에서
    변수를 찾아서 출력한다.
    '''
    wrd = s.split()[0]
    print(sym_tab[wrd], end=' ')
    
def do_input(s, sym_tab):
    '''변수 입력 함수.
    사용자에게 값을 입력받아서 변수에 넣은 후
    심벌 테이블(sym_tab) 참조에 변수를 넣는다.
    '''
    wrd = input()
    if '.' in wrd:
        sym_tab[s] = float(wrd)
    else:
        sym_tab[s] = int(wrd)