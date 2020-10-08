# three_notes

### 목적
- 여러 번의 복사 붙여넣기를 좀 더 빠르게 가능

### 주요기능
1. 세 개의 노트패드에 메모가 가능
2. 각각의 노트패드에서 복사 버튼을 통해 복사가능
3. 파일명과 경로를 설정하면 각각 텍스트 파일로 저장가능
4. 파일버튼을 클릭하면 전체 저장이 가능
 
### 미리보기
![Three notepads](https://user-images.githubusercontent.com/71266602/95447158-49a48900-099c-11eb-9a42-bb096a51ccfd.png)


Faster copy and paste (GUI basic mini project)

### 상세내용

```python
import tkinter.messagebox as msgbox
from tkinter import *
import pyperclip 
import time
from tkinter import filedialog
```
클립보드를 사용하기 위해서 pyperclip모듈을 사용하였음.
```python
def firstcopy():
    pyperclip.copy(first_txt.get("1.0", END))
    msgbox.showinfo("알림", "텍스트가 클립보드에 저장되었습니다.")
```
pyperclip모듈을 위와같이 사용하였음.
```python
    except Exception as err:  
        msgbox.showerror("에러", err)

```
에러는 위와 같이 한꺼번에 처리하고 에러를 표시하도록 하였음.
