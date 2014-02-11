Not much to say about it. This is a very simple brainfuck compiler. It can easily be upgraded to contain a few syntax checks for the brainfuck code.

To test it out just download the code, edit the contents of "bfcode" with your brainfuck code and run it.

Feel free to use it, dismember it and sell it to the highest bidder.


A little wiki love about what brainfuck really is:

Brainfuck is a minimalistic esoteric computer language, mostly use to fuck with your brain, hence the name.

It has only 8 commands:

">"	  increment the data pointer (to point to the next cell to the right).

"<"	  decrement the data pointer (to point to the next cell to the left).

"+"	  increment (increase by one) the byte at the data pointer.

"-"	  decrement (decrease by one) the byte at the data pointer.

"."	  output the byte at the data pointer.

","	  accept one byte of input, storing its value in the byte at the data pointer.

"["	  if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command,      jump it forward to the command after the matching ] command.

"]"	  if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next            command, jump it back to the command after the matching [ command.


A brainfuck program is a sequence of any of these commands. As an example (taken from wikipedia), this program prints "Hello World!", if you use in in a nice interpreter (like the one i made):

++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.



Ah hell, go read the wikipedia article to know more. Its really fun. really:

http://en.wikipedia.org/wiki/Brainfuck
