import marshal
import dis

)

byte_string = b'a\r\r\n\x00\x00\x00\x00\xf6\x971a\x00\x00\x00\x00'
with open('ConfusedCharacter.pyc', 'wb') as pyc:
     pyc.write(byte_string )
     marshal.dump(dis.Bytecode(marshal_c).codeobj, pyc)

#Confused Character
#Decrypting Marshal with @ConfusedCharacter
#Put Marshal Load in var
#run it