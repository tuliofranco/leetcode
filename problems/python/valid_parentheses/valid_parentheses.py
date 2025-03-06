class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pa = 0
        co = 0
        ch = 0
        
        if(len(s) % 2 != 0):
            False

        for valor in s:
            if (valor == "{"):
                ch += 1
                stack.append(valor)
            elif ( valor == "}"):
                if ( not(ch > 0)):
                    return False
                else:
                    if (stack[-1] != "{"):
                        return False
                    else:
                        ch -= 1
                        stack.pop()



            elif (valor == "("):
                pa += 1
                stack.append(valor)

            elif (valor == ")"):
                if ( not(pa > 0)):
                    return False
                else:
                    if (stack[-1] != "("):
                        return False
                    else:
                        pa -= 1
                        stack.pop()


            elif (valor == "["):
                co += 1
                stack.append(valor)

            elif (valor == "]"):
                if ( not(co > 0)):
                    return False
                if (stack[-1] != "["):
                    return False
                else:
                    co -= 1
                    stack.pop()
                    
        if((co != 0) or (pa != 0) or (ch != 0)):
            return False
        else: 
            return True