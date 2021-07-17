tag: user.maths
-
tag(): user.maths
help (math | maths): user.maths_help_show()
show (math | maths) help: user.maths_help_show()
hide maths help: user.maths_help_hide()

# Basic symbols
greek {user.greek_letters}: user.maths_greek_letter(greek_letters)
{user.tex_symbols}: user.maths_tex_symbol(tex_symbols)

# Matrices
matrix <number> by <number>: user.maths_matrix(number_1, number_2)

# Fractions
fraction: user.maths_fraction()
over:
    key(shift-left)
    user.maths_fraction()
    key(down)
<number> {user.maths_fractions}:
    user.maths_fraction()
    insert(number)
    key(down)
    insert(maths_fractions)
    key(right)

# Sub/Superscript
(super script | to the power): user.maths_begin_superscript()
sub script: user.maths_begin_subscript()
{user.maths_common_powers}: user.maths_superscript(maths_common_powers)

#
soup <user.maths_item>:
    user.maths_begin_superscript()
    user.maths_insert_item(maths_item)
    user.maths_end_superscript()


integral from <user.maths_item> to <user.maths_item>:
    user.maths_tex_symbol("int")
    user.maths_begin_subscript()
    user.maths_insert_item(maths_item_1)
    user.maths_end_subscript()
    user.maths_begin_superscript()
    user.maths_insert_item(maths_item_2)
    user.maths_end_superscript()
