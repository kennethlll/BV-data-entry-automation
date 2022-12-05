import pyautogui
# for the time gap
import time
# for copy and paste
import pyperclip
# read csv
import csv


def check(path):
    if pyautogui.locateOnScreen(path,  confidence=0.99) != None:
        time.sleep(0.5)
        return True
    else:
        time.sleep(0.5)
        return False


   



    

def excute():

    # check the BV and inventory page is opened
    if not (check("img/inventory.png") and check("img/bom.png")):
        print("BV is not fully opened")

    
    with open("data.csv", "r") as data:
        reader1 = csv.reader(data)
        next(reader1)
        # read every info in the data.csv
        for info in reader1:
            id, pn, name, fac, mat = info[0], info[1], info[2], info[3], info[4]
            # if the inverntory number already in the system

            #buffer time
            time.sleep(0.2)
            
            
            # inputing the PN
            print("Inputting P/N: ", pn)   
            PN = pyautogui.locateCenterOnScreen("img/pn.png")
            if PN:
                PN_shift = (PN.x+300, PN.y)

                # change cusor to the remote desktop window
                pyautogui.click(PN_shift)

                # click the part number
                pyautogui.click(PN_shift)
            time.sleep(0.3)
            pyautogui.press('backspace',presses=15)
            time.sleep(0.5)
            #write part number

            pyautogui.write(pn)
            #buffer time
            time.sleep(0.5)
            pyautogui.press('tab')
            time.sleep(1.5)
            # check the part whether exist or not
            if not (check("img/empt_inv.png")):
                print("inventory is already exsist")
                continue

            #inputing the desciption
            print("Inputting description: ", name) 
            PN = pyautogui.locateCenterOnScreen("img/des.png")
            if PN:
                PN_shift = (PN.x+300, PN.y)
                pyautogui.click(PN_shift)
            time.sleep(0.3)
            pyautogui.press('backspace',presses=15)
            #write part number
            pyautogui.typewrite(name,0.001)
            #buffer time
            time.sleep(0.3)

            #inputing the detail
            
            if check("img/nor.png"):
                print("Inputting inventory type") 
                pyautogui.click(pyautogui.locateCenterOnScreen("img/nor.png"))
                time.sleep(0.3)
                pyautogui.click(pyautogui.locateCenterOnScreen("img/manu.png"))
                time.sleep(0.3)
                #buffer time
                time.sleep(0.3)
            
            #inputing the wb
            if check("img/wb.png"):
                print("Inputting workbook detail") 
                pyautogui.click(pyautogui.locateCenterOnScreen("img/wb.png"))
                time.sleep(1.3)
                PN = pyautogui.locateCenterOnScreen("img/fac.png")
                if PN:
                    PN_shift = (PN.x+200, PN.y)
                    pyautogui.click(PN_shift)
                time.sleep(0.3)
                if fac == 'WJ':
                    pyautogui.click(pyautogui.locateCenterOnScreen("img/wj.png"))
                    time.sleep(0.3)
                if fac == 'PS':
                    pyautogui.click(pyautogui.locateCenterOnScreen("img/ps.png"))
                    time.sleep(0.3)
                if fac == 'GFE':
                    pyautogui.click(pyautogui.locateCenterOnScreen("img/gf.png"))
                    time.sleep(0.3)

                PN = pyautogui.locateCenterOnScreen("img/rev.png")
                if PN:
                    PN_shift = (PN.x+200, PN.y)
                    pyautogui.click(PN_shift)
                time.sleep(1)

                pyautogui.click(pyautogui.locateCenterOnScreen("img/0.png"))
                time.sleep(0.8)

                pyautogui.click(pyautogui.locateCenterOnScreen("img/wb_save.png"))
                time.sleep(0.8)

                PN = pyautogui.locateCenterOnScreen("img/close_wb.png")
                if PN:
                    PN_shift = (PN.x+145, PN.y-30)
                    pyautogui.click(PN_shift)
                time.sleep(0.6)

                PN = pyautogui.locateCenterOnScreen("img/inv_save.png")
                if PN:
                    PN_shift = (PN.x, PN.y)
                    pyautogui.click(PN_shift)
                time.sleep(0.3)



    
    print("COMPLETED")
