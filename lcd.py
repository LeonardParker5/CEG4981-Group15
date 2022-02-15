from rpi_lcd import LCD

def lcd_display(text):
    lcd = LCD()
    lcd.text(text, 1)
    return lcd
    
def lcd_erase(lcd):
    lcd = LCD()
    lcd.clear()