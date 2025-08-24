from app import *
import sys
from openai import OpenAI
 
# --- Placez votre clé api d'openai ici ---
OPENAI_KEY = "Your API KEY here !"
client = OpenAI(api_key=OPENAI_KEY) 

def convert():
    # Getting input text content
    T = ui.inputTextEdit.toPlainText()
    print(T)
    # choose voice from: 'alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer', 'coral', 'verse', 'ballad', 'ash'
    selected_voice = ui.combo_voice.currentText()
    
    speech = client.audio.speech.create(
        model = "gpt-4o-mini-tts", 
        
        voice = selected_voice, 
        input= T
    )

    with open ("output/sortie.wav", "wb") as f:
        f.write(speech.read())
    
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)

ui.btn_convert.clicked.connect(convert)
Form.show()
sys.exit(app.exec_())