
"""
 PyQt는 파이썬 플러그인으로 구현된 크로스 플랫폼 GUI 툴킷 Qt의 
 파이썬 바인딩이다.
 
 Qt는 C++ 라이브러리, 
 PyQt는 Qt를 파이썬에서 쓸 수 있게 해주는 API.
"""

import sys

from PyQt5.QtWidgets import *

# app = QApplication(sys.argv)
app = QApplication([])
label = QLabel("Hello world, I'm python")
label.show()
# sys.exit(app.exec_())
app.exec()  # 앱 실행


"""

1. exec_()와 exec()의 차이

python3 전까지는 exec이 예약된 키워드였기 때문에 
pyqt에서 밑줄을 추가해서 exec_로 사용하게 개발했다.
하지만, python3부터 exec는 더 이상 예약된 키워드가 아니다. 
따라서, pyqt에서도 밑줄이 없는 버전을 제공하게 되었다. 

exec_()가 이미 있음에도 굳이 exec()를 추가한 이유는
C++ 문서와 일치하도록 하기 위해서 이다.

PyQt4에서도 동작하게 하려면 app.exec_()를 쓰는 것이 좋지만,
PyQt6에서는 exec_()를 더 이상 지원하지 않는다.

"""
