def addition(varIn):
  k=0
  if varIn[2]=='+':
    k=int(varIn[0])+int(varIn[1])
  else:
    k=int(varIn[0])-int(varIn[1])
  return str(k).rjust(len(total_slashes(varIn)))

def bottom(varIn):
  varOut=""
  for i in range(len(varIn)):
    if i!=0:
      varOut+="    "+addition(varIn[i])
    else:
      varOut+=addition(varIn[i])
  return varOut
    
def total_slashes(varIn):
  varOut=""
  if len(varIn[0])>len(varIn[1]):
    varOut+=('-'*(len(varIn[0])+2))
  else:
    varOut+=('-'*(len(varIn[1])+2))
  return varOut

def slashes(varIn):
  varOut=""
  for i in range(len(varIn)):
    if i==0:
      varOut+=total_slashes(varIn[i])
    else:
      varOut+="    "+total_slashes(varIn[i])
  return varOut

def down(varIn):
  varOut=""
  if len(varIn[0])>len(varIn[1]):
    varOut=varIn[1].rjust(len(varIn[0]))
  else:
    varOut=varIn[1]
  return varOut

def front(v_in):
  v_out=""
  if len(v_in[0])>len(v_in[1]):
    v_out=v_in[0]
  else:
    v_out=v_in[0].rjust(len(v_in[1]))
  return v_out

def top(varIn):
  final=""
  for i in range(len(varIn)):
    if i==0:
      final+="  "+front(varIn[i])
    else:
      final+="      "+front(varIn[i])
  return final
  
def middle(varIn):
  varOut=""
  for i in range(len(varIn)):
    if i==0:
      varOut+=varIn[i][2]+" "+down(varIn[i])
    else:
      varOut+="    "+varIn[i][2]+" "+down(varIn[i])
  return varOut

# Check if only numbers
def containsDigit(varIn):
  varIn[0]=varIn[0].strip()
  varIn[1]=varIn[1].strip()
  for i in range(len(varIn)):
    for j in range(len(varIn[i])):
      # The ord() function returns the number representing the unicode
      # code of a specified character. Digits between 48 and 57
      if ord(varIn[i][j])>=48 and ord(varIn[i][j])<=57:
        continue
      else:
        return False
  return True

#-----------------#
# Main DEF        #
#-----------------#
def arithmetic_arranger(problems,showResult=False):
    final=[]
    if len(problems)>5:
      return "Error: Too many problems."
    for i in problems:
      if '+' not in i and '-' not in i:
        return "Error: Operator must be '+' or '-'."
      else:
        if '+' in i:
          l=i.split('+')
          if not containsDigit(l):
            return "Error: Numbers must only contain digits."
          else:
            if len(l[0])>4 or len(l[1])>4:
              return "Error: Numbers cannot be more than four digits."
            else:
              l.append('+')
              final.append(l)
        if '-' in i:
          l=i.split('-')
          if not containsDigit(l):
            return "Error: Numbers must only contain digits."
          else:
            if len(l[0])>4 or len(l[1])>4:
              return "Error: Numbers cannot be more than four digits."
            else:
              l.append('-')
              final.append(l)

    # Including results
    if showResult:
      return (top(final)+"\n"+middle(final)+"\n"+slashes(final)+"\n"+bottom(final))  
    # Results not included  
    else:
      return top(final)+"\n"+middle(final)+"\n"+slashes(final)