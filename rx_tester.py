import diameter as DiameterLib
import time
diameter_inst = DiameterLib.Diameter(
            str('OriginHost'), str('OriginRealm'), 
            str('UnitTest_Diameter'), str('001'), str('001')
        )
print("Instantiated Diameter Class")
time.sleep(1)
AA_request_1 = "010003c0c0000109010000143ce55613b6ec4e38000001074000003d70637363662e696d732e6d6e633030302e6d63633733382e336770706e6574776f726b2e6f72673b313139363332353734323b3135000000000001084000002f70637363662e696d732e6d6e633030302e6d63633733382e336770706e6574776f726b2e6f7267000000012840000029696d732e6d6e633030302e6d63633733382e336770706e6574776f726b2e6f7267000000000001024000000c0100001400000104400000200000010a4000000c000028af000001024000000c010000140000011b400000296570632e6d6e633030302e6d63633733382e336770706e6574776f726b2e6f7267000000000001bb40000054000001c24000000c00000002000001bc4000003d7369703a37333830303130303039303030313940696d732e6d6e633030302e6d63633733382e336770706e6574776f726b2e6f726700000000000205c00001c4000028af00000206c0000010000028af0000000100000207c000014c000028af000001fdc0000010000028af00000001000001fbc0000047000028af7065726d6974206f75742069702066726f6d203137322e32322e302e323120353030313620746f203139322e3136382e3130312e3220353030313600000001fbc0000046000028af7065726d697420696e2069702066726f6d203139322e3136382e3130312e3220353030313620746f203137322e32322e302e32312035303031360000000001fbc0000047000028af7065726d6974206f75742069702066726f6d203137322e32322e302e323120353030313720746f203139322e3136382e3130312e3220353030313700000001fbc0000046000028af7065726d697420696e2069702066726f6d203139322e3136382e3130312e3220353030313720746f203137322e32322e302e3231203530303137000000000200c0000010000028af0000000200000208c0000010000028af000000040000020cc000001a000028af75706c696e6b0a6f666665720a0000000000020cc000001d000028af646f776e6c696e6b0a616e737765720a00000000000001ffc0000010000028af0000000200000201c0000010000028af0000000100000201c0000010000028af0000000200000201c0000010000028af0000000300000201c0000010000028af0000000400000201c0000010000028af0000000500000201c0000010000028af0000000600000201c0000010000028af0000000c000000084000000cc0a86502000001234000000c00008ca0000001144000000c000000000000001b4000000c00008ca0"
AA_request_2 = "010006acc0000109010000143ce55614b6ec4e39000001074000003d70637363662e696d732e6d6e633030302e6d63633733382e336770706e6574776f726b2e6f72673b313139363332353734323b3136000000000001084000002f70637363662e696d732e6d6e633030302e6d63633733382e336770706e6574776f726b2e6f7267000000012840000029696d732e6d6e633030302e6d63633733382e336770706e6574776f726b2e6f7267000000000001024000000c0100001400000104400000200000010a4000000c000028af000001024000000c010000140000011b400000296570632e6d6e633030302e6d63633733382e336770706e6574776f726b2e6f7267000000000001f8c0000018000028af494d53205365727669636573000001234000000c00008ca0000001bb40000054000001c24000000c00000002000001bc4000003d7369703a37333830303130303039303030313940696d732e6d6e633030302e6d63633733382e336770706e6574776f726b2e6f7267000000000001ca80000010000032db0000000000000205c0000488000028af00000206c0000010000028af0000000100000207c0000144000028af000001fdc0000010000028af00000001000001fbc0000045000028af7065726d6974206f75742031372066726f6d2031302e39382e302e3820313730393220746f203139322e3136382e3130312e32203430303334000000000001fbc0000044000028af7065726d697420696e2031372066726f6d203139322e3136382e3130312e3220343030333420746f2031302e39382e302e38203137303932000001fbc0000045000028af7065726d6974206f75742031372066726f6d2031302e39382e302e3820313730393320746f203139322e3136382e3130312e32203430303335000000000001fbc0000044000028af7065726d697420696e2031372066726f6d203139322e3136382e3130312e3220343030333520746f2031302e39382e302e3820313730393300000200c0000010000028af0000000000000208c0000010000028af0000000000000204c0000010000028af0000a02800000203c0000010000028af0000fa000000020cc0000211000028af75706c696e6b0a6f666665720a6d3d617564696f203430303334205254502f41565020393820393720313035203130300d0a623d41533a34310d0a623d52533a3531320d0a623d52523a313533370d0a613d7274706d61703a393820414d522d57422f31363030302f310d0a613d7074696d653a32300d0a613d6d61787074696d653a3234300d0a613d7274706d61703a393720414d522f383030302f310d0a613d7274706d61703a3130352074656c6570686f6e652d6576656e742f31363030300d0a613d7274706d61703a3130302074656c6570686f6e652d6576656e742f383030300d0a613d666d74703a3938206d6f64652d6368616e67652d6361706162696c6974793d323b6f637465742d616c69676e3d303b6d61782d7265643d300d0a613d666d74703a3937206d6f64652d6368616e67652d6361706162696c6974793d323b6f637465742d616c69676e3d303b6d61782d7265643d300d0a613d666d74703a31303520302d31350d0a613d666d74703a31303020302d31350d0a613d637572723a716f73206c6f63616c206e6f6e650d0a613d637572723a716f732072656d6f7465206e6f6e650d0a613d6465733a716f73206d616e6461746f7279206c6f63616c2073656e64726563760d0a613d6465733a716f73206f7074696f6e616c2072656d6f74652073656e64726563760d0a613d73656e64726563760d0a000000000000020cc00000d4000028af646f776e6c696e6b0a616e737765720a6d3d617564696f203137303932205254502f415650203937203130300d0a613d7274706d61703a393720414d522f383030300d0a613d666d74703a3937206d6f64652d7365743d373b6f637465742d616c69676e3d300d0a613d7274706d61703a3130302074656c6570686f6e652d6576656e742f383030300d0a613d666d74703a31303020302d31350d0a613d7074696d653a32300d0a613d727463703a313730393320494e204950342031302e39382e302e380d0a00000001ffc0000010000028af00000002000000084000000cc0a8650200000201c0000010000028af0000000100000201c0000010000028af0000000200000201c0000010000028af0000000300000201c0000010000028af0000000400000201c0000010000028af0000000500000201c0000010000028af0000000600000201c0000010000028af0000000c000001144000000c000000000000001b4000000c00008ca0"

#Test 1
packet_vars, avps = diameter_inst.decode_diameter_packet(AA_request_1)
print("Received request with Command Code: " + str(packet_vars['command_code']) + ", ApplicationID: " + str(packet_vars['ApplicationId']) + " and flags " + str(packet_vars['flags']))
print("\n\n\n")
response_bytes = diameter_inst.Answer_16777236_258(packet_vars, avps)
print(response_bytes)

time.sleep(2)
#Test 2
packet_vars, avps = diameter_inst.decode_diameter_packet(AA_request_2)
print("Received request with Command Code: " + str(packet_vars['command_code']) + ", ApplicationID: " + str(packet_vars['ApplicationId']) + " and flags " + str(packet_vars['flags']))
print("\n\n\n")
response_bytes = diameter_inst.Answer_16777236_258(packet_vars, avps)
print(response_bytes)