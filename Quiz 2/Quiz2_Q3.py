# What is the value of endmsg after executing the following lines?

startmsg = "anaconda"
endmsg = ""
for i in range(1,1+len(startmsg)):
    endmsg = endmsg + startmsg[-i]
    