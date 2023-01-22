import sys

#try changing this multiline string to any liked image
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** * 
 **      *****************       ******************************     
          *************          **  * **** ** ************** *     
           *********            *******   **************** * *      
            ********           ***************************  *       
   *        * **** ***         *************** ******  ** *         
               ****  *         ***************   *** ***  *         
                 ******         *************    **   **  *         
                 ********        *************    *  ** ***         
                   ********         ********          * *** ****    
                   *********         ******  *        **** ** * **  
                   *********         ****** * *           *** *   * 
                     ******          ***** **             *****   * 
                     *****            **** *            ********    
                    *****             ****              *********   
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *                   
...................................................................."""

print('Bitmap image of a world map')
message = input('> ')
if message == '':
    sys.exit()

#loop over each line in the bitmap
for line in bitmap.splitlines():
  # loop over each character in the line
  for i, bit in enumerate(line):
    if bit == ' ':
      #Print an empty space like there is space in a  bitmap
      print(' ', end='')
    else:
      #print a charcter from the message
      print(message[i % len(message)],end='')
  print() #print a new line