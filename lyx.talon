app: lyx
app: LyX.exe
app: LyX for Windows
-
tag(): user.maths


add matrix row: key(alt-m w i)
(delete | remove) matrix row: key(alt-m w d)
add matrix column: key(alt-m c i)
(delete | remove) matrix column: key(alt-m c d)

square root: key(alt-m s)
generic root: key(alt-m r)

brackets: key(alt-m ()
square brackets: key(alt-m [)
curly brackets: key(alt-m {)
absolute: key(alt-m |)

accent hat: key(alt-m h)
accent tilde: key(alt-m &)
accent dot: key(alt-m .)
accent double dot: key(alt-m \")
accent bar: key(alt-m -)
accent vector: key(alt-m v)

blank summation: "\\sum "
summation:
    insert("\\stackrelthree ")
    key(down)
    insert("\\sum ")
    key(down)
blank product: "\\prod "
product:
    insert("\\stackrelthree ")
    key(down)
    insert("\\prod ")
    key(down)
blank limit: "\\lim "
limit:
    insert("\\underset \\lim ")
    key(down)
label above: "\\overset "
label below: "\\underset "
prime: user.maths_superscript("\\prime ")
degrees: user.maths_superscript("\\degrees ")
exponential:
    insert("\\exp ")
    key(alt-m ()
expectation:
    insert("E")
    key(alt-m ()
variance:
    insert("Var")
    key(alt-m ()
#
real numbers:
    insert("\\mathbb R")
    key(right)
complex numbers:
    insert("\\mathbb C")
    key(right)
integer numbers:
    insert("\\mathbb Z")
    key(right)
rational numbers:
    insert("\\mathbb Q")
    key(right)
natural numbers:
    insert("\\mathbb N")
    key(right)

text roman: "\\mathrm "
text bold: "\\mathbf "
text sans serif: "\\mathsf "
text italic: "\\mathit "
text typewriter: "\\mathtt "
text (beebee|blackboard bold | blackboard): "\\mathbb "

#
# Program control
#
new file: key(ctrl-n)
open file: key(ctrl-o)
save as: key(ctrl-shift-s)
(math | maths) mode: key(ctrl-m)
display mode: key(ctrl-shift-m)
normal mode: key(alt-p s)
view PDF: key(ctrl-r)
update PDF: key(ctrl-shift-r)
next tab: key(ctrl-pgdown)
(prior | previous) tab: key(ctrl-pgup)
close tab: key(ctrl-w)
move line up: key(alt-up)
move line down: key(alt-down)
#
insert (in line formula | in line): key(alt-i h i)
insert (numbered formula): key(alt-i h n)
insert (display formula | display): key(alt-i h d)
insert equation array: key(alt-i h e)
#
insert [bulleted] list: key(alt-p b)
insert numbered list: key(alt-p e)
insert description: key(alt-p d)
insert part: key(alt-p 0)
insert (section | heading): key(alt-p 2)
insert sub (section | heading): key(alt-p 3)
insert sub sub (section | heading): key(alt-p 4)
insert paragraph: key(alt-p 5)
insert sub paragraph: key(alt-p 6)
insert title: key(alt-p t)
insert author: key(alt-p shift-a)
insert date: key(alt-p shift-d)
insert abstract: key(alt-p a)
insert address: key(alt-p alt-a)
insert bibliography: key(alt-p shift-b)
insert quotation: key(alt-p alt-q)
insert quote: key(alt-p q)
insert verse: key(alt-p v)
