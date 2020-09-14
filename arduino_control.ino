#define ACTIVATE LOW

const int COPY_PIN =  2;
const int PASTE_PIN =  7;

int copyButtonState = 0;
int pasteButtonState = 0;
String command = "";


void setup() {
    Serial.begin(9600);
    pinMode(COPY_PIN, INPUT);
    pinMode(PASTE_PIN, INPUT);
    pinMode(13, OUTPUT);
}

void loop() {
    /* Copy button logic */
    delay(200);
    copyButtonState = digitalRead(COPY_PIN);
    if(copyButtonState == ACTIVATE) {
        command = "C";
        Serial.print(command);
    }

    /* Paste button logic */
    pasteButtonState = digitalRead(PASTE_PIN);
    if(pasteButtonState == ACTIVATE) {
        command = "V";
        Serial.print(command);
    }

}
