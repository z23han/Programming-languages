# JavaScript's Big Bang
#
# In class we saw one way to integrate our HTML Interpreter and our
# JavaScript interpreter to make a web browser. Our JavaScript interpreter
# returned a string, which was then rendered unchanged on the webpage.
#
# In practice, however, JavaScript output may include HTML tags and should
# be lexed, parsed and interpreted again. For example, on modern web
# browsers the following webpage ...
#
# <html>
# <script type="text/javascript">
# document.write("Tags in <i>my</i> output should be processed.");
# </script>
# </html>
#
# Does not output the literal string "Tags in <i>my</i> output should be
# processed." Instead, the <i> tags are lexed, parsed and interpreted
# again, and the web page contains "Tags in my output should be processed."
# with the word "my" drawn in italics. 
#
# This sort of recursive dependence -- in which intepreted HTML contains
# JavaScript which runs and creates new HTML which is then interpreted,
# and so on, is the heart of JavaScript's power. You can visualize it like
# a snake eating its own tail: http://en.wikipedia.org/wiki/Ouroboros 
#
# In this assignment you will extend our web browser so that the string 
# produced by JavaScript is not merely passed to the graphics library as a
# word, but is instead lexed, parsed and interpreted as HTML. (For the
# purposes of this assignment, if JavaScript creates HTML, it must created
# only well-balanced tags.) 
#
# Below is the top-level HTML Interpreter code for the web browser. You
# will not need to change any lexer definitions, token definitions, or
# anything about the JavaScript interpreter. 
#
# Hint: The required extension can be made by changin as few as three lines
# (because you already know so much about this topic)! It does require you
# to understand how lexers, parser and interpreters all fit together. 

import ply.lex as lex
import ply.yacc as yacc
import graphics as graphics
import jstokens
import jsgrammar
import jsinterp 
import htmltokens
import htmlgrammar

# Load up the lexers and parsers that you have already written in
# previous assignments. Do not worry about the "module" or 
# "tabmodule" arguments -- they handle storing the JavaScript
# and HTML rules separately. 
htmllexer  = lex.lex(module=htmltokens) 
htmlparser = yacc.yacc(module=htmlgrammar,tabmodule="parsetabhtml") 
jslexer    = lex.lex(module=jstokens) 
jsparser   = yacc.yacc(module=jsgrammar,tabmodule="parsetabjs") 

# The heart of our browser: recursively interpret an HTML abstract
# syntax tree. 
def interpret(ast):     
        for node in ast:
                nodetype = node[0]
                if nodetype == "word-element":
                        graphics.word(node[1]) 
                elif nodetype == "tag-element":
                        tagname = node[1];
                        tagargs = node[2];
                        subast = node[3];
                        closetagname = node[4]; 
                        if (tagname <> closetagname):
                                graphics.warning("(mistmatched " + tagname + " " + closetagname + ")")
                        else: 
                                graphics.begintag(tagname,tagargs);
                                interpret(subast)
                                graphics.endtag(); 
                elif nodetype == "javascript-element": 
                        jstext = node[1]; 
                        jsast = jsparser.parse(jstext,lexer=jslexer) 
                        result = jsinterp.interpret(jsast)
                        # graphics.word(result)
                        htmllast = htmlparser.parse(result, lexer=htmllexer)
                        interpret(htmllast)

# Here is an example webpage that includes JavaScript that generates HTML.
# You can use it for testing.
webpage = """<html>
<h1>JavaScript That Produces HTML</h1>
<p>
This paragraph starts in HTML ...
<script type="text/javascript">
write("<b>This whole sentence should be bold, and the concepts in this problem touch on the <a href='http://en.wikipedia.org/wiki/Document_Object_Model'>Document Object Model</a>, which allows web browsers and scripts to <i>manipulate</i> webpages.</b>");
</script> 
... and this paragraph finishes in HTML. 
</p> 
<hr> </hr> <!-- draw a horizontal bar --> 
<p> 
Now we will use JavaScript to display even numbers in <i>italics</i> and
odd numbers in <b>bold</b>. <br> </br> 
<script type="text/javascript">
function tricky(i) {
  if (i <= 0) {
    return i; 
  } ; 
  if ((i % 2) == 1) {
    write("<b>");
    write(i); 
    write("</b>"); 
  } else {
    write("<i>");
    write(i); 
    write("</i>"); 
  }
  return tricky(i - 1); 
} 
tricky(10);
</script> 
</p> 
</html>"""

htmlast = htmlparser.parse(webpage,lexer=htmllexer) 
graphics.initialize() # let's start rendering a webpage
interpret(htmlast) 
graphics.finalize() # we're done rendering this webpage
# Higher-Order Functions
#
# Back in Unit 3 we introduced Python List Comprehensions -- a concise
# syntax for specifying a new list in terms of a transformation of an old
# one.
#
# For exmaple:
#
# numbers = [1,2,3,4,5]
# odds = [n for n in numbers if n % 2 == 1] 
# squares = [n * n for n in numbers] 
#
# That code assigns [1,3,5] to odds and [1,4,9,16,25] to squares. The first
# operation is sometimes called "filter" (because we are filtering out
# unwanted elements) and the second operation is sometimes called "map"
# (because we are mapping, or transforming, all of the elements in a list). 
#
# Python also has functions behave similarly: 
#
# odds = filter(lambda n : n % 2 == 1, numbers) 
# squares = map(lambda n : n * n, numbers) 
#
# The filter() and map() definitions for odds and squares produce the same
# results as the list comprehension approaches. In other words, we can
# define (or implement) list comprehensions in terms of map and filter. 
#
# In this exercise we take that notion one step beyond, by making
# specialized maps and filters. For example, suppose that we know that we
# will be filtering many lists down to only their odd elements. Then we
# might want something like this:
#
# filter_odds = filter_maker(lambda n : n % 2 == 1)
# odds = filter_odds(numbers) 
#
# In this example, "filter_maker()" is a function that takes a function as
# an argument and returns a function as its result. We say that
# filter_maker is a *higher order function*. 
#
# Complete the code below with definitions for filter_maker() and
# map_maker(). 
#
# Hint: You can use either "lambda" or nested Python function definitions.
# Both will work. The function you return from filter_maker(f) will have to
# reference f, so you'll want to think about nested environments.
'''
def filter_maker(f):
    # Fill in your code here. You must return a function.
    return lambda x : filter(f, x)
'''

def filter_maker(f):
    def my_filter(lst):
        return filter(f, lst)
    return my_filter

'''
def map_maker(f):
    # Fill in your code here. You must return a function.
    return lambda x : map(f, x)
'''

def map_maker(f):
    def my_map(lst):
        return map(f, lst)
    return my_map

# We have included a few test cases. You will likely want to add your own.
numbers = [1,2,3,4,5,6,7]
filter_odds = filter_maker(lambda n : n % 2 == 1)
print filter_odds(numbers) == [1,3,5,7]


length_map = map_maker(len) 
words = "Scholem Aleichem wrote Tevye the Milkman, which was adapted into the musical Fiddler on the Roof.".split() 
print length_map(words) == [7, 8, 5, 5, 3, 8, 5, 3, 7, 4, 3, 7, 7, 2, 3, 5]

string_reverse_map = map_maker(lambda str : str[::-1]) 
# str[::-1] is cute use of the Python string slicing notation that 
# reverses str. A hidden gem in the homework!
print string_reverse_map(words) == ['melohcS', 'mehcielA', 'etorw', 'eyveT', 'eht', ',namkliM', 'hcihw', 'saw', 'detpada', 'otni', 'eht', 'lacisum', 'relddiF', 'no', 'eht', '.fooR']

square_map = map_maker(lambda n : n * n) 
print [n*n for n in numbers if n % 2 == 1] == square_map(filter_odds(numbers))





