"""Regular Expressioin সাধারনত world change করা যায় """
import re
# pattern="amr" #amr কথাই আছে বের করে দেয়
pattern= r"[A-Z]+ojol"# যে world ojol আছে সব গুলার আগের world বড় হাতের হবে 
text='''
skdfjasdfkhdfjk  adhf an kdjhf
akdfhd
amr sonar bangla ami tomay valobasi cirodin tomar akash tomar batas amr prane oma amr sojol aojol prane bajai basi sonar bangla ami tomai vlo basi ki chova ki caya go ki senho ki maya go ki acol bicai aco boter mule nodir kule kule ma tor bodon khali monini hoile ami noyon oma ami noyon cole basi sonar banla ami tomari vli vasi'''

# match=re.search(pattern,text)
# print(match)
matches=re.finditer(pattern,text)
for match in matches:
    print(match.span())
